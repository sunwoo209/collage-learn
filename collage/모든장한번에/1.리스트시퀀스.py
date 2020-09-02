a='hi'
b='hello'

c=[a,b]

slist=['영어','수학','사회','과학']
#list는 정수형이나 실수형 같은 다양한 자료형 가능
#시퀀스 (순차) 방식

print(slist[2])
#index(순번)_ 0,1,2,3 ~


print(slist[:-1])
#역으로 슬라이싱
#-3,-2,-1,0

print(slist[::2])
#2배수로 띄기

print(slist*2)
#연속출력

print('영어' in slist)
#in true or false

print(len(slist))
#갯수


slist.append('탐구')
print(slist)
#새로운 열 추가


x=['과탐','음악']
slist.extend(x)
print(slist)
#리스트에 리스트 추가


slist.insert(3,'인서트')
print(slist)
#삽입

slist.remove('수학')
print(slist)
#리스트내의 특정 값을 삭제

slist[1]='수학이아니야'
print(slist)
#1번째에 대체값


#del 순서를 삭제

#-----------------------------
friend_list=[]

friend=input("친구의 이름 1")
friend_list.append(friend)

friend=input("친구의 이름 1")
friend_list.append(friend)

friend=input("친구의 이름 1")
friend_list.append(friend)

friend=input("친구의 이름 1")
friend_list.append(friend)

print(friend_list)




#---------------
t1=[1,2,3]
t2=[4,5,6]
ta=['a','b','c']
tb=['d','e','f',]

m=[t1,t2]
j=[ta,tb]

x=[m,j]

print(x[1][0][0])

#---------------
heroes=[] # []는 리스트 생성 {}는 딕셔너리 생성 -> 딕셔너리로 생성했을때 딕변수1["이름"]="value값" 는 키 값
heroes = [ "아이언맨", "토르", "헐크", "스칼렛 위치"]
heroes.append("스파이더맨")
print(heroes)

heroes.insert (1, 배트맨) #순서 1에 배트맨 오도록 추가
#heroes[1] ="닥터 스트레인지"  // # 순서1에 변경하기

print(heroes)

del heroes[0] #0순서 삭제
