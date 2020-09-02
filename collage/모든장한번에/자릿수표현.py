s="Monty Python"
print(s[6:10])

#양수는 0~ 좌측부터
# - (음수) -1~ 우측부터
# 빈칸은 끝까지
#공백도 칸차지
# 123456
#-6-5-4-3-2-1
# : 로 범위 설정시 무조건 ->순서
a="TEAMLAB MOOC,AWESOME Python"
print(a[0:6],"and",a[-9:])

print(a[::2],"and",a[::-1])
