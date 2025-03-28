import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
import re

def get_usd_price():
    url = "https://alanchand.com/currencies-price/usd"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    prices = [td.text for td in soup.find_all("td", attrs={"data-v-c1354816": ""})]
    return str(prices) if prices else None

def setup_database():
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usd (date TEXT PRIMARY KEY,price TEXT)''')
    conn.commit()
    return conn, cursor

def insert_or_update_price(cursor, date_str, price):
    cursor.execute('''INSERT INTO usd (date, price) VALUES (?, ?) ON CONFLICT(date) DO UPDATE SET price = excluded.price''', (date_str, price))

def get_today_usd_price(cursor):
    date_str = datetime.today().strftime("%Y-%m-%d")
    cursor.execute("SELECT price FROM usd WHERE date = ?", (date_str,))
    result = cursor.fetchone()
    
    if result:
        try:
            prices_list = eval(result[0]) 
            if len(prices_list) > 1:
                price_digits = re.sub(r'\D', '', prices_list[4]) 
                price_digits = price_digits[:-3]+","+price_digits[-3:]
                return price_digits if price_digits else "Price not found."
        except Exception:
            return "Invalid data format."

    return "No data available for today."

def main():
    conn, cursor = setup_database()
    price = get_usd_price()
    
    if price:
        date_str = datetime.today().strftime("%Y-%m-%d")
        insert_or_update_price(cursor, date_str, price)
        conn.commit()
        print(f"USD price updated for {date_str}: {price}")
    else:
        print("Failed to fetch USD price.")
    
    usd = get_today_usd_price(cursor)
    conn.close()
    
    return(usd)

if __name__ == "__main__":
    main()