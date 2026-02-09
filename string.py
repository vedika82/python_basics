name="vedika anand"
print(name[0])# to print the first character of the string
print(name[6])
print(name[-8])# to print the 8th character from the end of the string
print(len(name))# to print the length of the string

#SLICING
print(name[0:6])# to print the characters from index 0 to 5
print(name[7:])# to print the characters from index 7 to the end of the string
print(name[:6])# to print the characters from the beginning of the string to index 5
print(name[:])# to print the whole string

#STRIDE
print(name[::2])# to print the characters from the whole string with a step of 2

# sliding +stride
print(name[1:6:2])# to print the characters from index 1 to 5 with a step of 2
print(name[0:6:2])# to print the characters from index 0 to 5 with a step of 2
print(name[1::2])# to print the characters from index 1 to the end

statement = name + " is a good girl" # concatenation of two strings
print(statement)

print (name*3) # to print the string 3 times


# New line escape sequence
print(" The BodyGuard\n is the best album" )

# Tab escape sequence
print(" The BodyGuard \t is the best album" )

# Include back slash in string
print(" The BodyGuard \\ is the best album" )

# r will tell python that string will be display as raw string
print(r" The BodyGuard \ is the best album" )

# Convert all the characters in string to upper case
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)

# Replace the old substring with the new target substring is the segment has been found in the string
a = "The BodyGuard is the best album"
b = a.replace('BodyGuard', 'Janet')
print(b)

# Find the substring in the string. Only the index of the first elment of substring in string will be the output
name = "The BodyGuard"
print(name.find('BodyGuard'))

# Find the substring in the string.
print(name.find('bodyguard'))# if the substring is not in the string then the output is a negative one.

print(name.find('Jasdfasdasdf'))#If the sub-string is not in the string then the output is a negative one. 


# Syntax
# string.split(separator, maxsplit)

# Parameters
# separator (optional): This is the delimiter at which the string will be split. If not provided, the default separator is any whitespace.
# maxsplit (optional): This specifies the maximum number of splits to perform. If not provided, there is no limit on the number of splits.

#Split the substring into list
name = "The BodyGuard"
split_string = (name.split())
print(split_string)