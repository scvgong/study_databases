from pymongo import MongoClient # MongoDB compass를 가져온것
# mongoDB에 접속 -> 자원에 대한 class를 받아냄
mongoClient = MongoClient("mongodb://localhost:27017") # 연결

# database 연결, local로 접속
database = mongoClient["local"]

# collection 작업
collection = database['fruits']

# insert 작업 진행, 한번에 여러데이터를 넣는게 좋다. 실행할때마다 데이터 삽입된다

mixed_fruit = {"name": "포도", 
               "color": ["보라","연보라색","초록색"], 
               "origin": "한국", 
               "season": "가을"}
result = collection.insert_one(mixed_fruit)
pass