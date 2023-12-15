import datetime
import pandas as pd
import os

class ActivityTracker:
    def __init__(self, activity_name):
        self.start_time = None
        self.end_time = None
        self.duration = None
        self.activity_name = activity_name
        self.file_name = f"{activity_name}.csv"
        if os.path.exists(self.file_name):
            self.df = pd.read_csv(self.file_name)
            self.counter = len(self.df)
        else:
            self.df = pd.DataFrame(columns=["Count", "Start Time", "End Time", "Duration"])
            self.counter = 0

    def start_activity(self):
        self.start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def end_activity(self):
        self.end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.start_time = datetime.datetime.strptime(self.start_time, "%Y-%m-%d %H:%M:%S")
        self.end_time = datetime.datetime.strptime(self.end_time, "%Y-%m-%d %H:%M:%S")
        self.duration = self.end_time - self.start_time
        self.counter += 1
        self.df = pd.concat([self.df, pd.DataFrame({"Count": [self.counter], "Start Time": [self.start_time], "End Time": [self.end_time], "Duration": [self.duration]})], ignore_index=True)
        self.df.to_csv(self.file_name, index=False)

    def display_activity(self):
        print(f'Start Time: {self.start_time}')
        print(f'End Time: {self.end_time}')
        print(f'Duration: {self.duration}')
        print(f'Count: {self.counter}')

def handle_user_input():
    activity_name = input("Enter the name of the activity: ")
    tracker = ActivityTracker(activity_name)
    while True:
        command = input("Enter 'start' to start the activity, or 'quit' to quit: ")
        if command == 'start':
            tracker.start_activity()
            print(f"Started {tracker.activity_name}")
            command = input("Enter 'end' to end the activity: ")
            if command == 'end':
                tracker.end_activity()
                tracker.display_activity()
            elif command == 'quit':
                exit()
            else:
                print("Invalid command. Please enter 'start'.")
        elif command == 'quit':
            exit()
        else:
            print("Invalid command. Please enter 'start', or 'quit'.")


if __name__ == '__main__':
    handle_user_input()
