name = input("Name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read()
print(f"Hi {name}!")
in_file.close()

in_file = open("numbers.txt", "r")
for line in in_file:
in_file.close()

in_file = open("numbers.txt", "r")
numbers = in_file.readlines()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i].strip())
result = numbers[0] + numbers[1] + numbers[2]
print(result)
in_file.close()

