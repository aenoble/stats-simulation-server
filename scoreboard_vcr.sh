#!/bin/bash

set -e

leaguestat_key=f109cf290fcf50d4
leaguestat_clientcode=lhjmq
format=json
view=scorebar

output_path="JSON/${view}_vcr"

datepath=`date +%Y-%m-%d`
url="http://chlcluster.leaguestat.com/feed/index.php?feed=sitekit&key=${leaguestat_key}&client_code=${leaguestat_clientcode}&season_id=178&view=${view}&date=${datepath}&fmt=${format}"

while true
do
    current_datepath=`date +%Y-%m-%d`
    timepath=`date +%H:%M:%S`
    curl $url > ${output_path}/${current_datepath}-${timepath}.json
    # wait 5 minutes
    sleep $(expr 60 \* 5)
done
