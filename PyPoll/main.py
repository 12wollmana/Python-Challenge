# Import Dependencies
import os
import csv

# Function Definitions

# Reads through an election_data CSV file
# Returns a dictionary:
#   "Votes": a dictionary of votes - votes[<candidate>] = <count>
#   "Total Votes": The total number of votes
def readPollCSV():
    csvPath = os.path.join("Resources", "election_data.csv")
    totalVotes = 0
    votes = {}

    with open(csvPath) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=",")

        csvHeader = next(csvReader) # Store off the header row
        for row in csvReader:
            voterID = int(row[0])
            # county = str(row[1]) # Not needed
            candidate = str(row[2])
            if(candidate in votes):
                votes[candidate] = votes[candidate] + 1
            else:
                votes[candidate] = 1
            totalVotes = totalVotes + 1
        
        return {
            "Votes" : votes,
            "Total Votes" : totalVotes
        }

# Finds the winner of the votes
# Takes a dictionary of votes - votes[<candidate>] = <count>
def calcWinner(votes): 
    maxVotes = 0
    winner = ""
    for candidate, numVotes in votes.items():
        if numVotes > maxVotes:
            maxVotes = numVotes
            winner = candidate
            
    return winner

# Creates a list of printable strings for the polling
# dictionary created in readPollCSV.
def getAnalysis(data, winner):
    votes = data["Votes"]
    totalVotes = data["Total Votes"]

    analysis = [
        "Election Results",
        "-------------------------",
        f"Total Votes: {totalVotes}",
        "-------------------------",
    ]

    for candidate, numVotes in votes.items():
        percent = round(numVotes/totalVotes * 100, 3)
        analysis.append(f"{candidate}: {percent}% ({numVotes})")
    analysis.append("-------------------------")
    analysis.append(f"Winner: {winner}")
    analysis.append("-------------------------")

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
data = readPollCSV()
winner = calcWinner(data["Votes"])
analysis = getAnalysis(data, winner)
printAnalysis(analysis)
saveAnalysis(analysis)
