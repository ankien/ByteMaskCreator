maskBit = int(input("Fill mask with 1's or 0's? [1/0]: "))
littleEndian = input("Little-endian output? (big-endian otherwise) [y/n]: ")
numOfBytes = int(input("How many bytes? [enter a positive integer]: "))

if maskBit:
    array = ["FF" for x in range(numOfBytes)]
else:
    array = ["0" for x in range(numOfBytes)]

with open("input.txt", 'r') as file:
    content = file.read().splitlines()

if littleEndian == 'y':
    for line in content:
        string = line.split(' ')
        index = int(string[0],16)
        addressInput = string[2].split('_')
        for byte in reversed(addressInput):
            array[index] = byte
            index += 1
else:
    for line in content:
        string = line.split(' ')
        index = int(string[0],16)
        addressInput = string[2].split('_')
        for byte in addressInput:
            array[index] = byte
            index += 1

output = open("output.txt",'w')
for i in range(numOfBytes - 1):
    output.write("0x" + str(array[i]) + ",")
output.write("0x" + str(array[i]))
output.close()

print("Your byte array has been placed in output.txt!\n")