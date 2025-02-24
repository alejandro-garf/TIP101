def calculate_tip(bill, service_quality):
    if service_quality == "poor":
        tip = bill * .10
    elif service_quality == "average":
        tip = bill * .15
    elif service_quality == "good":
        tip = bill * .17
    elif service_quality == "excellent":
        tip = bill * .20
    else:
        return None
    return tip

tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)
