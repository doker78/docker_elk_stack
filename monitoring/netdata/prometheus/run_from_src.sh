#
## install prometheus from source
curl -L 'https://github.com/prometheus/prometheus/releases/download/v1.7.1/prometheus-1.7.1.linux-amd64.tar.gz' -o /tmp/prometheus.tar.gz

# OR

wget -O /tmp/prometheus-2.3.2.linux-amd64.tar.gz https://github.com/prometheus/prometheus/releases/download/v2.3.2/prometheus-2.3.2.linux-amd64.tar.gz

## Create prometheus system user

sudo useradd -r prometheus

## Create prometheus directory

sudo mkdir /opt/prometheus
sudo chown prometheus:prometheus /opt/prometheus

## Untar prometheus directory

sudo tar -xvf /tmp/prometheus-2.3.2.linux-amd64.tar.gz -C /opt/prometheus --strip=1

## Install prometheus.yml
## use the following ./prometheus.yml file 
## Copy and save it at /opt/prometheus/prometheus.yml
## Make sure to replace your.netdata.ip with the IP or hostname of the host running netdata

