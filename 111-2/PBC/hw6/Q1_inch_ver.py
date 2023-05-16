# input strings, distance, and document
s1 = input()
s2 = input()
d = input()
doc = input()
dtype = d.isnumeric()
d = int(d)

# determine whether the input is illegal
if (dtype is False) or (d < 0) or (d > 1000)\
    or (len(s1) < 1) or (len(s2) < 1) or (len(doc) < 1)\
    or (len(s1) > 10000) or (len(s2) > 10000) or (len(doc) > 10000):
    print('ILLEGAL_INPUT')
    quit()

# record the output answer in order
answer = []
for i in range(len(doc)):
    # determine whether there are strings exist in doucment
    if doc[i:i+len(s1)] == s1 or doc[i:i+len(s2)] == s2:
        # determine whether the string is string1 or string2
        if doc[i:i+len(s1)] == s1:
            for j in range(i+len(s1), i+len(s1)+d):
                if doc[j:j+len(s2)] == s2:
                    answer.append(doc[i:j+len(s2)])
        elif doc[i:i+len(s2)] == s2:
            for j in range(i+len(s2), i+len(s2)+d):
                if doc[j:j+len(s1)] == s1:
                    answer.append(doc[i:j+len(s1)])

# determine whether there is answer
# print answer
if answer == []:
    print('^^NOT_FOUND^^')
else:
    for i in range(len(answer)):
        print(answer[i])