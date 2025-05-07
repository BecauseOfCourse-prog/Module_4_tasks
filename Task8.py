def bubble_sort(arr):
    for i in range(len(arr)):
        for n in range(len(arr)):
            if n < len(arr)-1 and arr[n] > arr[n+1]:
                cloud = arr[n]
                arr[n] = arr[n+1]
                arr[n+1] = cloud


my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Отсортированный список:", my_list)