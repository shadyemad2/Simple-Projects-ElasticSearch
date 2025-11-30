# Centralized Linux Log Monitoring Using Filebeat + Elasticsearch + Kibana

This project demonstrates a **centralized log monitoring system** for Linux servers using Filebeat, sending logs directly to **Elasticsearch** (Elastic Cloud SaaS) and visualizing them in **Kibana**. Alerts can be configured for suspicious activity such as failed SSH logins.

**Features:** real-time log collection, parsing authentication logs, structured storage in Elasticsearch, Kibana dashboards for failed logins, top IPs, targeted users, alerts for brute-force login attempts, fully CLI and SaaS-friendly, production-ready without Logstash.

**Architecture:** Linux VM (Filebeat) → Elasticsearch (Elastic Cloud SaaS) → Kibana (Dashboards & Alerts)

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

