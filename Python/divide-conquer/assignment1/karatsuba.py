import math

def karatsuba(strnum1, strnum2):
  num1 = int(strnum1)
  num2 = int(strnum2)

  if num1 < 10 or num2 < 10:
    return num1 * num2

  maxlen = max(len(str(num1)), len(str(num2))) // 2
  base = 10 ** maxlen

  def decompose(num):
    return num // base, num % base
  
  a, b = decompose(num1)
  c, d = decompose(num2)

  first = karatsuba(a ,c)
  second = karatsuba(b, d)
  third = karatsuba(a + b, c + d)

  return first * (base ** 2) + second + base * (third - first - second)