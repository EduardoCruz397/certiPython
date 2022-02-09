def grosspay(hours=40, rate=25, pieces=0, piecerate=0,salary=0):
    overtime = 0
    if pieces > 0:
        return pieces * piecerate
    if salary > 0:
        pass
    if hours > 40:
        overtime = (hours- 40) * (1.5 * rate)
        return overtime + (40 * rate)

print(grosspay(pieces=500, piecerate=4))