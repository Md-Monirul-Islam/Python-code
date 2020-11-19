student = [
    {"id":1,
     "success":True,
    "name":"Munna"
     },
    {"id":2,
     "success":False,
     "name":"Morir"
     }

]
print(sum(d["success"] for d in student))