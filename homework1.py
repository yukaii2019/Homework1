# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================
# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107033137.csv'
data = []
header = []
with open(cwb_filename, encoding='UTF-8-sig') as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================
# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
# Retrive ten data points from the beginning.

for i in data:
    if i['TEMP']== '-99' or i['TEMP']=='-999':
        i['TEMP'] = ''

station_id = ['C0A880','C0F9A0', 'C0G640', 'C0R190', 'C0X260']

ans = []
for j in station_id:
    target_data = list (filter(lambda item: item['station_id']==j,data))
    max = -999
    flg = 0
    for i in target_data:
        if i['TEMP']!='':
            if float(i['TEMP']) > max:
                flg=1
                max = float(i['TEMP'])    
    if flg==1:
        ans.append([j,max])
    else :
        ans.append([j,'None'])

print(ans)

#target_data = data[:10]

#=======================================
# Part. 4
#=======================================
# Print result
#print(target_data)
#========================================