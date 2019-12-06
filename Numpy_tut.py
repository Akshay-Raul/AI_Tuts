import numpy as np

numbers=[]

numbers.extend(range(1,21))

numpyFullArray = np.array(numbers)
numpyArray = np.reshape(numpyFullArray, (4,5))

result = numpyFullArray / 5
print((result))
print('\n')
print(np.average(numpyArray))
