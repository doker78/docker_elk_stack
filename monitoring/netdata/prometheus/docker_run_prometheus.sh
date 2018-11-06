#
## run Docker for prometheus

docker run -it --name prometheus --hostname prometheus --network=netdata-tutorial -p 9090:9090 centos:latest '/bin/bash'

