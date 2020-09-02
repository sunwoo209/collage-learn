import random

while True:
    user=input("가위, 바위 , 보 중에 입력하세요 :")
    if user=='가위':
        if random.choice(["가위","바위","보"])=="가위":
            print("무승부")
        elif random.choice(["가위","바위","보"])=="바위":
            print("패")
        else:
            print("승")
    if user=='바위':
        if random.choice(["가위","바위","보"])=="가위":
            print("승")
        elif random.choice(["가위","바위","보"])=="바위":
            print("무승부")
        else:
            print("패")
    if user=='보':
        if random.choice(["가위","바위","보"])=="가위":
            print("패")
        elif random.choice(["가위","바위","보"])=="바위":
            print("승")
        else:
            print("무승부")
