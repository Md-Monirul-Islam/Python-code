print('Input your Height :')
h_feat = int(input("feat :"))
h_inch = int(input("Inches :"))

h_inch += h_feat * 12
h_cm = round(h_inch * 2.54,1)
print("Your height is cm :",h_cm)