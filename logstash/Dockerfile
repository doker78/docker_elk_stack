# https://github.com/elastic/logstash-docker
FROM docker.elastic.co/logstash/logstash:6.4

# Logstash plugins 
RUN logstash-plugin install logstash-filter-json
RUN gosu logstash bin/logstash-plugin install logstash-input-rss
