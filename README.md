# RS3_ItemDB_Parser

This repository contains a Python script that uses the Playwright library to scrape item data from the website `https://chisel.weirdgloop.org/gazproj/mrid#1`. The script navigates through the website, extracting item data and saving it in a JSON format.

## Features

- **Automated Browsing**: Uses Playwright to navigate and interact with the website headlessly.
- **Data Extraction**: Extracts data such as item ID, name, tradeability, membership status, value, description, and available actions.
- **Dynamic Paging**: Searches through the item database in batches of 100 until a specified end or when the returned data is less than expected.
- **Error Handling**: Stops execution if the expected number of items are not found, preventing incomplete data scraping.
- **Output**: Saves the extracted data into `ItemDB.json`.

## How It Works

The script starts at a specified item ID and attempts to fetch data up to a specified maximum ID. It queries the website in batches of 100 items. If the last expected item of any batch isn't found, it assumes that it has reached the end of the available data and stops the script.

## Prerequisites

To run this script, you will need Python 3.8 or later and the Playwright Python package. You can install Playwright using pip:

```bash
pip install playwright
playwright install
Running the Script
To execute the script, navigate to the directory containing item_scraper.py and run the following command:

bash
Copy code
python item_scraper.py
Output
The data fetched by the script is saved in the ItemDB.json file within the same directory. Each entry in the JSON file represents an item with its details as described above.

Configuration
You can adjust the following variables at the beginning of the script to change the behavior of the data scraping process:

item_start: The starting ID for the item data scraping.
item_end: The upper limit for the item data scraping, which is set high by default to cover all possible items.
