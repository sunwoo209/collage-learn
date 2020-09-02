ID_Admin1="sunwoo209"
PS_Admin1="1234"


print("환영합니다!")
str_ID = input("사용자 ID를 입력해주세요.")
if str_ID == ID_Admin1:
    print("\n")
    print(str_ID+" 님 환영합니다!")
    str_password = input("비밀 번호를 입력해주세요.")
    if str_password == PS_Admin1:
        print("\n")
        print(ID_Admin1+" 님 다시와주셔서 감사합니다.")
    else:
        print("\n")
        print("패스워드를 다시 확인해주시기 바랍니다.")
else:
    print("\n")
    print("ID를 다시 확인해주시기 바랍니다.")
