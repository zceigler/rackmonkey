#!/bin/sh

DateTimeStamp=$(date '+%m_%d_%y_%H_%M')

cp /var/www/html/rackmonkey/rackmonkey.db /var/www/html/rackmonkey/db_backups/rackmonkey-$DateTimeStamp.db
sleep 1
echo "Backup complete."
