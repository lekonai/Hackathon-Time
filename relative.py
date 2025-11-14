def rel (boat_div_deg, w_from):
    raw = abs(boat_div_deg - w_from)
    return min(raw, 360 - raw)

print(rel(270, 60))