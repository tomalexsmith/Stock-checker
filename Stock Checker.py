import yfinance as yf
import os
import time
from tqdm import tqdm
import csv
from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

tickers = []
valid_tickers = []
save_location = ''
temp_save_location = ''

def main():    
    os.system('mode con: cols=110 lines=30')
    root = Tk()
    root.withdraw()
    os.system('cls')
    load_location()
    load_tickers()
    menu()
    
def get_date():
    return datetime.today().strftime('%d-%m-%Y')    
    
def load_tickers():
    global tickers
    
    f = open("bin/9FC57240175EA04D234B1F5BD19AD441.txt", "r")
    lines = f.read().splitlines()
    
    for line in lines:
        tickers.append(line)    
        
    f.close()
    
def load_location():
    global save_location
    txt_path = os.path.realpath("bin/E2766325832A21B4B45E4FDBBB098206.txt")
    save_path = os.path.join(os.path.realpath('./'), 'stock data')
    
    if os.path.getsize(txt_path) == 0:
        save_location = save_path
        f = open(txt_path, "w")
        f.write(str(save_path))
        f.close()
        return
    
    f = open(txt_path, "r")
    save_location = f.read() 
    f.close()
        

def logo():
    print(
    '''     
███████╗████████╗ ██████╗  ██████╗██╗  ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██║ ██╔╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████╗   ██║   ██║   ██║██║     █████╔╝     ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
╚════██║   ██║   ██║   ██║██║     ██╔═██╗     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████║   ██║   ╚██████╔╝╚██████╗██║  ██╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚══════╝   ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝'''
    )
    print(''' _      __    _     ___   ___       ____  _   _       __    _      __    ____ 
\ \_/  / /\  | |_| / / \ / / \     | |_  | | | |\ |  / /\  | |\ | / /`  | |_  
 |_|  /_/--\ |_| | \_\_/ \_\_/     |_|   |_| |_| \| /_/--\ |_| \| \_\_, |_|__ '''
    )
    print('\n\n')    
def menu_choice():
    return int(input("Enter your choice: "))

def save_location_menu():
    global temp_save_location
    global save_location
    
    while True:
        os.system('cls')
        logo()
        print("Save location")
        print("───────────────────────────────────────────────────────────────────────────────────────")
        print("Current save location: '" + save_location + "'")
        if temp_save_location:
            print("New save location: '" + temp_save_location + "'\n")
        else:
            print('')
        print("1. Change save location")
        print("2. Set to default save location")
        print("3. Confirm changes")
        print("4. Cancel")
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
                change_save_location()
            case 2:
                default_save_location()
            case 3:
                confirm_save_location()
                temp_save_location = ''
                return
            case 4:
                temp_save_location = ''
                return
            
        os.system('cls')
    
    
def change_save_location():
    global root   
    global temp_save_location
    os.system('cls')
    logo()
    f = filedialog.askdirectory(title='Save location', initialdir=os.path.expanduser("~"))
    
    if f:
        temp_save_location = f + '/stock data'
        


def default_save_location():   
    global temp_save_location
    
    temp_save_location = os.path.join(os.path.realpath('./'), 'stock data')
    

def confirm_save_location():
    global save_location
    global temp_save_location
    txt_path = os.path.realpath("bin/E2766325832A21B4B45E4FDBBB098206.txt")

    save_location = temp_save_location
    
    f = open(txt_path, "w")
    f.write(save_location)
    f.close()
    
def options_menu():
    while True:
        os.system('cls')
        logo()
        print("Options")
        print("───────────────────────────────────────────────────────────────────────────────────────")
        print("1. Add tickers")
        print("2. Remove a ticker")
        print("3. Clear list of tickers")
        print("4. Change stock data save location")
        print("5. Back")
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
                save_location_menu()
            case 5:
                return
            
        os.system('cls')


