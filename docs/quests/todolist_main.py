import todolist_functions

todolist_functions.connect()    # DB 커넥터 함수 실행

todolist_functions.insert_todoList() # 데이터 입력 함수 실행
user_info = todolist_functions.get_username()

todolist_functions.insert_user(user_info)     # user 입력 함수 실행

user_id = todolist_functions.insert_user
todolist_functions.select_todo(user_id,user_info)
todolist_functions.add_user()