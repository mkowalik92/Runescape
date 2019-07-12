user_coal_amount = int(input("Coal: "))
user_gold_amount = int(input("Gold: "))
user_mith_amount = int(input("Mith: "))
user_addy_amount = int(input("Addy: "))
user_rune_amount = int(input("Rune: "))

per_coal_exp = 30
per_gold_exp = 60
per_mith_exp = 110
per_addy_exp = 170
per_rune_exp = 240

total_coal_exp = per_coal_exp * user_coal_amount
total_gold_exp = per_gold_exp * user_gold_amount
total_mith_exp = per_mith_exp * user_mith_amount
total_addy_exp = per_addy_exp * user_addy_amount
total_rune_exp = per_rune_exp * user_rune_amount

total_exp_with_pros = total_coal_exp + total_gold_exp + total_mith_exp + total_addy_exp + total_rune_exp

print(total_exp_with_pros * 1.025)
