
# 📈 Share Price Monitoring CLI Application

A command-line application for tracking and recording share prices using Yahoo Finance data. This tool allows users to create and manage a customizable list of shares, with historical pricing data saved as CSV files.

## 🚀 Features

- **Track multiple shares**: Maintain a customizable list of stock symbols to monitor.
- **Live price retrieval**: Fetch real-time share prices using the [`yfinance`](https://pypi.org/project/yfinance/) package.
- **Automatic CSV logging**: Save historical price data for each tracked share, organized by date.
- **Persistent share list**: The list of tracked shares is stored locally and can be manually edited.
- **Simple CLI interface**: Interact with the program via a command-line interface.
- **File selection UI**: Uses `tkinter` for selecting files when needed.

## 🛠️ Installation

Ensure you have **Python 3.7+** installed, then install the required dependencies:

```sh
pip install yfinance pandas tk
```

## 📌 Usage

Run the application from the command line:

```sh
python share_monitor.py
```
  
## Core Functions:
 - Add shares: Add stock symbols (e.g., AAPL, GOOGL) to your tracking list.
 - Remove shares: Remove stocks from the list at any time.
 - View tracked shares: Display all currently tracked shares.
 - Fetch prices: Retrieve the latest prices for all tracked shares.
 - Export data: Prices are automatically logged in /data as CSV files. 

## CSV File Structure: 
Each share has its own CSV file in the /data folder, structured as follows:
|Date|Open|High|Low|Volume|
|:--|:--|:--|:--|:--|
|2025-02-08|152.00|149.80|151.50|10,000|

## 📂 File Structure
```bash
/share-price-monitor/
│── bin/                   # Stores the user's tracked share list
│── data/                  # Contains historical price CSV files
│── share_monitor.py       # Main application script
│── requirements.txt       # List of dependencies
│── README.md              # Project documentation
```
## ✨ Customization
- The tracked share list is stored in `/bin/tracked_shares.txt` and can be edited manually.
- The CSV data folder (`/data`) can be changed in the script settings.
## 🤝 Contributing

 1. Fork the repository.
 2. Create a feature branch: git checkout -b feature-name
 3. Commit changes: git commit -m "Add new feature" 
 4. Push to branch: git push origin feature-name
 5. Open a pull request.

## 📜 License
This project is licensed under the MIT License.
