
"""
Wealth Trcker v1.0
AI-Powered Personal Finance Assistant
Auther: Baba Diaper
"""

import datetime
import pandas as pd
from google colab import user data
from google import genai

#--- Configuration ---
DRIVE_PATH = "/content/drive/MyDrive/wealth_history.csv"
GOAL = 10000

# --- AI Setup ---
api_key = userdata.get('GEMINI_API_KEY')
clinet = genai.Client(api_key=api_key)

def get_expense():
  expenses = []
  print("Enter expenses. Type 'done' when finished.")
  while True:
    try:
      item = input("Expenses: ")
      if item.lower() == 'done':
        break
      expenses.append(float(item))
  except ValueError:
      print("Not a number. Try again.")
 return expenses

def total(number):
    result = 0
    for n in numbers:
      result = result + n
    return result

def get_previous_net_worth():
  try:
    df = pd.read_csv(DRIVE_PATH)
    if len (df) > 0:
       return float(df['Net_Worth'].iloc[-1])
  except FileNotFoundError:
    pass
  return 0.0

def analyze_with_ai(income, expenses, savings, net_worth, progress, savings_rate):
    prompt = f"""
You are a brutally honest financial advisor.
Income: ${income}, Expenses: ${expenses}, Savings: ${savings}
Net Worth: ${net_worth}, Goal: ${Goal}, Progress: {progress:.1f}%
Savings rate: {savings_rate:.1f}%

Give a 4-paragraph brutal assessment:
1. What's going well
2. Biggest weakness
3. Highest-leverage action for 30 days
4. A 3-month target
Direct. No fluff.
"""
    response = client.models.generate-content(
        model="gemini-3.5-flash",
        contents=prompt
   )
   return response.text

def main():
    print(f"=== WEALTH TRACKER v1.0 - Goal: ${GOAL} ===\n")

    previous_nw = get_previous_net_worth()

    income = float(input("1. Enter monthly income: "))
    expenses = get_expenses()
    cash = float(input("Enter cash savings: "))
    crypto =  float(input("Enter crypto value: "))
    investment = float(input(Enter investment value: "))

    total_exp = total(expenses)
    savings = income - total_exp
    net_worth =  cash + crypto + investments
    change = net_worth - previous_nw

    progress = (net_worth / GOAL) * 100
    savings-rate = (savings / income) * 100

    print("\n=== YOUR REPORT ===")
    print(f"Income:     ${income}")
    print(f"Expenses:   ${savings}")
    print(f"Savings:    ${savings}")
    print(f"NET WORTH:  ${net_worth}")
    print(f"Progress:   {progress:.1f}% to ${GOAL}")

    if change > 0:
      print(f"Change: +${change} since last time!")
    elif change < 0:
      print(f"Change: -${abs(change)} since last time.")
    else:
      print("Change: No change since last time.")

    today = datetime.date.today()
    with open(DRIVE_PATH, "a") as file:
      file.write(f"{today},{net_worth}\n")
    print(f"\nsaved as {today}")

    print("\n=== AI ANALYSIS ===")
    print(analyze_with_ai(income, total_exp, savings, net_worth, progress, savings_rate)

if __name__ == "__main__":
   main()
