from sshtunnel import SSHTunnelForwarder
from time import sleep

import json
import os
import sys

with open('config.json') as json_data:
    conf = json.load(json_data)


PORT = int(os.getenv('PORT', 8000))
print "the overlords have graciously granted me port: %i" % PORT

try:
    server = SSHTunnelForwarder(
        conf['server'],
        ssh_username=conf['username'],
        ssh_password=conf['password'],
        remote_bind_address=(conf["remoteBindAddr"], conf['remotePort']),
        local_bind_address=("", PORT)
    )
except:
    print "Unexpected error while defining server:", sys.exc_info()

print "the ssh tunnel has been defined"

try:
  server.start()
  print("running on port: %i" % server.local_bind_port)  # show assigned local port
  while True:
      sleep(1)
except KeyboardInterrupt:
  print "somehow there was a keyboard interupt..."
  pass
except:
  print "Unexpected error:", sys.exc_info()[0]

print "stdout, i am killed, thou livest. report me and my cause a'right"
server.stop()









