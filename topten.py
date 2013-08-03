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
for i in range(0,len(tweets),1):
 if 'text' in tweets[i]:
  tweet_line=tweets[i]["text"]
  words=tweet_line.encode('utf-8').split(" ")
  words=filter(bool,words)
  for j in range(0,len(words),1):
   words[j] = words[j].replace('\n', ' ')
   if words[j] in dic.keys():
    dic[words[j]]=dic[words[j]]+1
   else:
    dic[words[j]]=1
top={}
for key in dic:
 if dic[key] not in top:
  top[dic[key]]=[key]
 else:
  top[dic[key]].append(key)
sokey=sorted(top.keys())
k=0
for i in range(len(sokey)-1,len(sokey)-12,-1):
 for j in range(0,len(top[sokey[i]]),1):
  if k<10:
   print top[sokey[i]][j],float(sokey[i])
   k=k+1
  else:
   break
