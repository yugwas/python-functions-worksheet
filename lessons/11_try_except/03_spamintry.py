def spam(divide_by):
  return 42 / divide_by

try:
  print(spam(2))
  print(spam(12))
  print(spam(0))
  print(spam(1))
  print(spam("dog"))
except Exception:
  print("Error: Invalid argument.")

  
