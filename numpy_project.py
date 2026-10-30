import numpy as np
marks = np.array([[78,85,90],
                  [65,72,80],
                  [92,88,95],
                  [45,60,55],
                  [83,79,88]])

names = np.array(["Ali","Ahmed","Sara","Hamza","Ayesha"])
subjects = np.array(["Python","Math","Statistics"])

print(marks)
print(names)
print(subjects)

total = marks.sum(axis = 1)
print(total)

print(np.mean(marks,axis = 1))

print(marks.max())

print(np.mean(marks,axis = 0))

print(marks >= 85)
print(marks[marks >= 85])

a = np.argmax(total)
print(names[a])

print(np.sort(total))
print(np.shape(marks))
print(np.ndim(marks))

weight = np.array([0.5,0.3,0.2])
result = marks @ weight
print(result)