def min3 (num1, num2, num3):
    if num1 <= num2:
        if num1 <= num3:
            return num1
        else:
            return num3
    else:
        if num2 <= num3:
            return num2
        else:
            return num3
    
    
# Uncomment this code to test your function

print(min3(4, 7, 5))  
print(min3(4, 5, 5))  
print(min3(4, 4, 4))  
print(min3(-2, -6, -100))  
print(min3("Z", "B", "A"))  

print(min3(8, 9, 1))
print(min3(9, 8, 2))

# You should get this result:

# 4  
# 4  
# 4  
# -100  
# A  
  