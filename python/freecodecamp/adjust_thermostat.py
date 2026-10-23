def adjust_thermostat(current_f, target_c):     
    current_c = (current_f-32)*5/9     
    diff = round((target_c - current_c)*1.8, 2)      
    if diff == 0: return 'Hold'     
    elif diff > 0: return f"Heat: {diff} degrees Fahrenheit"     
    else: return f"Cool: {abs(diff)} degrees Fahrenheit"  

print(adjust_thermostat(32, 0))
print(adjust_thermostat(72, 18))