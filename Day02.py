possible_games = []
impossible_games = []

# file_path = "/Users/ameliem/coding/portfolio/AdventOfCode/input/Input-Day02.txt"
file_path = "/Users/ameliem/coding/portfolio/AdventOfCode/input/Input-Day02.txt"
with open(file_path) as input_file:
    for line in input_file:
        print(line)

        # Game 88: 2 blue, 4 red, 8 green; 4 blue, 7 red; 3 red, 10 green, 4 blue; 9 green, 3 blue, 5 red; 4 red, 6 blue, 3 green
        game_name, game_result = line.strip().split(":")
        print(game_name)
        game_id = int(game_name.split()[1])
        #_, game_id = game_name.split()
        # _ underscore for variables we don't want to use / keep
        # print(game_id)
        # print(game_result)
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

        if red_count <= 12 and green_count <= 13 and blue_count <= 14:
            possible_games.append(game_id)
            print(game_id)

        if red_count > 12 or green_count > 13 or blue_count > 14:
            impossible_games.append(game_id)
            print(game_id)

print("possible games:")
print(possible_games)
print("impossible games:")
print(impossible_games)

sum_possible_games = sum(possible_games)
print("sum_possible_games:", sum_possible_games)

sum_impossible_games = sum(impossible_games)
print("sum_impossible_games:", sum_impossible_games)

# pip3 install black
# pip3 install flake8
