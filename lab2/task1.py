
#task: 1
eng=int(input("enter marks in eng"))
math=int(input("enter marks in math"))
sci=int(input("enter marks in sci"))
sst=int(input("enter marks in sst"))
pst=int(input("enter marks in pst"))
total=eng+math+sci+sst+pst
print("\t\t"+"MARKSHEET")
print("english= "+str(eng))

print("math= "+str(math))

print("science= "+str(sci))

print("sst= "+str(sst))

print("pakistan studies= "+str(pst))

print("the total is="+str(total))
if (total <= 500 and total>400):
  print("GRADE=A1 GRADE")
elif( total <=400 and total>300):
  print("GRADE=A GRADE")
  
elif (total <=300 and total>200):
  print("GRADE=B GRADE")
  
elif (total <=200 and total>100):
  print("GRADE=C GRADE")
  
elif (total <100):
  print("GRADE=FAIL")
