
def find_breaking_floor(floors, breaking_floor):
    first_egg_drops = 0
    step = 1

    while step * (step + 1) // 2 < floors:
        step += 1

    current_floor = step
    previous_floor = 0
    attempts = 0

    while current_floor <= floors:
        attempts += 1

        if current_floor >= breaking_floor:
            break

        previous_floor = current_floor
        step -= 1
        current_floor += step

    for floor in range(previous_floor + 1, current_floor):
        attempts += 1

        if floor >= breaking_floor:
            return floor, attempts

    return current_floor, attempts


floors = 100
breaking_floor = 73

floor, attempts = find_breaking_floor(floors, breaking_floor)

print("Lowest breaking floor:", floor)
print("Number of attempts:", attempts)
