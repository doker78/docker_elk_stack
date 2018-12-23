# Docker and webapp with ELK		

[![](https://images.microbadger.com/badges/image/doker78/docker_elk_stack.svg)](https://microbadger.com/images/doker78/docker_elk_stack "Get your own image badge on microbadger.com") [![](https://images.microbadger.com/badges/version/doker78/docker_elk_stack.svg)](https://microbadger.com/images/doker78/docker_elk_stack "Get your own version badge on microbadger.com")
[![Build Status](https://dev.azure.com/tiptoptip777/elk-stack/_apis/build/status/doker78.docker_elk_stack?branchName=master)](https://dev.azure.com/tiptoptip777/elk-stack/_build/latest?definitionId=1?branchName=master)
### [ELK](https://www.elastic.co/elk-stack) is a search engine which provide full text search & analytics
[ELK Stack Features](https://www.elastic.co/products/stack)<br/>  	
[Logstash](https://www.elastic.co/products/logstash), an ETL for retrieving data from heterogeneous sources, transforming them and sending them to Elasticsearch <br/>
[Kibana](https://www.elastic.co/products/kibana), which provide an UI for exploring data, and create interactive dashboards <br/>
[Redis](https://redis.io/), an upstream broker which will serve as buffer in case of latency of the system, while avoiding excessive congestion in case of a peak <br/> 
[Curator](https://github.com/elastic/curator), a tool to manage ELK index <br/>
[Beats - Data Shippers](https://www.elastic.co/products/beats) client-side agent to send the logs/metrics to logstash<br/>
[ELK Introduction](https://www.elastic.co/webinars/introduction-elk-stack)<br/>
[APM GO Agent](https://www.elastic.co/blog/elastic-apm-go-agent-0-5-0-released)<br/>

#### Contents

- [Quick start](#quick-start---list-of-containers-version)
- [Go Build Images](#build-images)
- [Go with Compose](#run-with-docker-compose)
- [Access to Kibana](#access-kibana-for-view-status-after-successfully-set-up)
- [Build and Run nginx Webapp](#build-and-run-the-webapp-and-let-to-kibana-monitoring)
- [Curator ELK Indexing](#curator-indexing-on-elk)
- [Read the Docs](#docs-build-status)
- [CI with Travis-Ci](#-travis-ci)
- [CD with Codefresh](#-codefresh)
- [Docker Hub](#-dockerhub)
- [Front End](#-front-end-for-docker-registry)


#### [<img src="https://raw.githubusercontent.com/rtfd/readthedocs.org/master/media/images/favicon.ico" width="18"> Read the Docs](https://docker-elk-stack.readthedocs.io) 
[![Documentation Status](https://readthedocs.org/projects/docker-elk-stack/badge/?version=master)](https://docker-elk-stack.readthedocs.io/?badge=master)

 
#### [<img src="https://raw.githubusercontent.com/travis-ci/docs-travis-ci-com/master/favicon.ico" width="18"> Travis-Ci](https://travis-ci.org/doker78/docker_elk_stack) 
[![Build Status](https://travis-ci.org/doker78/docker_elk_stack.svg?branch=master)](https://travis-ci.org/doker78/docker_elk_stack)
 
   
#### [<img src="https://codefresh.io//wp-content/themes/codefresh/images/favicon.ico" width="18"> Codefresh](https://g.codefresh.io/public/accounts/doker78/pipelines/doker78/docker_elk_stack/docker_elk_stack)  
[![Codefresh build status]( https://g.codefresh.io/api/badges/pipeline/doker78/doker78%2Fdocker_elk_stack%2Fdocker_elk_stack?branch=master&key=eyJhbGciOiJIUzI1NiJ9.NTgzNWUwYmYxNmVhZTAwMTAwZTE0ZjNh.NgrFHZfxt_yeKIJ4tECwgFoAfVHO8OZFQM8S06Rk1Cg&type=cf-2)]( https://g.codefresh.io/repositories/doker78/docker_elk_stack/builds?filter=trigger:build;branch:master;service:5b8bd7ceab8f7b8214b4c11c~docker_elk_stack) 
 
    
#### [<img src="https://raw.githubusercontent.com/docker/docker.github.io/master/favicon.ico" width="18"> DockerHub](https://hub.docker.com/r/doker78/docker_elk_stack/)<br/>
<img src="pics/docker-build-ok.svg">


#### [<img src="https://github.com/favicon.ico" width="18"> Front End for Docker registry](https://github.com/brennerm/docker-registry-frontend)


<img src="https://github.com/doker78/docker_elk_stack/blob/master/pics/architecture_design.jpeg">


#### List of containers version
```
Elasticsearch (6.4.2)
Logstash (6.4.2),
Kibana (6.4.2),
Redis (latest),
Curator (latest)
```

#### Requirements

##### on host 

1. Install [Docker](https://www.docker.com/community-edition#/download) version **17.05+**
2. Install [Docker Compose](https://docs.docker.com/compose/install/) version **1.6.0+**
3. Clone this repository

##### increase `vm.max_map_count`

One must increase the `vm.max_map_count` kernel setting on all Docker hosts running Elasticsearch in order to pass the [bootstrap checks](https://www.elastic.co/guide/en/elasticsearch/reference/current/bootstrap-checks.html) triggered by the production mode.
To do this follow the recommended instructions from the Elastic documentation: [Install Elasticsearch with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-cli-run-prod-mode)

##### SELinux

On distributions which have SELinux enabled out-of-the-box you will need to either re-context the files or set SELinux
into Permissive mode in order for docker-elk to start properly


##### apparmor 

On distributions which have Apparmor service enables you will need to  remove the following service from you Docker host
```console
$ systemctl stop apparmor && systemctl disable apparmor
$ apt-get purge --auto-remove apparmor
$ service docker restart
$ docker system prune --all --volumes
$ shutdown -r now
delete volumes
$ docker volume rm $(docker volume ls -qf dangling=true)
$ docker volume ls -qf dangling=true | xargs -r docker volume rm
delete networks
$ docker network ls | grep "bridge"   
$ docker network rm $(docker network ls | grep "bridge" | awk '/ / { print $1 }')

docker network ls | awk '$3 == "bridge" && $2 != "bridge" { print $1 }'
remove images
$ docker images
$ docker rmi $(docker images --filter "dangling=true" -q --no-trunc)

$ docker images | grep "none"
$ docker rmi $(docker images | grep "none" | awk '/ / { print $3 }')
remove containers
$ docker ps
$ docker ps -a
$ docker rm $(docker ps -qa --no-trunc --filter "status=exited")
resize disk for vm
$ docker-machine create --driver virtualbox --virtualbox-disk-size "40000" default

```
#### docker on windows

If you're using  Windows, ensure the "Shared Drives" feature is enabled for the `C:` drive (Docker for Windows > Settings > Shared Drives)

**NOTE**: Always pay attention to the [upgrade instructions](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html)
for each individual component before performing a stack upgrade.

### plugins and integrations

See the following Wiki pages:

* [External applications](https://github.com/deviantony/docker-elk/wiki/External-applications)
* [Popular integrations](https://github.com/deviantony/docker-elk/wiki/Popular-integrations)

#### docker swarm

Experimental support for Docker Swarm is provided in the form of a `docker-stack.yml` file, which can be deployed in an
existing Swarm cluster using the following command:

```console
$ docker stack deploy -c docker-stack.yml elk
```

If all components get deployed without any error, the following command will show 3 running services:

```console
$ docker stack services elk
```

**NOTE:** to scale Elasticsearch in Swarm mode, configure *zen* to use the DNS name `tasks.elasticsearch` instead of
`elasticsearch`


#### Build images
```
$ cd docker_elk_stack/
$ docker-compose build
```

#### Run with docker-compose
```
# run all services in the background (detached mode) by adding the `-d` flag to the above command
$ docker-compose up -d
$ docker-compose logs -f <<< (see logs)
```
#### Plugins to any ELK component you have to:

To add plugins to any ELK component you have to:

1. Add a `RUN` statement to the corresponding `Dockerfile` (eg. `RUN logstash-plugin install logstash-filter-json`)
2. Add the associated plugin code configuration to the service configuration (eg. Logstash input/output)
3. Rebuild the images using the `docker-compose build` command

#### Access to view status 

By default, the stack exposes the following ports:
* 5000: Logstash TCP input.
* 9200: Elasticsearch HTTP
* 9300: Elasticsearch TCP transport
* 5601: Kibana

```
 http://[KIBANA_HOST]:5061
```
#### Tune the Kibana configuration

The Kibana default configuration is stored in `kibana/config/kibana.yml`.

#### Tune the Logstash configuration?

The Logstash configuration is stored in `logstash/config/logstash.yml`.

#### Tune the Elasticsearch configuration

The Elasticsearch configuration is stored in `elasticsearch/config/elasticsearch.yml`.

You can also specify the options you want to override directly via environment variables:
```yml
elasticsearch:

  environment:
    network.host: "_non_loopback_"
    cluster.name: "elk-cluster"
```
## JVM tuning

#### specify the amount of memory used by a service?

By default, both Elasticsearch and Logstash start with [1/4 of the total host
memory](https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/parallel.html#default_heap_size) allocated to
the JVM Heap Size.

The startup scripts for Elasticsearch and Logstash can append extra JVM options from the value of an environment
variable, allowing the user to adjust the amount of memory that can be used by each component:

| Service       | Environment variable |
|---------------|----------------------|
| Elasticsearch | ES_JAVA_OPTS         |
| Logstash      | LS_JAVA_OPTS         |



For example, to increase the maximum JVM Heap Size for Logstash:

```yml
logstash:

  environment:
    LS_JAVA_OPTS: "-Xmx1g -Xms1g"
```
#### enable a remote JMX connection to a service?

As for the Java Heap memory (see above), you can specify JVM options to enable JMX and map the JMX port on the Docker
host.

Update the `{ES,LS}_JAVA_OPTS` environment variable with the following content (I've mapped the JMX service on the port
18080, you can change that). Do not forget to update the `-Djava.rmi.server.hostname` option with the IP address of your
Docker host (replace **DOCKER_HOST_IP**):

```yml
logstash:

  environment:
    LS_JAVA_OPTS: "-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.port=18080 -Dcom.sun.management.jmxremote.rmi.port=18080 -Djava.rmi.server.hostname=DOCKER_HOST_IP -Dcom.sun.management.jmxremote.local.only=false"
```
#### restart a service with changes:

```console
$ docker-compose stop -t 1 container_name       // go to hibernate
$ docker-compose rm container_name              // shutdown the PC
$ docker-compose build container_name           // build new container 
$ docker-compose create docker_container_name   // create the container from image and put it in hibernate     
$ docker-compose start docker_container_name    // bring container to life from hibernation
```
#### Scale out the Elasticsearch cluster?

Follow the instructions from the Wiki: [Scaling out
Elasticsearch](https://github.com/doker78/docker_elk_stack/wiki/Elasticsearch-cluster)


#### build and run the webapp with Kibana monitoring

```
$ cd  webapp
$ docker build  -t dockerelkstack_webapp
$ docker run --network docker_elk_stack_logging --link redis:redis -p 80:80 -d --name webapp dockerelkstack_webapp
 ```
  note: It’s possible to automatically restart crashed containers by specifying a restart policy when initiating the container
  --restart always
 ```
$ docker run --network docker_elk_stack_logging --restart always --link redis:redis -p 80:80 -d --name webapp dockerelkstack_webapp
 ```

### Webapp-JoliAdmin Info
[Joli Admin](http://themifycloud.com/downloads/freee-responsive-bootstrap-joli-angular-js-admin-template-dashboard-web-app/) 
is a free admin template/Dashboard/Web [WebApp](https://github.com/sbilly/joli-admin) based on Angular JS
 Then navigate on the site [AdminUI](http://localhost) port 80 for Access to Joli Admin UI


### Curator indexing on ELK
[Curator](https://www.elastic.co/guide/en/elasticsearch/client/curator/current/about.html): Elasticsearch Curator helps you curate, or manage, your Elasticsearch indices and snapshots
```
$ docker run --network docker_elk_stack_logging --link elastic:elasticsearch -v "$PWD/curator/config":/config --rm bobrik/curator:latest --config /config/config.yml /config/actions.yml
```

 * After few minutes browsing, returning to Kibana  
 * An index (logstash-*) is now available  
<img src="https://raw.githubusercontent.com/doker78/docker_elk_stack/master/pics/kibana_pattern.png" width="400" height="200"/>  

 * Exploring logs (Discover tab) and dashboards (Dashboard tab)

<img src="https://raw.githubusercontent.com/doker78/docker_elk_stack/master/pics/kibana_logstash_index.png" width="400" height="200"/>

* Create Visualizations (Visualize tab)
<img src="https://raw.githubusercontent.com/doker78/docker_elk_stack/master/pics/kibana_logstash_visuals.png" width="400" height="200"/>   
  
  
Thanks

