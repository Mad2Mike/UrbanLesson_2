import matplotlib.pyplot as plt
import numpy as np
import requests

# requests
url = 'https://api.github.com'


response = requests.get(url, verify=False)


print(f"Status Code: {response.status_code}")
print("Response Content:")
print(response.json())

# numpy
array = np.arange(10)
added_array = array + 5
print("\nМассив после сложения 5:")
print(added_array)


multiplied_array = array * 2
print("\nМассив после умножения на 2:")
print(multiplied_array)


squared_array = array ** 2
print("\nМассив после возведения в квадрат:")
print(squared_array)


mean_value = np.mean(array)
print("\nСреднее значение исходного массива:")
print(mean_value)


sum_value = np.sum(array)
print("\nСумма элементов исходного массива:")
print(sum_value)


std_deviation = np.std(array)
print("\nСтандартное отклонение исходного массива:")
print(std_deviation)


#  matplotlib.pyplot

x = np.linspace(0, 10, 100)  # 100 точек от 0 до 10
y = np.sin(x)

plt.figure(figsize=(11, 2))
plt.plot(x, y, label='sin(x)', color='red', linewidth=4)
plt.title('График функции y = sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()