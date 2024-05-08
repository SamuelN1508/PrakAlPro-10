# Dictionary
Dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Mengubah keys dan values menjadi list
keys = list(Dictionary.keys())
values = list(Dictionary.values())

print(("keys     values    items"))

# Loopings setiap keys, values dan items
for i in range(len(Dictionary)):
    print(f"{keys[i]}        {values[i]}        {i+1}")
