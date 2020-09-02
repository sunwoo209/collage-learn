#def dex(x,y): # def 변수(받을값)
#    z=x+y       
#    return z  #원하는 변수 반환시켜서 dex 로 다시 재정의
#print(dex(1,2))

#지역변수와 전역변수
#지역변수는 함수 밖으로 나오는 순간 사라지게 된다.
#전역함수는 언제든 호출가능

#지역변수를 전역변수로 변환 해줄수 있다  [global 변수]

def dex(y):
    global stack
    stack= 3.14*y*y
    return

stack=0
r=float(input("값:"))
dex(r)
print(stack)


#만약 global을 썻을때 변수를 다시 쓴다면 지역변수였던것을 덮어쓰게된다.

