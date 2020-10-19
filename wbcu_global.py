# The "global" keyword
age = 1

def increase():
    global age
    age = 3

print(age) # 1
increase()
print(age) # 1