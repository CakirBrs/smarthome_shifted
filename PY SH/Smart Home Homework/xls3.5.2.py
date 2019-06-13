import xlrd
import matplotlib.pyplot as plt

def SOC(ChargeofBattery,BatteryCapacity):
    Socc=(ChargeofBattery*100/BatteryCapacity)
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
                hulog = girdi[icdekiler][2]
            else:
                print("""TABLO "x" Error :""" , icdekilerinYani)
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
    TimeC[count2-3] = sayiTimeC + sayiShifted
    
    return

def SaatlikToplayici(priority,TimeC,limitValue):
    elementSayisi=len(priority)
    elementinelementSayisi=len(priority[0])
    ShiftedValue=[]
    ShiftedCount=0
    for count1 in range(elementSayisi):
        for count2 in range(3,elementinelementSayisi):
            if False == isPeakTime(count2):
                TimeC_Ekleme(TimeC,priority,count1,count2)
                if len(ShiftedValue) > 0 :
                    ShiftedCount=len(ShiftedValue)
                    for i in range(ShiftedCount):
                        TimeC_ShiftedEkleme(TimeC,ShiftedValue,(ShiftedCount-1),count2,limitValue)
                        del ShiftedValue[-1]
            elif True == isPeakTime(count2):
                if TimeC[count2-3]+priority[count1][count2] < limitValue :
                    TimeC_Ekleme(TimeC,priority,count1,count2)
                else :
                    ShiftedValue.append(priority[count1][count2])                   
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

def discharge(batteryCurrentCharge,batteryMaxCap,batteryHourlyChargeValues,currentHour,YeniTimeC):
    if SOC(batteryCurrentCharge,batteryMaxCap) > 30: 
        print(YeniTimeC[currentHour])
        if SOC((batteryCurrentCharge-batteryDisChargeCap),batteryMaxCap) > 30:
            batteryCurrentCharge=batteryCurrentCharge-batteryDisChargeCap
            NewbatteryCurrenttChargee=batteryCurrentCharge
            batteryHourlyChargeValues[currentHour]=batteryCurrentCharge
            YeniTimeC[currentHour]=YeniTimeC[currentHour]-batteryDisChargeCap
        else:
            if batteryDisChargeCap-batteryCurrentCharge<0:
                sebekedenCekilenAzElktrik=batteryCurrentCharge-batteryDisChargeCap
            elif batteryDisChargeCap-batteryCurrentCharge>0:
                sebekedenCekilenAzElktrik=batteryDisChargeCap-batteryCurrentCharge
            batteryCurrentCharge=900
            YeniTimeC[currentHour]=YeniTimeC[currentHour]-sebekedenCekilenAzElktrik
        
    
    print(YeniTimeC[currentHour])
    NewbatteryCurrenttChargee=batteryCurrentCharge
    return NewbatteryCurrenttChargee

def SellE(currentE,currentTime,BirimFiyatlar):
    if (7 <= currentTime <= 17) :
        UcZamanliGelir=currentE*BirimFiyatlar[0]
    if (17 <= currentTime <= 22) :
        UcZamanliGelir=currentE*BirimFiyatlar[1]
    if (22 <= currentTime <= 23) or (0 <= currentTime <= 7) :
        UcZamanliGelir=currentE*BirimFiyatlar[2]
    TekZamanliGelir=currentE*BirimFiyatlar[3]
    return (TekZamanliGelir,UcZamanliGelir)
    
