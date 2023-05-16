# Bonus
# Q1

# Read the data
line1 = (input().split(','))
costomer = int(line1[0])
worker = int(line1[1])

line2 = (input().split(','))
duration = []  # Service time per person
for i in range(costomer):
    duration.append(int(line2[i]))

line3 = (input().split(','))
time = []  # Reserve time
for i in range(costomer):
    time.append(int(line3[i]))

line4 = (input().split(','))
pay = []  # Income
for i in range(costomer):
    pay.append(int(line4[i]))

# For sorting
durationbox = [0] * costomer
timebox = [0] * costomer
paybox = [0] * costomer
index = []
for i in range(costomer):
    index.append(i)
indexx = [0] * costomer

# Bubble sort
# 排序所有數值
for j in range(costomer):
    for i in range(costomer-1):
        if duration[i]>duration[i+1]:

            durationbox [i] = duration[i+1]
            durationbox[i+1] = duration[i]
            duration[i] = durationbox[i]
            duration[i+1] = durationbox[i+1]

            timebox[i] = time[i+1]
            timebox[i+1] = time[i]
            time[i] = timebox[i]
            time[i+1] = timebox[i+1]

            indexx[i] = index[i+1]
            indexx[i+1] = index[i]
            index[i] = indexx[i]
            index[i+1] = indexx[i+1]

            paybox[i] = pay[i+1]
            paybox[i+1] = pay[i]
            pay[i] = paybox[i]
            pay[i+1] = paybox[i+1]

        elif duration[i]==duration[i+1]:
            
            if time[i]>time[i+1]:

                durationbox [i] = duration[i+1]
                durationbox[i+1] = duration[i]
                duration[i] = durationbox[i]
                duration[i+1] = durationbox[i+1]

                timebox[i] = time[i+1]
                timebox[i+1] = time[i]
                time[i] = timebox[i]
                time[i+1] = timebox[i+1]

                indexx[i] = index[i+1]
                indexx[i+1] = index[i]
                index[i] = indexx[i]
                index[i+1] = indexx[i+1]

                paybox[i] = pay[i+1]
                paybox[i+1] = pay[i]
                pay[i] = paybox[i]
                pay[i+1] = paybox[i+1]

            if time[i]==time[i+1]:

                if index[i]>index[i+1]:

                    durationbox [i] = duration[i+1]
                    durationbox[i+1] = duration[i]
                    duration[i] = durationbox[i]
                    duration[i+1] = durationbox[i+1]

                    timebox[i] = time[i+1]
                    timebox[i+1] = time[i]
                    time[i] = timebox[i]
                    time[i+1] = timebox[i+1]
                    
                    indexx[i] = index[i+1]
                    indexx[i+1] = index[i]
                    index[i] = indexx[i]
                    index[i+1] = indexx[i+1]

                    paybox[i] = pay[i+1]
                    paybox[i+1] = pay[i]
                    pay[i] = paybox[i]
                    pay[i+1] = paybox[i+1]

                print(index)
        else:
            pass

# Set innitial value
income = 0  # Store accumulated income
served = 0  # Store the counts of people who are served

# create a empty timetable of each worker's working time
# 建立每個工人的工作時間條 (工人編號, 時間條)
timetable_worker = []
for i in range(worker):
    each_worker = [0] * 361  # 在指派之前，時間條是空的
    timetable_worker.append(each_worker)

for i in range(costomer):
    n = 0
    for j in range(31):
        for k in range(worker):
            if sum(timetable_worker[k][time[i]+j:time[i]+duration[i]+j]) == 0 and time[i] + duration[i] + j <= 360:
                if sum(timetable_worker[k]) + duration[i] != 361:
                    for m in range(duration[i]):
                        timetable_worker[k][time[i]+j+m] = 1
                    served += 1
                    income += pay[i]
                    n = 1
                    break
        if n == 1:
            break

# Print answer
print(served,income,sep=',')