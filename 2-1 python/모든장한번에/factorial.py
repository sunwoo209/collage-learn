#순열
n=int(input("정수 n 를 입력하시오:"))
r=int(input("정수 r 를 입력하시오:"))  
s=n-r

fact=1
for i in range(1,n+1):
    fact=fact*i

index=1
for t in range(1,s+1):
    index=index*t

result=int(fact/index)

print(n,"P",r,"은",result,"입니다")
