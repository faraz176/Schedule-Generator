import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pickle


# # fig, ax = plt.subplots()

# dis = []
# for i in range(1,13):
#         dis.append(str(i)+" AM")

# for i in range(1,13):
#     dis.append(str(i)+" PM")



# kiz = []

# for i in range(len(dis)):
#     kiz.append(dis[i])
#     vs = dis[i].split(" ")
#     ku = vs[0] + ":30" + " " +  vs[1]
#     kiz.append(ku)


# # print(len(kiz[1]))
# # print(len(kiz[0]))
# new_doil = []

# for i in kiz:
#     if len(i) <= 5:
#         bs = i.split(" ")
#         new_doil.append(bs[0] +":" + "00" +  " " + bs[1])
#     else:
#         new_doil.append(i)

# print(new_doil)

# for i in range(len(kiz)):
#     if new_doil[i] == "12:00 AM":
#         new_doil[i] = "12:00 PM"
#     elif new_doil[i] == "12:30 AM":
#         new_doil[i] = "12:30 PM"
#     elif  new_doil[i] == "12:00 PM":
#         new_doil[i] = "12:00 AM"
#     elif new_doil[i] == "12:30 PM":
#         new_doil[i] = "12:30 AM"

# #print(kiz)
# # new_list = []
# # for i in range(len(kiz)-1, -1, -1):
# #     new_list.append(kiz[i])

# print(new_doil)

# dict1 = {}
# thing = new_doil[:46]
# #print(thing)

# count = 1
# tis = 0
# for i in range(0, len(thing)):
#     if tis == 0:
#         dict1[thing[i]] = count
#         tis += 1
#     elif tis == 1:
#         dict1[thing[i]] = str(count) + ":" + "30" 
#         tis = 0
#         count += 1


# #print(dict1)
# dict1["12:00 AM"] = '0'
# print(dict1)

with open('time.pkl', 'rb') as f:
    b = pickle.load(f)

# Making sure each of the results is a string
for key, value in b.items():
    b[key] = str(value)




# Trying to find correct category to fit in time
# Editing CSV to fit appropriate times

sleep = input("What time did you sleep (Format it like this: '1:00 AM') ? ")
v = True
while v:
    activity = input("Please input activity or leave blank ")
    if activity == None:
        v = False
    else:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        date_today = datetime.today().strftime("%H:%M")
        date_today1 = datetime.today().weekday()
        new_day = days[date_today1]
        frick = []
        vz = date_today.split(":")
#print(vz)
        ip = vz[0]

        buz = []
        for key, value in b.items():
            if ip in value:
                buz.append(key)
        
        if int(vz[1]) >= 30:
            l1 = buz[1]
        else:
            l1 = buz[0]


    

        file = "schedule.csv"
        df = pd.read_csv(file, index_col="Unnamed: 0")
        print(type(df))
        df.loc[sleep:buz[0], new_day] = "Sleep"
        df.loc[l1, new_day] = activity
        print(df[new_day])



#print(dis)

# kiz = []
# for i in range(len(dis)):
#     kiz.append(dis[i].replace("00", ""))
    

# viz = []
# for i in kiz:
#     viz.append(i)
#     viz.append(i+"30")



#fiz = {'Monday': [0], 'Tuesday':[0], 'Wednesday':[0], 'Thursday':[0], 'Friday':[0], 'Saturday':[0],'Sunday':[0]}

# df = pd.DataFrame(fiz, index=kiz)
# print(df)

#Inserting time into csv file 
#f.to_csv('schedule.csv')

# file = "schedule.csv"
# df = pd.read_csv(file, index_col="Unnamed: 0")

# vosc = df.columns
# for i in range(len(vosc)):
#     column = vosc[i]
#     df[column] = df['Monday']


# vs = df['Monday'].value_counts()
# ax.plot(vs)
# ax.set_xlabel("Activites")
# ax.set_ylabel("Hours spent doing")
# plt.show()