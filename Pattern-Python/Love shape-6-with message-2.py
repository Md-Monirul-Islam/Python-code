num = int(input("Please enter the number : "))
msg = input("Please entr the message : ")
length = len(msg)
n = num // 2
for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1), end='')
    if num % 2 == 0:
        for j in range(2 * (n - i - 1)):
            print(" ", end='')
    else:
        for j in range(2 * (n - i - 1) + 1):
            print(" ", end=' ')
    for j in range(i + 1):
        print("* ", end='')
    print()
if num%2==0:
    if length%2==0:
        print("* " * ((num - length) // 2) + " ".join(msg) + " *" * ((num - length) // 2))
    else:
        print("* " * ((num - length) // 2) + " ".join(msg) + " *" * ((num - length) // 2)+1)




for i in range(num, 0, -1):
    print(" " * (num - i) + "* " * (i))