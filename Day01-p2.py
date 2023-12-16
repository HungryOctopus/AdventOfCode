import os # works with files and directories
import re # for regex

input_file = os.path.dirname(__file__) + "/input/Input-Day01.txt"# creates a number dictionnary
numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

regexFirst = r"(%s)" % ("|".join(list(numbers.values()) + list(numbers.keys())))
# %s is a placeholder
# % operator allows you to insert values into a string template.
regexLast = r"(?s:.*)%s" % (regexFirst)

def getFirst(s):
    return re.search(regexFirst, s).group()

def getLast(s):
    return re.search(regexLast, s).group(1)

#.group() allows you to access 
# specific portions of the matched text that correspond to capturing groups 
# defined in the regex pattern.

def getAsNumber(number):
    if number.isdigit():
        return number
    else:
        return numbers[number]
    
def calibration_value(s):
    return int("%s%s" % (getAsNumber(getFirst(s)), getAsNumber(getLast(s))))

with open(input_file) as input:
    result = 0
    for line in input:
        result += calibration_value(line.strip())
    print(result)



# The r in front of the string denotes that it is a "raw string." 
# For example, in a raw string, a backslash \ is treated as
# a literal character
