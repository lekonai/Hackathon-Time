def turningPen(prev_dir_deg, new_dir_deg):
    if prev_dir_deg == None:
        return 0
    
    diff = abs(prev_dir_deg - new_dir_deg)
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

def baseTime(bHeading, wSpeed, wDir, cAngle, fAngle):
    wFrom = (wDir+180)%360
    delta = abs((bHeading - wFrom))
    rel = min(delta, 360 - delta)
    sFactor =  0
    if rel >= 30 and rel < 60:
        sFactor = 1
    elif rel >= 60 and rel < 90:
        sFactor = 0.95
    elif rel >= 90 and rel < 135:
        sFactor = 0.85
    elif rel >= 135 and rel < 180:
        sFactor = 0.7
    else:               
        sFactor = 0
    bSpeed = wSpeed * sFactor
    tp = turningPen(cAngle, fAngle)

    return 10/(wSpeed*sFactor)+ tp



