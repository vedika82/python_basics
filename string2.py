# In Python, RegEx (short for Regular Expression) is a tool for matching and handling strings.
# This RegEx module provides several functions for working with regular expressions, including search, split, findall, and sub.
# Python provides a built-in module called re, which allows you to work with regular expressions. First, import the re module
import re

# The search() function searches for specified patterns within a string. Here is an example that explains how to use the search() function to search for the word "Jackson" in the string "Michael Jackson is the best".
s1 = "Michael Jackson is the best"

# Define the pattern to search for
pattern = r"Jackson"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")


# A simple example of using the \d special sequence in a regular expression pattern with Python code:
pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
# The match.group() method is used in Python's re module to retrieve the part of the string where the regular expression pattern matched. 
else:
    print("No match")
# When you use functions like re.search() or re.match(), they return a match object if the pattern is found. You can then use match.group() to get the matched text.




# The regular expression pattern is defined as r"\W", which uses the \W special sequence to match any character that is not a word character (a-z, A-Z, 0-9, or _). The string we're searching for matches in is "Hello, world!".
pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)
print("Matches:", matches)
# The findall() function finds all occurrences of a specified pattern within a string


s2 = "Michael Jackson was a singer and known as the 'King of Pop'"
# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)
# Print out the list of matched words
print(result)




# A regular expression's split() function splits a string into an array of substrings based on a specified pattern.
# Use the split function to split the string by the "\s"
split_array = re.split(r"\s", s2)
# The split_array contains all the substrings, split by whitespace characters
print(split_array)




# re.split("\s", s2):
# re.split: This function splits a string by the occurrences of a pattern.
# r"\s": This is a regular expression pattern that matches any whitespace character (spaces, tabs, newlines, etc.).
# s2: This is the string that you want to split.
# The sub function of a regular expression in Python is used to replace all occurrences of a pattern in a string with a specified replacement.
# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 