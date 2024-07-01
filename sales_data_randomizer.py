import csv
import shutil
import random
import time
import os

config = {
    'src': 'C:/Users/nahue/Desktop/Python/sales_data.csv',  # Source CSV file
    'dst': 'C:/Users/nahue/Desktop/Python/backup/sales_data_copy.csv',  # Backup destination
    'shuffled_dst': 'C:/Users/nahue/Desktop/Python/sales_data.csv',  # Shuffled CSV destination
    'backup_interval_hours': 24  # Backup interval in hours (default: 24 hours)
}

# Function to copy the original CSV file if not already backed up today

def backup_csv(src, dst):
    if not os.path.exists(dst) or time.time() - os.path.getmtime(dst) > config['backup_interval_hours'] * 3600:
        shutil.copy(src, dst, follow_symlinks=True)
    
# Reading the CSV file

def reading_csv(src):
    rows = []
    with open(src, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            rows.append(row)
    return rows

# Shuffle the CSV file       

def shuffle_csv(rows, shuffled_dst):
    # Separate header and data rows
    header = rows[0]
    data_rows = rows[1:]
    # Shuffle the data rows
    random.shuffle(data_rows)
    # Combine the header and the shuffled data rows
    shuffled_rows = [header] + data_rows

    with open(shuffled_dst, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(shuffled_rows)

    # Print the shuffled rows (optional)
    for row in shuffled_rows:
        print(', '.join(row))

# Log in

def log_in():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    while True:
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        if password == 'pass':
            print(f'{timestamp} - You successfully logged in as {username}!')
            print(' ')
            break
        else:
            print(f'{timestamp} - Your password is incorrect. Try again!')
            print(' ')

# Loop function

def loop_function():
    log_in()
    backup_csv(config['src'], config['dst'])
    rows = reading_csv(config['src'])
    shuffle_csv(rows, config['shuffled_dst'])

# Run the randomizing operation every 10 seconds (for demonstration purposes)

while True:
    loop_function()
    print(' ')
    print("CSV file shuffled and saved. Waiting for next iteration...")
    print(' ')
    time.sleep(10)