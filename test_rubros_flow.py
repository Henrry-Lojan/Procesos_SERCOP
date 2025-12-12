
import pandas as pd
from sercop_client import SercopClient

client = SercopClient()

print("--- Simulating App Flow ---")
# 1. Search
keyword = "seguridad"
year = 2024
print(f"Searching for '{keyword}' in {year}...")
results = client.search_processes(keyword, year=year)

if results and 'data' in results and len(results['data']) > 0:
    data = results['data']
    print(f"Found {len(data)} results.")
    
    # 2. Simulate User Selection (First row)
    selected_index = 0
    selected_item = data[selected_index]
    selected_ocid = selected_item.get('ocid')
    print(f"User selected row {selected_index}, OCID: {selected_ocid}")
    
    # 3. Fetch Details (Rubros Logic)
    print("Fetching details...")
    details = client.get_process_details(selected_ocid)
    
    if details:
        print("Details fetched successfully.")
        try:
            # Logic from app.py
            items = details['releases'][0]['tender']['items']
            if items:
                print(f"Found {len(items)} items (rubros).")
                for i, item in enumerate(items):
                    desc = item.get('description', 'N/A')
                    qty = item.get('quantity', 0)
                    unit_price = item.get('unit', {}).get('value', {}).get('amount', 0)
                    print(f"  Item {i+1}: {desc} | Qty: {qty} | Price: {unit_price}")
            else:
                print("No items found in tender data.")
        except Exception as e:
            print(f"Error extracting items: {e}")
            # print(details)
    else:
        print("Failed to fetch details.")

else:
    print("No results found to test selection.")
