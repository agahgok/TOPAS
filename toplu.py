# -*- coding: utf-8 -*-
import json
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dizi = []
dosya = open('./Data/tweets/list.txt', 'r',encoding='utf-8')
for satir in dosya:  # dosyamızdaki satırları sırasıyla çektik
    dizi.append(satir)  # yazdirma işlemi
dosya.close() 

dizi.pop()

final_list = list()
for i in dizi:
  final_list.append(i.strip())

newDF = pd.DataFrame()

date_sorter = [1,2,3,4,5,6,7,8,9,10,11,12]

total_retweet = [0,0,0,0,0,0,0,0,0,0,0,0]
total_retweet_sutun = [0,0,0,0,0,0,0,0,0,0,0,0]
total_retweet_nokta = [0,0,0,0,0,0,0,0,0,0,0,0]

total_reply = [0,0,0,0,0,0,0,0,0,0,0,0] #nokta icin
total_reply_cizgi = [0,0,0,0,0,0,0,0,0,0,0,0]
total_reply_sutun = [0,0,0,0,0,0,0,0,0,0,0,0]

total_favorite = [0,0,0,0,0,0,0,0,0,0,0,0] #cizgi icin
total_favorite_nokta = [0,0,0,0,0,0,0,0,0,0,0,0] 
total_favorite_sutun = [0,0,0,0,0,0,0,0,0,0,0,0]

date_sorter_days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

week = [0]*30
week_cizgi = [0]*30
week_nokta = [0]*30

week_reply_sutun = [0]*30
week_reply_cizgi = [0]*30
week_reply_nokta = [0]*30

week_favorite_sutun = [0]*30
week_favorite_cizgi = [0]*30
week_favorite_nokta = [0]*30

x = 1
for i in range(0,len(final_list)):
  with open("./Data/tweets/" + final_list[i],encoding='utf-8') as f:
    veri = json.load(f)
    #df = pd.DataFrame([veri])
    df = pd.DataFrame([veri],index=[x])
    newDF = newDF.append(df)
    x = x + 1
    
months = []
retweet = []
reply = []
favorite = []
days = []

t = 1
while t <= len(final_list):
  string_date = newDF['datetime'][t]
  months.append(int(string_date[5:7]))
  
  string_date_days = newDF['datetime'][t]
  days.append(int(string_date[8:10]))
  
  int_favorite = newDF['nbr_favorite'][t]
  favorite.append(int_favorite)
  
  int_reply = newDF['nbr_reply'][t]
  reply.append(int_reply)
  
  int_retweet = newDF['nbr_retweet'][t]
  retweet.append(int_retweet)
  
  t = t + 1


for i in range(0,len(months)):
    for j in range(0,len(date_sorter)):
        if(date_sorter[j] == months[i]):
            total_retweet[j] = total_retweet[j] + retweet[i]
            total_reply[j] = total_reply[j] + reply[i]
            total_favorite[j] = total_favorite[j] + favorite[i]
            total_favorite_nokta[j] = total_favorite_nokta[j] + favorite[i]
            total_reply_cizgi[j] = total_reply_cizgi[j] + reply[i]
            total_retweet_sutun[j] = total_retweet_sutun[j] + retweet[i]
            total_favorite_sutun[j] = total_favorite_sutun[j] + favorite[i]
            total_reply_sutun[j] = total_reply_sutun[j] + reply[i]
            total_retweet_nokta[j] = total_retweet_nokta[j] + retweet[i]
            
aaaa = pd.DataFrame(data = total_retweet, columns = {'total_retweet'})

months = pd.DataFrame(date_sorter)
aaaa = aaaa.assign(months = months.values)

reply_total = pd.DataFrame(total_reply)
aaaa = aaaa.assign(reply_total = reply_total.values)

favorite_total = pd.DataFrame(total_favorite)
aaaa = aaaa.assign(favorite_total = favorite_total.values)

favorite_total_nokta = pd.DataFrame(total_favorite_nokta)
aaaa = aaaa.assign(favorite_total_nokta = favorite_total_nokta.values)

reply_total_cizgi = pd.DataFrame(total_reply_cizgi)
aaaa = aaaa.assign(reply_total_cizgi = reply_total_cizgi.values)

retweet_total_sutun = pd.DataFrame(total_retweet_sutun)
aaaa = aaaa.assign(retweet_total_sutun = retweet_total_sutun.values)

favorite_total_sutun = pd.DataFrame(total_favorite_sutun)
aaaa = aaaa.assign(favorite_total_sutun = favorite_total_sutun.values)

