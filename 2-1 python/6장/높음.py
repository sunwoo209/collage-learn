import random

tries=0
guess=0;
answer=random.randint(1,100)

print("1부터 100사이의 숫자를 맞추시오")

while guess is not answer and tries < 5: # !=  is not
    guess =int(input("숫자를 입력하시오:"))
    tries=tries+1
    if guess<answer:
        print("낮음!")
    elif guess<answer:
        print("높음!")
if  guess == answer:
    print("축하합니다. 시도 횟수=",tries)
if  tries == 5:
    print("시도횟수가",tries,"회가  되었습니다. 정답은", answer,"입니다.")
