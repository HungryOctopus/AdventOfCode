import csv;
from csv import reader;

file_path = '/Users/ameliem/coding/portfolio/AdventOfCode/input/Input-Day02.csv'
# Open the CSV file for reading
with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')

        
# Initialize a list to store the sums of first and last digits
    possible_games = []
    impossible_games = []
    game_id = 0

    for row in reader:
        game_id += 1 
        print(game_id)
        for item in row:
            #Clean the rows from the semicolons
            cleaned_row = [item.replace(';',',')]

            #Split game number from results
            splitted_row = cleaned_row[0].split(':')
            #print(splitted_row)
            game_nr = splitted_row[0].strip()
            #print(game_nr)
            
            # Initialize counters for red, green, and blue
            
            red_count = 0
            green_count = 0
            blue_count = 0

            result_per_game = splitted_row[1].replace('"','').strip()
            array_result_per_game = result_per_game.split(', ')
            print(array_result_per_game)
            
            for result_item in array_result_per_game:    
                if 'red' in result_item:
                   red_count += int(result_item.replace(' red',''))
                if 'green' in result_item:
                   green_count += int(result_item.replace(' green',''))
                if 'blue' in result_item:
                   blue_count += int(result_item.replace(' blue',''))
                    #print(red_count)
            print(red_count, green_count, blue_count)

            if red_count <= 12 and green_count <= 13 and blue_count <= 14:
                possible_games.append(game_id)
                print(game_id)

            if red_count > 12 or green_count > 13 or blue_count > 14:
                impossible_games.append(game_id)
                print(game_id)

    # Calculate the sum of possible game IDs
    print(possible_games)
    sum_possible_games = sum(possible_games)
    print(sum_possible_games)
    print(impossible_games)
    sum_impossible_games = sum(impossible_games)
    print(sum_impossible_games)