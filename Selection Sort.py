def srt(arr):
    for i in range(0,len(arr)-1):
        minPos = i
        for j in range(i,len(arr)):
            if arr[j] < arr[minPos]:
                minPos = j
                
        temp = arr[i]
        arr[i] = arr[minPos]
        arr[minPos]=temp
        print(f'iteration no.{i+1} => {arr}')
        
        

arr = [5,3,8,6,7,2]
srt(arr)
print('SORTED array:',arr)

# print(len(arr))


# Output:
# [2,3,5,6,7,8]  
