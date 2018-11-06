#
## after entering bash console going throught installation process of netdata with kickstart script 

bash <(curl -Ss https://my-netdata.io/kickstart.sh) --dont-wait

## append --dont-start-it to prevent the installer from starting netdata
## After completing installation you should be able to hit the Netdata dashboard at http://localhost:19999/
