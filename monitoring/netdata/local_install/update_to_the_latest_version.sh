#
## updating netdata to the latest version 

#
## starting clone 
git clone https://github.com/firehol/netdata.git --depth=1

#
## go to the git downloaded directory
cd /path/to/git/downloaded/netdata

## download the latest version
git pull

## rebuild it, install it, run it
./netdata-installer.sh
