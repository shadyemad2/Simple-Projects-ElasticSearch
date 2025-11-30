






**Steps:**
1. Install Filebeat:
sudo dnf install filebeat -y
sudo systemctl enable filebeat

2. Configure Filebeat (`/etc/filebeat/filebeat.yml`):
output.elasticsearch:
  hosts: ["<ELASTICSEARCH_ENDPOINT>"]
  username: "elastic"
  password: "<CLOUD_PASSWORD>"

setup.kibana:
  host: "<KIBANA_ENDPOINT>"

3. Enable system module, load dashboards, and start Filebeat:
sudo filebeat modules enable system
sudo filebeat setup
sudo systemctl start filebeat
sudo journalctl -u filebeat -f

4. Generate Test Logs:
sudo sed -i 's/#*PubkeyAuthentication yes/PubkeyAuthentication no/' /etc/ssh/sshd_config
sudo systemctl restart sshd
ssh invaliduser@localhost

5. Kibana Setup:
- Create Data View: Name `linux-logs`, Index pattern `filebeat-*`, Timestamp field `@timestamp`
- Dashboards Examples:
  - Failed SSH Login Attempts: Bar chart `source.ip` vs count
  - Top Targeted Usernames: Pie chart `user.name`
  - Login Attempts Over Time: Area chart `@timestamp` vs count
  Screenshots placeholders: [Dashboard 1]  [Dashboard 2]  [Dashboard 3]

6. Alerts:
- Rule: failed SSH attempts > 5 in 1 minute
- Filter: `system.auth.ssh.event: "Failed password"`
- Notify via Email / Slack / Webhook
Screenshot placeholder: [Alert Screenshot]

7. Queries (KQL Examples):
- Failed login attempts: `system.auth.ssh.event : "Failed password"`
- Logs from specific IP: `source.ip : "192.168.1.10"`
- Filter SSH logs: `process.name : "sshd"`

**Project Structure:**
elk-log-monitoring/
├── filebeat-config/
│   └── filebeat.yml
├── docs/
│   ├── dashboard-1.png
│   ├── dashboard-2.png
│   └── alert-example.png
└── README.md

**Summary:** Collect logs from Linux servers using Filebeat directly to Elasticsearch, parse and structure logs with ingest pipelines, visualize and analyze logs in Kibana dashboards, configure alerts for suspicious activity, fully functional production-ready demo without Logstash.






# Centralized Linux Log Monitoring Using Filebeat + Elasticsearch + Kibana 
This project demonstrates a **centralized log monitoring system** for Linux servers using Filebeat, sending logs directly to **Elasticsearch** (Elastic Cloud SaaS) and visualizing them in **Kibana**. Alerts can be configured for suspicious activity such as failed SSH logins.



**Features:** 
real-time log collection, parsing authentication logs, structured storage in Elasticsearch, Kibana dashboards for failed logins, alerts for brute-force login attempts, fully CLI and SaaS-friendly.

**Architecture:** Linux VM (Filebeat) → Elasticsearch (Elastic Cloud SaaS) → Kibana (Dashboards & Alerts)

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

## Author
Shady Emad
