#리스트 컴프리헨션
#기존의 리스트형을 사용하여 간단하게 새로운 리스트를 만드는 기법
#리스트와 for문을 한줄에 사용할 수 있다.

num=range(5)
print(list(num))

#result=[]
#for i in num:
#    result.append(i)


result=[i for i in num if i % 2 == 0] #[변수 <- for i in 숫자열 ]순서
print(result)


result=[i*j for i in range(5) for j in range(5)]
print(result)

case_1=["A","B","C"]
case_2=["D","E","A"]
result=[i+j for i in case_1 for j in case_2 if not(i==j)]
print(result)


#2차원 리스트

result=[[i,i+10] for i in range(10)]
print(result)
print(result[3][1])

# 리스트안의 리스트

result=[[i+j for i in case_1]for j in case_2]
print(result)
#뒤의 for j 부터 먼저 할당
