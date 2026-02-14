

N = input().strip()

if '.' not in N:
   print('int',int(N))
else:
   integer, decimal = N.split('.')
   
   if int(decimal) == 0:
       print('int', int(integer))
       
   else:
       print('float', int(integer),"0."+(decimal))
