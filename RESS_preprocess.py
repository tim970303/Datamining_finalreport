import pandas as pd 
import csv
import random
import time

output = open('output.csv', 'w', newline='')
writer = csv.writer(output)

category = []
with open('2019-Oct.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        print(row)
        break
        out = []
        if row[1] == "purchase":
            out.append(row[7])
            if not row[3] in category:
                category.append(row[3])
                out.append(len(category))
            else:
                out.append(category.index(row[3])+1)
            writer.writerow(out)
                
# output = open('output2.csv', 'w', newline='')
# writer = csv.writer(output)

# category = []
# out = dict()
# userCount = 0
# with open('output.csv', newline='') as csvfile:
#     rows = csv.reader(csvfile)
#     for row in rows:
#         temp = out.get(row[0],[])
#         if not row[1] in temp:
#             temp.append(row[1])
#         out[row[0]] = temp
#     users = out.keys()
#     for user in users:
#         # print(out[user])
#         if len(out[user]) > 20:
#             out[user] = out[user][:20]
#         else:
#             while len(out[user]) < 20:
#                 out[user].append(0)
#         if random.random() <= 0.002:
#             userCount += 1
#             out[user].insert(0,userCount)
#             writer.writerow(out[user])
