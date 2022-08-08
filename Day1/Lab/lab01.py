# You can find information on how to convert numbers to a different base here:
# https://www.tutorialspoint.com/computer_logical_organization/number_system_conversion.htm

# You can find information on how to convert numbers to roman numerals here:
# https://www.romannumerals.org/converter


def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  digits = []
  while num != 0:
    digits.append(num % 2)
    num = num // 2
  
  digits = list(reversed(digits))
  digits = map(str, digits)

  return ''.join(digits)

binarify(29)

def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  if num<=0:  return '0' 
  digits = []
  while num != 0:
    digits.append(num % base)
    num = num // base

  digits = list(reversed(digits))
  digits = map(str, digits)

  return ''.join(digits)

int_to_base(29, 4)

def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  if string=="0" or base <= 0 : return 0 
  result = 0
  num = [int(i) for i in string]
  num = list(reversed(num))

  for i in range(0, len(string)):
    result += num[i] * base ** i

  return result

base_to_int("11101", 2)

def flexibase_add(str1, str2, base1, base2, base3):
  """add two numbers of different bases and return the sum"""
  num1 = base_to_int(str1, base1)
  num2 = base_to_int(str2, base2)
  tmp = num1 + num2
  result = int_to_base(tmp, base3)
  return result 

def flexibase_multiply(str1, str2, base1, base2, base3):
  """multiply two numbers of different bases and return the product"""
  num1 = base_to_int(str1, base1)
  num2 = base_to_int(str2, base2)
  tmp = num1 * num2
  result = int_to_base(tmp, base3)
  return result 

def romanify(num):
  """given an integer, return the Roman numeral version"""
  numerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
  

  result = ""
  return result


# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.