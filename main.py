from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl
import keyboard
import re
import os

print("*****************************************************************************")
print("            Welcome to the Johnos Skate Shop webscrapper")
print("*****************************************************************************")
print("")

while True:
    home_url = "https://johnosskateshop.co.za/?v=3df2295b05d9"
    r = requests.get(home_url)
    home_soup = BeautifulSoup(r.text, "lxml")

    categories_div = home_soup.find("div", class_ = "woof_block_html_items")
    categories_inputs = categories_div.find_all("input", type="hidden")

    print("Available product categories:\n")
    num = 1
    for category in categories_inputs:
        category_val = category.get('value')
        print(f"{num}. {category_val}") 
        num += 1

    cat = input("\nEnter the category number you want to scrape: ")

    base_url = "https://johnosskateshop.co.za/shop/?swoof=1&v=3df2295b05d9&product_cat="

    select_tag = home_soup.find("select", {"id": "woof_tax_select_product_cat"})
    if select_tag:
        # Extract all <option> tags and create a dictionary of category names and URLs
        options = select_tag.find_all("option")
        categories = {
        str(i): {"name": option.text.strip(), "url": f"{base_url}{option['value']}"}
        for i, option in enumerate(options[1:], start=1)  # Skip the first <option> with value '0'
        if option['value'] != "0" and not option.get("disabled")
        }


    url = categories[cat]['url']


    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")

    products_ul_tag = soup.find("ul", class_ = "products columns-4")
    products = products_ul_tag.find_all("a", class_ = "botiga-wc-loop-product__title")
    prices = products_ul_tag.find_all("span", class_ ="woocommerce-Price-amount amount")

    product_names = [product.text.strip() for product in products]
    links = [link.get("href") for link in products[:len(product_names)]]
    product_prices = [price.text for price in prices[:len(product_names)]]

    df = pd.DataFrame({"Product Name": product_names, "Price": product_prices, "Link": links})

    print(df)

    save = input("Do you want to save the data in an Excel file? (y/n): ")

    if save.lower() == "y":
        script_directory = os.path.dirname(os.path.realpath(__file__))

        file_head = categories[cat]["name"].replace(" ", "_").replace("/", "-")
        file_head = re.sub(r'[<>:"/\\|?*]', "", file_head)  # Remove invalid characters
        file_name = f"{file_head}.xlsx"
        file_path = os.path.join(script_directory, file_name)

        df.to_excel(file_path, index=False)  # Save the file without the index column
        print(f"Data has been successfully saved to {file_name}!")
    else:
        print("Big Shout Out!")

    print("\nPress 'Esc' to exit or any other key to continue...\n")
    event = keyboard.read_event()  # This will wait for a key press event
    if event.name == 'esc':  # Check if the pressed key is 'Esc'
        print("Exiting the program. Goodbye!")
        break
    else:
        continue
