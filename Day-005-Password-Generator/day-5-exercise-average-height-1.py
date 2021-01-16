# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

summation = 0
count = 0
for i in student_heights:
  summation +=i
  count+=1
average = summation/count
print(round(average))