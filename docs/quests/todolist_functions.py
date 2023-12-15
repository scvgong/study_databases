from pymongo import MongoClient

# 몽고 DB 커넥트 함수
def connect(): # connect 함수
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["local"]
    return database

database = connect()

collection = database["todolist"] # todolist를 collection로 변수선언
user_collection = database["user"]
user_todoList_collection = database["user_todoList"]

# todo_list에 대한 데이터 함수
def data_todoList():
    todo_list = [
        {
            "title": "주간 보고서 작성", 
            "description": "팀의 주간 성과와 진행 상황에 대한 보고서를 작성합니다."
        },
        {
            "title": "이메일 확인 및 응답", 
            "description": "미처 확인하지 못한 이메일을 확인하고 필요한 이메일에 대해 응답합니다."
        },
        {
            "title": "회의 준비", 
            "description": "다가오는 회의에 대해 준비합니다. 주제 연구, 발표 자료 준비 등이 포함될 수 있습니다."
        },
        {
            "title": "프로젝트 계획서 수정", 
            "description": "현재 진행 중인 프로젝트의 계획서를 검토하고 필요한 부분을 수정합니다."
        },
        {
            "title": "팀 멤버와의 1:1 면담", 
            "description": "팀 멤버와 개별적으로 만나서 그들의 업무 진행 상황, 이슈, 우려사항 등을 논의합니다."
        }
    ]
    return todo_list

# todoList를 받을 변수
 
input_data = data_todoList() # todo_list 데이터 넣어주는 변수

# DB에 todo_list 데이터 삽입 함수
def insert_todoList():
    for x in input_data: # 데이터 삽입이 반복될때
        if collection.count_documents(x) == 0: # 동일정보 확인후 없을경우만 진행
            collection.insert_one(x)# todolist DB를 insert 해준다
        pass
    
    return 

# 사용자 입력 함수
def get_username():
    user_name = input("사용자 이름 입력 : ")
    name = {"name":user_name} # key : name / value : user_name
    return name

# 사용자를 받을 변수
input_user = get_username()

# DB에 user 삽입 함수
def insert_user():
    result = user_collection.insert_one(input_user)
    inserted_id = result.inserted_id
    # print("inserted_id : {}".format(inserted_id))
    return inserted_id





# 사용자가 입력 받아서 todoList 작업 한 것을 DB에 저장하는 함수
# def run_todoList():
#     ## 1. 사용자 입력 변수, DB에서 todoList 찾기
#     user_name = get_username()
#     todoList = connect_data.find()

#     ## 2. todoList에 있는 id를 찾을수 있게 사용자에 매칭

#     ## 3. 사용자가 todoList 실행

#     ## 4. 작업완료 여부파악 -> 완료시 다음 사용자, 진행시 전사용자 다시 진행

#     ## 5. 모든 사용자 완료되면 DB에 todoList 진행사항 DB에 업로드
# def insert_user_todoList():
#     return