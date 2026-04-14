import json
import matplotlib.pyplot as plt

try:
    with open("expenses.json","r") as file:
        expenses=json.load(file)
except:
    expenses=[]

while True:
    print("\n===Expense Tracker===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Monthly Summary")
    print("4. Category Breakdown")
    print("5. Highest spending category")
    print("6. EXIT")

    choice=int(input("Enter choice: "))

    # ADD EXPENSE
    if choice == 1:
        date=input("Enter date:")
        category=input("Enter category: ")
        amount= float(input("Enter amount: "))
        description= input("Enter description: ")

        expense={
            "date":date,
            "category" : category,
            "amount" : amount,
            "description" : description
        }

        expenses.append(expense)

    # SAVE TO JSON
        with open("expenses.json","w") as file:
            json.dump(expenses,file)
        print("Expenses added successfully")

    #VIEW EXPENSES

    elif choice==2:
        if not expenses:
            print("No expenses found")
        else:
            print("\n--------All Expenses-------")
            for e in expenses:
                print(f"{e['date']} | {e['category']} | Rs{e['amount']} | {e['description']}")
    
    #MONTHLY SUMMARY
    elif choice==3:
        month=input("Enter month:")
        total=0

        for e in expenses:
            if e["date"].startswith(month):
                total+=e["amount"]
        print(f"Total spending for {month} : Rs{total}")  

    #CATEGORY BREAKDOWN
    elif choice==4:
        summary={}

        for e in expenses:
            cat=e["category"]
            summary[cat]=summary.get(cat,0)+e["amount"]
        print("\n-----------Category Breakdown---------")
        for cat,amt in summary.items():
            print(f"{cat}: Rs{amt}")

    #PIE CHART
        labels=list(summary.keys())
        values=list(summary.values())

        plt.figure()
        plt.pie(values,labels=labels,autopct='%1.1f%%')
        plt.title("Expense Distribution")
        plt.show()

    #HIGHEST SPENT CATEGORY
    elif choice==5:
        summary={}

        for e in expenses:
            cat=e["category"]
            summary[cat]=summary.get(cat,0) + e["amount"]

        if summary:
            highest=max(summary,key=summary.get)
            print(f"Highest spending category: {highest} (Rs{summary[highest]})")
        else:
            print("No data available")

        
    #EXIT
    elif choice==6:
        print("Exiting...")
        break

    else:
        print("INVALID CHOICE")
