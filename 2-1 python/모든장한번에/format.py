price=10000.5123
print("상품의 가격은 %0.3f원입니다." %price)
#%0.3f=소수점 3째자리까지 출력
#f만 정수 부분 포함 6칸

#"{자료형}".format(인수)
#{0} 0번째 {1} 1번째

print("i'm{0}years {1}old.".format(20,30))

print("%10d" %12) #10자리 확보하고 우측정렬로 12

#________12
print("%-10d" %12) #좌측정렬
#12

print("%10.4f" %1.123456789)


#0 번째 순서의10공간 확보후  우측정렬
print("{0:>10s}".format("Apple"))
#_____Apple
#ex
print("{2:>10.5f}".format("Apple",5.243,1.234))
