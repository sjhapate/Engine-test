import os
import numpy as np
import csv
import pdb
import itertools
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Auswertung_Teillast_Ventilspiel_Lekage.xlsx', sheet_name='Teillast kalt')
a=df[['Mittelwert von min max ']]

# Replace NaN with zero and infinity with large finite numbers (default behaviour) numpy format.
b = np.nan_to_num(np.array(a)) 

raw_data = [];min_max0 = [];min_max1 = [];min_max2 = [];min_max3 = [];min_max4 = [];min_max5 = []
t1=[];t2=[];t3=[]

# -------importance parameters of engine to plot graph-------
offset=int(71)
number_cyl=int(3)
encoder=int((768)/(number_cyl*2))
gate_width = int(50)
# ------------------------------------------------------------

# def window_size(num_of_cyl):
#     t=0;
#     for i in range(num_of_cyl):  
#         if i==0:
#             val_strcyl1= int(offset-(int(gate_width/2)))
#             strtcyl.append(val_strcyl1) 
#             stopcyl.append(int(strtcyl[t]+gate_width)) 
#         else:
#             strtcyl.append(int(strtcyl[t]+(encoder)))             
#             stopcyl.append(int(stopcyl[t]+(encoder)))
#             t += 1
            
# window_size(number_cyl*2);
    
# calculation of all three cylinders start/stop window size  
strtcyl1= int(offset-(int(gate_width/2))); stopcyl1= int(strtcyl1+gate_width)
strtcyl2= int(strtcyl1+(encoder)); stopcyl2= int(stopcyl1+(encoder))
strtcyl3= int(strtcyl2+(encoder)); stopcyl3= int(stopcyl2+(encoder))
strtcyl4= int(strtcyl3+(encoder)); stopcyl4= int(stopcyl3+(encoder))
strtcyl5= int(strtcyl4+(encoder)); stopcyl5= int(stopcyl4+(encoder))
strtcyl6= int(strtcyl5+(encoder)); stopcyl6= int(stopcyl5+(encoder))
# ------------------------------------------------------------

#finding max/min values of all cylinders from their window size     
q1=np.max(b[strtcyl1:stopcyl1]) 
q2=np.min(b[strtcyl2:stopcyl2])
q3=np.max(b[strtcyl3:stopcyl3])
q4=np.min(b[strtcyl4:stopcyl4])
q5=np.max(b[strtcyl5:stopcyl5])
q6=np.min(b[strtcyl6:stopcyl6])

# Get the indices of maximum and minimum element in numpy array
result0 = np.where(b[strtcyl1:stopcyl1] == np.amax(b[strtcyl1:stopcyl1]))
# print('List of Indices of maximum element :', strtcyl1+result0[0])

result1 = np.where(b[strtcyl2:stopcyl2] == np.amin(b[strtcyl2:stopcyl2]))
# print('List of Indices of minimum element :', strtcyl2+result1[0])

result2 = np.where(b[strtcyl3:stopcyl3] == np.amax(b[strtcyl3:stopcyl3]))
# print('List of Indices of maximum element :', strtcyl3+result2[0])

result3 = np.where(b[strtcyl4:stopcyl4] == np.amin(b[strtcyl4:stopcyl4]))
# print('List of Indices of minimum element :', strtcyl4+result3[0])

result4 = np.where(b[strtcyl5:stopcyl5] == np.amax(b[strtcyl5:stopcyl5]))
# print('List of Indices of maximum element :', strtcyl5+result4[0])

result5 = np.where(b[strtcyl6:stopcyl6] == np.amin(b[strtcyl6:stopcyl6]))
# print('List of Indices of minimum element :', strtcyl6+result5[0])

#comparison of three cylinder at same point 
for j in b[int(strtcyl1+result0[0]):int(strtcyl3+result2[0]+50)]:
    #print(j)
    t1.append(j-b[int(strtcyl1+result0[0])]);

for j in b[int(strtcyl3+result2[0]):int(strtcyl5+result4[0]+50)]:
    t2.append(j-b[int(strtcyl3+result2[0])]);

for j in b[int(strtcyl5+result4[0]):int(encoder+strtcyl6+result5[0]+50)]:
    t3.append(j-b[int(strtcyl5+result4[0])]);
    

plt.figure(1, figsize=(10, 10))
font = {'family': 'serif','color':  'red','weight': 'normal','size': 25,}

ind = np.arange(3)
width = 0.35
plt.ylabel('Max value of each cylinder',font)
plt.title('Monitoring of three cylinder ',font)
# plt.xticks(ind, ('cylinder 1','cylinder 2', 'cylinder 3', 'cylinder 1', 'cylinder 2', 'cylinder 3'),rotation='vertical',color='r')
plt.xlabel('Pulse',font)
plt.grid(linestyle='-', linewidth=0.5,axis='both', which='major')

wa=[q1-q2,q3-q4,q5-q6]
w_comp=[t1,t2,t3]

wacc=[q1-q2,q1-q2,q1-q2]

p1=plt.plot(t1,'r--')
p2=plt.plot(t2,'b--')
p3=plt.plot(t3,'g--')
plt.legend(['cylinder 1','cylinder 2','cylinder 3'],fontsize = 'xx-large')
# plt.legend(p1,p3,p2,('cylinder 1','cylinder 2', 'cylinder 3'),fontsize = 'x-large')
# p2=plt.bar(ind, wa, width,color='r')
# p1=plt.bar(ind, wacc, width,color='g')
plt.savefig("test1.png")
plt.show()