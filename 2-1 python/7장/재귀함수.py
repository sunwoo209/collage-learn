#재귀함수
def factorial(n):
    if n==1:
        return 1    # break 를 걸지않으면 무한루프에 걸리게된다.
    else:
        return n*factorial(n-1)
