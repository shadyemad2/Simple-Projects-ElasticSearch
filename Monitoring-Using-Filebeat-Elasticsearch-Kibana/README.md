## centralized log monitoring system (Filbeat + ElasticSearch + Kibana)
<img width="1282" height="712" alt="filebeat-conf" src="https://github.com/user-attachments/assets/8a57b7b5-8d7b-4304-adea-a6f3de3b75b3" /># Centralized Linux Log Monitoring Using Filebeat + Elasticsearch + Kibana 
This project demonstrates a **centralized log monitoring system** for Linux servers using Filebeat, sending logs directly to **Elasticsearch** (Elastic Cloud SaaS) and visualizing them in **Kibana**. Alerts can be configured for suspicious activity such as failed SSH logins.

<img width="969" height="613" alt="image" src="https://github.com/user-attachments/assets/a0363c7c-5bce-4611-a0ac-d763cba47edc" />

**Features:** 
real-time log collection, parsing authentication logs, structured storage in Elasticsearch, Kibana dashboards for failed logins, alerts for brute-force login attempts, fully CLI and SaaS-friendly.

**Architecture:** Linux VM (Filebeat) → Elasticsearch (Elastic Cloud SaaS) → Kibana (Dashboards & Alerts)

## 📁 Steps

1. Install Filebeat:
sudo dnf install filebeat -y
sudo systemctl enable filebeat

<img width="1124" height="456" alt="filebeat-status" src="https://github.com/user-attachments/assets/e4a2d294-aa49-4017-93c2-bc5419028a5d" />
<img width="716" height="247" alt="filebeat" src="https://github.com/user-attachments/assets/3d6655cd-a46c-4cd1-a33f-bab67a0e6501" />

3. Configure Filebeat (`/etc/filebeat/filebeat.yml`):
output.elasticsearch:
  hosts: ["<ELASTICSEARCH_ENDPOINT>"]
  username: "elastic"
  password: "<CLOUD_PASSWORD>"

setup.kibana:
  host: "<KIBANA_ENDPOINT>"
  
<img width="1282" height="712" alt="filebeat-conf" src="https://github.com/user-attachments/assets/01966b88-60b5-4609-af96-c75d4a95b941" />

3. Enable system module, load dashboards, and start Filebeat:

sudo filebeat modules enable system
sudo filebeat setup
sudo systemctl start filebeat
sudo journalctl -u filebeat -f

5. Generate Test Logs:
sudo sed -i 's/#*PubkeyAuthentication yes/PubkeyAuthentication no/' /etc/ssh/sshd_config
sudo systemctl restart sshd
ssh invaliduser@localhost

<img width="1330" height="741" alt="test-ssh" src="https://github.com/user-attachments/assets/7518522a-aa5c-4539-890c-b0a54eff67d3" />

7. Kibana Setup:
- Create Data View: Name `linux-logs`, Index pattern `filebeat-*`, Timestamp field `@timestamp`
  <img width="1920" height="863" alt="Screenshot (2206)" src="https://github.com/user-attachments/assets/33af4ebd-694f-4a98-afad-af82827bb4a0" />
  <img width="1912" height="795" alt="d" src="https://github.com/user-attachments/assets/059f8549-1284-4f8d-adef-7a6180a18b89" />

- Dashboards Examples:
  Failed Login Attempts Over Time: Area chart `@timestamp` vs count
  <img width="1920" height="810" alt="1" src="https://github.com/user-attachments/assets/6a0df805-8787-42b4-a32a-3f5f7bdd392b" />
  <img width="1920" height="695" alt="2" src="https://github.com/user-attachments/assets/e9209200-d144-4213-882d-04e8daf5935a" />

6. Alerts:
- Rule: failed SSH attempts > 5 in 1 minute
- Filter: `system.auth.ssh.event: "Failed password"`
- Notify via Email / Slack / Webhook
Screenshot placeholder: [Alert Screenshot]

7. Queries (KQL Examples):
- Failed login attempts: `system.auth.ssh.event : "Failed password"`
- Logs from specific IP: `source.ip : "192.168.1.10"`
- Filter SSH logs: `process.name : "sshd"`


### Summary

Collect logs from Linux servers using Filebeat directly to Elasticsearch, parse and structure logs with ingest pipelines, visualize and analyze logs in Kibana dashboards, configure alerts for suspicious activity, fully functional production-ready demo without Logstash.


Emad
