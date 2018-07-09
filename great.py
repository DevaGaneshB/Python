print("enter 3 nos")
a=input()
b=input()
c=input()
d=max(a,b,c)
print("Max="+str(d))




print("enter 2 nos")
a=input()
b=input()
c=a-b
print('sub='+str(c))



print("enter 2 nos")
a=input()
b=input()
c=a+b
print('sum='+str(c))



print("enter 2 nos")
a=input()
b=input()
c=a*b
print('MUL='+str(c))



print("enter 2 nos")
a=input()
b=input()
c=a/b
print('QUT='+str(c))



print("enter 2 nos")
a=input()
b=input()
c=a%b
print('MOD='+str(c))




print("enter 2 nos")
a=input()
b=input()
print('A='+str(a))

print('B='+str(b))





print("enter 2 nos")



print("Enter  a number")
n=input()
def primegen(a):
  b=[]
  flag=0
  for i in range (1,a):
    flag=0
    for j in range(1,i):
      if (i%j) == 0:
        flag=flag+1
    if flag<2:
      b.append(i)
  print(b)   
primegen(n)  




print("Enter a no")
a=input()
def fibonacci(a):
  s=[]
  i=0
  a1=0
  a2=1
  s.append(a1)
  s.append(a2)
  while i<a:
    (a1,a2)=(a2,a1+a2)
    s.append(a2)
    i=i+1 
  print(s)
fibonacci(a)




















