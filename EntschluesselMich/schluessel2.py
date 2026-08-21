from Object_class import Schluessel
import time

schluessel=Schluessel()

dict={-1:[0,0],0:[0,0],1:[3,4],2:[9,3],3:[1,4],4:[4,7],5:[2,0],6:[9,4],7:[1,0],8:[9,1],
        9:[2,7],10:[3,6],11:[1,0],12:[1,5]}

time_now=0

for value in dict:
    if time_now==4:
        entry=schluessel.schluessel
        if entry==2:
            schluessel.name=6
            schluessel.write("file.csv",[schluessel.name])
            time_now += 1
            time.sleep(1)
            continue
    schluessel.name=dict[value][schluessel.age]
    schluessel.write("file.csv", [schluessel.name])
    time_now+=1
    time.sleep(1)

schluessel.write("file.csv", [""])

