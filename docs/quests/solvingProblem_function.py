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

# 데이터 함수
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

# DB에 데이터 입력 함수
def insert_solving(connect_data,input_data):
    connect_data.insert_many(input_data)

# 퀴즈 함수

def run_quiz(connect_data):
    user_name = get_username() # 사용자 이름 입력
    questions = connect_data.find() # DB에서 데이터 찾기
    score = 0
    
    for idx,question in enumerate(questions,start=1): # 1부터 시작
        print(f"{idx}.{question['question']}") #문제에 번호 붙여서 출력, list에 저장된 question 출력

        for i, choice in enumerate(question['choices']):
            print(f"{i+1}.{choice}") # 답항에 번호 붙여서 출력, list에 저장된 choices 출력
        
        answer = input("답을 입력해 주세요 : ")
        if int(answer) == question['answer_number']: # 입력한 값이랑 DB에 저장된 번호 매칭
            score += question['score'] # 점수 합산
        
    print("최종 점수 : {}".format(score) ) 

    grade = ''
    if score >= 80:
        print("A 등급입니다.")
        grade = 'A'
    elif score >= 60:
        print("B 등급입니다.")
        grade = 'B'
    else :
        print("F등급입니다.")
        grade = 'F'

    insert_score(connect_data,user_name,score,grade) # DB에 추가 데이터 삽입

def get_username():
    user_name = input("사용자 이름을 입력 : ")
    return user_name

def insert_score(connect_data,username,score,grade): # 사용자가 입력한 값 DB에 저장
    connect_data.insert_one({"username": username, "score":score, "grade":grade })
