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
    #buraya yeni liste ekle bu liste fazla olan enerjilerin aletlerinin değerlerini ve sürelerini alsın
    ShiftedValue=[]
    #ShiftedValue_Subset=[]
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


loc = ("list3.xlsx")
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
limitValue=6000

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
TimeC2=[0]*24
TimeC3=[0]*24
e_time=[]
t_time=[]
count2=3
print(TimeC[count2-3])
print("asdasdasdasd")

SaatlikToplayici2(priority1,TimeC2)
SaatlikToplayici2(priority2,TimeC2)
SaatlikToplayici2(priority3,TimeC2)
SaatlikToplayici2(priority4,TimeC2)
SaatlikToplayici2(priority5,TimeC2)
SaatlikToplayici2(priority6,TimeC2)


SaatlikToplayici(priority1,TimeC,limitValue)
SaatlikToplayici(priority2,TimeC,limitValue)
SaatlikToplayici(priority3,TimeC,limitValue)
SaatlikToplayici(priority4,TimeC,limitValue)
SaatlikToplayici(priority5,TimeC,limitValue)
SaatlikToplayici(priority6,TimeC,limitValue)

toplam_TimeC=0
toplam_TimeC2=0
for i in range(24):
    toplam_TimeC=+toplam_TimeC + TimeC[i]
    toplam_TimeC2=toplam_TimeC2 + TimeC2[i]

print("toplam_TimeC:",toplam_TimeC,"\ntoplam_TimeC2:",toplam_TimeC2)


print("fin2")


print("fin2.5")

plt.step(time, TimeC)
#plt.step(time, e_time)
#plt.plot(time,limittime,color='red')
plt.show()
plt.step(time, TimeC2)
plt.show()
plt.step(time, TimeC)
plt.step(time, TimeC2)
plt.show()
print("fin3")

plt1= plt.figure(1)
plt.step(time, TimeC)

plt2= plt.figure(2)
plt.step(time, TimeC2)

plt.show()
#raw_input()




