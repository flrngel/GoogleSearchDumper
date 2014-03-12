#!/bin/bash
DATE=`date +%Y.%m.%d`
GSD_file="$1/GoogleSearchDump_$DATE_$RANDOM.txt"
ROTATE_file="$2"
CMD="cp -rf $ROTATE_file $GSD_file"
$CMD
cat /dev/null > $2
# sleep 1 day
