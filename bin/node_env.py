#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('/var/www/html/rackmonkey/rackmonkey.db')
cursor = conn.execute("SELECT device.name, domain.name, environment.name FROM device LEFT OUTER JOIN domain ON device.domain = domain.id LEFT OUTER JOIN environment ON device.environment = environment.id;")
for row in cursor:
  print row[0] + "." + row[1] + "\t" + row[2]
conn.close()
