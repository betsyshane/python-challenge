#importing 
import os
import csv

# defining the folder path
electioncsv = os.path.join("../Resources", "election_data.csv")

# opening the CSV
with open(electioncsv,newline="") as csvFile:
    csvreader = csv.reader(csvFile,delimiter = ",")
    # skip the headers
    csv_headers = next(csvreader)
    #defining variables
    totalvotes = 0
    votes = []
    candidatelist = []
    candidatecountsdict = {}
    candidatecounts = []
    count = 0
    candidatepercentsdict = {}
    candidatepercents = []
    percent = 0

    #The total number of votes cast
    #each line is a unique vote
    for row in csvreader:
        totalvotes += 1
        votes.append(row[2])
    #print(totalvotes)

    #A complete list of candidates who received votes
    for candidate in votes:
        if candidate not in candidatelist:
            candidatelist.append(candidate)
    #testing print(candidatelist)

    #The total number of votes each candidate won
    for candidate in candidatelist:
        count = 0
        for vote in votes:
            if candidate == vote:
                count += 1
        candidatecountsdict[candidate] = count
        candidatecounts.append(count)
    # testing print(candidatecounts)

   

    for name in candidatelist:
        percent = round(float((candidatecountsdict[name]) / float(totalvotes)) * 100,3)
        candidatepercentsdict[name] = percent
        #I ended up adding regular lists too because I wasn't sure how to do a max from a dict
        candidatepercents.append(percent)
    # testing print(candidatepercents)
    #The percentage of votes each candidate won
    
    #The winner of the election based on popular vote.
    winner = candidatelist[candidatecounts.index(max(candidatecounts))]
    #testing print(winner)



    # def candidateoutput(x): 
    #     for i in x:
    #          print(f"{i}: {candidatepercentsdict[i]}% ({candidatecountsdict[i]})")
            

    # results = print(candidateoutput(candidatelist))
    
    def output():
        print(f"""
    Election Results
    -------------------------
    Total Votes: {totalvotes}
    -------------------------""")
        for i in candidatelist:
            print(f"    {i}: {candidatepercentsdict[i]}% ({candidatecountsdict[i]})")
        print(f"""    -------------------------
    Winner: {winner}
    -------------------------""")

    output()

    # COULD NOT GET THIS TO WORK FOR WHATEVER REASON
        # output = f"""
        # Election Results
        # -------------------------
        # Total Votes: {totalvotes}
        # -------------------------
        # {results}
        # -------------------------
        # Winner: {winner}
        # -------------------------"""

    # results = output()


    output = f"""
        Election Results
        -------------------------
        Total Votes: {totalvotes}
        -------------------------
        {candidatelist[0]}: {candidatepercents[0]}% ({candidatecounts[0]})
        {candidatelist[1]}: {candidatepercents[1]}% ({candidatecounts[1]})
        {candidatelist[2]}: {candidatepercents[2]}% ({candidatecounts[2]})
        {candidatelist[3]}: {candidatepercents[3]}% ({candidatecounts[3]})
        -------------------------
        Winner: {winner}
        -------------------------"""

    # results = output()

    # print(results)


    # with open("Output.txt", "w") as text_file:
    #     print(output,file=text_file)

    with open("Output.txt", "w") as text_file:
        print(output, file=text_file)