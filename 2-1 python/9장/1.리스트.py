heroes=[] # []는 리스트 생성 {}는 딕셔너리 생성 -> 딕셔너리로 생성했을때 딕변수1["이름"]="value값" 는 키 값
heroes = [ "아이언맨", "토르", "헐크", "스칼렛 위치"]
heroes.append("스파이더맨")
print(heroes)

heroes.insert (1, 배트맨) #순서 1에 배트맨 오도록 추가
#heroes[1] ="닥터 스트레인지"  // # 순서1에 변경하기

print(heroes)

del heroes[0] #0순서 삭제
