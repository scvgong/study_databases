from pymongo import MongoClient

mongo_url = "mongodb://localhost:27017"
client = "local"
dbm = 'solvingProblem'

def connect(mongo_url,client,dbm): # connect 함수
    mongoClient = MongoClient(mongo_url)
    database = mongoClient[client]
    collection = database[dbm]
    
    return collection

connect_data = connect(mongo_url,client,dbm)



# def quiz(connect_data):
#     quizs = connect_data.find({},{"_id":0,'question':1})
#     for question in quizs:
#         answer = connect_data.find({},{"_id":0,"choices":1})
#         for answer_correct in answer:
#             print("1번 문제 : {}\n답항 : {}".format(question,answer_correct))

# quiz(connect_data)

# quiz_data => 데이터 함수
# 답항 출력, 정답 번호 입력 받기

# 문제 출력
