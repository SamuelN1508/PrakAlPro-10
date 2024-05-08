# Meminta input
input = input("Masukan nama file : ")

# Fungsi untuk mencari alamat domain (kata-kata setelah @)
def domain_name(email):
    # List kosong
    list = []
    # String kosong
    
    # Cara mudah
    domain = email.split('@')[1]
    
    # Cara Ribet
    # Looping setiap huruf di alamat email
    # for x in email:
    #     # Memasukan setiap huruf dalam list dengan index berbeda
    #     list.append(x)
    # # Mencari index "@"
    # index = list.index("@")
    
    # # String domain akan ditambah setiap huruf setelah "@"
    # for x in list[index+1:]:
    #     domain += x
    return domain

# Fungsi menghitung domain
def count_domain(input):
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
                
                # Mencari nama domain menggunakan fungsi domain_name()
                domain = domain_name(kata[1])
                
                # Mengecek apakah email sudah pernah ditambah ke dict
                if domain not in dict:
                    # Jika belom ada maka akan dibuat dict baru
                    dict[domain] = 1
                else:
                    # Jika sudah ada maka akan ditambah satu
                    dict[domain] += 1
    print(dict)
                    
count_domain(input)           