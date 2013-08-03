import sys
import json 
tweet_file = open(sys.argv[1])
tweets=[]
for line in tweet_file:  # for loading tweet text in to a list
 try:
   tweets.append(json.loads(line))
 except:
   pass
dic={} #creating an  empty directory
times=0
for i in range(0,len(tweets),1):
 if 'text' in tweets[i]:
  tweet_line=tweets[i]["text"]
  words=tweet_line.encode('utf-8').split(" ")
  words=filter(bool,words)
  for j in range(0,len(words),1):
   words[j] = words[j].replace('\n', ' ')
   if words[j] in dic.keys():
    dic[words[j]]=dic[words[j]]+1
    times=times+1
   else:
    dic[words[j]]=1
    times=times+1
#print dic
for i in range(0,len(tweets),1):
 if 'text' in tweets[i]:
  tweet_line=tweets[i]["text"]
  words=tweet_line.encode('utf-8').split(" ")
  words=filter(bool,words)
  for j in range(0,len(words),1):
   words[j] = words[j].replace('\n', ' ')
   if words[j] in dic.keys():
    print words[j],float(dic[words[j]])
    del dic[words[j]]
