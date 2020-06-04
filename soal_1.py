def konversi_waktu(waktu):
    digit_2 =  lambda x: '0'+str(x) if x < 10 else str(x) #untuk mengubah 1 digit angka menjadi 2 digit angka
    if waktu < 360000: #dengan kondisi waktu kurang 36000 atau waktu 0 sampai 359999
        jam = digit_2(waktu // 3600) #menentukan jam dengan membagi input dengan 3600, menggunakan // karena membulatkan kebawah, karena jam bukan float
        menit = digit_2((waktu%3600)//60) #menentukan menit dengan modulus dari 3600 yang merupakan satu jam untuk kemudian dibagi 60 menggunakan // karena untuk pembulatan kebawah dan menit bukan float 
        detik = digit_2((waktu%3600)%60) #menentukan detik dengan sisa dari modulus jam dan menit
    return jam,menit,detik

try:
    waktu = int(input('Masukkan detik : ')) #masukan dengan assign waktu atau penamaan waktu
    print(f'Konversi : {konversi_waktu(waktu)[0]}:{konversi_waktu(waktu)[1]}:{konversi_waktu(waktu)[2]}') #mencetak sekaligus menggunakan function pada konversi waktu dengan index 0 1 2 dengan 0 adalah jam, 1 adalah menit, dan 2 adalah detik
except:
    print('Invalid input!') #untuk kondisi yang tidak memenuhi sepert string, float dan waktu >= 360000
