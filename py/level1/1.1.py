from random import randint

def fibonacci(limit):
  fib = [0, 1]
  while True:
    next_fib = fib[-1] + fib[-2]
    if next_fib > limit: return fib
    fib.append(next_fib)

count_numbers = randint(1,10)
numbers = []
print(f'Введіть {count_numbers} кількість чисел')
for i in range(count_numbers):
  numbers.append(int(input(f'Число {i} = ')))

arithmetic_mean = sum(numbers)/len(numbers)
closest_number = min(numbers, key=lambda x: abs(x - arithmetic_mean))
closest_count = numbers.count(closest_number)
print(f"Ймовірність вибору числа {closest_number}, яке наближене до середнього"+
      f" арефметичного: {arithmetic_mean:.2f}, рівна {closest_count/len(numbers):.2f}")

numbers_like_fibinacchi = fibonacci(max(numbers))
numbers_fib = [x for x in numbers if x not in numbers_like_fibinacchi]
print(f"Після очистки колізій з Фібоначі: {numbers_fib}")

numbers_dupl = numbers_fib
if min(numbers_fib) != 0:
  numbers_dupl =  [x for x in numbers_fib
                   if not(x % min(numbers_fib) == 0 and x != min(numbers_fib))]
print(f"Після очистки кратних мініуму: {numbers_dupl}")