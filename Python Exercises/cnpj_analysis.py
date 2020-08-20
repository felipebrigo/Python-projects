import timeit

#Slicing the whole datafile in 1200 characters each time
def slicing():
    global data_length
    global data
    textsliced=[]
    a=0
    '''bunchsize = 1000000
    bunch = []
        for line in r:
            x, y, z = line.split(' ')[:3]
            bunch.append(line.replace(x,x[:-3]).replace(y,y[:-3]).replace(z,z[:-3]))
            if len(bunch) == bunchsize:
                w.writelines(bunch)
                bunch = []
        w.writelines(bunch)'''
    with open("/Users/mac/Documents/Lista FCA Leandro/Teste-layout.txt", "r") as r, open("teste.txt", "w") as w:
        r=r.read()
        textsliced=[r[i:i+1200] for i in range(0, len(r), 1200)]
    #with open(("teste.txt"), 'w') as file:
        w.writelines(textsliced)
    #return r
'''    for a in range(a,len(textsliced)):
        
        print(textsliced[a],end="")
    
    a=0
    i=0
    j=1199
    d=""
    d=data[i:j]
    for a in range(0,data_length,1200):
        d=data[i:j]
        data_list.append(d)
        i+=1200
        j+=1200
'''
slicing()
#print(data_list)
#print(data[0:100])
#print(data[-1000:-1])      
#print(len(r))
print(timeit.timeit(slicing, number=1))

'''
#Header treatment - 1200 characteres
def header_treatment():
    global data
    header=data[0:1199]
    #Here head treatment and slices 
    
#Company treatment - 1200 characters    
def data_cnpj():
    global data
    company_data=data[0:1199]

#Partners treatment - 1200 characters
def partner():
    global data
    partner_data=data[0:1199]


#Import Pandas to re-arrange all list

#Export to csv file

#Main
slicing()
header_treatment()


import pprint
pp=pprint.PrettyPrinter(indent=4)
pp.pprint(data)
print(len(data))'''
