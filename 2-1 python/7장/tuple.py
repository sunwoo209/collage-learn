def dex ( a,b ,*args):  # 가변인수는 * (asterisk 라고 부름)로 표현할 수 있는데,
    print(args)         # * 는 파이썬에서 기본적으로 곱셈 또는 제곱 연산 등을 묶어
    return a+b+sum(args)# 주는 가변 인수를 만든다. #기본적으로 해체 불가

print(dex(1,2,3,4,5))
