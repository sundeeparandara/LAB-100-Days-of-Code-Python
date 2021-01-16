import numpy as np

student_heights = np.array(input("Input a list of student heights ").split()).astype(int)
print(student_heights)

print(int(np.mean(student_heights)))