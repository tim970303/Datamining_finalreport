import pandas as pd 
import random
import time
import csv
random.seed(time.time())


def strQ2B(ustring):
    """全形轉半形"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:                              #全形空格直接轉換            
            inside_code = 32 
        elif (inside_code >= 65281 and inside_code <= 65374): #全形字元（除空格）根據關係轉化
            inside_code -= 65248

        rstring += chr(inside_code)
    return rstring

singer = []
with open("userid-timestamp-artid-artname-traid-traname.tsv", "r") as f:
    output = open('output.csv', 'w', newline='')
    writer = csv.writer(output)
    row = 0
    insertCount = 0
    last_user = ""
    user_count = 0
    for line in f:
        row += 1
        print(line)
        insertCount += 1
        line_after_split = line.split("\t")
        if  line_after_split[0] != last_user:
            last_user = line_after_split[0]
            print(line_after_split[0] + ": " + str(insertCount))
            insertCount = 0
            user_count += 1
        if (insertCount >= 200 and line_after_split[0] == last_user):
            continue
        out = [int(line_after_split[0].split("_")[1])]
        if not line_after_split[2] in singer:
            singer.append(line_after_split[2])
            out.append(len(singer))
        else:
            out.append(singer.index(line_after_split[2])+1)
        
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
#         if len(out[user]) > 20:
#             out[user] = out[user][:20]
#         else:
#             while len(out[user]) < 20:
#                 out[user].append(0)
#         userCount +=1
#         out[user].insert(0,userCount)
#         writer.writerow(out[user])