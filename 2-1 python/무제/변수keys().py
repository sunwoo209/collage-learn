problems={'파이썬': '최근에 가장 떠오르는 프로그래밍 언어',
          '변수': '데이터를 저장하는 메모리 공간',
          '함수': '작업을 수행하는 문장들의 집합에 이름을 붙인것',
          '리스트': '서로 관련이 없는 항목들의 모임'}

for word in problems.keys(): #변수.keys() 하게되면 key 값( 파이썬 변수 ~ )를 모두 호출 // 값을 호출하고 싶다면 변수.values()//키-값 쌍을 모두출력 변수.items()
    print("다음은 어떤 단어에 대한 설명일까요?")
    print(problems[word])
    print("(1)파이썬 (2)함수 (3)리스트 (4)변수")
    ans=input()

    if ans==word:
        print("정답입니다!")

    else:

        print("정답이 아닙니다!")
