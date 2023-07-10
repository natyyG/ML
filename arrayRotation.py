x = int(input("Enter the number you want to rotate the array: "))
sample_array = [1,2,3,4,5]
new_array = sample_array[len(sample_array)-x:] + sample_array[:len(sample_array)-x]
print(new_array)