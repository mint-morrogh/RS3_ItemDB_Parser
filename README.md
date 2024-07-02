# RS3_ItemDB_Parser

This repository contains a Python script that uses the Playwright library to scrape item data from the website `https://chisel.weirdgloop.org/gazproj/mrid#1`. The script navigates through the website, extracting item data and saving it in a JSON format.

## Features

- **Automated Browsing**: Uses Playwright to navigate and interact with the website headlessly.
- **Data Extraction**: Extracts data such as item ID, name, tradeability, if member item, value, description, and available actions.
- **Dynamic Paging**: Searches through the item database in batches of 100 until a specified end, or when the returned data is less than determined range.
- **Error Handling**: Stops execution if the expected number of items are not found, preventing incomplete data scraping.
- **Output**: Saves the extracted data into `ItemDB.json`.

## Prerequisites

To run this script, you will need Python 3.8 or later and the Playwright Python package. You can install Playwright using pip:

```bash
pip install playwright
playwright install
```

The data fetched by the script is saved in the ItemDB.json file within the same directory. Each entry in the JSON file represents an item with its details as described above.

Configuration
You can adjust the following variables at the beginning of the script to change the behavior of the data scraping process:

item_start: The starting ID for the item data scraping.
item_end: The upper limit for the item data scraping, which is set high by default to cover all possible items.
