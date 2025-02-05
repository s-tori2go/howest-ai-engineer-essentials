# Pull and start the containers:
docker compose -f compose.yaml up -d

# Check logs to verify the health of services:
docker compose logs influxdb
docker compose logs telegraf

# Navigate to http://localhost:8086 in the browser.

# Update the Telegraf configuration with the token and restart the service:
docker compose restart telegraf

# Debug Telegraf
docker compose logs telegraf
