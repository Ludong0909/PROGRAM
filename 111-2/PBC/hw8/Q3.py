import csv
import numpy as np
import matplotlib.pyplot as plt

# open csv file
with open('submission_complete.csv', newline='', encoding='utf-8') as csvfile:

    # read content
    rows = csv.reader(csvfile)
    next(rows)

    # 1.name  2.hw  3.problem  6.time  8.result  9.score
    # hw_score (question, students, score, attempts, time)
    hw_score = [[], [], [], [], []]
    exams = ['HW0', 'Quiz', 'Midterm1', 'Midterm 1 bonus', 'Midterm2']
    for row in rows:
        if row[2] not in exams:
            if row[3] in hw_score[0]:
                for i in range(len(hw_score[0])):
                    if row[3] == hw_score[0][i]:
                        if row[1] in hw_score[1][i]:
                            for j in range(len(hw_score[1][i])):
                                if row[1] == hw_score[1][i][j]:
                                    hw_score[2][i][j] = int(row[9])
                                    hw_score[3][i][j] += 1
                                    hw_score[4][i][j] = row[6]
                        else:
                            hw_score[1][i].append(row[1])
                            hw_score[2][i].append(int(row[9]))
                            hw_score[3][i].append(1)
                            hw_score[4][i].append(row[6])
            else:
                hw_score[0].append(row[3])
                hw_score[1].append([row[1]])
                hw_score[2].append([int(row[9])])
                hw_score[3].append([1])
                hw_score[4].append([row[6]])

# Swich order
hw_score[0][21], hw_score[0][22] = hw_score[0][22], hw_score[0][21]
hw_score[1][21], hw_score[1][22] = hw_score[1][22], hw_score[1][21]
hw_score[2][21], hw_score[2][22] = hw_score[2][22], hw_score[2][21]
hw_score[3][21], hw_score[3][22] = hw_score[3][22], hw_score[3][21]

hw_score[0][22], hw_score[0][23] = hw_score[0][23], hw_score[0][22]
hw_score[1][22], hw_score[1][23] = hw_score[1][23], hw_score[1][22]
hw_score[2][22], hw_score[2][23] = hw_score[2][23], hw_score[2][22]
hw_score[3][22], hw_score[3][23] = hw_score[3][23], hw_score[3][22]


# fig3 HW4Q4 0,13
fig, ax = plt.subplots(1,1, figsize=(10, 6)) 
plt.hist(np.array(hw_score[2][13]), bins=10, range=(0,20), color='blue', alpha = 0.5)
ax.set_ylabel('Number of Students', fontsize=12)
ax.set_xlabel('Score (pts)', fontsize=12)
ax.set_xticks(np.linspace(0,20,10+1))
ax.set_title('HW4-4 Statistic of Score', fontsize=12)
ax.grid()
plt.show()


# Calculate Statistics
for i in range(len(hw_score[0])):
    print(hw_score[0][i], 100 * np.mean(hw_score[2][i]) / np.max(hw_score[2][i]), '%', np.mean(hw_score[3][i]))
    hw_score[2][i] = np.mean(hw_score[2][i]) / np.max(hw_score[2][i])
    hw_score[3][i] = np.mean(hw_score[3][i])

print('\n平均分數:', 100 * np.mean(hw_score[2]), '%')
print('標準差:', 100 * np.std(hw_score[2]), '%')

for i in range(len(hw_score[2])):
    if hw_score[2][i] < np.mean(hw_score[2]) - 2 * np.std(hw_score[2]):
        print(hw_score[0][i], '的分數比平均低超過兩個標準差，僅有', 100 * hw_score[2][i], '%')
    if hw_score[2][i] > np.mean(hw_score[2]) + 2 * np.std(hw_score[2]):
        print(hw_score[0][i], '的分數比平均高超過兩個標準差，高達', 100 * hw_score[2][i], '%')


# fig1
fig, ax = plt.subplots(1,1, figsize=(10, 6)) 
ax.bar(np.array(range(len(hw_score[2]))), 100 * np.array(hw_score[2]), color='blue', width = 0.3, alpha = 0.5)
ax.axhline(y=100 * np.mean(hw_score[2]), color='pink', linestyle='-')
ax.axhline(y=100 * (np.mean(hw_score[2]) - 2 * np.std(hw_score[2])), color='k', linestyle='-')
ax.legend(['average', 'average $-$ 2$\sigma$', 'Score (%)'], loc='lower right')
ax.axhline(y=100 * (np.mean(hw_score[2]) + 2 * np.std(hw_score[2])), color='k', linestyle='-')
ax.set_xticks(np.array(range(len(hw_score[2]))))
ax.set_xticklabels(['hw1-1', 'hw1-2', 'hw1-3', 'hw2-1', 'hw2-2', 'hw2-3', 'hw3-1', 'hw3-2', 'hw3-3', 'hw3-4',
                    'hw4-1', 'hw4-2', 'hw4-3', 'hw4-4','hw5-1', 'hw5-2', 'hw5-3', 'hw5-4', 'hw6-1', 'hw6-2',
                    'hw6-3', 'hw7-1', 'hw7-2', 'hw7-3'], rotation='vertical')
ax.set_ylim(60, 100)
ax.set_ylabel('Score (%)', fontsize=12)
ax.set_title('Average Score', fontsize=12)
ax.grid()
plt.show()


# fig2
for i in range(len(hw_score[0])):
    print(hw_score[0][i], hw_score[3][i])
print(np.mean(hw_score[3]))
print(np.std(hw_score[3]))

fig, ax = plt.subplots(1,1) 
ax.bar(np.array(range(len(hw_score[2]))), hw_score[3], color='blue', width = 0.5, alpha = 0.5)
ax.axhline(y=np.mean(hw_score[3]), color='pink', linestyle='-')
'''
ax.axhline(y=np.mean(hw_score[3])-2*np.std(hw_score[3]), color='k', linestyle='-')
ax.axhline(y=np.mean(hw_score[3])+2*np.std(hw_score[3]), color='k', linestyle='-')
'''
ax.set_xticks(np.array(range(len(hw_score[2]))))
ax.set_xticklabels(['hw1-1', 'hw1-2', 'hw1-3', 'hw2-1', 'hw2-2', 'hw2-3', 'hw3-1', 'hw3-2', 'hw3-3', 'hw3-4',
                    'hw4-1', 'hw4-2', 'hw4-3', 'hw4-4','hw5-1', 'hw5-2', 'hw5-3', 'hw5-4', 'hw6-1', 'hw6-2',
                    'hw6-3', 'hw7-1', 'hw7-2', 'hw7-3'], rotation='vertical')
ax.legend(['Average', 'Submission'])
ax.set_ylabel('Submissions per person (Times)')
ax.set_title('Average Submission Times')
ax.grid()
plt.show()

