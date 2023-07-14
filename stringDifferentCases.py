name = "anwar....n!.anwar"
story = "My name is Anwar and I'm a student department of CSE"
str1 = "anwarhossain"

print(name.strip("...n!"))  # remove charter

print(story.capitalize())  # only first char upper and everything else lower case

print(name.replace("anwar", "hossain"))  # replace string

print(name.count("anwar"))  # using count same string or charter

print(name.endswith("anwar"))  # string check last charter/word if same return ture otherwise false

print(story.endswith("is", 5, 10))  # string slicing and check charter/word if same return ture otherwise false

# find same string if you find same string then return index number otherwise return -1
print(story.find("is"))

# find same string if you find same string then return index number otherwise  error
print(story.index("Anwar"))

print(str1.isalnum())  # find A-Z , a-z or 0-9  return ture otherwise false

print(str1.isalpha())  # only alpha return ture otherwise false

print(str1.islower())  # if all alphabet is lower return ture otherwise false

print(str1.isprintable())  # if you use \n or \t return false other ture

# str1 = "     "
print(str1.isspace())  # using space return ture otherwise false

print(str1.swapcase())  # if string lower case then convert uppercase else lowercase

print(story.title())  # this function convert only first charter uppercase
