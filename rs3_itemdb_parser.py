import asyncio
import json
from playwright.async_api import async_playwright
import random
import time


# total items as of 7/2/2024 = 57098
# this will go until the current search range returns less than 100, and then break from loop.
item_start = 1
item_end = 100000

async def open_and_interact_with_website():
    async with async_playwright() as p:
        # Launch headlessly
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://chisel.weirdgloop.org/gazproj/mrid#1')
        time.sleep(1)
        print("Website opened")

        # uncheck "hide noted"
        if await page.is_checked('input#note'):
            await page.uncheck('input#note')
            time.sleep(.2)
        print("Unchecked 'Hide Noted'")

        data = [] 
        for start in range(item_start, item_end, 100):
            end = min(start + 99, item_end)

            # clear results
            await page.click('button#clear')
            time.sleep(.2)
            await page.wait_for_function("document.querySelector('#currentlist').textContent.trim() == ''")
            print("Cleared results")

            # search bar
            await page.fill('input#q', f'{start}-{end}')
            time.sleep(.2)
            print(f"Entered search range: {start}-{end}")

            # "go" and wait for the search to complete
            await page.click('button#go')
            time.sleep(.2)
            print("Started search")

            # wait until rows appear in the table body
            await page.wait_for_function("document.querySelector('#currentlist').textContent.trim() !== ''")
            time.sleep(.2)
            print(f"Data is loaded for range: {start}-{end}")

            # Extract data
            rows = await page.query_selector_all('tr.mridrow')
            last_id_found = False
            for row in rows:
                id_text = await (await row.query_selector('td.mrid-id')).text_content()
                if id_text == str(end):
                    last_id_found = True

                item = {
                    'id': id_text,
                    'name': await (await row.query_selector('td.mrid-name')).text_content(),
                    'tradeable': await (await row.query_selector('td.mrid-trade')).text_content(),
                    'members': await (await row.query_selector('td.mrid-mem')).text_content(),
                    'value': await (await row.query_selector('td.mrid-val')).text_content(),
                    'examine': await (await row.query_selector('td.mrid-examine')).text_content(),
                    'actions_inventory': await (await row.query_selector('td.mrid-inv')).text_content(),
                    'actions_worn': await (await row.query_selector('td.mrid-worn')).text_content(),
                    'actions_ground': await (await row.query_selector('td.mrid-ground')).text_content()
                }
                data.append(item)
            
            if last_id_found:
                print(f"Search Range is full for items {start}-{end}")
            else:
                print(f"Data collection stopped short at item ID {id_text} for range {start}-{end}, writing to JSON file")
                break  # Stop the loop if the last ID is not found (search range returns less than 100)

            # implicit wait to be considerate
            await asyncio.sleep(random.uniform(2, 4))

        # write to json
        with open('ItemDB.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("Data extracted and written to JSON file.")

        # close
        await browser.close()
        print("Browser closed")

# asyncio event loop
asyncio.run(open_and_interact_with_website())
