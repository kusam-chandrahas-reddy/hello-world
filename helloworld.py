i = input('Enter name:')
print ('Hello '+str(i)+'!')
password = 'MyPassword'
print ('Here is my password: '+str(password))
jira_api_token='4FV4TGjHr5t4d4eFBv75645C'
atlassian_api_token='4FV4TGjHr5t4d4eFBv75645C'
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

print ('Here is my password updated one : '+str(password))