def menu():    
    while True:
        logo()
        print("Main menu")
        print("───────────────────────────────────────────────────────────────────────────────────────")
        print("1. GET STOCK DATA")
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
    
    f = open("bin/9FC57240175EA04D234B1F5BD19AD441.txt", "w")
    
    for ticker in tickers:
        f.write(str(ticker) + "\n")
    
    f.close()
    exit()  
            

def clear_tickers():
    global tickers
    
    valid_choice = False
    
    while not valid_choice:
        valid_choice = False
        os.system('cls')
        logo()
        confirm = input("Are you sure you want to clear the list of tickers? (y/n): ").lower()
        
        if confirm == 'y':
            tickers = []
            valid_choice = True
            
            os.system('cls')
            logo()

            for i in tqdm(range(100), desc='Clearing tickers...'):
                time.sleep(0.005)
            
            time.sleep(0.5)    
            print("\n\nSuccessfully cleared tickers!")
            time.sleep(2)
        elif confirm == 'n':
            return
        else:
            os.system('cls')
            logo()
            print("Please enter a valid selection...")
            time.sleep(3)

def check_tickers():
    global valid_tickers
    
    f = open("bin/40CBE43828B87C2959741245FADFDAD0.csv", "r")
    csv_dl = csv.DictReader(f)
    for row in csv_dl:
        ticker = str(row["Symbol"])
        valid_tickers.append(ticker)
        
    f.close()

def add_tickers():
    global valid_tickers
    global tickers 
    valid_choice = False
    duplicate = False
    ticker = ''
    
    os.system('cls')
    logo()
    
    ticker = input("Enter a ticker (type 'end' to finish): ")
    
    if ticker.lower() == 'end':
        return
    
    if ticker.upper() in tickers:
        os.system('cls')
        logo()
        print("{0} is already in the list of tickers...".format(ticker.upper()))
        time.sleep(2)
        add_tickers()
        return
    
    if not valid_tickers:
        check_tickers()
    
    if ticker.upper() not in valid_tickers:
        while not valid_choice:
            valid_choice = False
            os.system('cls')
            logo()
            confirm = input("Are you sure {} is correct? (y/n): ".format(ticker.upper())).lower()
            
            if confirm == 'y':
                valid_choice = True
                break
            elif confirm == 'n':
                add_tickers()
                return
            else:
                os.system('cls')
                logo()
                print("Please enter a valid selection...")
                time.sleep(3)
        
    tickers.append(ticker.upper())
    os.system('cls')
    logo()

    for i in tqdm(range(100), desc='Adding ticker...'):
        time.sleep(0.001)
    
    time.sleep(0.5) 
    print("\n\nSuccessfully added {}!".format(ticker.upper()))
    time.sleep(2)
    
    add_tickers()
    return
    
    # valid_choice = False
    
    # while not valid_choice:
    #     valid_choice = False
    #     os.system('cls')
    #     logo()
    #     confirm = input("Would you like to add another ticker? (y/n): ").lower()
        
    #     if confirm == 'y':
    #         add_tickers()
    #         return
    #     elif confirm == 'n':
    #         return
    #     else:
    #         os.system('cls')
    #         logo()
    #         print("Please enter a valid selection...")
    #         time.sleep(3)
    

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
    
    try:
        os.mkdir(save_location)
    except:
        pass
    
    try:
        os.mkdir(save_location+'/'+date)
    except:
        pass
    
    for i in tickers:
        ticker = yf.Ticker(i)
        df_tick = ticker.history(period='5y')
        df_tick = df_tick.reset_index()
        try:
            df_tick.to_csv(save_location+'/'+date+"/"+i+" "+date+".csv")
        except:
            pass
        
    for i in tqdm(range(100), desc='Downloading stock data...'):
        time.sleep(0.001)
        
    time.sleep(0.5)
    print("\n\nSuccessfully downloaded stock data!")
    os.startfile(save_location+ '/' + date)
    time.sleep(3)

if __name__ == "__main__":
    main()
