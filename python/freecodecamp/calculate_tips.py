def calculate_tips(meal_price, custom_tip):

    tips = float('.'.join(meal_price[1:].split()))
    arr = tips*.15, tips*.20, tips*int(custom_tip[:-1])/100

    return [f'${tip:.2f}' for tip in arr]
print(calculate_tips("$10.00", "25%"))