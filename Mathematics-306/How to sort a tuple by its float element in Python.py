rate_of_product = [("item1",'12.20'),("item2","130.30"),("item3","132.123")]
print(sorted(rate_of_product,key=lambda x : float(x[1]),reverse=True))