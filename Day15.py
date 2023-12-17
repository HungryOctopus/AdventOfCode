import os

file_path = os.path.dirname(__file__) + "/input/Input-Day15.txt"

# test_input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


def apply_hash(file_path):
    with open(file_path) as input_file:
        content = input_file.read()  # Read the content of the file
        input_list = content.split(",")  # Split the content into a list
        result = 0
        current_value = 0
        for item in input_list:
            for char in item:
                current_value = ((current_value + int(ord(char))) * 17) % 256
            result += current_value
            current_value = 0  # reinitialise the value
        print("FINAL RESULT: ", result)


""" def apply_test(test_input):
    input_list = test_input.split(",")
    result = 0
    current_value = 0
    for item in input_list:
        print(item)
        for char in item:
            ascii_val = int(ord(char))
            print("ASCII: ", ascii_val)
            print("CURRENT VALUE bf: ", current_value)
            current_value += ascii_val
            print("CURRENT VALUE bf + ascii: ", current_value)
            current_value = (current_value * 17) % 256
            print("CURRENT VALUE MODULO: ", current_value)
        print("CURRENT VALUE: ", current_value)
        result += current_value
        current_value = 0
        print("RESULT: ", result)
    print("FINAL RESULT: ", result) """

apply_hash(file_path)
# apply_test(test_input)