season = input("1: Winter\n2: Summer\nSelect season:")
if season=="1":
    loc = ("winter.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    seasonn="Winter"
elif season == "2":
    loc = ("summer.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    seasonn="Summer"
else:
    print("Only type 1 or 2. Please restart this script.")

BirimFiyatlar=[]
Gn_Elektrik_Birim_Fiyat=input("Tpye daylight power price per kWh. Leave blank for standard value.(Standart Value: 0.4592 TL)\n") #Gündüz elektrik birim fiyatını girin.(TL/kWh)(Boş Bırakılırsa Alınacak Standart Değer
if Gn_Elektrik_Birim_Fiyat == "":
    Gn_Elektrik_Birim_Fiyat=0.4592
    a=Gn_Elektrik_Birim_Fiyat+3
BirimFiyatlar.append(Gn_Elektrik_Birim_Fiyat)

Pu_Elektrik_Birim_Fiyat=input("Tpye puant power price per kWh. Leave blank for standard value.(Standart Value: 0.7035 TL)\n") #Standart Value:Puant elektrik birim fiyatını girin.(TL/kWh)(Boş Bırakılırsa Alınacak Standart Değer
if Pu_Elektrik_Birim_Fiyat == "":
    Pu_Elektrik_Birim_Fiyat=0.7035
BirimFiyatlar.append(Pu_Elektrik_Birim_Fiyat)

Ge_Elektrik_Birim_Fiyat=input("Tpye night time power price per kWh. Leave blank for standard value.(Standart Value: 0.2853 TL)\n") #Gece elektrik birim fiyatını girin.(TL/kWh)(Boş Bırakılırsa Alınacak Standart Değer
if Ge_Elektrik_Birim_Fiyat == "":
    Ge_Elektrik_Birim_Fiyat=0.2853
BirimFiyatlar.append(Ge_Elektrik_Birim_Fiyat)

Te_Elektrik_Birim_Fiyat=input("Tek zamanlı elektrik birim fiyatını girin.(TL/kWh)(Boş Bırakılırsa Alınacak Standart Değer: 0.4612 TL)\n")
if Te_Elektrik_Birim_Fiyat == "":
    Te_Elektrik_Birim_Fiyat=0.4612
BirimFiyatlar.append(Te_Elektrik_Birim_Fiyat)

e_source=[]
priorityList=[]
limitValue=7000
batteryMaxCap=6000/2
batteryPerMax=batteryMaxCap*80/100
batteryChargeCap=batteryMaxCap*20/100
batteryDisChargeCap=batteryMaxCap*30/100
batteryCiH=[]
batteryCurrentCharge=300
batteryHourlyChargeValues=[]
batteryPerVal=[]
FazlaElektrik=[]

for i in range(27):
    FazlaElektrik.append(0)

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
        FazlaElektrik[i]=(e_source[0][2]-batteryChargeCap)

print(SOC(batteryCurrentCharge,batteryMaxCap))

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

print(seasonn,limitValue,"toplam_TimeC:",toplam_TimeC,"\n",seasonn,limitValue,seasonn ,"toplam_TimeC2:",toplam_TimeC2)

limittime= []
for i in range(24):
    limittime.append(limitValue)

YeniTimeC=[]
for i in range(len(TimeC)):
    YeniTimeC.append(0)

for i in range(len(TimeC)):
    YeniTimeC[i]=TimeC[i]

print(" ")

for i in range(len(batteryCiH)):
    if batteryCurrentCharge+batteryCiH[i] > batteryPerMax and (i<17 and 22<i):
        FazlaElektrik[i]=(batteryCurrentCharge+batteryCiH[i])-batteryPerMax
        batteryCurrentCharge=batteryPerMax
        batteryHourlyChargeValues.append(batteryCurrentCharge)
                                                                    #batteryPerVal.append(SOC(batteryHourlyChargeValues[i],batteryMaxCap))
        #satfonk(batteryCurrentCharge+batteryCiH[i]-batteryPerMax)
    elif i<17 or 22<i:
        batteryCurrentCharge=batteryCurrentCharge+batteryCiH[i]
        batteryHourlyChargeValues.append(batteryCurrentCharge)
                                                                    #batteryPerVal.append(SOC(batteryHourlyChargeValues[i],batteryMaxCap))
    elif 16<i<23:
        batteryHourlyChargeValues.append(batteryCurrentCharge)
    else:
        print("WTF!!")
    if 16<i<23:
        batteryCurrentCharge=discharge(batteryCurrentCharge,batteryMaxCap,batteryHourlyChargeValues,i,YeniTimeC)
        batteryHourlyChargeValues[i]=batteryCurrentCharge

toplam_TimeC=0
toplam_TimeC2=0
toplam_YeniTimeC=0
for i in range(24):
    toplam_TimeC=+toplam_TimeC + TimeC2[i]
    toplam_YeniTimeC=toplam_YeniTimeC + YeniTimeC[i]

print(seasonn,limitValue,"1.1:",toplam_TimeC/1000,"\n",seasonn,limitValue,"1.5:",toplam_YeniTimeC/1000)
gündüzFatura=0
puantFatura=0
geceFatura=0
tekzfatura=0

gündüzFatura2=0
puantFatura2=0
geceFatura2=0
tekzfatura2=0

for i in range(len(TimeC2)):
    if 6<i<17:
        gündüzFatura=gündüzFatura+YeniTimeC[i]-FazlaElektrik[i+3]
        gündüzFatura2=gündüzFatura2+TimeC2[i]
    elif 16<i<22:
        puantFatura=puantFatura+YeniTimeC[i]-FazlaElektrik[i+3]
        puantFatura2=puantFatura2+TimeC2[i]
    elif i>21 or i<7:
        geceFatura=geceFatura+YeniTimeC[i]-FazlaElektrik[i+3]
        geceFatura2=geceFatura2+TimeC2[i]
    tekzfatura=tekzfatura+YeniTimeC[i]-FazlaElektrik[i+3]
    tekzfatura2=tekzfatura2+TimeC2[i]

ToplamFatura=(gündüzFatura*(BirimFiyatlar[0])/1000+puantFatura*BirimFiyatlar[1]/1000+geceFatura*BirimFiyatlar[2]/1000)
tekzfaturatutar=tekzfatura*BirimFiyatlar[3]/1000

ToplamFatura2=(gündüzFatura2*(BirimFiyatlar[0])/1000+puantFatura2*BirimFiyatlar[1]/1000+geceFatura2*BirimFiyatlar[2]/1000)
tekzfaturatutar2=tekzfatura2*BirimFiyatlar[3]/1000
#print("A:",ToplamFatura,"\nB:",ToplamFatura2)
print(seasonn,limitValue,"  Smart triple-time tariff bill:",ToplamFatura,"TL\n",seasonn,limitValue,"Smart single-time tariff bill:",tekzfaturatutar,"TL")
print(seasonn,limitValue,"  Standart triple-time tariff:",ToplamFatura2,"TL\n",seasonn,limitValue," Standart single-time tariff bill:",tekzfaturatutar2,"TL")

skz=[]
skz1=[]
skz2=[]
skz3=[]
skz2.append(22)
skz2.append(22)
skz1.append(17)
skz1.append(17)
skz.append(0)
skz.append(10000)
skz3.append(0)
skz3.append(3000)

sayacc=0
sayacc2=0
for i in range(len(TimeC)):
    sayacc=TimeC[i]+sayacc
    sayacc2=TimeC2[i]+sayacc2


plt5= plt.figure(5)
plt.title('1.2')
plt.plot(skz1,skz , color='black', linestyle='dashed')
plt.plot(skz2,skz , color='black', linestyle='dashed')
plt.step(time, TimeC,color='orange')
plt.plot(time,limittime,color='red')
plt.xlabel('Time')
plt.ylabel('Watt') 

plt8= plt.figure(8)
plt.title('1.5')
plt.plot(skz1,skz , color='black', linestyle='dashed')
plt.plot(skz2,skz , color='black', linestyle='dashed')
plt.step(time, YeniTimeC,color='green')
plt.plot(time,limittime,color='red')
plt.xlabel('Time')
plt.ylabel('Watt') 

plt9= plt.figure(9)
plt.title('1.4')
#plt.plot(skz1,skz3 , color='black', linestyle='dashed')
#plt.plot(skz2,skz3 , color='black', linestyle='dashed')
plt.step(time, batteryHourlyChargeValues,color='green')
plt.xlabel('Time')
plt.ylabel('Watt')

plt10= plt.figure(10)
plt.title('1.3')
#plt.plot(skz1,skz , color='black', linestyle='dashed')
#plt.plot(skz2,skz , color='black', linestyle='dashed')
plt.plot(time, batteryCiH,color='green')
plt.xlabel('Time')
plt.ylabel('Watt')

plt6= plt.figure(6)
plt.title('1.1')
plt.xlabel('Time')
plt.ylabel('Watt') 
plt.plot(skz1,skz , color='black', linestyle='dashed')
plt.plot(skz2,skz , color='black', linestyle='dashed')
plt.step(time, TimeC2,color='blue')
plt.plot(time,limittime,color='red')

plt7 = plt.figure(7)
plt.title("Summer Consumption Comparison")
plt.xlabel('Time')
plt.ylabel('Watt') 
plt.step(time, TimeC,color="orange")
plt.step(time, TimeC2,color="blue")
plt.step(time, YeniTimeC,color="green")
plt.plot(time,limittime,color='red')
plt.plot(skz1,skz , color='black', linestyle='dashed')
plt.plot(skz2,skz , color='black', linestyle='dashed')

fig = plt.figure()
plt1 = fig.add_subplot(221)
plt2 = fig.add_subplot(222)
plt3 = fig.add_subplot(223)
plt4 = fig.add_subplot(224)

plt1.step(time, TimeC,color='orange')
plt1.plot(time,limittime,color='red')

plt2.step(time, TimeC2,color='blue')
plt2.plot(time,limittime,color='red')

plt3.step(time, TimeC,color="orange")
plt3.step(time, TimeC2,color="blue")
plt3.plot(time,limittime,color='red')

plt4.step(time, YeniTimeC,color='orange')
plt4.plot(time,limittime,color='red')

plt.show()
