import xlrd
import matplotlib.pyplot as plt

def ExcelDelX(List):
    ListCount=len(List)
    print(ListCount)
    ListCountSubset=len(List[0])
    print(ListCountSubset)
    for count in range(ListCount):
        for count2 in range(3,ListCountSubset):
            value=List[count][count2]
            if value == "":
                value = 0
            elif value == "x" or value == "X":
                #print(List[count][2])
                value = List[count][2]
            else:
                print("""Excel "x" ERROR :""" , count2)
                continue
            List[count][count2] = value
    return

def isPeakTime (time):
    if (time-3) in [17,18,19,20,21,22]:
        return True
    else:
        return False

def Add_TimeC(TimeC,priority,count1,count2):

    valueTimeC= TimeC[count2-3]
    valuePriority= priority[count1][count2]
    TimeC[count2-3] = valueTimeC + valuePriority
    return


def Add_Shifted_TimeC(TimeC,ShiftedValue,ShiftedCount,count2,limitValue):

    valueTimeC= TimeC[count2-3]
    valueShifted= ShiftedValue[ShiftedCount-1]
    if valueTimeC+valueShifted > limitValue :
        return
    TimeC[count2-3] = valueTimeC + valueShifted
    del ShiftedValue[-1]
    return


def addition_hours_value(priority,TimeC,limitValue):
    ElementNumber=len(priority)
    NumberOfElementNumber=len(priority[0])
    ShiftedValue=[]
    for count1 in range(ElementNumber):
        for count2 in range(3,NumberOfElementNumber):
            if False == isPeakTime(count2):
                Add_TimeC(TimeC,priority,count1,count2)
                if len(ShiftedValue) > 0 :
                    ShiftedCount=len(ShiftedValue)
                    Add_Shifted_TimeC(TimeC,ShiftedValue,ShiftedCount,count2,limitValue)
                
            elif True == isPeakTime(count2):
                if TimeC[count2-3]+priority[count1][count2] < limitValue :
                    Add_TimeC(TimeC,priority,count1,count2)
                else :
                    ShiftedValue.append(priority[count1][count2])
                
                if len(ShiftedValue) > 0 and TimeC[count2-3] < limitValue :
                    ShiftedCount=len(ShiftedValue)
                    Add_Shifted_TimeC(TimeC,ShiftedValue,ShiftedCount,count2,limitValue)
    return


def SaatlikToplayici2(priority,TimeC): #ötelenmeyen
    elementSayisi=len(priority)
    elementinelementSayisi=len(priority[0])
    for count1 in range(elementSayisi):
        for count2 in range(3,elementinelementSayisi):
            sayiTimeC= TimeC[count2-3]
            sayiPriority= priority[count1][count2]
            TimeC2[count2-3] = sayiTimeC + sayiPriority
    return