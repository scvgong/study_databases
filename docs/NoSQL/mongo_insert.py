from pymongo import MongoClient # MongoDB compass를 가져온것
# mongoDB에 접속 -> 자원에 대한 class를 받아냄
mongoClient = MongoClient("mongodb://localhost:27017") # 연결

# database 연결, local로 접속
database = mongoClient["local"]

# collection 작업
collection = database['fruits']

# insert 작업 진행
collection.insert_one({"name": "오렌지", "color": "오렌지", "origin": "미국", "season": "겨울"})

dict_fruits = {"name": "포도", "color": "보라", "origin": "한국", "season": "가을"}
collection.insert_one(dict_fruits)

pass