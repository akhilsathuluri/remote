def check_model(register_model):
    # Do template matching and decide resulting identified model as a number
    identified_model = 3
    if identified_model == register_model:
        return True, identified_model
    elif identified_model != register_model:
        return False, identified_model
    else:
        return 'ERROR', 0
