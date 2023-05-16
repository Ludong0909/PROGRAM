# Hw6 for PBC
# Created on 20230416 by Tsai,C,Y
# Q3------------------------------------------------------------

article0 = input()
article0 = '。' + article0 + '。'
out = str(article0[0])
number = list("0123456789,.%")

for i in range(1,len(article0)-1):
    append = False
    is_number_front = False
    is_number_rare = False

    for j in range(len(number)):
        if article0[i-1] == str(number[j]):
            is_number_front = True
        if article0[i+1] == str(number[j]):
            is_number_rare = True

    for j in range(len(number)):
        if (is_number_front == False and article0[i] == str(number[j])) and (is_number_rare == False and article0[i] == str(number[j])):
            if (is_number_front == False and article0[i] == str(number[j])):
                out += ('<<')
                append = True
            if (is_number_rare == False and article0[i] == str(number[j])):
                out += (str(article0[i])+'>>')
                append = True
        else:
            if (is_number_front == False and article0[i] == str(number[j])):
                out += ('<<'+str(article0[i]))
                append = True
            if (is_number_rare == False and article0[i] == str(number[j])):
                out += (str(article0[i])+'>>')
                append = True

    if append == False:
        out += str(article0[i])

out += article0[-1]
print(out[1:-1])