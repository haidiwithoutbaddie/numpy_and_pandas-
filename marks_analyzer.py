import numpy as np
marks = np.array([[75,80,90],
                  [60,85,70],
                  [95,90,85],
                  [40,65,55],
                  [88,78,92]])
print(marks)
print(marks.sum(axis = 1))
print(marks.mean(axis = 0))
print(marks.max())
print(np.all(marks >= 80, axis = 1))
