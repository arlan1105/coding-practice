def validate_pin(pin):
    return True if (len(pin) == 6 or len(pin) == 4) and pin.isdigit() else False 