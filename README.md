# Web Scraping

A collection of web scraping projects developed to practice data extraction, automation, and data preprocessing. This repository demonstrates the ability to handle both real-world e-commerce websites and structured educational platforms.

## 📂 Projects in this Repository

### 1. Lotus's Product Scraper (`/lotusScraping`)
* **Target:** Real-world E-commerce website (Lotus's Thailand).
* **Goal:** Extract product information including names and prices.
* **Tools:** Python, Selenium / BeautifulSoup.
* **Key Challenge:** Handling dynamic content and real-world web structures that require robust CSS selector targeting.

### 2. Books to Scrape Automation (`/bookScraping`)
* **Target:** [Books to Scrape](https://books.toscrape.com/) (A sandbox for web scraping).
* **Goal:** Successfully scraped 1,000 book items across multiple pages.
* **Key Feature:** **Pagination Automation** – Implemented a loop system to navigate through all pages automatically.
* **Output:** Data saved in structured formats (.csv / .xlsx) ready for data analysis.

---

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** * `BeautifulSoup4`: For parsing HTML content.
    * `Selenium`: For handling dynamic elements (if applicable).
    * `Pandas`: For data structuring and exporting to CSV/Excel.
    * `Requests`: For making HTTP connections.

## 📈 Data Science Workflow
This project is part of my Data Science & AI learning path. Web scraping is the first step in my workflow:
1.  **Data Collection:** Extracting raw data from web sources.
2.  **Data Cleaning:** Using **Pandas** to handle missing values and formatting prices.
3.  **Analysis:** Preparing datasets for Machine Learning models (e.g., Price Prediction).

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/saranyapatt/webScraping.git](https://github.com/saranyapatt/webScraping.git)
