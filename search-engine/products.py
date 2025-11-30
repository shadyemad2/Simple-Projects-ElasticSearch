from elasticsearch import Elasticsearch

es = Elasticsearch(
    cloud_id="shady-deployment:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyQzMzZkY2UzOTUzYWI0NGRlODNhNDI2NjMyMTNhN2FhNyQ4MGRmMGI5ZDM2Yzg0NjhhYTI2YjU5MjdiMzk2MTBiMQ==",
    basic_auth=("elastic", "LblkxvmmwszS5N2gJZGz3jpn")
)

index_name = "project_products"

def search_products():
    keyword = input("Enter search keyword: ")
    
    # Optional filters
    tag_filter = input("Filter by tag (press Enter to skip): ")
    max_price = input("Max price (press Enter to skip): ")
    
    sort_choice = input("Sort by (1-Most sold, 2-Lowest price, press Enter for default): ")
    
    # Fuzziness added here
    query = {
        "query": {
            "bool": {
                "must": [
                    {"multi_match": {
                        "query": keyword,
                        "fields": ["name", "description"],
                        "fuzziness": "AUTO"  # ← Fuzziness enabled
                    }}
                ],
                "filter": []
            }
        }
    }
    
    # Add tag filter
    if tag_filter:
        query["query"]["bool"]["filter"].append({"term": {"tags": tag_filter}})
        
    # Add price filter
    if max_price:
        query["query"]["bool"]["filter"].append({"range": {"price": {"lte": float(max_price)}}})
    
    # Sorting
    if sort_choice == "1":
        query["sort"] = [{"sold": {"order": "desc"}}]
    elif sort_choice == "2":
        query["sort"] = [{"price": {"order": "asc"}}]
    
    results = es.search(index=index_name, body=query)
    
    print("\nSearch Results:")
    if results['hits']['total']['value'] == 0:
        print("No results found.")
    for hit in results['hits']['hits']:
        src = hit["_source"]
        print(f"- {src['name']} | ${src['price']} | Sold: {src['sold']} | Tags: {src['tags']}")

def main():
    print("=== Product Search CLI ===")
    while True:
        print("\n1. Search products")
        print("2. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            search_products()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

