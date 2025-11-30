# 🔎 Simple Product Search Engine  
### Elasticsearch SaaS + Python Fuzzy Search CLI + Kibana Dashboards & Alerts

A practical mini–search-engine project built using **Elasticsearch SaaS**, a Python CLI interface with **Fuzzy Search (auto-correct)**, and full data visualization using **Kibana Dashboards & Alerts**.

This project simulates a real-world product search engine using a simple `products.json` dataset.

<img width="4741" height="2760" alt="image" src="https://github.com/user-attachments/assets/b646acb1-b5ae-48a4-8bf0-4fa882da6cd2" />


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


```
products.json → Elasticsearch Index
             → Python CLI Search
             → Kibana Dashboards + Alerts
```

---

## 📁 2. Dataset (products.json)

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

## 📤 3. Uploading Data to Elasticsearch SaaS

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

## 🐍 4. Python Search CLI (with fuzziness)

Create `products.py`:

<img width="761" height="411" alt="test-search" src="https://github.com/user-attachments/assets/560583b0-d2c5-47d6-9f50-f354d4047214" />
<img width="1076" height="725" alt="test-search0" src="https://github.com/user-attachments/assets/5f779013-6460-4c09-be52-7dd081e74936" />
<img width="1085" height="615" alt="test-search1" src="https://github.com/user-attachments/assets/e4a9348d-b13c-4e21-bceb-0f9a238a258c" />


---

## 📊 5. Kibana Dashboards

### 📈 Dashboard 1 — Top Selling Products  
### 💰 Dashboard 2 — Highest Price Distribution (Pie Chart)  
<img width="1920" height="817" alt="dashboards0" src="https://github.com/user-attachments/assets/d2c6e7ec-4dc8-45bc-afd6-1cc0e0a4024f" />

### 🏷️ Dashboard 3 — Active vs Inactive products
<img width="1088" height="528" alt="dashboard1" src="https://github.com/user-attachments/assets/d3cc0407-a8de-4643-8a20-8344798699fb" />


---

## 🚨 6. Alerts Example

Sample alert (price above threshold):

step-1
<img width="1920" height="876" alt="alert0" src="https://github.com/user-attachments/assets/89108170-a505-4f65-bd3d-c47484c95274" />
step-2
<img width="1920" height="821" alt="alert1" src="https://github.com/user-attachments/assets/4e864c4c-15b0-4fd6-8b72-57b513f488bf" />
step-3
<img width="1912" height="880" alt="alert2" src="https://github.com/user-attachments/assets/c30a049a-04f2-4a82-ba92-95f6d4f3568d" />
step-4
<img width="1918" height="843" alt="alert3" src="https://github.com/user-attachments/assets/24e53f73-7a75-481a-a819-4a976e0b690f" />
step-5
<img width="1133" height="708" alt="alert4" src="https://github.com/user-attachments/assets/1094e76b-79a0-45f6-9e58-8fefff26bc54" />

---

## 📂 7. Project Structure

```
.
├── products.py
├── products.json
├── README.md

```

---

## 🎯 8. What You Learn from This Project

✔ How Elasticsearch indexes text  
✔ How to use Python to perform full-text search  
✔ How fuzzy search works (`fuzziness: AUTO`)  
✔ How to build dashboards in Kibana  
✔ How to create alerts  
✔ How search engines filter, sort, and rank results  
✔ A real, fully working mini search engine  

---

---

## Author
Shady Emad




