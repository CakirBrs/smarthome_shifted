import xlrd
import matplotlib.pyplot as plt

loc = ("list3.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
BirimFiyatlar=[]
Gn_Elektrik_Birim_Fiyat=0.4592
BirimFiyatlar.append(Gn_Elektrik_Birim_Fiyat)
Pu_Elektrik_Birim_Fiyat=0.7035
BirimFiyatlar.append(Pu_Elektrik_Birim_Fiyat)
Ge_Elektrik_Birim_Fiyat=0.2853
BirimFiyatlar.append(Ge_Elektrik_Birim_Fiyat)
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