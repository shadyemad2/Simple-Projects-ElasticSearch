# 🔎 Simple Product Search Engine  
### Elasticsearch SaaS + Python Fuzzy Search CLI + Kibana Dashboards & Alerts

A practical mini–search-engine project built using **Elasticsearch SaaS**, a Python CLI interface with **Fuzzy Search (auto-correct)**, and full data visualization using **Kibana Dashboards & Alerts**.

This project simulates a real-world product search engine using a simple `products.json` dataset.

---

## 📌 1. Project Overview

The system allows you to:

- Upload a product catalog (`products.json`) into Elasticsearch  
- Search products using a Python CLI interface  
- Support fuzzy search for typo tolerance (e.g., `iphon` → `iPhone`)  
- Apply filters (tags, max price)  
- Apply sorting (most sold, lowest price)  
- Build interactive dashboards in Kibana  
- Create price/misbehavior alerts  

This project demonstrates the core building blocks of real search engines.

---

## 🏗️ 2. Architecture Diagram

> *(Insert image here: `screenshots/architecture.png`)*

```
products.json → Elasticsearch Index
             → Python CLI Search
             → Kibana Dashboards + Alerts
```

---

## 📁 3. Dataset (products.json)

Example dataset:

```json
[
  {
    "name": "iPhone 15",
    "description": "Latest Apple smartphone",
    "price": 1200,
    "sold": 540,
    "tags": ["mobile", "apple"]
  },
  {
    "name": "MacBook Air M2",
    "description": "Lightweight powerful laptop",
    "price": 1600,
    "sold": 320,
    "tags": ["laptop", "apple"]
  }
]
```

---

## 📤 4. Uploading Data to Elasticsearch SaaS

### 1️⃣ Create an Index with Mappings

Kibana → Dev Tools:

```json
PUT project_products
{
  "mappings": {
    "properties": {
      "name": { "type": "text" },
      "description": { "type": "text" },
      "tags": { "type": "keyword" },
      "price": { "type": "float" },
      "sold": { "type": "integer" }
    }
  }
}
```

### 2️⃣ Bulk Upload Your Products

```json
POST project_products/_bulk
{ "index": {} }
{ "name": "iPhone 15", "description": "...", "price": 1200, "sold": 540, "tags": ["mobile"] }
{ "index": {} }
{ "name": "MacBook Air M2", "description": "...", "price": 1600, "sold": 320, "tags": ["laptop"] }
```

---

## 🐍 5. Python Search CLI (with fuzziness)

Create `products.py`:

```python
from elasticsearch import Elasticsearch

es = Elasticsearch(
    cloud_id="YOUR_CLOUD_ID",
    basic_auth=("elastic", "YOUR_PASSWORD")
)

index_name = "project_products"

def search_products():
    keyword = input("Enter search keyword: ")

    tag_filter = input("Filter by tag (press Enter to skip): ")
    max_price = input("Max price (press Enter to skip): ")

    sort_choice = input("Sort by (1-Most sold, 2-Lowest price, press Enter for default): ")

    query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "multi_match": {
                            "query": keyword,
                            "fields": ["name", "description"],
                            "fuzziness": "AUTO"
                        }
                    }
                ],
                "filter": []
            }
        }
    }

    if tag_filter:
        query["query"]["bool"]["filter"].append({"term": {"tags": tag_filter}})

    if max_price:
        query["query"]["bool"]["filter"].append(
            {"range": {"price": {"lte": float(max_price)}}}
        )

    if sort_choice == "1":
        query["sort"] = [{"sold": {"order": "desc"}}]
    elif sort_choice == "2":
        query["sort"] = [{"price": {"order": "asc"}}]

    results = es.search(index=index_name, body=query)

    print("\nSearch Results:")
    if results['hits']['total']['value'] == 0:
        print("No results found.\n")

    for hit in results['hits']['hits']:
        src = hit["_source"]
        print(
            f"- {src['name']} | ${src['price']} | Sold: {src['sold']} | Tags: {src['tags']}"
        )

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
```

Run it:

```bash
python3 products.py
```

---

## 📊 6. Kibana Dashboards

### 📈 Dashboard 1 — Top Selling Products  
> *(Insert image: `screenshots/top_selling.png`)*

### 💰 Dashboard 2 — Highest Price Distribution (Pie Chart)  
> *(Insert image: `screenshots/highest_prices.png`)*

### 🏷️ Dashboard 3 — Tags Distribution  
> *(Insert image: `screenshots/tags_distribution.png`)*

---

## 🚨 7. Alerts Example

Sample alert (price above threshold):

> *(Insert image: `screenshots/alert.png`)*

---

## 📂 8. Project Structure

```
.
├── products.py
├── products.json
├── README.md
└── screenshots/
      architecture.png
      top_selling.png
      highest_prices.png
      tags_distribution.png
      alert.png
```

---

## 🎯 9. What You Learn from This Project

✔ How Elasticsearch indexes text  
✔ How to use Python to perform full-text search  
✔ How fuzzy search works (`fuzziness: AUTO`)  
✔ How to build dashboards in Kibana  
✔ How to create alerts  
✔ How search engines filter, sort, and rank results  
✔ A real, fully working mini search engine  

---

## 🚀 10. Perfect for Your LinkedIn / GitHub Portfolio

This project shows strong skills in:

- Search engines  
- Python scripting  
- Data indexing  
- Cloud Elasticsearch  
- Dashboarding  
- Monitoring & Alerts  

---

## 🎉 Done!

If you want:
- A better diagram  
- A GitHub description  
- A LinkedIn post template  
Just tell me!


