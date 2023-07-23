dic = {
    "Anwar": "human begin",
    "black": "colour",
    210: "anwar"
}
print(dic["Anwar"])
print(dic["black"])
print(dic[210])

employee = {}

# for i in range(3):
#     name = input()
#     salary = input()
#     employee[name] = salary
#
# for value in employee.values():
#     print(value)


# print(employee)
info = {"name": "anwar", "age": 24, "gender": "male"}

print(info)
print(info["name"])
print(info["age"])
print(info["gender"])
print(info.get("name"))

bio = {"first name": "anwar", "last name": "hossain", "date of barth": "21-03-2000"}

print(bio)
print(bio["first name"])
print(bio["last name"]) # error  throw
print(bio.get("date of barth"))
print(bio.keys())
print(bio.values())
for key in bio.keys():
    print(bio[key])

for key, value in bio.items():
    print(f"the value corresponding to the key {key}, is {value}")
