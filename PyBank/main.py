# Import Dependencies
import os
import csv

# Function Definitions

# Reads the Budget CSV saved in the Resources folder.
# Returns a dictionary of statistics for the data
def readBudgetCSV(): 
    csvPath = os.path.join("Resources", "budget_data.csv")
    totalMonths = 0
    totalNet = 0
    totalAmount = 0
    greatestIncMonth = ""
    greatestIncProfit = 0
    greatestDecMonth = ""
    greatestDecProfit = 0

    with open(csvPath) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=",")

        csvHeader = next(csvReader)
        for row in csvReader:
            date = str(row[0])
            amount = float(row[1])

            totalMonths = totalMonths + 1
            totalAmount = totalAmount + amount
            totalNet = totalAmount + abs(amount)

            if((amount > 0) and (amount > greatestIncProfit)):
                greatestIncMonth = date
                greatestIncProfit = amount

            if((amount < 0) and (amount < greatestDecProfit)):
                greatestDecMonth = date
                greatestDecProfit = amount

    budgetData = {
        "Months" : totalMonths,
        "Total" : totalNet,
        "Average" : totalAmount / totalMonths,
        "IncMonth" : greatestIncMonth,
        "IncProfit" : greatestIncProfit,
        "DecMonth" : greatestDecMonth,
        "DecProfit" : greatestDecProfit
    }
    return budgetData

# Creates a list of printable strings for the budget statistics 
# created in readBudgetCSV.
def getAnalysis(budgetData):
    months = budgetData["Months"]
    total = budgetData["Total"]
    average = budgetData["Average"]
    incMonth = budgetData["IncMonth"]
    incProfit = budgetData["IncProfit"]
    decMonth = budgetData["DecMonth"]
    decProfit = budgetData["DecProfit"]

    analysis = [
        "Financial Analysis",
        "----------------------------",
        f"Total Months: {months}",
        f"Total: ${round(total)}",
        f"Average Change: ${round(average)}",
        f"Greatest Increase in Profits: {incMonth} (${round(incProfit)})",
        f"Greatest Decrease in Profits: {decMonth} (${round(decProfit)})"
    ]

    return analysis

# Prints the analysis from getAnalysis to the terminal
def printAnalysis(analysis):
    for line in analysis:
        print(line)
    return


# Saves the analysis from getAnalysis to a text file
# in the Analysis folder
def saveAnalysis(analysis):
    textPath = os.path.join("Analysis", "results.txt")
    with open(textPath, "w") as textFile:
        for line in analysis:
            textFile.write(line +"\n")
    return

# Actual Work
budgetData = readBudgetCSV()
analysis = getAnalysis(budgetData)
printAnalysis(analysis)
saveAnalysis(analysis)
