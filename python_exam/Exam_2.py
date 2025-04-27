# This program calculates the distance a thief has traveled before being caught by the owner.
# The owner is 43km away from the thief, and the owner has traveled 152km.
# The thief is 25km ahead of the owner.
def calculate_distance(x,y,z):
    thief_distance_covered = x - z
    theif_pace = y*z
    distance_when_catched = theif_pace/thief_distance_covered
    return round(distance_when_catched, 1)

def result_to_file(x,y,z, result):
    with open("result_Exam_2.txt", "w") as file:
        file.write("Inputs from user:\n")
        file.write(f"Thief's head start (x): {x} km\n")
        file.write(f"Owner's distance traveled (y): {y} km\n")
        file.write(f"Thief still ahead by (z): {z} km\n\n")
        file.write(f"Result:\nOwner will catch the thief after traveling {result} km more.")

def main():
        x = float(input("Enter the distance thief had already gone (x): "))
        y = float(input("Enter the distance owner had traveled (y): "))
        z = float(input("Enter how far ahead the thief still is (z): "))

        calculated_distance = calculate_distance(x, y, z)
        result_to_file( x, y, z, calculated_distance)
if __name__ == "__main__":
  main()
