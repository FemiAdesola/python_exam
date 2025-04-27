
# 🏃 Catch-Up Distance Calculator

A simple Python script that calculates how much further an owner must travel to catch a thief, based on the thief's head start, the owner's current distance, and the remaining gap between them.

## 📘 Description
A car was stolen. Luckily the owner catches it and begins to chase the thief after the thief had already gone x km. After the owner traveled y km, he learned that the thief was still z km ahead. After how many more km did the owner catch up to the thief? 
Make a python code which reads from the user the x, y and z.  
Then solve the problem with python code. Make a function which writes the result in the result.txt file.

With the x=43, y=152 and z=25 the result is 211,1 

## 📘 Evaluation

This tool helps determine the remaining distance an owner must cover to catch a thief using a mathematical formula. The result is displayed in the console and saved to a file called `result.txt`.

## 🧮 Formula

```
distance_needed = (owner_distance * remaining_gap) / (thief_head_start - remaining_gap)
```

Where:
- `thief_head_start` (x): Initial lead the thief has (in km)
- `owner_distance` (y): Distance the owner has already traveled (in km)
- `remaining_gap` (z): Distance still separating the owner and thief (in km)

⚠️ The formula is invalid when `x == z`, as it would result in division by zero. The script handles this case with an error message.

## 🗂️ Files

- `main()`: Collects user input and controls the workflow.
- `compute_catch_up_distance(x, y, z)`: Core function to calculate the distance.
- `save_result_to_file(result, filename="result.txt")`: Saves the result to a text file.

## 🚀 How to Run

1. Make sure you have Python installed (Python 3 recommended).
2. Save the script to a `.py` file.
3. Run it using:

```bash
python your_script_name.py
```

4. Enter the required inputs when prompted.

## 🖥️ Example

```
Inputs from user:
Thief's head start (x): 43.0 km
Owner's distance traveled (y): 251.0 km
Thief still ahead by (z): 25.0 km

Result:
Owner will catch the thief after traveling 348.6 km more.
```

The result will also be saved in `result.txt`.

## ❗ Error Handling

- Raises a `ValueError` if the inputs cause a division by zero (`x == z`).
- Input must be numerical (float-compatible).

## 📄 Output

The output is written in the format:
```
Owner will catch the thief after traveling X km more.
```


---

# ➕ Number Analyzer

This Python script collects up to 5 numbers (or until the user enters 0), categorizes them into even and odd, and computes:

- Sum of all numbers
- Sum of even numbers
- Sum of odd numbers
- Average of all numbers

## ▶️ How It Works

1. The user is prompted to enter numbers one by one.
2. Input stops when either:
   - The user has entered 5 numbers
   - The user enters 0
3. The script then calculates and displays the results.

## ⚠️ Notes

- If no valid number is entered, the program will notify the user that the average cannot be calculated.
- Input validation ensures only integers are accepted.

## 📋 Example Output

```
Enter numbers one by one. Enter 0 as long as to stop.
Enter a number: 3
Enter a number: 8
Enter a number: 5
Enter a number: 4
Enter a number: 2

--- Results ---
Sum of all numbers: 22
Sum of even numbers: 14
Sum of odd numbers: 8
Average of all numbers: 4.40
```

---

# File Structure
## 📂 File Structure

```
python_exam/
│   ├── Exam_1.py   # Main script in Exam_1
│   ├── Exam_1.md   # Question in exam 2
│   ├── Exam_2.py         # OMain script in Exam_2
│   ├── Exam_2B.py   # Main script in Exam_2B
│   ├── result_Exam_2.txt   # Output report Exam_2
│   └── result_Exam_2B.txt        # Output report Exam_2B
│ 
└──  README.md    # Description
```

## 📌 License

This project is for educational purposes and does not include a specific license.

## 👨‍💻 Author

Developed as part of a programming exercise involving input handling, arithmetic operations, and file writing in Python.