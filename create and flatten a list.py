

print ('Welcome to the bilimadam\'s codes.', end='\n' )
print ('...', end='\n')
print ('...', end='\n')
print ('...', end='\n')

def createbody(x):
    try:
        x.append (int(input('How long do you want to create a list = ')))
        return x
    except ValueError:
         print ('Please give a integer !', end='\n')
         createbody(listsize)

def intcontrol(x):
    try:
        a = int(x)
        return True
    except ValueError:
        return False

def floatcontrol(x):
    try:
        a = float(x)
        return True
    except ValueError:
        return False

def listcreate():
    a = []
    control1 = ''
    
    while (control1 != 'end'):
        control2 = input('Do you want to add a list in list ?''\n''if yes, write \'yes\'''\n''Answer = ')
        if control2 == 'yes':
            a.append(listcreate())
            control1 = input('To finish this section, write \'end\'''\n''if dont want to finish just enter''\n''Answer = ')
            continue
        
        x = input('Input : ')
        fcontrol = floatcontrol(x)
        icontrol = intcontrol(x)
        
        if x == 'True' or x == 'False':
            if x == 'True':
                a.append(True)
            else:
                a.append(False)
        elif icontrol == True:
            a.append(int(x))
        elif fcontrol == True:
            a.append(float(x))
        else:
            a.append(x)
        control1 = input('To finish this section, write \'end\'''\n''if dont want to finish just enter''\n''Answer = ')
    
    return a

def flatterlist (l):
    if type(l) != list:
        flattenedlist1.append(l)
    else:  
        for k in l:
            if type(k) != list:
                flattenedlist1.append(k)    
            else:
                for i in range (len(k)):
                    if len(k) > 1:
                        flatterlist(k[i])
                    elif len(k) < 1:
                        continue
                    elif type(k) == list:
                        flatterlist(k[i])
                    else:
                        flattenedlist1.append(k)
    
    return flattenedlist1
    

flattenedlist1 = []
yourlist = []
listsize = []
createbody(listsize)
#print (listsize)

for _ in range (listsize[0]):
    control = input('Do you want to add a list in list ?''\n''if yes, write \'yes\'''\n''Answer = ')
    if control == 'yes':
        yourlist.append(listcreate())
        print('\n', 'Your list now appering like : ', yourlist, '\n')
        continue
    
    x = input('Input : ')
    fcontrol = floatcontrol(x)
    icontrol = intcontrol(x)
        
    if x == 'True' or x == 'False':
        if x == 'True':
            yourlist.append(True)
        else:
            yourlist.append(False)
    elif icontrol == True:
        yourlist.append(int(x))
    elif fcontrol == True: 
        yourlist.append(float(x))
    else:
        yourlist.append(x)
    

print ('\n', 'Yourlist is = ', yourlist, '\n')

flattenedlist = flatterlist(yourlist)
print ('\n', f'The flattened list is = {flattenedlist}', '\n')

