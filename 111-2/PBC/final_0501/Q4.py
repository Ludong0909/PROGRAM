keyword = input()
article = input()

length = len(keyword)

output = []
for i in range(len(article)):
    if article[i] == keyword[0] and article[i + length - 1] == keyword[-1]:
        output.append(article[i:i+length])
if len(output) == 0:
    print('^^^NOT_FOUND^^^')
else:
    for i in range(len(output)):
        print(output[i])
