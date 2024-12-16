
```markdown
# Pizza Ordering System

Welcome to the **Pizza Ordering System**! This is a Python-based program that allows you to order a pizza by selecting the size, adding toppings like pepperoni and extra cheese, and calculates the final bill. It's a simple console application that offers an easy way to practice user input handling and conditional logic in Python.

## Features

- **Pizza Size Selection**: Choose from three available sizes (Small, Medium, Large).
- **Toppings**: Optionally add pepperoni and/or extra cheese to your pizza.
- **Order Summary**: The system provides a detailed summary of your order, including the pizza size, selected toppings, and the final bill.
- **Input Validation**: Ensures valid input for pizza size, pepperoni, and cheese options.

## Requirements

- Python 3.x or higher is required to run the program.
  
## Installation

1. **Clone the repository** to your local machine:

   ```bash
   git clone https://github.com/AyushTIW30/Pizza_Bill/blob/main/Pizza_Bill.py
   ```

 

2. **Navigate to the project folder**:

   ```bash
   cd Pizza_Bill
   ```

3. **Run the program**:

   ```bash
   python Pizza_Bill.py
   ```

   If you are using a Python environment or IDE, open the `pizza_ordering.py` file and run it directly.

## How It Works

### 1. **Pizza Size Selection**:
   The program will prompt you to choose your pizza size:
   - **Small** ($15)
   - **Medium** ($20)
   - **Large** ($25)

   It will validate your choice to ensure that you enter either `S`, `M`, or `L`.

### 2. **Toppings Options**:
   The program will ask you if you want to add **pepperoni** or **extra cheese** to your pizza.
   - **Pepperoni**: Adds $2 to the total bill.
   - **Extra Cheese**: Adds $4 to the total bill.

   It will validate your input to ensure you enter `Y` for Yes or `N` for No.

### 3. **Order Summary**:
   After gathering all the necessary inputs, the program will display an order summary:
   - The pizza size chosen and its base price.
   - The cost for adding pepperoni (if selected).
   - The cost for adding extra cheese (if selected).
   - The **final bill** showing the total cost of your pizza.

### Example Interaction:

```
Welcome to the Pizza Ordering System!
=========================================
Please choose your pizza size:
[S] Small ($15)
[M] Medium ($20)
[L] Large ($25)
Your choice (S, M, L): M

Would you like to add pepperoni? (Y/N): Y

Would you like extra cheese? (Y/N): N

==================== ORDER SUMMARY ====================
Pizza Size: M - $20
Add Pepperoni: Yes - $2
Add Extra Cheese: No - $0

=======================================================
Your final bill is: $22

Thank you for ordering! Enjoy your pizza!
=======================================================
```

### 4. **Input Validation**:
   The program includes input validation to ensure users only enter valid responses for pizza size, pepperoni, and cheese choices. If an invalid input is provided (e.g., entering something other than `S`, `M`, `L` for pizza size), it will prompt the user to try again.

## Code Explanation

1. **Pizza Size Selection**: 
   The user is prompted to select a pizza size. The program validates the input to ensure it's one of the allowed options (`S`, `M`, `L`).

2. **Pepperoni Option**:
   After selecting the pizza size, the program asks whether the user wants to add pepperoni. If the user enters `Y`, $2 is added to the bill; otherwise, the price remains unchanged.

3. **Extra Cheese Option**:
   Similarly, the user is asked if they want extra cheese. If they choose `Y`, $4 is added to the total bill.

4. **Calculating and Displaying the Bill**:
   Based on the user's choices, the program calculates the total cost. It then displays a detailed order summary, including the pizza size, any additional toppings, and the final bill.

5. **Order Summary**:
   The order summary includes:
   - The pizza size and its base price.
   - The cost of any selected toppings (pepperoni and extra cheese).
   - The final total.

## Author

Created by **AyushTIW30**.

## Contributions

Feel free to fork the repository, open issues, and submit pull requests if you'd like to contribute to the project!

```
