def verificarParam(param):
    if (param is None):
        return True
    if isinstance(param, str):
        return True
    
    return False

def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    
    contador = 0

    for period in permanence_period:
        if verificarParam(period[0]) or verificarParam(period[1]):
            return None
        
        if target_time >= period[0] and target_time <= period[1]:
            contador += 1

    return contador
