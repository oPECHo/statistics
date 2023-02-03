import statistics as stat
import math
from tabulate import tabulate
def classInterval(data,iniate,terminate,Np):
    I=math.ceil((terminate-iniate)/Np)
    Iuse=I-1
    fsum=0
    for i in range(1,Np+1):
        end=iniate+Iuse
        f=0
        for num in data:
            if iniate<= num <= end:
                f+=1
        fsum=fsum+f
        RF=f/N
        Per=RF*100
        RFS=fsum/N
        FPer=RFS*100
        Aclass = str(iniate)+"-"+str(end)
        table = [[i,Aclass,f,fsum,RF,Per,RFS,FPer]]
        print(tabulate(table,tablefmt="plain"))
        iniate=end+1
while True:
 data=[]
 นอกเกณ=[]
 #input
 try:
     Percent=float(input("Percentile(if don't want to find type None):"))
 except:
     Percent= None
 data=[float(i) for i in input("input:").split()]#เติมข้อมูลตัวเลขหลายตัว
 #process
 data.sort()
 Max= max(data)
 Min= min(data)
 N=len(data)
 #Average
 Avg=stat.mean(data)
 #med
 Med=stat.median(data)
 #mean
 Mode=stat.mode(data)
 
 def mean(list):
     x=(0,0)
     for num in list:
         k=list.count(num)
         if k > x[0]:
             x=(k,num)
     return x[1]
 

 #find summation on list
 def summation(number):
     total=0
     for i in number :
         total+=i
     return total
 sum=summation(data)
 
 #พิสัย
 พิสัย=Max-Min
 
 #Med
 c=(N//2)-1
 if N%2==0:
     Med=(data[c]+data[c+1])/2
 else:
     Med=data[c+1]

 #Q
 IxQ1=((N+1)/4)-1
 IxQ2=(IxQ1*2)+1
 IxQ3=(IxQ1*3)+2
 #Q1
 z=int(IxQ1//1)
 Q1=data[z]+(data[z+1]-data[z])*(IxQ1-z)
 #Q2
 a=int(IxQ2//1)
 Q2=data[a]+(data[a+1]-data[a])*(IxQ2-a)
 #Q3
 b=int(IxQ3//1)
 Q3=data[b]+(data[b+1]-data[b])*(IxQ3-b)
 IQR=Q3-Q1
 #SD
 sumSD=0
 for x in data:
     y=(x-Avg)**2
     sumSD+=y
 SDประชากร=(sumSD/N)**(1/2)
 SDตัวอย่าง=(sumSD/(N-1))**(1/2)
 #Out range
 นอกเกณสูงสุด=Q3+1.5*IQR
 นอกเกณต่ำสุด=Q1-1.5*IQR
 for x in data:
     if x<นอกเกณต่ำสุด:
         นอกเกณ.append(x)
     elif x>นอกเกณสูงสุด:
         นอกเกณ.append(x)
 #Percentile
 
 if Percent != None:
   IxP=((N+1)*Percent/100)-1
   p=int(IxP//1)
   Percentile=data[p]+(data[p+1]-data[p])*(IxP-p)
 else:
   Percentile=""
 #output
 print("data:",data)
 print("N:",N)
 print("max:",Max)
 print("min:",Min)
 print("range:",พิสัย)
 print("average:",Avg)
 print("Median:",Med)
 print("Mode:",Mode)
 print("Q1:",Q1,"Q2:",Q2,"Q3:",Q3)
 print("Percentile:",Percentile)
 print("IQR:",IQR)
 print("SD Population:",'%.2f'%SDประชากร,"varaince:",'%.2f'%(SDประชากร**2),"CV:",'%.2f'%(SDประชากร/Avg))
 print("SD Exammple:",'%.2f'%SDตัวอย่าง,"varaince:",'%.2f'%(SDตัวอย่าง**2),"CV:",'%.2f'%(SDตัวอย่าง/Avg))
 print("Out of range:",นอกเกณ)
 #class Interval
 try:
     x,y,z=(int(i) for i in input("start last layer(if don't want type None):").split())
 except:
     x,y,z= None,None,None
 if x != None:
    classInterval(data,x,y,z)
 print("-----------------------------------------------------------------------------------------")