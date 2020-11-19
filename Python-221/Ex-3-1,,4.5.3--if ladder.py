temperature = int(input("enter any temparature : "))
if temperature < 0:
    print("The weather is freezing.")
elif temperature < 10:
    print("The weather is very cool.")
elif temperature < 20:
    print("The weather is chilly.")
elif temperature < 30:
     print("The weather is warm.")
elif temperature < 40:
    print("The weather is hot.")
else:
    print("The weather is too hot.")