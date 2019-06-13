import xlrd 
import matplotlib.pyplot as plt

loc = ("list.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)


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
time = list(range(1,25))
time2=[]
e_time=[]
t_time=[]
limittime= []
battery_cap=0
