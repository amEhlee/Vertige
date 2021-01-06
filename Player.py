class Player(Avatar):
    # initalize player variables
    player_health = 100  # store player health
    inventory = []  # store player inventory

    #variables used for player attacking and possible items
    
    # initalize possible weapons each weapon has an array with min, max attack values
    wrench = [5.0, 8.0]  # main weapon has attack range of 0.1 to 5
    heat_ray = [0.1, 10]  # was going to be used as alternative stronger weapon ran out of time
    punch = [0.1, 5.0]  # default weapon

    # set the current weapon to use in this case player starts unarmed
    weapon = punch  # current weapon in use
