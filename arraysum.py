arr1 = [1,2,3,4,5,6,7]
arr2 = [1,2,3,4,5,6,7]
arr3 = []
length_of_array = 0
if(len(arr1)<len(arr2)):
    length_of_array = len(arr1)
else:
    length_of_array = len(arr2)
    
for i in range(length_of_array):
    value = arr1[i] + arr2 [i]
    arr3.append(value)
print("The program prints the sumation of the two array's")
print(arr3)
        