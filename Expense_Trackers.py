from ex import Expense
import calendar
import datetime


def main():
    budget = 20000
    print("Hello, World! 🌍")
    print("Program Running 🏃")
     
    
    print("\n")

    #1
    expense = get_expense_details()

    #2
    expense_file_path = "ExpenseTracker/expense.csv"
    save_to_file(expense, expense_file_path)

    #3
    summarize_expense(budget, expense_file_path)


#1
def get_expense_details():
    #a
    expense_name = input("What is the name of the expense? ")
    #b
    expense_amount = float(input("How much was the expense? "))

    print(f"Expense name is {expense_name} and the expense amount is {expense_amount}")

    expense_categories = [
        "🏡 Home",
        "💼 Work",
        "👕 Apparel",
        "🚇 Transport",
        "🍜 Food",
        "🎉 Fun",
        "✨ Misc",
    ]

    while True:
        print("Which category does this expense fall into?")

        for i, category_name in enumerate(expense_categories):
            print(f"{i+1}. {category_name}")
        
        value_range = f"[1-{len(expense_categories)}]"

        #c
        selected_index = int(input(f"Select Category :: {value_range} ")) - 1  # -1 because list starts from index 0 and options are printed from 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]

            print(f"Selected category: {selected_category}")
            
            #object
            new_expense = Expense(name=expense_name, amount=expense_amount, category=selected_category)
            return new_expense

        else:
            print("Invalid category selected")    

        break



#2
def save_to_file(expense: Expense, expense_file_path: str):
    try:
        with open(expense_file_path, "a", encoding="utf-8") as f:
            f.write(f"{expense.name},{expense.amount},{expense.category}\n")

        print("\n")
        print(f"{expense} saved to {expense_file_path}")


    except Exception as e:
        print(f"An error occurred: {e}")



#3
def summarize_expense(budget, expense_file_path):
    print("\nSummary of user expenses:")
    try:
        with open(expense_file_path, "r", encoding="utf-8") as f:
            ExpenseList = []

            lines = f.readlines()
            for line in lines:
                line = line.strip()  # Remove any leading/trailing whitespace or newlines
                if line:  # Check if the line is not empty

                    try:
                        expense_name, expense_amount, expense_category = line.split(",")
                        print(f"{expense_name} {expense_amount} {expense_category}")

                        # use class 
                        line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
                        ExpenseList.append(line_expense)  # Append object

                    except ValueError:
                        print(f"Skipping invalid line: {line}")


        # Dictionary 
        amount_by_category = {}
        for curr_expense in ExpenseList:
            key = curr_expense.category

            if key in amount_by_category:
                amount_by_category[key] += curr_expense.amount
            else:
                amount_by_category[key] = curr_expense.amount


        # Expenditure based on category 
        print("\nExpense by Category:")
        for key, amount in amount_by_category.items():
            print(f"{key}: {amount:.2f}")
        

        # Total & Remaining Expenditure 
        total_spent = sum(x.amount for x in ExpenseList)
        print(f"\nTotal spent: {total_spent:.2f}")

        remaining_budget = budget - total_spent
        print(f"Remaining Budget: {remaining_budget:.2f}")



        # Calculate daily budget
        today = datetime.datetime.now()
        _, days_in_month = calendar.monthrange(today.year, today.month)
        remaining_days = days_in_month - today.day

        if remaining_days > 0:
            print(f"Remaining Days in Month: {remaining_days}")
            daily_budget = remaining_budget / remaining_days

            formatted_text = f"Daily Budget: {daily_budget:.2f}"
            print(red(formatted_text))
        else:
            print("No days remaining in the month.")

        

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


def red(*texts):
    combined_text = ' '.join(map(str, texts))
    return f"\033[91m{combined_text}\033[0m"


if __name__ == "__main__":
    main()
