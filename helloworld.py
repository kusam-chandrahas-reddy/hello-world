i = input('Enter name:')
print ('Hello '+str(i)+'!')
password = 'MyPassword'
print ('Here is my password: '+str(password))

import os
cmd = input('Enter command:')
if cmd == 'echo':
  output = os.popen(str(cmd)+' '+password)
elif cmd == 'ls':
  output = os.popen(str(cmd))
else:
  print ('Command is invalid...exiting')
  exit(0)
display = output.read()
print (display)
