def bubble_sort(array):
    for i in range (len(array)):
        for j in range (len(array)-i-1):
            if array [j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array 

mhs_ips = [3.8, 2.9, 3.3, 4.0, 2.7]
print("Indeks Prestasi Semester (IPS)")
print("List sebelum diurutkan : ", mhs_ips)
print("List setelah diurutkan : ", bubble_sort(mhs_ips))