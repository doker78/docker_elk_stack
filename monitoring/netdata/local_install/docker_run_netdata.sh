#
## installing netdata on VM or container

## run netdata dockerize latest relize of CentOS on docker network created previosily networks (see README.md)

docker run -it --name netdata --hostname netdata --network=netdata-net -p 19999:19999  centos:latest '/bin/bash'

#
## This command creates an interactive tty session (-it)
## gives the container both a name in relation to the docker daemon 
## and a hostname, in this way we will be know how
## docker maps hostname resolution to this container 
## forwards the local port 19999 to the container’s port 19999 (-p 19999:19999)
## sets the command to run (/bin/bash)
## then chooses the base container images (centos:latest). 
#