reply_total_sutun = pd.DataFrame(total_reply_sutun)
aaaa = aaaa.assign(reply_total_sutun = reply_total_sutun.values)

retweet_total_nokta = pd.DataFrame(total_retweet_nokta)
aaaa = aaaa.assign(retweet_total_nokta = retweet_total_nokta.values)

toplam_retweet = []
tweet_counts_of_day = []
for i in range(0,len(date_sorter_days)):
    for j in range(0,len(days)):
        if(days[j] == date_sorter_days[i]):
            
            week[i] = week[i] + retweet[j]
            week_cizgi[i] = week_cizgi[i] + retweet[j]
            week_nokta[i] = week_nokta[i] + retweet[j]
            
            week_reply_sutun[i] = week_reply_sutun[i] + reply[j] 
            week_reply_cizgi[i] = week_reply_cizgi[i] + reply[j]
            week_reply_nokta[i] = week_reply_nokta[i] + reply[j]
            
            week_favorite_sutun[i] = week_favorite_sutun[i] + favorite[j]
            week_favorite_cizgi[i] = week_favorite_sutun[i] + favorite[j]
            week_favorite_nokta[i] = week_favorite_sutun[i] + favorite[j]
            
bbbb = pd.DataFrame(data = date_sorter_days, columns = {'date_sorter_days'})

total_week_sutun = pd.DataFrame(week)
bbbb = bbbb.assign(total_week_sutun = total_week_sutun.values)

total_week_cizgi = pd.DataFrame(week_cizgi)
bbbb = bbbb.assign(total_week_cizgi = total_week_cizgi.values)

total_week_nokta = pd.DataFrame(week_nokta)
bbbb = bbbb.assign(total_week_nokta = total_week_nokta.values)

total_week_reply_sutun = pd.DataFrame(week_reply_sutun)
bbbb = bbbb.assign(total_week_reply_sutun = total_week_reply_sutun.values)

total_week_reply_cizgi = pd.DataFrame(week_reply_cizgi)
bbbb = bbbb.assign(total_week_reply_cizgi = total_week_reply_cizgi.values)

total_week_reply_nokta = pd.DataFrame(week_reply_nokta)
bbbb = bbbb.assign(total_week_reply_nokta = total_week_reply_nokta.values)

total_week_favorite_sutun = pd.DataFrame(week_favorite_sutun)
bbbb = bbbb.assign(total_week_favorite_sutun = total_week_favorite_sutun.values)

total_week_favorite_cizgi = pd.DataFrame(week_favorite_cizgi)
bbbb = bbbb.assign(total_week_favorite_cizgi = total_week_reply_nokta.values)

total_week_favorite_nokta = pd.DataFrame(week_favorite_nokta)
bbbb = bbbb.assign(total_week_favorite_nokta = total_week_favorite_nokta.values)

#AY

#RETWEET_AY_CIZGI
plt.plot(aaaa['months'], aaaa['total_retweet'])
plt.title("RETWEET-AY GRAFİĞİ")
plt.xlabel("AYLAR")
plt.ylabel("RETWEET SAYISI")
plt.savefig('RETWEET_AY_CIZGI.png')
plt.close()

#RETWEET_AY_SUTUN
plt.bar(aaaa['months'], aaaa['retweet_total_sutun'])
plt.title("RETWEET-AY GRAFİĞİ")
plt.xlabel("AYLAR")
plt.ylabel("RETWEET SAYISI")
plt.savefig('RETWEET_AY_SUTUN.png')
plt.close()

#RETWEET_AY_NOKTA
plt.plot(aaaa['months'], aaaa['retweet_total_nokta'],"ro")
plt.title("RETWEET-AY GRAFİĞİ")
plt.xlabel("AYLAR")
plt.ylabel("RETWEET SAYISI")
plt.savefig('RETWEET_AY_NOKTA.png')
plt.close()

#REPLY_AY_NOKTA
plt.plot(aaaa['months'], aaaa['reply_total'],"ro")
plt.title("RELPY-AY GRAFİĞİ")
plt.xlabel("AYLAR")
plt.ylabel("REPLY SAYISI")
plt.savefig('REPLY_AY_NOKTA.png')
plt.close()

#REPLY_AY_CIZGI
plt.plot(aaaa['months'], aaaa['reply_total_cizgi'])
plt.title("RELPY-AY GRAFİĞİ")
plt.xlabel("AYLAR")
plt.ylabel("REPLY SAYISI")
plt.savefig('REPLY_AY_CIZGI.png')
plt.close()

#REPLY_AY_SUTUN
plt.bar(aaaa['months'], aaaa['reply_total_sutun'])
plt.title("RELPY-AY GRAFİĞİ")
plt.xlabel("AYLAR")
plt.ylabel("REPLY SAYISI")
plt.savefig('REPLY_AY_SUTUN.png')
plt.close()

