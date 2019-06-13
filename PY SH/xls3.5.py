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

def isPeakTime (time):
    if (time-3) in [17,18,19,20,21,22]:
        return True
    else:
        return False

def TimeC_Ekleme(TimeC,priority,count1,count2):
    sayiTimeC= TimeC[count2-3]
    sayiPriorityi= priority[count1][count2]
    TimeC[count2-3] = sayiTimeC + sayiPriorityi
    return

def TimeC_ShiftedEkleme(TimeC,ShiftedValue,ShiftedCount,count2,limitValue):
    sayiTimeC= TimeC[count2-3]
    sayiShifted= ShiftedValue[ShiftedCount-1]
    if sayiTimeC+sayiShifted > limitValue :
        return
    TimeC[count2-3] = sayiTimeC + sayiShifted
    del ShiftedValue[-1]
    return

def SaatlikToplayici(priority,TimeC,limitValue):
    elementSayisi=len(priority)
    elementinelementSayisi=len(priority[0])
    ShiftedValue=[]
    for count1 in range(elementSayisi):
        for count2 in range(3,elementinelementSayisi):
            if False == isPeakTime(count2):
                TimeC_Ekleme(TimeC,priority,count1,count2)
                if len(ShiftedValue) > 0 :
                    ShiftedCount=len(ShiftedValue)
                    TimeC_ShiftedEkleme(TimeC,ShiftedValue,ShiftedCount,count2,limitValue)
            elif True == isPeakTime(count2):
                if TimeC[count2-3]+priority[count1][count2] < limitValue :
                    TimeC_Ekleme(TimeC,priority,count1,count2)
                else :
                    ShiftedValue.append(priority[count1][count2])
                if len(ShiftedValue) > 0 and TimeC[count2-3] < limitValue :
                    ShiftedCount=len(ShiftedValue)
                    TimeC_ShiftedEkleme(TimeC,ShiftedValue,ShiftedCount,count2,limitValue)
    return

def SaatlikToplayici2(priority,TimeC):
    elementSayisi=len(priority)
    elementinelementSayisi=len(priority[0])
    for count1 in range(elementSayisi):
        for count2 in range(3,elementinelementSayisi):
            sayiTimeC= TimeC[count2-3]
            sayiPriority= priority[count1][count2]
            TimeC[count2-3] = sayiTimeC + sayiPriority
    return

def discharge(batteryCurrentCharge,batteryMaxCap,batteryHourlyChargeValues,currentHour):
    if SOC(batteryCurrentCharge,batteryMaxCap) > 30: 
        batteryHourlyChargeValues[currentHour]=batteryCurrentCharge-batteryDisChargeCap
    return

