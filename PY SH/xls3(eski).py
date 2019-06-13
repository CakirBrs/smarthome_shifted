import xlrd
import matplotlib.pyplot as plt





def SOC(ChargeofBattery,BatteryCapacity):
    return (ChargeofBattery*100/BatteryCapacity)


def TabloX(girdi):
    iceriSayi=len(girdi)
    print(iceriSayi)
    iciniciSayi=len(girdi[0])
    print(iciniciSayi)
    for icdekiler in range(iceriSayi):
        for icdekilerinYani in range(3,iciniciSayi):
            hulog=girdi[icdekiler][icdekilerinYani]
            if hulog == "":
                hulog = 0
            elif hulog == "x" or hulog == "X":
                #print(girdi[icdekiler][2])
                hulog = girdi[icdekiler][2]
            else:
                print("""TABLO "x" HATASI :""" , icdekilerinYani)
                continue
            girdi[icdekiler][icdekilerinYani] = hulog

    return


def SaatlikToplayici(priority,TimeC):
    elementSayisi=len(priority)
    elementinelementSayisi=len(priority[0])
    for count1 in range(elementSayisi):
        for count2 in range(3,elementinelementSayisi):
            sayiTimeC= TimeC[count2-3]
            sayiPriority= priority[count1][count2]
            TimeC[count2-3] = sayiTimeC + sayiPriority
    return



loc = ("list2.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

priority6=[]
priority5=[]
priority4=[]
priority3=[]
priority2=[]
priority1=[]
battery=[]
e_source=[]

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

TabloX(priority1)
TabloX(priority2)
TabloX(priority3)
TabloX(priority4)
TabloX(priority5)
TabloX(priority6)

print("fin")


time = list(range(1,25))
TimeC=[0]*24
e_time=[]
t_time=[]
#count2=3
#print(TimeC[count2-3])
#print("asdasdasdasd")
SaatlikToplayici(priority1,TimeC)
SaatlikToplayici(priority2,TimeC)
SaatlikToplayici(priority3,TimeC)
SaatlikToplayici(priority4,TimeC)
SaatlikToplayici(priority5,TimeC)
SaatlikToplayici(priority6,TimeC)
print("fin2")


plt.step(time, TimeC)
#plt.step(time, e_time)
#plt.plot(time,limittime,color='red')
plt.show()
print("fin3")




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
    




print("fin2")