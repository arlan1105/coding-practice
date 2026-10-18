EXPECTED_BAKE_TIME = 40

def bake_time_remaining(n=30):
    '''Calculate the elapsed cooking time.'''
    return EXPECTED_BAKE_TIME-n
    
def preparation_time_in_minutes(number_of_layers):
    '''Parameters:
        number_of_layers (int): The number of layers in the lasagna.'''
    return number_of_layers*2
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.

        Returns:
        int: The total time elapsed (in minutes) preparing and baking.
        
        This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).'''
    return (number_of_layers*2)+elapsed_bake_time
    

 