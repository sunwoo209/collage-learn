products={"떡볶이":0,"순대":0,"튀김":0,"어묵":0,"닭꼬치":0,"만두":0}


while(True):
    print("====메뉴 주문 받기====")
    print("1. 메뉴 보기 ")
    print("2. 현재 까지 누적 주문 보기")
    print("3. 주문 추가 하기 ")
    print("4. 주문 취소 하기 ")
    print("5. 주문 마감 결정 하기")
    print("======================")

    num=input("번호를 선택 해주세요:")

    if num == "1":
        print("=======================================")
        print("떡볶이","순대","튀김","어묵","닭꼬치","만두")
        print("=======================================")

    elif num == "2":
        print("=======================================")
        print(products)
        print("=======================================")

    elif num == "3" :
             print("=======================================")
             product=input("음식 이름?:")
             count=int(input("몇 인분 추가?:"))
             products[product] = products[product]+count
             print(products)
             print("=======================================")            

    elif num == "4" :
             print("=======================================")
             product=input("음식 이름?:")
             count=int(input("몇 인분 취소?:"))
             products[product] = products[product]-count
             print(products)
             print("=======================================")

    elif num == "5" :
             print("=======================================")
             print(products)
             print("주문이 접수 되었습니다.")
             print("=======================================")
             break
