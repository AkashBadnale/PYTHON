people = {
          1: {'name': 'John',},
              2: {'name': 'Marie'},
          3: {'name': 'Ann',},
          4: {'name': 'John'},
     }
print(people)
unique = {}
for key, value in people.items(): 
       if value not in unique.values(): 
          unique[key] = value
print(unique)
