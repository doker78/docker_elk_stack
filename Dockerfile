FROM docker.elastic.co/elasticsearch/elasticsearch:6.4.2

MAINTAINER Boris Sh.

# https://github.com/elastic/elasticsearch-docker
RUN elasticsearch-plugin install analysis-icu

# Add user for logstash and kibana
CMD esusers useradd username -p password -r logstash,kibana4_server
