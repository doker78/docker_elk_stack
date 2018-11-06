#!/bin/bash

# start nginx and filebeat
/etc/init.d/nginx start
/etc/init.d/filebeat start

# check the running logs
tail -f /var/log/nginx/access.log -f /var/log/nginx/error.log
