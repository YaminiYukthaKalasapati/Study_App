import csv
from datetime import datetime

def log_progress(user, activity, score=None):
    with open('logs.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), user, activity, score])