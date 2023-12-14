from pymongo import MongoClient # MongoDB compass를 가져온것
# mongoDB에 접속 -> 자원에 대한 class를 받아냄
mongoClient = MongoClient("mongodb://localhost:27017") # 연결

# database 연결, local로 접속
database = mongoClient["local"]

# collection 작업
collection = database['fruits']

# insert many 작업 진행
list_fruits = [
    {"name": "사과", "color": "빨강", "origin": "한국", "season": "가을"},
    {"name": "바나나", "color": "노랑", "origin": "필리핀", "season": "계절 상관 없음"},
    {"name": "포도", "color": "보라", "origin": "한국", "season": "가을"},
    {"name": "오렌지", "color": "오렌지", "origin": "미국", "season": "겨울"}
]

insert_result = collection.insert_many(list_fruits)

list_inserted_ids = insert_result.inserted_ids

#delete inserted records by _ids
collection.delete_many({"_id":list_inserted_ids[0]})

pass
