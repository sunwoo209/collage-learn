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


