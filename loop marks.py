'''
per=int(input('Enter any percentage:'))
if(per<0):
  print('invalid perctange....')
elif(per>100):
    print('invalid perctange.....')
elif(per>=60):
    print('pass in first Div.....')
elif(per>=45):
    print('pass in second Div.....')
elif(per>=33):
    print('pass in third Div.......')
else:
    printinput('fail......')
 '''

p=int(input('enter your marks in physics:'))
c=int(input('enter your marks in chemistry:'))
m=int(input('enter your marks in mats:'))
per=(p+c+m)*0.33
if(p<33 and c<33 and m<33):
  print('your fail in PCM')
elif(p<33 and c<33):
  print('you are in fail in pc')
elif(c<33 and m<33):
  print('you are fail in CM')
elif(p<33 and m<33):
  print('you are fail in PM')
elif(p<33):
  print('you are fail in P and pass in CM')
elif(p<33):
  print('you are fail in C and pass in PM')
elif(p<33):
  print('you are fail in M and pass in PC')
elif(p>33 and c>33 and p+c+m>66):
  print('you are pass and marks obtain from300:',p+c+m,'\n your percantage obtainan are:',per)

  
      

    
       
