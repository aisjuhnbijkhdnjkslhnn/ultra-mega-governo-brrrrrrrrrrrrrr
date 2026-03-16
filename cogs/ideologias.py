# Ideologia Selection Commands

def select_ideology(ideology):
    """Select an ideology and perform related actions."""
    if ideology == 'liberal':
        return 'You have selected Liberalism!'
    elif ideology == 'conservative':
        return 'You have selected Conservatism!'
    elif ideology == 'socialist':
        return 'You have selected Socialism!'
    else:
        return 'Unknown ideology selected.'