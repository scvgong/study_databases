import solvingProblem_function

mongo_url = "mongodb://localhost:27017"
client = "local"
dbm = 'solvingProblem'

connect_data = solvingProblem_function.connect(mongo_url,client,dbm)
input_data = solvingProblem_function.quiz_data()

# 데이터 삽입
solvingProblem_function.insert_solving(connect_data,input_data)

# 퀴즈 실행
solvingProblem_function.run_quiz(connect_data)
