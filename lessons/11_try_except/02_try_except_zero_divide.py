#Fill in code here:
def spam(divide_by):
  try:
    #This code is tried before it actually gets run, if it causes an error Python will skip down to the except statement below.
    return 42 / divide_by
  except ZeroDivisionError:
    #This code will be run if any of the tries above cause an error, Python will not go back up to the try block after the except block is run.
    print("Error: Invalid argument.")
  except TypeError:
    print("Enter a number.")



print(spam(2))
print(spam(12))
print(spam(0))
print(spam("dog"))
print(spam(1))
