import os

import csv

from collections import Counter

# Sets path to csv file
pathtofile = os.path.join('Resources', 'election_data.csv')
pathToOpen = os.path.join('analysis', 'Elections_Results.txt')

# opens election data and stores it in 'csvfile'
with open(pathtofile) as csvfile:
    
    reader = csv.DictReader(csvfile, delimiter=',')

    # create empyty list to store candidate occurences
    candidates = []

    # add those candidate occurences to list
    for row in reader:
        candidates += [row['Candidate']]

#  use counter to create dictionary of the number of times unique value appeared in list
candidateDict = Counter(candidates)

# test the above newly created dictionary with print
# print(candidateDict)

#  calcuates total votes by adding all the values from keys together in dictionary
totalVotes = sum(candidateDict.values())

#  pulls first key and the value associated and places them in variables
first_key = list(candidateDict)[0]
first_val = list(candidateDict.values()) [0]

#  pulls second key and the value associated and places them in variables
second_key = list(candidateDict)[1]
second_val = list(candidateDict.values()) [1]

#  pulls third key and the value associated and places them in variables
third_key = list(candidateDict)[2]
third_val = list(candidateDict.values()) [2]

#  calculate winner
winner = max(candidateDict, key = candidateDict.get)

# display results below
print(f'Total Votes: {totalVotes}')
print(f'{first_key}: {round(((first_val/totalVotes)*100),3)}% ({first_val})')
print(f'{second_key}: {round(((second_val/totalVotes)*100),3)}% ({second_val})')
print(f'{third_key}: {round(((third_val/totalVotes)*100),3)}% ({third_val})')
print(f'Winner: {winner}')


# write results to text file
with open (pathToOpen, 'w') as f:
    f.write('Election Results\n')
    f.write('----------------------------\n')
    f.write(f"Total Votes: {totalVotes}\n")
    f.write(f'{first_key}: {round(((first_val/totalVotes)*100),3)}% ({first_val})\n')
    f.write(f'{second_key}: {round(((second_val/totalVotes)*100),3)}% ({second_val})\n')
    f.write(f'{third_key}: {round(((third_val/totalVotes)*100),3)}% ({third_val})\n')
    f.write('----------------------------\n')
    f.write(f'Winner: {winner}\n')
    f.write('----------------------------\n')

                
        
        




# print(reader.count(row['Candidate']))