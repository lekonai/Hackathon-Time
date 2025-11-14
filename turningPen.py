def turningPen(prev_dir_deg, new_dir_deg):
    if prev_dir_deg == None:
        return 0
    
    diff = abs(prev_dir_deg, new_dir_deg)
    diff = min(diff, 360 - diff)

    if diff == 0:
        return 0.0
    elif diff <= 10:
        return 0.5
    elif diff <= 20:
        return 1.0
    elif diff <= 30:
        return 1.5
    elif diff <= 40:
        return 2.0
    elif diff <= 50:
        return 2.5
    elif diff <= 60:
        return 3.0
    else:
        return 4.0
    

