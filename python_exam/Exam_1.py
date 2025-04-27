def main():

    all_numbers = []
    even_numbers = []
    odd_numbers = []
    i = 0

    print("Enter numbers one by one. Enter 0 as long as to stop.")
    while True:
        if i >= 5:
            break
        try:
            num = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if num == 0 :
            break
        all_numbers.append(num)
        if num % 2 != 0:
            odd_numbers.append(num)          
        else:
            even_numbers.append(num) 
            
        i += 1 

    if len(all_numbers) == 0:
        print("The average cannot be calculated!")
        return

    sum_all = sum(all_numbers)
    sum_even = sum(even_numbers)
    sum_odd = sum(odd_numbers)
    average = sum_all / len(all_numbers)

    print("\n--- Results ---")
    print(f"Sum of all numbers: {sum_all}")
    print(f"Sum of even numbers: {sum_even}")
    print(f"Sum of odd numbers: {sum_odd}")
    print(f"Average of all numbers: {average:.2f}")


if __name__ == "__main__":
    main()