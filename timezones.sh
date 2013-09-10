#!/bin/bash
padding=11
for timezone in Italy:Europe/Rome UK:Europe/London 'East Coast:America/New_York' 'West Coast:America/Los_Angeles'
do
	label=$(echo $timezone | cut -d':' -f1)
	timezone_code=$(echo $timezone | cut -d':' -f2)
	printf "%-$(echo $padding)s" "$label"
	TZ=$timezone_code date +"%H:%M"
done

