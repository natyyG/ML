x = input("")
reverse = reversed(x)
print()
if(list(reverse) == list(x)):
    print("Palindrome")
else:
    print("Not palindrome")