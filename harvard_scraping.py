import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# ============================================================
# Function: scrape_harvard
# Purpose : Scrape faculty information from Harvard SEAS website
# Details :
#   - Extracts faculty name, title, email (if available), and research areas
#   - Navigates through paginated directory pages
#   - Saves data in a structured format for further use
# ============================================================
def scrape_harvard():
    page_num = 0  # Start from the first page
    harvard_data = []  # List to store faculty data

    # Loop through pages until no more faculty are found
    while True:  
        url = f'https://seas.harvard.edu/faculty?page=%2C{page_num}'
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.content, 'html.parser')
    
        # Locate all faculty blocks on the current page
        people = soup.find_all('div', {'class': 'person__detailed'})
        if not people:  # Stop when no faculty are found
            print("No more people found on this page. Ending scrape.")
            break

        print(f"Scraping page {page_num + 1} ...")
        for person in people:

            # Extract faculty name
            name_tag = person.find('h2', class_='person__detailed-name')
            if name_tag:
                span = name_tag.find('span', class_='person__name')
                name = span.get_text(strip=True) if span else name_tag.get_text(strip=True)
            else:
                name = "N/A"

            # Extract faculty title/position
            title_tag = person.find('div', class_='person-directory__primary-title')
            title = title_tag.get_text(strip=True) if title_tag else "N/A"

            # Build profile URL (for detailed info like research areas)
            profile_tag = person.find('h2', class_='person__detailed-name').find('a')
            if profile_tag:
                profile_url = profile_tag['href']
                if not profile_url.startswith("http"):
                    profile_url = "https://seas.harvard.edu" + profile_url
            else:
                profile_url = "N/A"

            # Extract research areas from profile page
            research_areas = "N/A"
            if profile_url and profile_url != "N/A":
                profile_response = requests.get(profile_url, headers={"User-Agent": "Mozilla/5.0"})
                if profile_response.status_code == 200:
                    profile_soup = BeautifulSoup(profile_response.content, 'html.parser')
                    research_tag = profile_soup.find(
                        'div', 
                        class_='person__detailed-section person__detailed-section--research-interests accordion'
                    )
                    if research_tag:
                        research_list = [a.get_text(strip=True) for a in research_tag.find_all('a')]
                        research_areas = " | ".join(research_list)
            time.sleep(1)  # Pause between requests

            # Extract email
            contact_div = person.find('div', class_='person-directory__contact')
            email_tag = contact_div.find('a', href=True) if contact_div else None
            email = email_tag.get_text(strip=True).replace("(at)", "@").replace(" ", "") if email_tag else "N/A"

            # Append all extracted data to results list
            harvard_data.append({
                'Name': name,
                'Title': title,
                'Email': email,
                'Research Areas': research_areas,
                'University': 'Harvard University'
            })

        # Go to the next page
        page_num += 1
        time.sleep(2)  # Extra pause between pages to avoid overloading server

    print("Scraping completed for Harvard University.")
    return harvard_data

# Main Script Execution
if __name__ == "__main__":
    # Run the scraper
    harvard_faculty = scrape_harvard()

    # Convert to DataFrame
    df = pd.DataFrame(harvard_faculty)

    # Save results to CSV file
    df.to_csv('harvard_faculty.csv', index=False)

    print("Scraping completed. Data saved to 'harvard_faculty.csv'.")
