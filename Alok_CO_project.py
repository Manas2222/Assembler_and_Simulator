# import csv
# from helper import *


# def Addition(Lst):
#     if (len(Lst) !=4 ):
#         return -1
    

#     if (registers(Lst[1]) == -1 or registers(Lst[2]) == -1 or registers(Lst[3]) == -1):
#         #errors found +=1
#         return -1
    
#     op_code = opcode(Lst[0])
#     if (op_code == -1): 
#         #errors Found += 1
#         return -1
    
#     op_code = op_code + '00' + registers(Lst[1]) + registers(Lst[2]) + registers(Lst[3])

#     return op_code

def readfile():
    f=open('C:\Users\aloks\Desktop\CO_text.txt','r')
    data = f.read()
    file_lst = data.split()
    for i in file_lst:
        Lst=[]
        if i != '\n' and i != ',' :
            Lst.append(i)
            if len(Lst) == 4: # eg. add, r1,r2,r3
                print (Addition(Lst))
                Lst.clear()   # clears list after every function call for the next elements be inserted
readfile()


# print('--------------')
# Lst=['add', 'R1', 'R2', 'R3']
# print(Addition(Lst))