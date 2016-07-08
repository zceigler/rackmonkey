#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('/var/www/html/rackmonkey/rackmonkey.db')
cursor = conn.execute("SELECT device.name, domain.name FROM device LEFT OUTER JOIN domain ON device.domain = domain.id;")
for row in cursor:
  print row[0] + "." + row[1]
conn.close()
