#!/bin/sh
while [[ true ]]; do
	sleep 3;
	if [  -e "/mnt/log/restart" ]; then
		kill -1 `pidof vlmcsd`
		rm "/mnt/log/restart"
	fi
	if [  -e "/mnt/log/start" ]; then
		kill -18 `pidof vlmcsd`
		rm "/mnt/log/start"
	fi	
	if [  -e "/mnt/log/stop" ]; then
		kill -19 `pidof vlmcsd`
		rm "/mnt/log/stop"
	fi	
done