# Meminta input
input = input("Masukan nama file : ")
# Dict kosong
dict = {}
# Membuka file
with open(input, "r") as file:
    # Membaca setiap lines pada file
    lines = file.readlines()
    
    # Looping setiap kata dalam kalimat
    for line in lines:
        
        # Mencari email
        if line.startswith("From") and len(line.split()) < 3:
            # Ketika email sudah ditemukan maka akan displit
            kata = line.split()
            
            # Mengecek apakah email sudah pernah ditambah ke dict atau blm
            if kata[1] not in dict:
                # Jika belom ada maka akan dibuat dict baru
                dict[kata[1]] = 1
            else:
                # Jika sudah ada maka akan ditambah satu
                dict[kata[1]] += 1

print(dict)