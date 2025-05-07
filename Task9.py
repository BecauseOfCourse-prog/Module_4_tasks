def insertion_sort(arr):
    for i in range(len(arr)):
        index = i
        if i < len(arr)-1 and arr[i+1] < arr[i]:
            for n in range(i+1):
                if arr[index+1] < arr[index]:
                    cloud = arr[index+1]
                    arr[index+1] = arr[index]
                    arr[index] = cloud
                index -= 1


my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)
print("Отсортированный список:", my_list)