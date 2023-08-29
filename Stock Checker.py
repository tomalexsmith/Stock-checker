import yfinance as yf
import os
import time
from tqdm import tqdm
import csv
from datetime import datetime

tickers = []
valid_tickers = []

def main():
    os.system('cls')
    load_tickers()
    menu()
    
def get_date():
    return datetime.today().strftime('%Y-%m-%d')
    
def load_tickers():
    global tickers
    
    f = open("bin/tickers.txt", "r")
    lines = f.read().splitlines()
    
    for line in lines:
        tickers.append(line)    
        
    f.close()


def logo():
    print("Yahoo Finance")
    print("█▀ ▀█▀ █▀█ █▀▀ █▄▀   █▀▀ █░█ █▀▀ █▀▀ █▄▀ █▀▀ █▀█")
    print("▄█ ░█░ █▄█ █▄▄ █░█   █▄▄ █▀█ ██▄ █▄▄ █░█ ██▄ █▀▄\n\n\n")


def menu_choice():
    return int(input("Enter your choice: "))

def options_menu():
    while True:
        os.system('cls')
        logo()
        print("Options")
        print("───────────────────────────────────────────────────────────────────────────────────────")
        print("1. Add a ticker to the list of tickers")
        print("2. Remove a ticker from the list of tickers")
        print("3. Clear list of tickers")
        print("4. Back")
        print("───────────────────────────────────────────────────────────────────────────────────────")
        
        valid_choice = False
            
        try:
            choice = int(input("\n\nEnter your choice: "))
            valid_choice = True
        except ValueError:
            os.system('cls')
            options_menu()
                

        match choice:
            case 1:
                add_tickers()
            case 2:
                remove_tickers()
            case 3:
                clear_tickers()
            case 4:
                return
            
        os.system('cls')


def menu():    
    while True:
        logo()
        print("Main menu")
        print("───────────────────────────────────────────────────────────────────────────────────────")
        print("1. Get stock data")
        print("2. View list of tickers")
        print("3. Options")
        print("4. Save and exit")
        print("───────────────────────────────────────────────────────────────────────────────────────")
        
        valid_choice = False
        
        try:
            choice = int(input("\n\nEnter your choice: "))
            valid_choice = True
        except ValueError:
            os.system('cls')
            menu()
            
        
        match choice:
            case 1:
                get_stock_data()
            case 2:
                view_tickers()
            case 3:
                options_menu()
            case 4:
                save_exit()
                
        os.system('cls')

def save_exit():
    global tickers
    
    f = open("bin/tickers.txt", "w")
    
    for ticker in tickers:
        f.write(str(ticker) + "\n")
    
    exit()
    

def clear_tickers():
    global tickers
    
    choices = ["y", "yes"]
    valid_choice = False
    
    while not valid_choice:
        os.system('cls')
        logo()
        confirm = input("Are you sure you want to clear the list of tickers? (y/n): ").lower()
        
        if confirm in choices:
            tickers = []
            valid_choice = True
            
            os.system('cls')
            logo()

            for i in tqdm(range(100), desc='Clearing tickers...'):
                time.sleep(0.005)
            
            time.sleep(0.5)    
            print("\n\nSuccessfully cleared tickers!")
            time.sleep(2)
        else:
            os.system('cls')
            logo()
            print("Please enter a valid selection...")
            time.sleep(3)

def check_tickers():
    global valid_tickers
    
    f = open("bin/valid_tickers.csv", "r")
    csv_dl = csv.DictReader(f)
    for row in csv_dl:
        ticker = str(row["Symbol"])
        valid_tickers.append(ticker)
        
    f.close()

def add_tickers():
    global valid_tickers
    global tickers 
    os.system('cls')
    logo()

    ticker = input("Enter a ticker: ")
    if ticker.upper() in tickers:
        os.system('cls')
        logo()
        print("{0} is already in the list of tickers...".format(ticker.upper()))
        time.sleep(3)
        return
    
    if not valid_tickers:
        check_tickers()
    
    if ticker.upper() not in valid_tickers:
        os.system('cls')
        logo()
        print("{0} is not a valid stock ticker...".format(ticker.upper()))
        time.sleep(3)
        return
        
    tickers.append(ticker.upper())
    os.system('cls')
    logo()

    for i in tqdm(range(100), desc='Adding ticker...'):
        time.sleep(0.001)
    
    time.sleep(0.5) 
    print("\n\nSuccessfully added {}!".format(ticker.upper()))
    time.sleep(2)

def remove_tickers():
    global tickers 
    os.system('cls')
    logo()
    
    ticker = input("Enter a ticker: ")
    if ticker.upper() not in tickers:
        os.system('cls')
        logo()
        print("{0} is not in the list of tickers...".format(ticker.upper()))
        time.sleep(3)
    else: 
        tickers.remove(ticker.upper())
        os.system('cls')
        logo()

        for i in tqdm(range(100), desc='Removing ticker...'):
            time.sleep(0.001)
        
        time.sleep(0.5)
        print("\n\nSuccessfully removed {}!".format(ticker.upper()))
        time.sleep(2)

        
def view_tickers():
    global tickers
    os.system('cls')
    logo()
    
    print("List of tickers")
    print("───────────────────────────────────────────────────────────────────────────────────────\n")
    if tickers:
        for ticker in tickers:
            print("{}".format(ticker))
    else:
        print("Empty")
    print("\n───────────────────────────────────────────────────────────────────────────────────────\n\n")
    input("Press enter to go back to main menu...")

def get_stock_data():
    global tickers
    failed_downloads = []
    date = get_date()
    os.system('cls') 
    logo()
    
    if not tickers:
        print("Ticker list is empty, please add to it before requesting stock data...")
        time.sleep(3)
        return
    
    for i in tickers:
        ticker = yf.Ticker(i)
        df_tick = ticker.history(period='5y')
        df_tick = df_tick.reset_index()
        df_tick.to_csv("stock data/"+i+" "+date+".csv")
        
    for i in tqdm(range(100), desc='Downloading stock data...'):
        time.sleep(0.001)
        
    time.sleep(0.5)
    print("\n\nSuccessfully downloaded stock data!")
    os.startfile(os.path.realpath("stock data/"))
    time.sleep(3)

if __name__ == "__main__":
    main()
