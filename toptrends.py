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
 if 'entities' in tweets[i]:
  for j in range(0,len(tweets[i]['entities']['hashtags']),1):
   if (tweets[i]['entities']['hashtags'][j]['text']) in dic.keys():
     dic[tweets[i]['entities']['hashtags'][j]['text']]=dic[tweets[i]['entities']['hashtags'][j]['text']]+1
   else:
     dic[tweets[i]['entities']['hashtags'][j]['text']]=1
top={}
for key in dic:
 if dic[key] not in top:
  top[dic[key]]=[key]
 else:
  top[dic[key]].append(key)
reversed(sorted(top.keys()))
sokey=list(reversed(sorted(top.keys())))
k=0
#print top
for i in range(0,len(sokey),1):
  for j in range(0,len(top[sokey[i]]),1):
   if k<10:
    print top[sokey[i]][j],float(sokey[i])
    k=k+1
   else:
    break
