Data = [14, 4, 20, 86, 10, 12, 82, 16, 18, 6,24,26,28,9,22,30,32,38,34,40,52,58,92,88,78,46,7,50,60,100,94,98,36,42,96,44,54,72,74,48,56,76,84,80,2,8,90,1,3,5,101]

print("Pilih opsi:")
print("1. Data belum terurut")
print("2. data diurutkan menggunakan Bubble Sort")

Pilihan = int(input("Masukkan pilihan (1 atau 2): "))

if Pilihan == 1:
    print("List belum terurut:", Data)
elif Pilihan == 2:
    print("List sebelum diurutkan:", Data)
    Banyak_Data = len(Data)


    for i in range (Banyak_Data - 1):
        for j in range (Banyak_Data - 1):
            if Data [j] > Data [j + 1]:
                temp = Data[j]
                Data[j] =  Data [j + 1]
                Data[j + 1] = temp
        print(f"Iterasi ke-{i + 1}: {Data}")

    print("data setelah diurutkan:", Data)
else:
    print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
