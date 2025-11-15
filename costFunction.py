
def costFunction(newHeading, boatHeading, windFrom):
   
    #newHeading is the new angle you want the boat to be heading at
    #boatHeading is the angle you want the boat to be heading at
    #windForm is the windDirectionAngle + 180 (mod 360)

    move = True
    localWindSpeed = 30
    boatSpeed = 0
    speedFactor = 0
    turnPenalty = 0
    changeInHeading = abs(newHeading - boatHeading)
    baseTime = 10 
    actualAngle = abs(boatHeading - windFrom)

    attackAngle = min(actualAngle, 360 - actualAngle)

    if actualAngle < 30:
        move = False
        return "error"
    else:
        if 30 <= attackAngle < 60 :
            speedFactor = 1
        elif 60 <= attackAngle < 90 :
            speedFactor = 0.95
        elif 90 <= attackAngle < 135 :
            speedFactor = 0.85
        elif 135 <= attackAngle < 180 :
            speedFactor = 0.7
        else:
            speedFactor = 0
    
    boatSpeed = localWindSpeed * speedFactor

    changeInHeading = min(changeInHeading, 360 - changeInHeading)

    if changeInHeading == 0:
        timePenalty = 0
    if 0 < changeInHeading <= 10:
        timePenalty = 0.5
    if 10 < changeInHeading <= 20 :
        timePenalty = 1
    if 20 < changeInHeading <= 30:
        timePenalty = 1.5
    if 30 < changeInHeading <= 40:
        timePenalty = 2
    if 40 < changeInHeading <= 50:
        timePenalty = 2.5
    if 50 < changeInHeading < 60:
        timePenalty = 3
    if timePenalty >= 60 : 
        timePenalty = 4
    

    timeForEachMove = (baseTime/boatSpeed) + timePenalty

    return timeForEachMove

cost = costFunction(90,120,50)

if cost != "error":
    print(f'cost is: {cost}' )
else:
    print("error")
