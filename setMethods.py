# union set :

s1 = {1, 2, 3, 4, }
s2 = {3, 4, 5}

print(s1.union(s2))
s1.update(s2)
print(s1)

team1 = {"anwar", "rukon", "shakil"}
team2 = {"anwar", "shakil", "tanvir"}

team = team1.union(team2)  # union set
team1.update(team2)  # update team1
print("update team1 :", team1)
print("union :", team)

# intersection AnB:
team1 = {"anwar", "rukon", "shakil"}
team2 = {"anwar", "shakil", "tanvir"}

team = team1.intersection(team2)
print("Intersection : ", team)

team1 = {"anwar", "rukon", "shakil"}
team2 = {"anwar", "shakil", "tanvir"}

team1.intersection_update(team2)
print("update intersection:", team1)

# symmetric difference:
book1 = {"DS", "MICRO", "C"}
book2 = {"DBMS", "C", "MICRO"}

final_result = book1.symmetric_difference(book2)
print("symmetric dif: ", final_result)

# Set difference A-B:
book1 = {"DS", "MICRO", "C"}
book2 = {"DBMS", "C", "MICRO"}

final_result = book1.difference(book2)
print("difference", final_result)

# disjoint Set : check item two set if same item return false otherwise ture,
book1 = {"DS", "MICRO", "C"}
book2 = {"DBMS", "C", "MICRO"}

final_result = book1.isdisjoint(book2)
print("disjoint set :", final_result)

# super set : check B set all item has A set if given return ture otherwise false
book1 = {"DS", "MICRO", "C"}
book2 = {"C", "MICRO"}
book3 = {"C", "MICRO", "ECONOMIC"}

final_result = book1.issuperset(book2)
print("Super set :", final_result)

final_result = book1.issuperset(book3)
print("Super set :", final_result)

# Sub set :
book1 = {"DATA Structure", "Microprocessor", "C"}
book2 = {"C"}

final_result = book2.issubset(book1)
print("SuB  set :", final_result)

# insert item using Add function:
book1 = {"DATA Structure", "Microprocessor", "C"}
book1.add("Operating system")

print(book1)

# remove item in set using remove/ discard:
book1 = {"DATA Structure", "Microprocessor", "C"}
book1.discard("C")
print(book1)

# delete set use del
book1 = {"DATA Structure", "Microprocessor", "C"}
''' del book1'''
print(book1)

# if else statement use in set
colours = {"Red", "Yellow"}
if "Red" in colours:
    print("Yes red colour present")
else:
    print("No red colour not present")
