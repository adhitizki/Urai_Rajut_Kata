def urai(kata): #fungsi untuk urai kata
    kata_baru = '' #mendefinisikan kata baru yang kosong untuk digunakan menambahkan kata, dengan tujuan kata baru merupakan hasil urai
    for i in range(len(kata)): #mendefiniskan per kata dengan index
        kata_baru += kata[:i] #menambahkan kata baru dengan 0 sampai index -1
    kata_baru += kata #menambahkan kata terakhir yang komplit karena kalau diatas i+1 maka dia out of range
    return kata_baru #mengembalikan kata yang telah diurai

def rajut(kata): #fungsi untuk rajut kata
    panjang_kata = kata.count(kata[0])  #menghitung kemunculan huruf pertama karena merepresentasikan panjang kata asli
    kata_baru = kata[len(kata)-panjang_kata:] #dapat dilihat bahwa kata asli terdapat pada panjang_kata urutan terakhir, semisal ccocodcode dengan panjang kata asli sebanyak 4 jadi kata asli berada pada urutan 4 terakhir
    return kata_baru

print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
