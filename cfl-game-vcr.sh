#!/bin/bash

set -e

game_id="12873"

line_score_url="http://andrew.pairshaped.ca/games/${game_id}"
game_leaders_url="http://andrew.pairshaped.ca/games/${game_id}/leaders"
play_by_play_url="http://andrew.pairshaped.ca/games/${game_id}/play_by_play"
head_to_head_url="http://andrew.pairshaped.ca/games/${game_id}/team_game_stats"
team_player_stats_url="http://andrew.pairshaped.ca/games/${game_id}/team_player_stats"

while true
do
    current_datepath=`date +%Y-%m-%d`
    timepath=`date +%H:%M:%S`

    view="line_score"
    output_path="JSON/${view}_vcr"
    curl $line_score_url > ${output_path}/${current_datepath}-${timepath}.json

    view="game_leaders"
    output_path="JSON/${view}_vcr"
    curl $game_leaders_url > ${output_path}/${current_datepath}-${timepath}.json

    view="play_by_play"
    output_path="JSON/${view}_vcr"
    curl $play_by_play_url > ${output_path}/${current_datepath}-${timepath}.json
    
    view="head_to_head"
    output_path="JSON/${view}_vcr"
    curl $head_to_head_url > ${output_path}/${current_datepath}-${timepath}.json

    view="team_player_stats"
    output_path="JSON/${view}_vcr"
    curl $team_player_stats_url > ${output_path}/${current_datepath}-${timepath}.json
    # wait 1 minute
    sleep $(expr 60 \* 1)
done
