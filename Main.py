while True:
    code = input("Enter binary code or type quit to quit : ")
    code = code.strip()
    if code.upper() == "QUIT":
        break
    b = True
    if not code.isnumeric():
        b = False
    else:
        binary = []
        for i in range(len(code)):
            binary.append(code[i])
        for i in binary:
            if int(i) != 0 and int(i) != 1:
                b = False
    if b:
        binary.reverse()
        x = []
        power = 0
        while power < len(binary):
            x.append(2**power)
            power += 1
        sum = 0
        for digit in range(len(binary)):
            if int(binary[digit]) == 1:
                sum += x[digit]
        print(sum)
print("Thanks for using my converter!")
