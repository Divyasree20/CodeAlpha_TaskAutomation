# 📂 CodeAlpha Task Automation

This repository contains various task automation scripts built with Python to streamline repetitive processes.

## 📌 Features

1. **File Organizer**: Automatically organizes files into directories based on file type.
2. **Web Scraper**: Fetches live weather data, stock prices, and news headlines, saving them to CSV files.
3. **Data Cleaner**: Cleans and processes CSV data (removing duplicates, correcting errors, etc.).
4. **Auto Rename**: Renames files in bulk with a standardized naming format.

## 📂 Project Structure

```
File_Organizer/
├── FilesToRename/          # Directory for files to rename
├── auto_rename.py         # Automates file renaming
├── cleaned_data.csv       # Cleaned CSV output
├── data.csv               # Raw CSV input
├── data_cleaner.py        # Cleans and processes CSV files
├── main.py                # Main script to run all tasks
├── news_headlines.csv     # Scraped news data
├── organize.py            # File organizer script
├── stock_prices.csv       # Scraped stock prices
├── weather_data.csv       # Scraped weather data
└── web_scraper.py         # Scrapes weather, stocks, and news
```

## 🚀 How to Run

1. Clone the repository:
    git clone https://github.com/Divyasree20/CodeAlpha_TaskAutomation.git
    cd CodeAlpha_TaskAutomation/File_Organizer

2. Ensure Python is installed (>=3.8). Install dependencies if needed:
    pip install -r requirements.txt
   
4. Run the main script:
    python main.py
  

## 📊 Output

- Cleaned CSV data: `cleaned_data.csv`
- Weather, stock prices, and news headlines are saved to CSV files.
- Automatically organized and renamed files.

## 🤝 Contribution
Feel free to fork and contribute! Create a pull request for any improvements.

## 📜 License
This project is open-source and available under the MIT License.

---

Made with ❤️ by [Divyasree](https://github.com/Divyasree20)

