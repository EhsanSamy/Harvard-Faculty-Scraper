# Harvard Faculty Scraper

**Harvard-Faculty-Scraper** is a Python tool designed to scrape **faculty names, emails, and academic positions** from university websites. It’s a quick and reliable way to gather structured academic data for **research, networking, or collaboration purposes**.

## 🚀 Key Features
- Extracts **Faculty Name**
- Extracts **Email Address**
- Extracts **Title/Position** (e.g., Professor, Lecturer, Assistant Professor)
- Saves results to a **clean CSV file** for easy analysis
- Handles large university faculty pages efficiently

## 🛠️ Technology Stack
- **Python 3** – Core language
- **requests** – Fetches web pages
- **BeautifulSoup** – Parses and navigates HTML
- **pandas** – Structures and exports data

## 📂 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/EhsanSamy/Harvard-Faculty-Scraper.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python harvard_scraping.py
   ```

4. Check the output:
   ```
   output/harvard_faculty.csv
   ```

## 📊 Example Output

| Name           | Title                  | Email              | Research Areas                | University         |
|----------------|------------------------|--------------------|-------------------------------|--------------------|
| Dr. John Smith | Professor of AI        | john.smith@uni.edu | Artificial Intelligence, NLP  | Harvard University |
| Dr. Sara Ahmed | Assistant Professor CS | sara.ahmed@uni.edu | Data Mining, Machine Learning | Harvard University |

## ✨ Future Improvements
- Add support for multiple universities
- Enable export to **Excel** or **Google Sheets**
- Implement automated email verification

## 📌 Why This Project?
Collecting academic data manually is **time-consuming and error-prone**. This tool **automates the process**, making it efficient for researchers, students, and professionals looking to **connect with faculty members** or **analyze academic networks**.

## 🔗 Connect with Me
- 💼 [LinkedIn](https://www.linkedin.com/in/ehsan-samy)
- 📧 [Gmail](mailto:ehsansamy9@gmail.com)
- 🗃️ [GitHub](https://github.com/EhsanSamy)
