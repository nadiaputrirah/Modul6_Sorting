def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        if array[min_index] > array[j]:
            min_index = j

        array[i], array[min_index] = array[min_index], array[i]
    
    return array

anggota_org = ["Zhafira", "Nirmala", "Askara", "Nalendra", "Cakra", "Sastra", "Agni", "Bagas", "Jerome", "Kiara"]
print("Before : " , anggota_org)
print("After : " ,selection_sort(anggota_org))