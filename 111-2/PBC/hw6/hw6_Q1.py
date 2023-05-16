# Hw6 for PBC
# Created on 20230414 by Tsai,C,Y
# Q1------------------------------------------------------------

# Read input
s1 = str(input())  # Keyword1
s2 = str(input())  # Keyword2
d = int(input())  # Distance between keywords
article = input()  # Input article

# Define a function to get the numbers and location of keywords
def find_index(s1, s2, article):
    indexs1 = []
    indexs2 = []
    counts1 = article.count(s1)
    counts2 = article.count(s2)
    indexs1.append(article.find(s1))
    indexs2.append(article.find(s2))

    for i in range(counts1 - 1):
        indexs1.append(article.find(s1, indexs1[i] + len(s1)))

    for i in range(counts2 - 1):
        indexs2.append(article.find(s2, indexs2[i] + len(s2)))

    return(indexs1, indexs2)

# Get location and number of keywords
indexs1, indexs2 = find_index(s1, s2, article)
index_total = (indexs1 + indexs2)
counts1, counts2 = article.count(s1), article.count(s2)

# Judge if the input is valid
if len(s1) > 1e4 and len(s2) > 1e4:
    print('ILLEGAL_INPUT')
elif 0 > d or d > 1000:
    print('ILLEGAL_INPUT')

# If valid, search keyword in article
else:
    found = False  # Use a boolean to store whether there exist any answer
    if article.count(s1) > 0 and article.count(s2) > 0:  # Judge if keyword exist
        for i in range(counts1 * counts2):
            if len(index_total) <= 1:
                break
            if len(indexs1) == 0 or len(indexs2) == 0:
                break

            indexmin = min(index_total)
            index_total.remove(indexmin)

            if min(indexs1) == indexmin:

                indexs1.remove(indexmin)
                for j in range(len(indexs2)):
                    if abs(indexmin - indexs2[j]) <= d:  # Judge the distance between two keywords
                        found = True
                        print(article[indexmin:indexs2[j] + len(s2)])

            else:

                indexs2.remove(indexmin)
                for j in range(len(indexs1)):
                    if abs(indexmin - indexs1[j]) <= d:  # Judge the distance between two keywords
                        found = True
                        print(article[indexmin:indexs1[j] + len(s1)])

# If there is no expected answer
    if found == False:
        print('^^NOT_FOUND^^')