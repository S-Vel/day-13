import re

def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("1233@@#$$%$"))

def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False

print(end_num('abcdef12233'))
print(end_num('abcdef634556'))
print(end_num('abc'))

results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 9, 11, and 222 are important")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))

def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("30 Days challenge"))
print(text_match("Day_13_task"))