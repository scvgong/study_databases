# connect function
from pymongo import MongoClient
mongo_url = "mongodb://localhost:27017"
client = "local"
dbm = 'fruits'

def connect(mongo_url,client,dbm): # connect 함수
    mongoClient = MongoClient(mongo_url)
    database = mongoClient[client]
    collection = database[dbm]
    
    return collection

def data(): # 데이터 함수
    fruits = [
        {"name": "사과", "color": "빨강", "origin": "한국", "season": "가을"},
        {"name": "바나나", "color": "노랑", "origin": "필리핀", "season": "계절 상관 없음"},
        {"name": "포도", "color": "보라", "origin": "한국", "season": "가을"},
        {"name": "오렌지", "color": "오렌지", "origin": "미국", "season": "겨울"}
    ]
    return fruits

connect_data = connect(mongo_url,client,dbm) # connect 함수 변수 선언
input_data = data() # data 함수 변수 선언

# insert function
def insert_fruit(connect_data,input_data): # 삽입함수
    for fruit in input_data:
        connect_data.insert_one(fruit)


insert_fruit(connect_data,input_data)