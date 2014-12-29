#!/bin/bash

set -e

datepath=`date +%Y-%m-%d`
leaguestat_key=f109cf290fcf50d4
leaguestat_clientcode=lhjmq
format=json
view=scorebar

output_path="JSON/${view}_vcr"

url="http://chlcluster.leaguestat.com/feed/index.php?feed=sitekit&key=${leaguestat_key}&client_code=${leaguestat_clientcode}&season_id=178&view=${view}&date=${datepath}&fmt=${format}"

while true
do
    timepath=`date +%H:%M:%S`
    curl $url > ${output_path}/${datepath}-${timepath}.json
    # wait 5 minutes
    sleep $(expr 60 \* 5)
done
