import os


isDecode = input("Would you like to encode? (e) Or would you like to decode? (d)")


if isDecode.casefold() == "d":
    #Getting the main string
    Emojis = input("Paste in the string of Emojis")


    # Function to get the version input
    def set_old():
        return input("Are you using the old system? (Right = 00, Left = 01, Normal = 10, Up = 11) Or the new system (Up = "
                     "00, Left = 01, Right = 10, Normal = 11) (o for old n for new)")


    # Getting the version input
    old = set_old().casefold()

    convert = input(
        "Do you want it converted to text? (press any key) Or would you like a binary dump? (b) Or would you like a hex "
        "dump? (h)")


    # Making sure the input is either an 'o' or a 'n'
    if old != "o":
        if old != "n":
            print("Invalid input. Redoing")
            old = set_old().casefold()
            if old != "o":
                if old != "n":
                    print("Stop it!")
                    old = set_old().casefold()
                    input("Press any key...")
                    exit()

    # Predefining the variables
    decode = ""
    n = 0
    i = 0
    current = ""

    # Decoding to binary
    while i < len(Emojis):
        if Emojis[i] == ":":
            if n == 1:
                if old == "o":
                    if current == "extraZoeyRight":
                        decode += "00"
                    elif current == "extraZoeyLeft":
                        decode += "01"
                    elif current == "extraZoey":
                        decode += "10"
                    elif current == "extraZoeyUp":
                        decode += "11"
                elif old == "n":
                    if current == "extraZoeyUp":
                        decode += "00"
                    elif current == "extraZoeyLeft":
                        decode += "01"
                    elif current == "extraZoeyRight":
                        decode += "10"
                    elif current == "extraZoey":
                        decode += "11"
                current = ""
                n = 0
            else:
                n = 1
        else:
            current += Emojis[i]
            #print(Emojis[i])
        i += 1


    #Print the results
    if convert.casefold() == "b":
        print(decode)
    elif convert.casefold() == "h":
        print(hex(int(decode)))
    else:
        #I found this bit of code at https://stackoverflow.com/questions/40557335/binary-to-string-text-in-python
        print(''.join(chr(int(decode[i * 8:i * 8 + 8], 2)) for i in range(len(decode) // 8)))
    input("Press any key...")
elif isDecode.casefold() == "e":
    def set_old():
        return input("Are you using the old system? (Right = 00, Left = 01, Normal = 10, Up = 11) Or the new system ("
                     "Up = 00, Left = 01, Right = 10, Normal = 11) (o for old n for new)")


    # Getting the version input
    old = set_old()
    # Making sure the input is either an 'o' or a 'n'
    if old != "o":
        if old != "n":
            print("Invalid input. Redoing")
            old = set_old()
            if old != "o":
                if old != "n":
                    print("Stop it!")
                    old = set_old()
                    input("Press any key...")
                    exit()

    text = input("Type in text to encode")

    t = ''.join(bin(ord(text[i])).replace("b", "") for i in range(len(text)))
    print(t)
    current = ''
    for i in range((len(t) / 2).__int__()):
        #print(i)
        #print(t[(i * 2)])
        #print((t[(i * 2) + 1]))
        f = ''.join(t[(i * 2)] + (t[(i * 2) + 1]))
        #print(f)
        if old == "o":
            if f == "00":
                current += ":extraZoeyRight:"
            elif f == "01":
                current += ":extraZoeyLeft:"
            elif f == "10":
                current += ":extraZoey:"
            elif f == "11":
                current += ":extraZoeyUp:"
        elif old == "n":
            if f == "00":
                current += ":extraZoeyUp:"
            elif f == "01":
                current += ":extraZoeyLeft:"
            elif f == "10":
                current += ":extraZoeyRight:"
            elif f == "11":
                current += ":extraZoey:"
    print(current)
    copy = input("Would you like to copy the output to the clip board? (y/n))")
    if copy == "y":
        #Snippet from https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard-on-windows-using-python
        cmd = ('echo ' + current.strip() + '| clip')
        os.system(cmd)
    input("Press any key...")

