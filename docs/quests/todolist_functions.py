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
# input_user = get_username()


# DB에 user 삽입 , 사용자에 대한 _id 변수로 받기
def insert_user(user_info):
    if user_collection.count_documents(user_info) == 0:
        result = user_collection.insert_one(user_info)
        inserted_id = result.inserted_id
    else:
        user_data = user_collection.find_one(user_info)
        inserted_id = user_data['_id'] if user_data is not None else None
        # user_collection.find_one(input_user)['_id']
    
    return inserted_id


# To-do 리스트 보여주기 및 선택 함수
def select_todo(user_id,user_info):
    
    while True: # 작업을 계속할 수 있도록 루프
        todos = list(collection.find({},{"_id":0})) # To-do 리스트 가져오기
        print("ToDo List 중 하나 선택하세요 : ")
        for i, todo in enumerate(todos, start = 1): # To-do 리스트 출력
            print(f"{i}. {todo['title']}") 

        selected = int(input("Title 번호 : ")) - 1 # 사용자 선택
        if 0 <= selected < len(todos): # 선택한 번호가 유효한 범위에 있는지 확인
            selected_todo = todos[selected]  # 선택한 To-do 항목
            status = input("Status : ") # 상태 입력 받기

            user_id = insert_user(user_info) # user 정보를 id 넣기
            user_name = user_info['name'] # username 넣기
            
            user_todoList_collection.insert_one({"user_id": user_id, "name":user_name, "todo": selected_todo, "status": status})  # 선택한 항목 및 상태 저장
            print("저장")
        else :
            print("다시")

        if input("종료 여부 : ").lower() in ['q','x']: # 종료 조건 확인
            break # 작업 종료

        if user_todoList_collection.find({"user_id":user_id, "user_name":user_name}) != 0:
            user_todoList_collection.update_one({"user_id": user_id, "name":user_name, "todo": selected_todo, "status": status},upsert=True) 
        
def add_user():
    while True:  # 여러 사용자를 위한 루프
        print("------------------------")
        new_user = get_username()  # 사용자 데이터 받기
        user_id = insert_user(new_user)  # 사용자 데이터 삽입 및 ID 저장
        select_todo(user_id, new_user)  # 사용자가 To-do 항목 선택 및 상태 업데이트
        if input("다른 사용자를 위해 계속하려면 'c'를, 종료하려면 'q' 또는 'x'를 입력하세요: ").lower() not in ['c']:  # 종료 조건 확인
            break  # 실행 종료
    print("------------------------")