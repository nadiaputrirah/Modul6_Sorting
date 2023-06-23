def addMahasiswa():
    jumlah = int(input("Jumlah mahasiswa: "))
    mahasiswa = []
    while jumlah > 0:
        nama = input("Nama mahasiswa: ")
        mahasiswa.append(nama)
        jumlah -= 1
    
    panggil(mahasiswa)

def removeMahasiswa(arrayMahasiswa):
    print("Data mahasiswa %s" % arrayMahasiswa)
    mahasiswa = input("Hapus mahasiswa: ")
    arrayMahasiswa.remove(mahasiswa)
    print("Data Mahasiswa %s" % arrayMahasiswa)
    panggil(arrayMahasiswa)

def ascMahasiswa(arrayMahasiswa):
    arrayMahasiswa.sort()
    print(arrayMahasiswa)
    panggil(arrayMahasiswa)

def viewMahasiswa(arrayMahasiswa):
    for x in arrayMahasiswa:
        print("Nama Mahasiswa %s" % x)
    panggil(arrayMahasiswa)

def panggil(arrayMahasiswa):
    print("\n<=========Menu Data Mahasiswa=========>")
    print("1. Tambah Data Mahasiswa")
    print("2. Hapus Data Mahasiswa")
    print("3. Urutkan Data Mahasiswa")
    print("4. Lihat Data Mahasiswa")
    print("5. Tutup")

    pilih = int(input("Pilih: "))
    if pilih == 1:
        addMahasiswa()
    elif pilih == 2:
        removeMahasiswa(arrayMahasiswa)
    elif pilih == 3:
        ascMahasiswa(arrayMahasiswa)
    elif pilih == 4:
        viewMahasiswa(arrayMahasiswa)
    else:
        print("Selesai")

panggil([])
