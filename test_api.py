from sercop_client import SercopClient
import json

client = SercopClient()

keywords = ["limpieza", "seguridad", "mantenimiento", "obra", "alimentos"]
years = [2024, 2025]

print("Testing SERCOP API...")

for year in years:
    print(f"\n--- Testing Year: {year} ---")
    for kw in keywords:
        print(f"Searching for '{kw}'...")
        results = client.search_processes(kw, year=year)
        if results and 'data' in results and len(results['data']) > 0:
            print(f"SUCCESS: Found {len(results['data'])} results for '{kw}' in {year}")
            # Print first result title to verify
            print(f"Sample: {results['data'][0].get('description')}")
        else:
            print(f"No results for '{kw}' in {year}")
