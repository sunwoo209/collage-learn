dan = int(input("원하는 단은 :"))
i = 1
while i <= 9:
    print("%s*%s=%s" % (dan,i , dan*i))
    i= i + 1

# %s	문자열
# %d	정수
# %f	부동소수점 실수

#%20s	전체 20칸을 차지하는 문자열(공백을 앞에 붙인다.)
#%-10d	전체 10칸을 차지하는 숫자(공백을 뒤에 붙인다.)
#%.5f	부동소수점의 소수점 아래 5자리까지 표시

#print("{2}의 {0} 점수는 {1}점입니다. {1}점! {1}점!".format("수학", 100, "철수"))
