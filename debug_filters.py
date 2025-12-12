from sercop_client import SercopClient
import datetime

client = SercopClient()

# Test Parameters
keyword = "limpieza"
year = 2024 # Try 2024 as it should have data
entity_filter = "" # Leave empty to test basic search first
process_types = ["Menor Cuantía", "Ínfima Cuantía"]

print(f"--- DEBUGGING SEARCH: '{keyword}' Year: {year} ---")

results = client.search_processes(keyword, year=year)

if not results or 'data' not in results:
    print("API returned NO data.")
else:
    data = results['data']
    print(f"API returned {len(data)} raw results.")
    
    # Simulate Filters
    filtered_count = 0
    for item in data:
        print(f"\nChecking Item: {item.get('description')}")
        print(f"  Type: {item.get('internal_type')}")
        print(f"  Buyer: {item.get('buyerName')}")
        print(f"  Date: {item.get('date')}")
        
        # 1. Process Type
        p_type = item.get('internal_type', '')
        if process_types and not any(pt.lower() in p_type.lower() for pt in process_types):
            print("  -> EXCLUDED by Process Type")
            continue
            
        # 2. Entity
        buyer_name = item.get('buyerName', '')
        if entity_filter and entity_filter.lower() not in buyer_name.lower():
            print("  -> EXCLUDED by Entity")
            continue
            
        print("  -> INCLUDED")
        filtered_count += 1

    print(f"\nFinal Filtered Count: {filtered_count}")
