def my_function():
    print("Hello from a function")
    print("Bye")


hello = "hello_world"
print(len(hello))
print("my mane")

a_str = "He had the bat"
print(a_str.find('t'))
print(a_str.find('t', 8))
print(a_str.find('t', a_str.find('t')+1))

river = "Mississippi"
target = input("Input a character to find: ")
for index in range(len(river)):
    if river[index] == target:
        print("Letter found at index ", index)
        break
    else:
        print("Letter", target, "not found in", river)