# Johnos Skate Shop Web Scraper

This Python project scrapes product data from the [Johnos Skate Shop](https://johnosskateshop.co.za/) website, allowing users to browse and save product information from specific categories into an Excel file.

---

## Features

- **Dynamic Category Selection**: Fetches and displays available product categories directly from the website.
- **Product Scraping**: Retrieves product names, prices, and links for a chosen category.
- **Data Export**: Saves scraped data into a well-formatted Excel file.
- **User-Friendly Interface**: Offers an intuitive way to select categories, save data, and continue or exit the script.

---

## Requirements

To run this project, ensure you have the following installed:

- Python 3.8 or newer
- Libraries:
  - `beautifulsoup4`
  - `requests`
  - `pandas`
  - `openpyxl`
  - `keyboard`

Install these libraries using pip:

```bash
pip install beautifulsoup4 requests pandas openpyxl keyboard
```

---

## How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/johnos-skate-shop-scraper.git
   ```
2. Navigate to the project directory:
   ```bash
   cd johnos-skate-shop-scraper
   ```
3. Run the script:
   ```bash
   python scraper.py
   ```

---

## User Guide

1. Upon running the script, it will display a list of available product categories.
2. Enter the number corresponding to the category you'd like to scrape.
3. The script will scrape product names, prices, and links, displaying them in your console.
4. Choose whether to save the data as an Excel file:
   - If "y(yes)", the data will be saved in the same directory as the script.
5. Continue scraping or exit the program.

---

## Output Example

Sample scraped data:

| Product Name       | Price    | Link                              |
|--------------------|----------|-----------------------------------|
| Skateboard A       | R1,200.00| https://johnosskateshop.co.za/... |
| Skateboard Wheels  | R300.00  | https://johnosskateshop.co.za/... |

Saved as an Excel file named: `category_name(number_of_items).xlsx`

---

## Potential Issues

- **Keyboard Library**: The `keyboard` library requires administrative privileges on some systems. Replace it with `input()` for simpler environments.
- **Dynamic Site Changes**: The website structure may change, requiring adjustments to the scraping logic.

---

## Contribution

Feel free to fork this repository and submit pull requests for improvements or bug fixes. Contributions are highly welcome as this is just a project developed as a proof of webscrapping concepts!

---

## Acknowledgments

- The website [Johnos Skate Shop](https://johnosskateshop.co.za/) for providing the data.
- Libraries used: `BeautifulSoup`, `Requests`, `Pandas`, and `OpenPyxl`.


