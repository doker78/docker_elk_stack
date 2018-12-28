### Graphing systems metrics stack with Netdata, Prometheus, and Grafana
- Basics of getting Netdata, Prometheus and Grafana	 
- All working together and monitoring application servers 	
- Using docker on your localhost Will working with docker properly in an ad-hoc way,	
launching containers that run ‘/bin/bash’ and attaching a TTY to them


### Netdata, Prometheus, and Grafana
- Troubleshoot python code case

#### Grafana
- Grafana has been the go to graphing tool for… some time now
- We can point Grafana at Prometheus and use Prometheus as a data source

- [Grafana Download 5.2.3](https://grafana.com/grafana/download/5.2.3)
- [Release Notes v5.2.x](https://community.grafana.com/t/release-notes-v5-2-x/7894)
- [Grafana_Dashboards](https://grafana.com/dashboards)

#### Netdata
- Netdata impressed by the amount of metrics exposes to you
- [Install Netdata](https://github.com/firehol/netdata/wiki/Installation)

#### Prometheus
- Prometheus is a monitoring application which flips the normal architecture around and polls
rest endpoints for its metrics
- This architectural change greatly simplifies and decreases the time necessary to begin monitoring your applications
- Running a single Prometheus server per application becomes feasible with the help of Grafana

- [Concepts Prometheus Data Model](https://prometheus.io/docs/concepts/data_model/)
- [Concepts Prometheus Functions](https://prometheus.io/docs/prometheus/latest/querying/functions/)

#### Pretty simple overall monitoring architecture: 
- Install Netdata on your application servers
- Point Prometheus at Netdata
- Point Grafana at Prometheus
Note
for discovery server use Consul

Prometheus can plug into consul and automatically begin to scrape new hosts that
register a Netdata client with Consul.
- [Consul Demo](https://demo.consul.io/ui/dc1/services)

This stack will offer visibility into your application and systems performance

### Getting Started - Netdata
Create container which we will install Netdata on 
We need to run a container, forward the necessary port that netdata listens on, and
attach a tty so we can interact with the bash shell on the container. But
before we do this we want name resolution between the two containers to work.
In order to accomplish this we will create a user-defined network and attach
both containers to this network. The first command we should run is: 
```
docker network create --driver bridge netdata-net
```

With this user-defined network created we can now launch our container we will
install Netdata on and point it to this network

##### Run the docker with Netdata on Centos 
```
docker run -it --name netdata --hostname netdata --network=netdata-net -p 19999:19999  centos:latest '/bin/bash'
```

This command:
- creates an interactive tty session (-it)
-  gives the container both a name in relation to the docker daemon and a hostname (this is so you know what
container is which when working in the shells and docker maps hostname
resolution to this container)
- forwards the local port 19999 to the container’s
port 19999 (-p 19999:19999)
- sets the command to run (/bin/bash)
- chooses the base container images (centos:latest).

In shell we can install Netdata 
Take a look at this link:
- [Install Netdata](https://github.com/firehol/netdata/wiki/Installation)

Run the following command in your container
```
bash <(curl -Ss https://my-netdata.io/kickstart.sh) --all --dont-wait
```
#### Netdata dahsboard setup
After the install completes 
You should be able to hit the Netdata dashboard at
[Login to Netdata](http://192.168.0.101:19999/) 


Navigate to http://192.168.0.101:19999/api/v1/allmetrics?format=prometheus&help=yes In your
browser. This is the endpoint which publishes all the metrics in a format which
Prometheus understands. Let’s take a look at one of these metrics.
`netdata_system_cpu_percentage_average{chart="system.cpu",family="cpu",dimension="system"}
0.0831255 1501271696000` 
This metric is representing several things which I will
go in more details in the section on prometheus
For now understand that this metric: `netdata_system_cpu_percentage_average` has several labels: [chart,
family, dimension]
This corresponds with the first cpu chart you see on the Netdata dashboard.

<img src="https://github.com/ldelossa/NetdataTutorial/raw/master/Screen%20Shot%202017-07-28%20at%204.00.45%20PM.png" data-canonical-src="https://github.com/ldelossa/NetdataTutorial/raw/master/Screen%20Shot%202017-07-28%20at%204.00.45%20PM.png" width="800" height="450" />

This CHART is called ‘system.cpu’, The FAMILY is cpu, and the DIMENSION we are
observing is “system”. You can begin to draw links between the charts in netdata
to the prometheus metrics format in this manner.

### Prometheus setup process
We will be installing prometheus in a container for purpose of demonstration.
While prometheus does have an official container I would like to walk through
the install process and setup on a fresh container. This will allow anyone
reading to migrate this tutorial to a VM or Server of any sort.

Let’s start another container in the same fashion as we did the Netdata
container
```console
docker run -it --name prometheus --hostname prometheus --network=netdata-net -p 9090:9090  centos:latest '/bin/bash'
```
This should
drop you into a shell once again
Once there quickly install your favorite
editor as we will be editing files later in this tutorial.
`yum install vim -y`

- Prometheus provides a tarball of their latest stable versions here:
- -Prometheus Download](https://prometheus.io/download/)


```
curl -L 'https://github.com/prometheus/prometheus/releases/download/v2.5.0-rc.2/prometheus-2.5.0-rc.2.linux-amd64.tar.gz' -o /tmp/prometheus.tar.gz

mkdir /opt/prometheus

tar -xf /tmp/prometheus.tar.gz -C /opt/prometheus/ --strip-components 1
./opt/prometheus/prometheus
...
INFO[0000] Listening on :9090 source="web.go:259"
```

Go to http://192.168.0.101:9090/


##### Prometheus metrics setup
Two key elements in Prometheus metrics
Viewed here: [Prometheus Data Model](https://prometheus.io/docs/concepts/data_model/)  
two key elements in Prometheus metrics
- ‘metric’
- ‘labels’
Labels allow for granularity between metrics
```
netdata_system_cpu_percentage_average{chart="system.cpu",family="cpu",dimension="system"} 0.0831255 1501271696000
```
- first we need to hook up Prometheus to poll Netdata stats
- Here our metric is
`‘netdata_system_cpu_percentage_average’` and our labels are `‘chart’`, `‘family’`,
and `‘dimension'`
The last two values constitute the actual metric value for the metric type (gauge, counter, etc…)
We can begin graphing system metrics with this information

Prometheus gets it config from the file located (in our example) at
`/opt/prometheus/prometheus.yml`

Documented here: [prometheus documentation] (https://prometheus.io/docs/operating/configuration/)
- We will be adding a new “job” under the “scrape_configs”
- “scrape_configs” section look (we can use the dns name Netdata due to the custom user-defined
network we created in docker beforehand)

```yml
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
      - targets: ['localhost:9090']
# this is our new section with new job calling name netdata
  - job_name: 'netdata'

    metrics_path: /api/v1/allmetrics
    params:
      format: [ prometheus ]

    static_configs:
      - targets: ['netdata:19999']
```

- Start prometheus  `/opt/prometheus/prometheus`      
- Navigate to prometheus at ‘http://192.168.0.101:9090/targets’ we should see our
target being successfully scraped          
- Go back to the Prometheus’s homepage and begin to type ‘netdata_’  Prometheus should auto complete metrics
it is now scraping

<img src="https://github.com/ldelossa/NetdataTutorial/raw/master/Screen%20Shot%202017-07-28%20at%205.13.43%20PM.png" data-canonical-src="https://github.com/ldelossa/NetdataTutorial/raw/master/Screen%20Shot%202017-07-28%20at%205.13.43%20PM.png" width="800" height="450" />

#### Metrics exploration
- While exploring how we can graph some metrics
- Get the CPU spinning with a pointless busy loop
- On the shell do the following:

```console
[root@srv/]# while true; do echo "HOT HOT HOT CPU"; done
```

NetData cpu graph should be showing some activity
In order to do this let’s keep our metrics page open for reference:
http://localhost:19999/api/v1/allmetrics?format=prometheus&help=yes  
We are setting out to graph the data in the CPU chart so let’s search for “system.cpu”
in the metrics page above. We come across a section of metrics with the first
comments  `# COMMENT homogeneus chart "system.cpu", context "system.cpu", family
"cpu", units "percentage"` 
Lets Specific metric we would like to graph   

```
# COMMENTnetdata_system_cpu_percentage_average: dimension "system", value is percentage, gauge, dt 1501275951 to 1501275951 inclusive
netdata_system_cpu_percentage_average{chart="system.cpu",family="cpu",dimension="system"} 
```

Metric name we care about is
‘netdata_system_cpu_percentage_average’ so throw this into Prometheus and see
what we get.  We should see something similar to this (I shut off my busy loop)

<img src="https://github.com/ldelossa/NetdataTutorial/raw/master/Screen%20Shot%202017-07-28%20at%205.47.53%20PM.png" data-canonical-src="https://github.com/ldelossa/NetdataTutorial/raw/master/Screen%20Shot%202017-07-28%20at%205.47.53%20PM.png" width="800" height="450" />
- Prometheus will tag on an ‘instance’ label for us which corresponds to our statically defined job in
the configuration file
This allows us to tailor our queries to specific instances
Now we need to isolate the dimension we want in our query
To do this let us refine the query slightly
- Place this into our query text box
https://github.com/ldelossa/NetdataTutorial/raw/master/Screen%20Shot%202017-07-28%20at%205.47.53%20PM.png
`netdata_system_cpu_percentage_average{dimension="system"}` We now wind up with
the following graph.

<img src="https://github.com/ldelossa/NetdataTutorial/raw/master/Screen%20Shot%202017-07-28%20at%205.54.40%20PM.png" data-canonical-src="https://github.com/ldelossa/NetdataTutorial/raw/master/Screen%20Shot%202017-07-28%20at%205.54.40%20PM.png" width="800" height="450" />

We can emulate entire charts from NetData by using the `chart` dimension   
If you’d like you can combine the ‘chart’ and ‘instance’ dimension to create per-instance
charts. 
Example:
`netdata_system_cpu_percentage_average{chart="system.cpu", instance="netdata:19999"}`
<img src="https://github.com/ldelossa/NetdataTutorial/raw/master/Screen%20Shot%202017-07-28%20at%205.54.40%20PM.png" data-canonical-src="https://github.com/ldelossa/NetdataTutorial/raw/master/Screen%20Shot%202017-07-28%20at%205.54.40%20PM.png" width="800" height="450" />


This is the basics of using Prometheus to query NetData   
read this page
-[Netdata Basics] (https://github.com/firehol/netdata/wiki/Using-Netdata-with-Prometheus#netdata-support-for-prometheus).
The key point here is that NetData can export metrics from its internal DB or
can send metrics “as-collected” by specifying the `‘source=as-collected’` url
parameter like so   
`http://192.168.0.101:19999/api/v1/allmetrics?format=prometheus&help=yes&types=yes&source=as-collected`
For choose to use this method you will need to use Prometheus's set of
[Prometheus functions] (https://prometheus.io/docs/querying/functions/) to obtain useful
metrics as you are now dealing with raw counters from the system
- For example
you will have to use the `irate()` function over a counter to get that metric’s
rate per second. If your graphing needs are met by using the metrics returned by
NetData’s internal database (not specifying any source= url parameter) then use
that. If you find limitations then consider re-writing your queries using the
raw data and using Prometheus functions to get the desired chart.

# Setup of Grafana
Finally we make it to grafana. This is the easiest part in my opinion. This time
we will actually run the official grafana docker container as all configuration
we need to do is done via the GUI. Let’s run the following command:

```console
docker run -i -p 3000:3000 --network=netdata-net grafana/grafana
```

This will get grafana running at `‘http://localhost:3000/’` 
- Login using the credentials Admin:Admin.

- The first thing we want to do is click `‘Add data source’`
- Look in the following screenshot      

<img src="https://github.com/ldelossa/NetdataTutorial/raw/master/Screen%20Shot%202017-07-28%20at%206.36.55%20PM.png" data-canonical-src="https://github.com/ldelossa/NetdataTutorial/raw/master/Screen%20Shot%202017-07-28%20at%206.36.55%20PM.png" width="800" height="450" />
- After that Create a new Dashboard by clicking on the top left Grafana Icon and create a new graph in that dashboard
- Fill in the query and save

<img src="https://github.com/ldelossa/NetdataTutorial/raw/master/Screen%20Shot%202017-07-28%20at%206.39.38%20PM.png" data-canonical-src="https://github.com/ldelossa/NetdataTutorial/raw/master/Screen%20Shot%202017-07-28%20at%206.39.38%20PM.png" width="800" height="450" />
Thanks

## Conclusion

- There you have it, a complete systems monitoring stack which is very easy to
deploy. 
- Begin to understand how Prometheus and a service discovery mechanism such as Consul can play together nicely 
- This monitoring stack system can automatically register Netdata services into Consul and Prometheus
automatically begins to scrape them   
- Once achieved you do not have to think about the monitoring system until Prometheus cannot keep up with your scale
Enjoy
