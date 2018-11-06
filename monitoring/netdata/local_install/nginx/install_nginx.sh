#
## running CentOS

## isntall nginx
yum install epel-release
yum install nginx 

# run version test 
nginx -V

#
## start nginx service

systemctl status nginx
systemctl enable nginx
systemctl status nginx

#
## firewalld set up  of access to NGINX

firewall-cmd --permanent --add-port=80/tcp
firewall-cmd --permanent --add-port=443/tcp
firewall-cmd --reload

# 
## Enable NGINX stub module
# edit the /etc/nginx/nginx.conf
## add the following block to conf file

location /stub_status {
		stub_status;
			allow 127.0.0.1;	#only allow requests from localhost
			deny all;			#deny all other hosts	
}

#
## Restart nginx 

nginx -t
systemctl restart nginx

#
## test nginx stub status module work

curl http://127.0.0.1/stub_status

#
## Install netdata on CentOS

 bash <(curl -Ss https://my-netdata.io/kickstart.sh) all

 #
 ## Netdata listens on port 19999 by default
 http://[NGINX_HOST_IP]:19999

 #
 ## Adding firewalld rules

firewall-cmd --permanent --add-port=19999/tcp
firewall-cmd --reload 

#
## configure Netdata for monitoring NGINX
## he netdata configuration for Nginx plugin is stored in the /etc/netdata/python.d/nginx.conf
## change IP to the NGINX_HOST_IP 
## see the picture attached there
#

#
## restart Netdata after adding NGINX conf

systemctl restart netdata

#
## check Netdata working
http://domain_name:19999
# OR
http://SERVER_IP:19999

