# Budget Calculator

def calculate_budget():
    # User input
  income = float(input("Enter your monthly income: $"))
  rent = float(input("Enter rent expense: $"))
  food = float(input("Enter food expense: $"))
  entertainment = float(input("Enter entertainment expense: $"))

    #Calculations
  total_expenses = rent + food + entertainment
  remaining = income - total_expenses

    # Advice
  if remaining < 0:
      advice = "You're overspending! Get it together."
  elif remaining < 100:
      advice = "Your budget is tight. Cup noodles it is."
  else:
      advice = "Great job! You have money left over turn up."

    # Summary
  print("\n=== BUDGET SUMMARY ===")
  print(f"Monthly Income: ${income:.2f}")
  print(f"Total Expenses: ${total_expenses:.2f}")
  print(f"Remaining Money: ${remaining:.2f}")
  print(f"\nBudget Advice: {advice}")


# Call function
calculate_budget()
