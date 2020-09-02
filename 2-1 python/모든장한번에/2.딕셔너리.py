phone_book = {}
phone_book["홍길동"] ="010-1234-5678"
print(phone_book)

#{'홍길동 ': '010 1234 5678'}


phone_book ={"홍길동": "010-1234-5678"}
phone_book["강감찬"] = "010-1234-5679"
phone_book["이순신"] = "010-1234-5680"
print(phone_book)

print(phone_book["강감찬"])

#딕셔너리 기존내용에 새로운 키라면 내용이 추가되고 원래 키값이 있으면 덮어쓴다.


for key in sorted(phone_book.keys()):
print(key, phone_book[key])

for k, v in phone_book.items(): # items 자체가 키,값 으로 불러오기때문에 k , v 에 할당 가능
print(“Key:”, k)
print(“Value:”, v)
