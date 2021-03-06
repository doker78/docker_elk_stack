.. docker_elk_stack documentation master file, created by
   sphinx-quickstart on Thu Aug 23 13:34:32 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to docker_elk_stack's documentation!


.. toctree::
   :maxdepth: 2
   :caption: Contents:



.. Indices and tables


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Docker and webapp with ELK





It is based on the following componnents:

Elasticsearch, search engine which provide full text search & analytics
Logstash, an ETL for retrieving data from heterogeneous sources, transforming them and sending them to Elasticsearch
Kibana, which provide an UI for exploring data, and create interactive dashboards
Redis, an upstream broker which will serve as buffer in case of latency of the system, while avoiding excessive congestion in case of a peak
Curator, a tool to manage our index
Beats, client-side agent to send the logs/metrics to our stack

List of containers version for each stack component


Elasticsearch (6.4)
Logstash (6.4)
Kibana (6.4)
Redis (latest)
Curator (latest)


- Build with docker-compose

build the images
docker-compose build

- Run with docker-compose


run stack added -d for daemon mode
  docker-compose up -d
inspect the logs
  docker-compose logs -f


 - Access kibana for view status after successfully set up    

 http://KIBANA_HOST:5061
  

 - Build and Run the webapp and let to Kibana monitoring 


  docker build ./webapp -t dockerelkstack_webapp
  docker run --network dockerelkstack_logging --link redis:redis -p 80:80 -d --name webapp dockerelkstack_webapp

  It’s possible to automatically restart crashed containers by specifying a restart policy when initiating the container
  --restart always

 docker run --network dockerelkstack_logging --restart always --link redis:redis -p 80:80 -d --name webapp dockerelkstack_webapp


** Joli Admin is a free for personal caching admin template/Dashboard/Web App based on Angular JS
 Then navigate on the site [AdminUI](http://localhost) port 80 for Access to Joli Admin UI


 * Index management with Curator after ELK is UP

  docker run --network dockerelkstuck_logging --link elastic:elasticsearch -v "./curator/config":/config --rm bobrik/curator:latest --config /config/config.yml /config/actions.yml

 * After few minutes browsing, returning to Kibana
 An index is now available  


 * After creating index, we can now exploring our web app logs (Discover tab)  

 Create visualizations (Visualize tab) and dashboards (Dashboard tab)  




- Documentation Status

- Travis-ci.org
 
- CI/CD with Codefresh
   
- Docker Hub and Docker Automated build

- Monitoring Dockers with Netdata, Prometheus, Grafana
 
- Docker Registry Front-End

