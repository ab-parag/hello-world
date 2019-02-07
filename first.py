#convert given data format to dictionary
########################################
#Comma seaprated data 

t="0 0.44 0.45,1 0.34 0.35,2 0.12 0.11"
d=dict()
li=t.split(',')
for i in li:
 #print(i)
 item=i.split(' ')[0]
 d[item] = i.split(' ')[1]

#print(d)

########################################
#totally unformatted data

t="0 0.44 0.48 1 0.44 0.59 2 0.39 0.59 3 0.35 0.70 4 0.39 0.74"
d=dict()
li=t.split(' ')
val=[]
key=0
flag=0
for i in li:
    if float(i).is_integer():
        key=int(i)
        flag=0
    else:
        val.append(float(i))
        d[key]=val
        flag=1
    if flag==0:
        val=[]
print(d)
