def counter_clockwise(masukan):
    list_baru = [] #untuk list yang nanti digunakan untuk mengisi list yang sudah diputar
    for i in range(len(masukan[0])-1,-1,-1): #untuk memberikan index pada baris dimana ketika diputar akan menjadi kolom
        list_baris = [] #membuat list untuk baris baru yang sudah diputar
        for j in range(len(masukan)): #untuk memberikan index pada kolom dimana ketika diputar akan menjadi baris
            list_baris.append(masukan[j][i]) #menambahkan angka untuk satu dengan tiap kolom yang dari baris sebelumnya
        list_baru.append(list_baris) #list baru yang merupakan list hasil counter clock wise
    return list_baru #mengembalikan nilai fungsi awal

list_awal = [[1,2,3],
            [4,5,6],
            [7,8,9]]

print(counter_clockwise(list_awal))


for i in counter_clockwise(list_awal): #supaya menampilkan dengan setelah baris ter-enter
    print(i)        