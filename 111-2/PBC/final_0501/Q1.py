lastname = '陳林黃張李王吳劉蔡楊許鄭謝郭洪曾邱廖賴周徐蘇葉莊呂江何蕭羅高簡朱鍾施游詹沈彭胡余盧潘顏梁趙柯翁魏方孫戴范宋鄧杜侯曹薛傅丁溫紀蔣歐藍連唐馬董石卓程姚康馮古姜湯汪白田涂鄒巫尤鐘龔嚴韓黎阮袁童陸金錢邵'
words = ['先生','小姐','姓']
dict = {}
for i in range (len(lastname)):
    dict[lastname[i]] = 0
article = input()

for i in range(len(article)-3):
    for name in lastname:
        if name == article[i] and (article[i+1:i+3] == '先生' or article[i+1:i+3] == '小姐' or article[i+1] == '姓' or article[i-1] == '姓'):
            dict[name] += 1

output_name = []
output_times = []
for name in lastname:
    if dict[name] > 0:
        output_name.append(name)
        output_times.append(dict[name])

length = len(output_times)
output_name_box = [0] * length
output_times_box = [0] * length

for j in range(len(output_times)):
    for i in range(len(output_times)-1):
        if output_times[i] < output_times[i+1]:
            output_times_box[i] = output_times[i+1]
            output_times_box[i+1] = output_times[i]

            output_name_box[i] = output_name[i+1]
            output_name_box[i+1] = output_name[i]

            output_name[i] = output_name_box[i]
            output_name[i+1] = output_name_box[i+1]
            output_times[i] = output_times_box[i]
            output_times[i+1] = output_times_box[i+1]

if len(output_name) > 0:
    for i in range(len(output_name)):
        print(output_name[i],':',output_times[i],sep='')