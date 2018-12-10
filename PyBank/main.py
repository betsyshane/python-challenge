#importing 
import os
import csv

# defining the folder path
budgetcsv = os.path.join("../Resources", "budget_data.csv")

# opening the CSV
with open(budgetcsv,newline="") as csvFile:
    csvreader = csv.reader(csvFile,delimiter = ",")
    # skip the headers
    csv_headers = next(csvreader)
    
    
    #totalMonths = sum(1 for row in csvreader)
    
    #print(totalMonths)
    
    netprofitloss = 0
    totalMonths = 0
    profitlosslist = []
    differencelist = []
    difflisttotal = 0
    i = 0
    diff = 0
    maxdiffmonth = 0
    mindiffmonth = 0
    monthlist = []

    #print(headers)
    # print(csvreader)
    for row in csvreader:
    # The total number of months included in the dataset
    # every row is a new month, so count the rows
        totalMonths += 1
    # The total net amount of "Profit/Losses" over the entire period
        netprofitloss += int(row[1])       
    #The average change in "Profit/Losses" between months over the entire period
    #creating a list to store the profit/loss numbers in
        profitlosslist.append(int(row[1]))
        monthlist.append(row[0])

    for number in range(len(profitlosslist) - 1): 
        diff = profitlosslist[number+1] - profitlosslist[number]
        differencelist.append(diff)
        
    for number in differencelist:
        difflisttotal += number



    avgdifference = difflisttotal/totalMonths
    
    #The greatest increase in profits (date and amount) over the entire period
    maxdifference = max(differencelist)
    #Pulling the index (+1) to print the month
    maxdiffmonth = monthlist[differencelist.index(max(differencelist))+1]    

    #The greatest decrease in losses (date and amount) over the entire period
    mindifference = min(differencelist)
    mindiffmonth = monthlist[differencelist.index(min(differencelist))+1]


   
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: {netprofitloss}")
    print(f"Average  Change: {avgdifference}")
    print(f"Greatest Increase in Profits: {maxdiffmonth} (${maxdifference})")
    print(f"Greatest Decrease in Profits: {mindiffmonth} (${mindifference})")

    output = f"""
    Financial Analysis
    ------------------
    Total Months: {totalMonths}
    Total: {netprofitloss}
    Average  Change: {avgdifference}
    Greatest Increase in Profits: {maxdiffmonth} (${maxdifference})
    Greatest Decrease in Profits: {mindiffmonth} (${mindifference})
    """
    print(output)

    with open("Output.txt", "w") as text_file:
        print(output, file=text_file)

