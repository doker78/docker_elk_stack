FROM nginx

RUN apt-get update \
	&& apt-get install curl sudo git -y \
	&& curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.4.2-amd64.deb \
	&& sudo dpkg -i filebeat-6.4.2-amd64.deb \
	&& rm -rf /var/log/nginx/*.log \
	&& touch /var/log/nginx/access.log \
	&& touch /var/log/nginx/error.log \
	&& git clone https://github.com/doker78/docker_elk_stack \
	&& mv docker_elk_stack/webapp/joli/* /usr/share/nginx/html/

ADD ./filebeat.yml /etc/filebeat/filebeat.yml

ADD ./start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh
CMD [ "/usr/local/bin/start.sh" ]
