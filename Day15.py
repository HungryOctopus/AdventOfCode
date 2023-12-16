import os  # works with files and directories

file_path = (
    os.path.dirname(__file__) + "/input/Input-Day15.txt"
)  # creates a number dictionnary

# test_input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


def apply_hash(file_path):
    with open(file_path) as input_file:
        content = input_file.read()  # Read the content of the file
        # input_list = test_input.split(",")
        input_list = content.split(",")  # Split the content into a list
        result = 0
        current_value = 0
        for item in input_list:
            print(item)
            for char in item:
                ascii_val = int(ord(char))
                print("ASCII: ", ascii_val)
                current_value += ascii_val
                current_value = (current_value * 17) % 256
            print("CURRENT VALUE: ", current_value)
            result += current_value
        print("RESULT: ", result)


apply_hash(file_path)
