letter = "Hey my name is {} and i am from {}"
country = "Bangladesh"
name = "Anwar hossain"
print(letter.format(name, country))

# another way formatting string
letter = "Hey my name is {1} and i am from {0}"
country = "Bangladesh"
name = "Anwar hossain"
print(letter.format(country, name))

# another way formatting string

country = "Bangladesh"
name = "Anwar hossain"
letter = f"Hey my name is {name} and i am from {country}"
print(letter)

# print full f-sting print
print(f"Hey my name is {{name}} and i am from {{country}}")

price = 4.00
txt = f"for only {price} dollars!"
print(txt)

print(f"{2 * 30}")
print(type(f"{2 * 30}"))

name = "anwar"
uni = "diit"
bio = f"Hey my name is {name} and i am  student of {uni}"
print(bio)