loc = ("list3.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

Gn_Elektrik_Birim_Fiyat=input("Gündüz elektrik birim fiyatını girin.(TL/kWh)(Boş Bırakılırsa Alınacak Standart Değer: 0.4592 TL)\n")
if Gn_Elektrik_Birim_Fiyat == "":
    Gn_Elektrik_Birim_Fiyat=0.4592
    a=Gn_Elektrik_Birim_Fiyat+3

Pu_Elektrik_Birim_Fiyat=input("Puant elektrik birim fiyatını girin.(TL/kWh)(Boş Bırakılırsa Alınacak Standart Değer: 0.7035 TL)\n")
if Pu_Elektrik_Birim_Fiyat == "":
    Pu_Elektrik_Birim_Fiyat=0.7035

Ge_Elektrik_Birim_Fiyat=input("Gece elektrik birim fiyatını girin.(TL/kWh)(Boş Bırakılırsa Alınacak Standart Değer: 0.2853 TL\n")
if Ge_Elektrik_Birim_Fiyat == "":
    Ge_Elektrik_Birim_Fiyat=0.2853

Te_Elektrik_Birim_Fiyat=input("Tek zamanlı elektrik birim fiyatını girin.(TL/kWh)(Boş Bırakılırsa Alınacak Standart Değer: 0.4612 TL\n")
if Te_Elektrik_Birim_Fiyat == "":
    Te_Elektrik_Birim_Fiyat=0.4612

e_source=[]
priorityList=[]
limitValue=6000
batteryMaxCap=limitValue/2
batteryPerMax=batteryMaxCap*80/100
batteryChargeCap=batteryMaxCap*20/100
batteryDisChargeCap=batteryMaxCap*30/100
batteryCiH=[]
batteryCurrentCharge=300
batteryHourlyChargeValues=[]
batteryPerVal=[]

n=6
for i in range(n):
    priorityList.append([])

for i in range(1,sheet.nrows): 
    cell_value=sheet.cell_value(i, 0)
    print(cell_value)
    if cell_value == 1:
        priorityList[0].append(sheet.row_values(i))
    if cell_value == 2:
        priorityList[1].append(sheet.row_values(i))
    if cell_value == 3:
        priorityList[2].append(sheet.row_values(i))
    if cell_value == 4:
        priorityList[3].append(sheet.row_values(i))
    if cell_value == 5:
        priorityList[4].append(sheet.row_values(i))
    if cell_value == 6:
        priorityList[5].append(sheet.row_values(i))
    if cell_value == 12:
        e_source.append(sheet.row_values(i))

for i in range(len(priorityList)):
    TabloX(priorityList[i])

TabloX(e_source)

for i in range(3,len(e_source[0])):
    if batteryChargeCap <= e_source[0][2]:
        batteryCiH.append(e_source[0][i])
    elif batteryChargeCap-e_source[0][2] <0: 
        batteryCiH.append(batteryChargeCap)
        #fazla elektriği sat    

print(SOC(batteryCurrentCharge,batteryMaxCap))

for i in range(len(batteryCiH)):
    if batteryCurrentCharge+batteryCiH[i] > batteryPerMax:
        batteryCurrentCharge=batteryPerMax
        batteryHourlyChargeValues.append(batteryCurrentCharge)
                                                                    #batteryPerVal.append(SOC(batteryHourlyChargeValues[i],batteryMaxCap))
        #satfonk(batteryCurrentCharge+batteryCiH[i]-batteryPerMax)
    else:
        batteryCurrentCharge=batteryCurrentCharge+batteryCiH[i]
        batteryHourlyChargeValues.append(batteryCurrentCharge)
                                                                    #batteryPerVal.append(SOC(batteryHourlyChargeValues[i],batteryMaxCap))
    if 16<i<23:
        discharge(batteryCurrentCharge,batteryMaxCap,batteryHourlyChargeValues,i)



time = list(range(1,25))
TimeC=[0]*24
TimeC2=[0]*24
TimeC3=[0]*24
e_time=[]
t_time=[]
count2=3


for i in range(len(priorityList)):
    SaatlikToplayici2(priorityList[i],TimeC2)

for i in range(len(priorityList)):
    SaatlikToplayici(priorityList[i],TimeC,limitValue)

toplam_TimeC=0
toplam_TimeC2=0
for i in range(24):
    toplam_TimeC=+toplam_TimeC + TimeC[i]
    toplam_TimeC2=toplam_TimeC2 + TimeC2[i]

print("toplam_TimeC:",toplam_TimeC,"\ntoplam_TimeC2:",toplam_TimeC2)

limittime= []
for i in range(24):
    limittime.append(limitValue)

plt5= plt.figure(5)
plt.title('Smart Consumption')
plt.step(time, TimeC,color='orange')
plt.plot(time,limittime,color='red')
plt.xlabel('Time')
plt.ylabel('Watt') 

plt6= plt.figure(6)
plt.title('Standart Consumption')
plt.xlabel('Time')
plt.ylabel('Watt') 
plt.step(time, TimeC2,color='blue')
plt.plot(time,limittime,color='red')

plt7 = plt.figure(7)
plt.title("Consumption Comparison")
plt.xlabel('Time')
plt.ylabel('Watt') 
plt.step(time, TimeC,color="orange")
plt.step(time, TimeC2,color="blue")
plt.plot(time,limittime,color='red')

fig = plt.figure()
plt1 = fig.add_subplot(221)
plt2 = fig.add_subplot(222)
plt3 = fig.add_subplot(223)

plt1.step(time, TimeC,color='orange')
plt1.plot(time,limittime,color='red')

plt2.step(time, TimeC2,color='blue')
plt2.plot(time,limittime,color='red')

plt3.step(time, TimeC,color="orange")
plt3.step(time, TimeC2,color="blue")
plt3.plot(time,limittime,color='red')

plt.show()