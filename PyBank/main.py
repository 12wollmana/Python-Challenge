# Import Dependencies
import os
import csv

# Function Definitions

# Reads the Budget CSV saved in the Resources folder.
# Returns a dictionary of statistics for the data
def readBudgetCSV(): 
    csvPath = os.path.join("Resources", "budget_data.csv")
    totalMonths = 0
    totalChange = 0
    totalAmount = 0
    greatestIncMonth = ""
    greatestIncProfit = 0
    greatestDecMonth = ""
    greatestDecProfit = 0
    isFirstRow = True
    lastAmount = 0

    with open(csvPath) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=",")

        csvHeader = next(csvReader) # Store off the header row
        for row in csvReader:
            date = str(row[0])
            amount = float(row[1])

            totalMonths = totalMonths + 1
            totalAmount = totalAmount + amount

            change = amount - lastAmount
            if(not isFirstRow): # Don't want to do this on the first row
                totalChange = totalChange + change
                if((change > 0) and (change > greatestIncProfit)):
                    greatestIncMonth = date
                    greatestIncProfit = change

                if((change < 0) and (change < greatestDecProfit)):
                    greatestDecMonth = date
                    greatestDecProfit = change
            
            lastAmount = amount
            isFirstRow = False
    
    print(f"Total Change: {totalChange}")
    # Save to a dictionary to pass off data easier 
    # (an object/class might be better, but we haven't covered them yet)
    budgetData = {
        "Months" : totalMonths,
        "Total" : totalAmount,
        "Average" : totalChange / (totalMonths - 1),
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

    # Create a loopable list to print out to file and terminal
    analysis = [
        "Financial Analysis",
        "----------------------------",
        f"Total Months: {months}",
        f"Total: ${round(total)}",
        f"Average Change: ${round(average,2)}",
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
