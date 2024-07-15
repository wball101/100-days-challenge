# fruits = ["apple", "mango", "pear"]
# for item in fruits:
#     print(item)
#     print(item + " pie")
# print(fruits)

#FizzBuzz
target = 100
for num in range(1, target + 1):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)
