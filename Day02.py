possible_games = []
power_set_list = []

file_path = "/Users/ameliem/coding/portfolio/AdventOfCode/input/Input-Day02.txt"
with open(file_path) as input_file:
    for line in input_file:
        game_name, game_result = line.strip().split(":")
        game_id = int(game_name.split()[1])

        cleaned_row = game_result.replace(";", ",")

        red_count = 0
        green_count = 0
        blue_count = 0

        array_result_per_game = cleaned_row.split(", ")
        print(array_result_per_game)

        for result_item in array_result_per_game:
            cube_count, cube_color = result_item.split()
            # print(cube_count)

            # takes the highest value for red, blue and green
            if "red" == cube_color and red_count <= int(cube_count):
                red_count = int(cube_count)
            if "green" == cube_color and green_count <= int(cube_count):
                green_count = int(cube_count)
            if "blue" == cube_color and blue_count <= int(cube_count):
                blue_count = int(cube_count)

            print(red_count, green_count, blue_count)

        # part 2
        power_set = red_count * green_count * blue_count
        power_set_list.append(power_set)

        if red_count <= 12 and green_count <= 13 and blue_count <= 14:
            possible_games.append(game_id)
            print(game_id)

# Solution part 1
sum_possible_games = sum(possible_games)
print("sum_possible_games:", sum_possible_games)

# Solution part 2
sum_power_set_list = sum(power_set_list)
print("sum power set list:", sum_power_set_list)
# pip3 install black
# pip3 install flake8
# _ underscore for variables we don't want to use / keep