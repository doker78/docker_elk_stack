# Run following command to enable credential caching:
```console
$ git config credential.helper store
$ git push https://github.com/repo.git
```

Username for 'https://github.com': <USERNAME>
Password for 'https://USERNAME@github.com': <PASSWORD>

# Use should also specify caching expire
# After enabling credential caching, it will be cached for 7200 seconds (2 hour)

git config --global credential.helper "cache --timeout 7200"
.
