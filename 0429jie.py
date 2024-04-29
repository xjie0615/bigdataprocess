#import random#count = 1
#while count <= 11:
   # for i in range (1,6):
       # randNum = random.randint (1,49)
        #print ('%3d'%(randNum),end ='')
   # print ( )
   #count += 1
#print ('

import random
again = 1
while again == 1:
    for i in range (1,7):
        randNum = random.randint (1,49)
        print ('%3d'%(randNum),end='')
        print()
        again= eval(input('continue :1 or quit :0 --->'))
    print('over')