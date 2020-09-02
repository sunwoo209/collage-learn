t=[1,2,3]
#1,2,3을 변수 t 에 패킹
a,b,c=t  #리스트 t 에 있는 값 1,2,3을 변수 a,b,c에 언패킹
print(a)
print(b)
print(c)

#패킹되는 리스트에 변수로 넣을때 개수가 맞아야됨
#1,2,3  a,b 는 안된다는 뜻 무 적 권 1대1매칭



xy=[1,2,3]
yz=[4,5,6]
zq=[7,8,9]

t=[]
t.append(xy)
t.append(yz)
t.append(zq)

print(t)

unpack1,unpack2,unpack3=t

print(unpack1)
print(unpack2)
print(unpack3)
