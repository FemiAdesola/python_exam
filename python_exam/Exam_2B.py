def compute_catch_up_distance(thief_head_start, owner_distance, remaining_gap):

    # Calculate how many more kilometers the owner needs to travel to catch the thief.
    
    # Formula: d = (y * z) / (x - z)
    # Where:
    #     x = thief_head_start (km head start before chase begins)
    #     y = owner_distance (km owner has already traveled)
    #     z = remaining_gap (how far ahead the thief still is)
  
    if thief_head_start == remaining_gap:
        raise ValueError("Invalid input: Division by zero (x - z = 0).")

    distance_needed = (owner_distance * remaining_gap) / (thief_head_start - remaining_gap)
    return round(distance_needed, 1)

def save_result_to_file(x,y,z, result):
    with open("result_Exam_2B.txt", "w") as file:
        file.write("Inputs from user:\n")
        file.write(f"Thief's head start (x): {x} km\n")
        file.write(f"Owner's distance traveled (y): {y} km\n")
        file.write(f"Thief still ahead by (z): {z} km\n\n")
        file.write(f"Result:\nOwner will catch the thief after traveling {result} km more.")

def main():
    try:
        x = float(input("Thief's head start before chase (x in km): "))
        y = float(input("Distance owner has traveled (y in km): "))
        z = float(input("Distance thief is still ahead (z in km): "))

        calculated_distance = compute_catch_up_distance(x, y, z)
        print(f"Owner will catch the thief after traveling {calculated_distance} km more.")
        save_result_to_file(x,y,z, calculated_distance)

    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
