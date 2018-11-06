# https://github.com/elastic/elasticsearch-docker
FROM docker.elastic.co/elasticsearch/elasticsearch:6.4

MAINTAINER Boris Shkarupelov

# Add your elasticsearch plugins
RUN elasticsearch-plugin install analysis-icu

# Add user for logstash and kibana
CMD esusers useradd username -p password -r logstash,kibana4_server
