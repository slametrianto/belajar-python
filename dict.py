customer = {"Name": "Eko", "Age":30, "Address": "Bekasi"}

name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

customer["Company"] = "X"
customer["Name"] = "nurreni"

#menghapus
del customer("Age")

for key, value in customer.items():
    print(f"{key}:{value}")

