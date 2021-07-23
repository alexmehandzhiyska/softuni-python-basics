bad_grades_threshold = int(input())
bad_grades = 0
score = 0
problem_counter = 0
last_problem = ''

while bad_grades < bad_grades_threshold:
  problem_name = input()

  if problem_name == 'Enough':
    print(f'Average score: {"{:.2f}".format(score / problem_counter)}\nNumber of problems: {problem_counter}\nLast problem: {last_problem}')
    exit()
  else:
    last_problem = problem_name
    grade = int(input())
    score += grade
    problem_counter += 1
    
    if (grade <= 4):
      bad_grades += 1

      
print(f'You need a break, {bad_grades} poor grades.')