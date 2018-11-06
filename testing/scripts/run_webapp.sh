docker run --network dockerelkstack_logging --link redis:redis -p 80:80 -d --name webapp dockerelkstack_webapp
