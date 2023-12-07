file_path = "/Users/ameliem/coding/portfolio/AdventOfCode/input/Input-Day04.txt"

points_per_card = []
result_list = []

with open(file_path) as input_file:
    for line in input_file:
        _, card_values = line.strip().split(":")

        winning_numbers, card_numbers = card_values.strip().split("|")

        card_numbers_list = card_numbers.strip().split(" ")
        while "" in card_numbers_list:
            card_numbers_list.remove("")
        s_card_numbers_list = sorted(card_numbers_list)

        winning_numbers_list = winning_numbers.strip().split(" ")
        while "" in winning_numbers_list:
            winning_numbers_list.remove("")
        s_winning_numbers_list = sorted(winning_numbers_list)

        card_points = 0

        for num in s_card_numbers_list:
            if num in s_winning_numbers_list:
                card_points += 1

        if card_points != 0:
            points_per_card.append(card_points)
            print(points_per_card)

            result_list.append(2 ** (card_points - 1))
            print(result_list)

solution = sum(result_list)
print("Solution: ", solution)