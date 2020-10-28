users1 = {'sara': 29, 'sina': 25}
users2 = {'shayan': 32, 'samin': 28}

# Merge
# new_dict = { **users1, **users2 }
# new_dict = users1 | users2

# Update
# users1.update(users2)
users1 |= users2

print(users1)

