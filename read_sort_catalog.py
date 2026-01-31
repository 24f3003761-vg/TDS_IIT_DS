from unicodedata import category

# i want to read the catalog json file, 
# 1. Filter out any product with price < 80.78.
# 2. Sort the remaining items by:
#        category (A→Z)
#        then price (highest→lowest)
#         then name (A→Z)
# 3. print the minified json of the sorted list.
import json
def read_sort_catalog(file_path):
    with open(file_path, 'r') as file:
        catalog = json.load(file)

    # Step 1: Filter out products with price < 80.78
    filtered_catalog = [item for item in catalog if item['price'] >= 80.78]

    # Step 2: Sort the remaining items
    sorted_catalog = sorted(
        filtered_catalog,
        key=lambda x: (x['category'], -x['price'], x['name'])
    )

    # Step 3: Print the minified JSON of the sorted list
    print(json.dumps(sorted_catalog, separators=(',', ':')))

# main function to call the read_sort_catalog
if __name__ == "__main__":
    read_sort_catalog('catalog.json')