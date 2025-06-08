# -*- coding:utf-8 -*-
import json
import pandas as pd
import numpy as np
import codecs
import csv 

dizi = []
dosya = open('list.txt', 'r')
for satir in dosya:  # dosyamızdaki satırları sırasıyla çektik
    dizi.append(satir)  # yazdirma işlemi
    
final_list = []
for i in dizi:
  final_list.append(i.strip())


txt_arr = []
x = int(0)
for i in final_list:
    f = open(final_list[x], 'r', encoding="utf8")
    file_contents = json.load(f)
    txt_arr.append(file_contents["text"])
    f.close
    #file =  codecs.open("deneme.txt", "a","utf-8")
    #text = open("deneme.txt","a", encoding="utf8", errors='ignore')
   # file.write(str(txt_arr[x]))
    x = x + 1
print(txt_arr)


x = 0
with open('dene121me.csv', 'w', newline='\n', encoding='utf-8') as csv_file:
    for a in txt_arr:
        writer = csv.writer(csv_file, delimiter=' ')
        writer.writerow(txt_arr[x])
        x = x + 1