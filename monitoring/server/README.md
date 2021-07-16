# Monitoring Server
This set of docker services and configurations is to create a centralized server monitor.
If you ant to monitor the machine where you install these tools you should also setup `monitoring-client`

## Prerequisites
1. Docker
2. Traefik

## Services
1. Prometheus
2. Grafana
3. Loki

## Setup
1. Clone this repository
2. Copy `.env.example` to `.env` and edit
3. Edit `prometheus/config/prometheus.yml` to configure prometheus
3. Edit `loki/config/loki-config.yml` to configure prometheus
4. Run `docker-compose up -d`