
import requests
import json
from sercop_client import SercopClient

client = SercopClient()

# Test search
print("--- Testing Search ---")
results = client.search_processes("seguridad", year=2024)
if results and 'data' in results and len(results['data']) > 0:
    first_result = results['data'][0]
    print(f"First result OCID: {first_result.get('ocid')}")
    print(f"Keys in first result: {list(first_result.keys())}")
    
    # Check if items are in the search result
    if 'items' in first_result:
        print("Items found in search result!")
    else:
        print("Items NOT found in search result.")

    # Test get_process_details
    print("\n--- Testing Details ---")
    ocid = first_result.get('ocid')
    details = client.get_process_details(ocid)
    if details:
        # Save to file to inspect just in case
        with open("details_sample.json", "w") as f:
            json.dump(details, f, indent=2)
        
        # Check structure for items
        # customized for likely OCDS structure: data.records[0].compiledRelease.tender.items ?
        # or simplified.
        print(f"Keys in details: {list(details.keys())}")
else:
    print("No results found or error.")
