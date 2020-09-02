alist=['a1','a2','a3']
blist=['b1','b2','b3']

for a, b in zip(alist, blist):
    print(a,b)
#zip 함수는 1개이상의 리스트 값이 같은 인덱스에 있을 때 [병렬]로 묶는 함수
#a1 b1
#a2 b2
#a3 b3
a,b,c=zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c)


#같은 인덱스끼리 묶이는것
a,b,c = print([sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))])
print(a,b,c)

# x 튜플 = 1 , 10 , 100    sum 111
