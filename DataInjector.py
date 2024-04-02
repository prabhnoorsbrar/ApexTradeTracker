import csv
from CreateSheets import sheetUpdate

def inject_data(threshold, balance, threshold_02, balance_02):
    filename = "ProfitLoss_03.csv"
    filename_02 = "ProfitLoss_04.csv"
    
    # Read the existing data from the CSV file and convert relevant columns to float
    data = []
    data_02 = []
    with open(filename, 'r', newline='') as file, open(filename_02, 'r', newline='') as file_2:
        csv_reader = csv.reader(file)
        csv_reader_2 = csv.reader(file_2)
        
        # Populate data list from the first file
        next(csv_reader)  # Skip the header row

        for row in csv_reader:
            if row:
                data.append(row)
        
        # Populate data_02 list from the second file
        next(csv_reader_2)  # Skip the header row

        for row in csv_reader_2:
            if row:
                data_02.append(row)
    
    # Debug prints to check the content of data and data_02
    #print("Data:", data)
    #print("Data_02:", data_02)
    
    # Get the latest day from the existing data
    if data:
        latest_day = int(data[-1][0])
    else:
        0
    if data_02:
        latest_day_02 = int(data_02[-1][0])
    else:
        0
    
    
    if data:
        latest_day = int(data[-1][0])
    else:
        latest_day = 0


    if data_02:
        latest_day_02 = int(data_02[-1][0])
    else:
        latest_day_02 = 0

    # Increment the day by 1 for the new row
    new_day = latest_day + 1
    new_day_02 = latest_day_02 + 1
    
    # Calculate P&L for the new row
    pnl = "N/a"
    if data:
        pnl = float(balance) - float(data[-1][2]) 
    else: 
        pnl = float(balance) - 50000

    pnl_2 = "N/a"
    if data_02:
        pnl_2 = float(balance_02) - float(data_02[-1][2]) 
    else: 
        pnl_2 = float(balance_02) - 50000
    
    # Prepare the new row to be added
    new_row = [str(new_day), str(round(pnl, 2)), str(balance), str(threshold)]
    new_row_02 = [str(new_day_02), str(round(pnl_2, 2)), str(balance_02), str(threshold_02)]
    
    # Write the new row to the CSV file
    with open(filename, 'a', newline='') as file, open(filename_02, 'a', newline='') as file_2:
        csv_writer = csv.writer(file)
        csv_writer_02 = csv.writer(file_2)
        csv_writer.writerow(new_row)
        csv_writer_02.writerow(new_row_02)

    sheetUpdate(filename,filename_02)
    

    













