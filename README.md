# Spider_Australia
A Scrapy program that scraps Australia Football Clubs, and ready to be forked and expanded 

##How to use
Assume Scrapy has installed, inside this repository, do

    scrapy crawl AFL -o afl.json
Then you should be abe to see a json file with the name of "afl.json" 
The json files consisted of 
- Name of the football club 
- URL for the football club
- URL for the logo of the club

##Issues
Brisbane Lions doesn't play well, same as its URL, for some reason its logo's URL can't detect the spacing between AFL and Tenant, 
so y'all can manually concatenate the space with "%20" 
