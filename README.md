# Elasticsearch Projects: 
<img width="3422" height="2281" alt="image" src="https://github.com/user-attachments/assets/6d464910-0e7c-4618-8905-22b0dc22f29c" />


## Project 1: Centralized Linux Log Monitoring
Collect Linux logs via **Filebeat** → **Elasticsearch (SaaS)** → visualize in **Kibana dashboards**.  
Features: failed SSH login detection, alerts for brute-force attempts.  
Steps: install Filebeat, configure `filebeat.yml`, enable system module, load dashboards, start service, generate test logs.  
Dashboards: Failed SSH logins (bar), login attempts over time.  
Alerts: e.g., failed SSH >5/min, notify via Email/Slack/Webhook. 


## Project 2: Simple Product Search Engine
CLI Python script searches products stored in **Elasticsearch**, supports filters, sorting, and **fuzzy search**.  
Features: search by name/description, filter by tag/max price, sort by most sold/lowest price, Kibana dashboards for top-selling & high-priced products, alerts for business metrics.  
Steps: load `products.json` to `project_products` index, run `products.py`, search via CLI, create Kibana visualizations and alerts.  

**Summary:** Two practical Elasticsearch projects: centralized log monitoring and CLI product search, fully SaaS-compatible, with dashboards and alerts, production-ready and expandable.
