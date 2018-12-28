# install from source
git clone https://github.com/elasticsearch/curator.git
pip install -r requirements.txt
# keep no more than 90 days of indices
curator.py --host my-elasticsearch -d 90
# Delete by space
curator.py --host my-elasticsearch -C space -g 10024
# close indices after 30 days and delete after 90
curator.py --host my-elasticsearch -c 30 -d 90
# bloom filter is resources allocated to speed indexing operations
# not indexing new data 2 days after the date has rolled over
curator.py --host my-elasticsearch -b 2 -c 30 -d 90
# forceMerge operation will try to reduce the segment count in each shard in your indices
# The default is to merge to 2 segments per shard, but you can override this default with the --max_num_segments
# This will disable bloom filters for indices older than 2 days, “optimize” indices older than 2 days, close indices older than 30 days and delete indices older than 90 days
curator.py --host my-elasticsearch -b 2 -o 2 -c 30 -d 90
# Order of operations
Delete (by space or time)<br/>
Close<br/>
Disable bloom filters<br/>
Optimize<br/>
#  run the test suite just run 
python setup.py test

