g,s,c = [int(x) for x in input().split()]

province_cost = 8
duchy_cost = 5
estate_cost = 2

gold_cost = 6
silver_cost = 3
copper_cost = 0

gold_value = 3
silver_value = 2
copper_value = 1

total_buy_power = g * gold_value + s * silver_value + c * copper_value

best_treasure_card = ""
if total_buy_power >= gold_cost:
    best_treasure_card = "Gold"
elif total_buy_power >= silver_cost:
    best_treasure_card = "Silver"
elif total_buy_power >= copper_cost:
    best_treasure_card = "Copper"

best_victory_card = ""
if total_buy_power >= province_cost:
    best_victory_card = "Province"
elif total_buy_power >= duchy_cost:
    best_victory_card = "Duchy"
elif total_buy_power >= estate_cost:
    best_victory_card = "Estate"

if best_victory_card != "":
    print(best_victory_card + " or " + best_treasure_card)
else:
    print(best_treasure_card)
