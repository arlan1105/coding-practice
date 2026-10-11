def launch_fuel(payload):
    fuel = payload / 5
    total = payload+fuel
    add_fuel = 1

    while add_fuel >= 1:
        prev_fuel = fuel
        fuel = total / 5
        add_fuel = fuel - prev_fuel
        total += add_fuel

    return round(fuel, 1)
        
print(launch_fuel(243))