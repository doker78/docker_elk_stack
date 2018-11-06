

### Two key elements in Prometheus metrics
- We have the ‘metric’ and its ‘labels’

- Labels allow for granularity between metrics 
netdata_system_cpu_percentage_average{chart="system.cpu",family="cpu",dimension="system"} 0.0831255 1501271696000

- Metrics is ‘netdata_system_cpu_percentage_average’ and our labels are ‘chart’, ‘family’, and ‘dimension


- We can begin graphing system metrics with this information		
- First we need to hook up Prometheus to poll Netdata stats		
- After adding prometheus.yml and restart the prometheus service 		
 we will be able to get monitoring functionality of netdata metrics		
```
netdata_system_cpu_percentage_average{dimension="system"}

netdata_system_cpu_percentage_average{chart="system.cpu", instance="netdata:19999"}
```
