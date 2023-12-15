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

# 분리 입력(fruits, fruits_colors)
# insert fruits 작업 진행
dict_fruit = {"name": "포도", 
               "origin": "한국", 
               "season": "가을"}
result = collection.insert_one(dict_fruit)

# insertedId: ObjectId("657bf123bd5e41a4bcb0e7df")
print("result.inserted_id : {}".format(result.inserted_id ))
inserted_id = result.inserted_id # 현재 파일에서 사용하는 변수 = 클래스에서 사용하는 변수 타입이 다르다

# insert fruits_colors 작업 진행
# [{"fruits_id" : ObjectId("657bf123bd5e41a4bcb0e7df"),"color": "보라"},
#  {"fruits_id" : ObjectId("657bf123bd5e41a4bcb0e7df"),"color":"연보라색"},
#  {"fruits_id" : ObjectId("657bf123bd5e41a4bcb0e7df"),"color":"초록색"}]

fruits_colors = [{"color": "보라"},
                 {"color":"연보라색"},
                 {"color":"초록색"}]

list_fruits_colors = list()

for dict_color in fruits_colors:
    dict_color["fruits_id"] = inserted_id
    list_fruits_colors.append(dict_color)
    pass


# collection fruits_color
collection_fruits_colors = database["fruits_colors"]

collection_fruits_colors.insert_many(list_fruits_colors)

# find from fruits_colors
documents = collection_fruits_colors.find({"fruits_id" : { "$eq" : inserted_id }})

pass