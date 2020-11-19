str = "46m"
try:
    i = float(str)
except (ValueError,TypeError):
    print("Not numaric")
print("success.")