# quiz 데이터 db에 입력
from pymongo import MongoClient

mongo_url = "mongodb://localhost:27017"
client = "local"
dbm = 'solvingProblem'

def connect(mongo_url,client,dbm): # connect 함수
    mongoClient = MongoClient(mongo_url)
    database = mongoClient[client]
    collection = database[dbm]
    
    return collection

def quiz_data():
    quiz_list = [
        {
            "question": "Python의 생성자 함수 이름은 무엇인가요?",
            "choices": ["__init__", "__main__", "__str__", "__del__"],
            "answer": "__init__",
            "answer_number": 1,
            "score": 20
        },
        {
            "question": "Python에서 'Hello, World!'를 출력하는 코드는 무엇인가요?",
            "choices": ["print('Hello, World!')", "console.log('Hello, World!')", "printf('Hello, World!')", "echo 'Hello, World!'"],
            "answer": "print('Hello, World!')",
            "answer_number": 1,
            "score": 20
        },
        {
            "question": "Python의 주석을 나타내는 기호는 무엇인가요?",
            "choices": ["//", "/* */", "#", "--"],
            "answer": "#",
            "answer_number": 3,
            "score": 20
        },
        {
            "question": "Python에서 리스트의 길이를 반환하는 함수는 무엇인가요?",
            "choices": ["size()", "length()", "len()", "sizeof()"],
            "answer": "len()",
            "answer_number": 3,
            "score": 20
        },
        {
            "question": "Python에서 문자열을 숫자로 변환하는 함수는 무엇인가요?",
            "choices": ["str()", "int()", "char()", "float()"],
            "answer": "int()",
            "answer_number": 2,
            "score": 20
        }
    ]

    return quiz_list

connect_data = connect(mongo_url,client,dbm)
input_data = quiz_data()

def insert_solving(connect_data,input_data):
    connect_data.insert_many(input_data)

insert_solving(connect_data,input_data)



