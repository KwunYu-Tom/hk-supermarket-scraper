# Hong Kong Supermarket Locator Scraper 🛒

A Python-based automation tool that scrapes major supermarket addresses in Hong Kong (starting with Wellcome) and provides an interactive command-line interface for users to filter locations by region.

## 🚀 Project Overview
This project was designed to automate the collection of supermarket geographic data. Instead of manually searching for store locations, this script fetches the data directly from the web, cleans the formatting, and organizes it for easy access.

### Key Features
- **Web Scraping:** Uses `BeautifulSoup` and `requests` to extract data from dynamic HTML.
- **Data Cleaning:** Implements `.strip()` and duplicate removal logic to ensure high-quality data.
- **Interactive CLI:** A user-friendly loop that allows filtering by **Hong Kong Island (HK)**, **Kowloon (KL)**, and **New Territories (NT)**.
- **Local Persistence:** Saves the raw HTML locally to reduce server requests and improve debugging speed.

## 🛠️ Tech Stack
- **Language:** Python 3
- **Libraries:** - `BeautifulSoup4` (Data Parsing)
  - `Requests` (HTTP Client)
- **Version Control:** Git & GitHub

## 📂 Project Structure
```text
├── hk-supermarket-scraper.py  # Main application logic
├── response.html              # Locally cached HTML data 
└── README.md                  # Project documentation
