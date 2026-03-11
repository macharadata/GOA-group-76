def maskify(cc):
    
    if len(cc) <= 4:
        return cc
    
    masked_part = "#" * (len(cc) - 4)
    visible_part = cc[-4:]
    
    return masked_part + visible_part