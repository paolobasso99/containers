# Monitoring client
This set of docker services and configurations is to be applied to every server you want to monitor.

## Prerequisites
### On the centralized monitoring server
1. Loki
2. Prometheus
### On the host you want to monitor
1. Docker
2. Docker Compose
3. Traefik Proxy

## Explaination
With this setup you will send useful metrics to a centralized Prometheus and Loki server.
Under your \$MONITORING_SUBDOMAIN.\$DOMAIN (configurable in the `.env` file) you will find the metrics exposed:
| Service       | Path             | Metrics Path             |
| ------------- | ---------------- | ------------------------ |
| node-exporter | `/node-exporter` | `/node-exporter/metrics` |
| cAdvisor      | `/cadvisor`      | `/cadvisor/metrics`      |
You will also be able to have all you docker containers' logs, aswell as the machine varlogs available in Loki.
You may want to ship other logs using promtail.

## Setup
### Send Docker container logs to Loki
1. Install `grafana/loki-docker-driver` with: `docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions`
2. Add this code to `/etc/docker/daemon.json`:
  ```json
  {
    ...
    "debug" : true,
    "log-driver": "loki",
    "log-opts": {
        "loki-url": "https://<user><password>@loki.example.com/loki/api/v1/push",
        "loki-batch-size": "400",
        "loki-tenant-id": "servername"
    }
  }
  ```
3. Restart the Docker Daemon: `sudo systemctl restart docker.service`

### Installing containers
1. Clone this repository
2. Copy `.env.example` to `.env` and edit. WARNING: It is suggested to use the same credentials for every client you setup in order to use only one Prometheus job.
3. Edit `promtail/config/promtail-config.yml`
4. Run `docker-compose up -d`