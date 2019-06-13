import xlrd 
import matplotlib.pyplot as plt

# Give the location of the file 
loc = ("list.xlsx") 

# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

# For row 0 and column 0 
a= sheet.cell_value(0, 0)
print(a)
print(sheet.nrows) 
print(sheet.ncols) 
print(type(sheet.row_values(1)))


def SOC(charge_ob):
    return (charge_ob*100/50)


priority6=[]
priority5=[]
priority4=[]
priority3=[]
priority2=[]
priority1=[]
battery=[]
e_source=[]
print((sheet.nrows))

for i in range(1,sheet.nrows): 
    
    cell_value=sheet.cell_value(i, 0)
    print(cell_value)
    if cell_value == 1:
        priority1.append(sheet.row_values(i))
    if cell_value == 2:
        priority2.append(sheet.row_values(i))
    if cell_value == 3:
        priority3.append(sheet.row_values(i))
    if cell_value == 4:
        priority4.append(sheet.row_values(i))
    if cell_value == 5:
        priority5.append(sheet.row_values(i))
    if cell_value == 6:
        priority6.append(sheet.row_values(i))
    if cell_value == 11:
        battery.append(sheet.row_values(i))
    if cell_value == 12:
        e_source.append(sheet.row_values(i))

time = list(range(1,25))
time2=[]
e_time=[]
t_time=[]

#print(sheet.cell_value(3, 3))
#print(sheet.row_values(3))


for ii in range(3,sheet.ncols): #sütun
    ph=0
    e_valuee=0
    for i in range(3,sheet.nrows): #satır
        
        valuee=sheet.cell_value(i, ii)
        if valuee=="":
            continue
        ph=ph+valuee
    e_valuee=-sheet.cell_value(2,ii)
    tph=ph+e_valuee

    time2.append(ph)
    e_time.append(e_valuee)
    t_time.append(tph)



#61 e taşınacak battery for döngüsüne taşınacak

limittime= []
for i in range(24):
    limittime.append(60)
plt.step(time, time2)
plt.step(time, e_time)
plt.plot(time,limittime,color='red')
plt.show()

print(battery[0][2])
battery_cap=0
print(len(battery))
for i in range(len(battery)):
    battery_cap=battery_cap+battery[i][2]
    print(battery_cap)
chargeRate=battery_cap*20/100
dischargeRate=battery_cap*30/100
charge_ob=5
SoC=SOC(charge_ob)
max_SoC=battery_cap*80/100

r_t_time=[]

for ii in range(24):
    totaloS=0
    for i in range(len(e_source)):
        totaloS=totaloS+e_source[i][ii+3]
    




print("fin")