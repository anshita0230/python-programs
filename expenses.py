#expense tracker using generator and json
import json
import os
file_name="expense.json"

if os.path.exists(file_name):
    with open(file_name,"r")as f:
     expense=json.load(f)
else:
    expense=[]

while True:
    name=input("enter the name : ")
    note=input("enter the name of purchasing : ")
    amount=float(input("enter the amount : "))

    expense.append({"name":name,"note":note,"amount":amount})

    more=input("add another ? (y/n) : ").lower()
    if more!="y":
        break

with open(file_name,"w")as f:
    json.dump(expense,f,indent=4)
print("expenses saved", file_name)

def add_expense():
    name=input("enter the name : ")
    note=input("enter the name of purchasing : ")
    amount = float(input("Enter the amount: "))
    expense.append({"name": name, "note": note, "amount": amount})

def read_expense():
    with open(file_name,"r")as f:
        expenses=json.load(f)
        for exp in expense:
            yield exp
def list_expenses():
    for i,expense in enumerate(read_expense(),start=1):
        print(f"{i}.{expense['name']}-{expense['note']}-{expense['amount']}")

def filter_expenses(min_amount):
    for expense in read_expense():
        if expense["amount"]>=min_amount:
            print(f"{expense['name']}-{expense['amount']}")
while True:
    print("\n=== Expense Tracker ====")
    print("1.Add Expense ")
    print("2.List Expense ")
    print("3.Filter Expense ")
    print("4.Exit ")

    choice=input("enter choice: ")

    if choice=="1":
        add_expense()
    elif choice=="2":
        list_expenses()
    elif choice=="3":
        amount=float(input("enter the minimum amount to filter "))
        filter_expenses(amount)
    elif choice=="4":
        print("goodbye !")
        break
    else:
        print("invalid choice")

