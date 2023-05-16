# Hw6 for PBC
# Created on 20230416 by Tsai,C,Y

# Q2------------------------------------------------------------
article = input()
article_sub = article
article0 = article
symbol = list("。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !\"#$%&'()*+,-./:;<=>?@[\]^_`{¦}~',',")

for sym in symbol:
    article_sub = article_sub.replace(sym,',')

pun = []
for i in range(len(article_sub)):
    if article_sub[i] == ',':
        pun.append(article[i])

article_sub = article_sub.split(',')
replace = False
sentence = []

for i in range(len(article_sub)):
    if article_sub[i].find('大')>=0 or article_sub[i].find('蛇')>=0 or article_sub[i].find('丸')>=0:
        replace = True
        index = article.find(article_sub[i])
        sentence.append(article_sub[i].replace('','!').strip('!'))
        #article = article.replace(article[index:index+len(article_sub[i])],sentence)
    else:
        sentence.append(article_sub[i])

art = sentence[0]
for i in range(len(sentence)-1):
    art += pun[i] + sentence[i+1]
       
if replace == True:
    print(art)
else:
    print(article0)