# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

state = []

for i in student_scores:
  #print(i)
  for j in student_scores:
    if i >= j:
      state.append(True)
    else:
      #print(state)
      state = []
      break
  if len(state) == len(student_scores):
    print(f"The hightest score in the class is: {i}")
    break