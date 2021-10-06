def spam():
  eggs = "spam local"  #1
  print(eggs) #prints "spam local"

def bacon():
  eggs = "bacon local"  #2
  print(eggs) #prints "bacon local"
  spam()
  print(eggs) #prints "bacon local"

eggs = "global"  #3
bacon()
print(eggs) # prints "global"

#There are three variables all named eggs

#1 is a Variable named eggs that exists in a local scope when spam() is called.
#2 is a variable named eggs that exists in a local scope when bacon() is called.
#3 is a variable named eggs that exists in the global scope.

#This is confusing and it is why you should avoid using the same variable name in different scopes.