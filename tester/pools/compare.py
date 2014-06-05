def compare(a,b):
    
    a = a.split(" ")

    while('' in a):
        a.remove('')
    while('\n' in a):
        a.remove('\n')
        
   # print a

    b = b.split(" ")
    while('' in b):
        b.remove('')
    while('\n' in a):
        a.remove('\n')
    
    #print b
    m = len(a)
    n = len(b)
    exist = 0.0
    for item in b:
        for item2 in a:
            if item == item2:
##                print item
##                print item2
                exist = exist +1
                #print exist
                break
    exist = exist * 1.0
    length = len(b) * 1.0
    #print (exist/len(b))
    return exist/float(n)

#print compare("Blah blah blah Hi i am hi hi in here bleep vleep brrpp","Hi i am in here")
