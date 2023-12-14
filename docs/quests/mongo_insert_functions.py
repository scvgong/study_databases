# connect function
from pymongo import MongoClient
def connect(): # connect 함수
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["local"]
    collection = database['fruits']
    
    return collection

# insert function

def data(): # 데이터 함수
    fruits = [
        {"name": "사과", "color": "빨강", "origin": "한국", "season": "가을"},
        {"name": "바나나", "color": "노랑", "origin": "필리핀", "season": "계절 상관 없음"},
        {"name": "포도", "color": "보라", "origin": "한국", "season": "가을"},
        {"name": "오렌지", "color": "오렌지", "origin": "미국", "season": "겨울"}
    ]
    return fruits

connect_data = connect()
input_data = data()

def insert_fruit(): # 삽입함수
    for fruit in input_data:
        connect_data.insert_one(fruit)


insert_fruit()