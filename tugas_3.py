books = []

def asc_insertion_sort(array):
    for i in range (1, len(array)):
        item = array[i]
        j = i - 1

        while j >= 0 and array[j] > item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item
    
    return array

def dsc_insertion_sort(array):
    for i in range (1, len(array)):
        item = array[i]
        j = i - 1

        while j >= 0 and array[j] < item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item
    
    return array

def add_books():
    total = int(input("Masukkan Total Buku : "))
    count = 1
    while(total > 0):
        nama = input(f'Masukkan Judul Buku ke-{count} : ')
        books.append(nama)
        count+=1
        total = total - 1

    while(True):
        total = total - 1
        if(total < 0):
           break 

def menu():
    add_books()
    print("<========== Urutkan ? =========>")
    print("1. Insertion Ascending")
    print("2. Insertion Descending")

    pilih = int(input("Pilih: "))
    if (pilih == 1):
        print("Sorting Buku Secara Ascending")
        asc_insertion_sort(books)
    elif (pilih == 2):
        print("Sorting Buku Secara Descending")
        dsc_insertion_sort(books)
    else:
        print("Pilihan tidak tersedia..")

    hitung = 1
    for i in books:
        print(f'Judul Buku ke-{hitung} : ', i)
        hitung+=1

menu()