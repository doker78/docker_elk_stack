# docker network creating
docker network create -d ipvlan --subnet=192.168.1.0/24 --gateway=192.168.1.1 --ip-range=192.168.1.160/27 -o parent=eth1 -o ipvlan_mode=l2 test_net
