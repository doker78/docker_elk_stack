
#
## Navigate in your browser 
```
http://localhost:19999/api/v1/allmetrics?format=prometheus&help=yes 
```

#
## This is the endpoint which publishes all the metrics in a format which Prometheus understands

#
##  take a look at one of these metrics

netdata_system_cpu_percentage_average{chart="system.cpu",family="cpu",dimension="system"}

#
## this metric has several labels: [chart, family, dimension]
## and corresponds with the first cpu chart on the Netdata dashboard:

netdata_system_cpu_percentage_average 

#
## see the screen shot available in this repository
## This CHART is called ‘system.cpu’, The FAMILY is cpu, and the DIMENSION we are observing is “system”