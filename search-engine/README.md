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

<img width="4741" height="2760" alt="image" src="https://github.com/user-attachments/assets/b646acb1-b5ae-48a4-8bf0-4fa882da6cd2" />


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

<img width="1030" height="796" alt="mapping" src="https://github.com/user-attachments/assets/855bfab2-0958-4538-aead-a943946df4f5" />

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

<img width="1920" height="755" alt="bulk" src="https://github.com/user-attachments/assets/eff632b0-6324-40fd-a5ad-5d85c504154d" />

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


