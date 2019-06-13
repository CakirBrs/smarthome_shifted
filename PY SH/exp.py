limittime= []
limittime2=[]
limit2=[]
"""
for i in range(24):
    x=i
    limittime.append(x)
    limittime2.append(100+x)

limit2.append(limittime)
limit2.append(limittime2)

a=1000
#del limittime2[-1]
print(limit2[0][23])

print("fin")

def TabloX(girdi):
    iceriSayi=len(girdi)
    print(iceriSayi)
    iciniciSayi=len(girdi[0])
    print(iciniciSayi)
    for icdekiler in range(iceriSayi):
        for icdekilerinYani in range(3,iciniciSayi):
            hulog=girdi[icdekiler][icdekilerinYani]
            if hulog=="":
                hulog=0
            elif hulog=="x" or hulog=="X":
                hulog=girdi[icdekiler][3]
            else:
                print("TABLO "x" HATASI ")
                continue
            girdi[icdekiler][icdekilerinYani]=hulog


TabloX(limit2)

deneme0=0
deneme1=0
deneme2=0
deneme3=0
#for i in range(3):
#    deneme + i=0
#    print(deneme + i)


time=17
if time in [17,18,19,20,21,22]:
    print("sdfsdfsdf")

print("mhhcvb")
"""
A=[1,2,3,4,5,6,7,8,9,10]

B=[5]*3
C=[6]*4
A.insert(1,B)
liste=[]
liste.append(0)
a=len(liste)
listeS=liste[a-1]


A=B
sss=18
if 16<sss<22:
    asdasd=15
print("fin")
deneme=[]
for i in range(23):
    deneme.append(0)
deneme[2]=0
print("fins")

