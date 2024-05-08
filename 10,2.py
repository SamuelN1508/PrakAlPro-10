# List yang ingin digabung
Lista = ['red', 'green', 'blue']
Listb = ['#FF0000','#008000', '#0000FF']

# Dict kosong
dict = {}

# Looping untuk memasukan list b ke a
i = 0
for x in Lista:
    dict[x] = Listb[i]
    i += 1

print(dict)