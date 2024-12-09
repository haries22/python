Data = [14, 4, 20, 8, 10, 12, 2, 16, 18, 6]
print("data sebelum di urutkan:", Data)
Banyak_Data = len(Data)
for i in range (Banyak_Data - 1):
    for j in range (Banyak_Data - 1):
        if Data [j] > Data [j + 1]:
            temp = Data[j]
            Data[j] =  Data [j + 1]
            Data[j + 1] = temp
print("Data setelah diurutkan:", Data)