#FAVORI_AY_CIZGI
plt.plot(aaaa['months'], aaaa['favorite_total'])
plt.title("FAVORİ-AY GRAFİĞİ")
plt.xlabel("AYLAR")
plt.ylabel("FAVORI SAYISI")
plt.savefig('FAVORI_AY_CIZGI.png')
plt.close()

#FAVORI_AY_NOKTA
plt.plot(aaaa['months'], aaaa['favorite_total_nokta'],"ro")
plt.title("FAVORİ-AY GRAFİĞİ")
plt.xlabel("AYLAR")
plt.ylabel("FAVORI SAYISI")
plt.savefig('FAVORI_AY_NOKTA.png')
plt.close()

#FAVORI_AY_SUTUN
plt.bar(aaaa['months'], aaaa['favorite_total_sutun'])
plt.title("FAVORİ-AY GRAFİĞİ")
plt.xlabel("AYLAR")
plt.ylabel("FAVORI SAYISI")
plt.savefig('FAVORI_AY_SUTUN.png')
plt.close()

#GUN

#RETWEET_GUN_SUTUN
plt.bar(bbbb['date_sorter_days'], bbbb['total_week_sutun'])
plt.title("RETWEET-GUN GRAFİĞİ")
plt.xlabel("GUN")
plt.ylabel("RETWEET SAYISI")
plt.savefig('RETWEET_GUN_SUTUN.png')
plt.close()

#RETWEET_GUN_CIZGI
plt.plot(bbbb['date_sorter_days'], bbbb['total_week_cizgi'])
plt.title("RETWEET-GUN GRAFİĞİ")
plt.xlabel("GUN")
plt.ylabel("RETWEET SAYISI")
plt.savefig('RETWEET_GUN_CIZGI.png')
plt.close()

#RETWEET_GUN_NOKTA
plt.plot(bbbb['date_sorter_days'], bbbb['total_week_nokta'],"ro")
plt.title("RETWEET-GUN GRAFİĞİ")
plt.xlabel("GUN")
plt.ylabel("RETWEET SAYISI")
plt.savefig('RETWEET_GUN_NOKTA.png')
plt.close()

#REPLY_GUN_SUTUN
plt.bar(bbbb['date_sorter_days'], bbbb['total_week_reply_sutun'])
plt.title("REPLY-GÜN GRAFİĞİ")
plt.xlabel("GÜNLER")
plt.ylabel("REPLY SAYISI")
plt.savefig('REPLY_GUN_SUTUN.png')
plt.close()

#REPLY_GUN_CIZGI
plt.plot(bbbb['date_sorter_days'], bbbb['total_week_reply_cizgi'])
plt.title("REPLY-GÜN GRAFİĞİ")
plt.xlabel("GÜNLER")
plt.ylabel("REPLY SAYISI")
plt.savefig('REPLY_GUN_CIZGI.png')
plt.close()

#REPLY_GUN_NOKTA
plt.plot(bbbb['date_sorter_days'], bbbb['total_week_reply_nokta'],"ro")
plt.title("REPLY-GÜN GRAFİĞİ")
plt.xlabel("GÜNLER")
plt.ylabel("REPLY SAYISI")
plt.savefig('REPLY_GUN_NOKTA.png')
plt.close()

#FAVORI_GUN_SUTUN
plt.bar(bbbb['date_sorter_days'], bbbb['total_week_favorite_sutun'])
plt.title("FAVORİ-GÜN GRAFİĞİ")
plt.xlabel("GÜNLER")
plt.ylabel("FAVORİ SAYISI")
plt.savefig('FAVORI_GUN_SUTUN.png')
plt.close()

#FAVORI_GUN_CIZGI
plt.plot(bbbb['date_sorter_days'], bbbb['total_week_favorite_cizgi'])
plt.title("FAVORİ-GÜN GRAFİĞİ")
plt.xlabel("GÜNLER")
plt.ylabel("FAVORİ SAYISI")
plt.savefig('FAVORI_GUN_CIZGI.png')
plt.close()

#FAVORI_GUN_NOKTA
plt.plot(bbbb['date_sorter_days'], bbbb['total_week_favorite_nokta'],"ro")
plt.title("FAVORİ-GÜN GRAFİĞİ")
plt.xlabel("GÜNLER")
plt.ylabel("FAVORİ SAYISI")
plt.savefig('FAVORI_GUN_NOKTA.png')
plt.close()

os.system('"ListeleSayfasi.exe"')
