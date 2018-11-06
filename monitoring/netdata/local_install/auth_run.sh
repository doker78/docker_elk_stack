# run and save the file with generated passwords

printf "yourusername:$(openssl passwd -apr1)" > /etc/nginx/passwords

## And enable the authentication inside your server directive:

server {
    # ...
    auth_basic "Protected";
    auth_basic_user_file passwords;
    # ...
}