#From Codecademy

#1
def is_even(x):
  return x %2 == 0
print(is_even(900))
print(is_even(233))

#2
#classify 7.0 as integer
def is_int(x):
  absoluteCount = abs(x)
  roundCount = round(absoluteCount)
  return absoluteCount - roundCount == 0
print(is_int(-1.5))
print(is_int(3.0))
print(is_int(3.5))
print(is_int(-2))

#3
def digit_sum(x):
  total = 0
  while x > 0:
      total += x % 10
      x = x // 10
  return total
print(digit_sum(369))

#4
def facts(x):
  total = 1
  while x > 0:
      total = total * x
      x = x - 1
  return total
print(facts(4))
print(facts(1))

#5
def is_prime(x):
  if x < 2:
      return False
  else:
      for n in range(2, x-1):
          if x % n == 0:
              return False
      return True
print(is_prime(13))
print(is_prime(10))


#6
def reverse(text):
  characters = list(text)
  reverse = str()
  for i in range(1, len(characters)+1):
    reverse += text[-i]
  return reverse
print(reverse("Python!"))
