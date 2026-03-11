def well(x):
    g = x.count("good")
    if g > 2: return "I smell a series!"
    if g > 0: return "Publish!"
    return "Fail!"