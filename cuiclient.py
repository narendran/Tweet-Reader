import sys,twitter,subprocess,time
#subprocess is to execute linux shell commands in python

client = twitter.Api(consumer_key='yMNI0YTEKdNBjX5GyNZBw',consumer_secret='OghfzFIesnuCjqKo7SCL2lqH3iH5wQDe3yU9NoIeio', access_token_key='306646649-t3xZEcLvihWUvdWF38FE1wFMsYjB2psG5nYwMaB5', access_token_secret='c1vBemCblKpwXE99coKZHrl1QSLLtUZS7X7AYP4n0g')
while True :
    for arg in sys.argv:
         if(arg!='cuiclient.py'):
            name=client.GetUser(arg)
            print name.screen_name, name.status.text, name.status.id
            texty= name.screen_name + name.status.text
            current=time.mktime(time.gmtime())
            stringtime=name.status.created_at+' UTC'
            msgtime=time.mktime(time.strptime(stringtime,'%a %b %d %H:%M:%S +0000 %Y %Z'))
            if((msgtime+61)>current):
                subprocess.call(["espeak", texty])
            else:
                subprocess.call(["espeak","No new tweets"])
    time.sleep(60)