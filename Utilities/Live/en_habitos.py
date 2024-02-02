import os
import pandas as pd
from datetime import datetime

class HabitsManager:
    def __init__(self, user):
        self.user = user
        self.habits = pd.DataFrame(columns=['Habit', 'Completed', 'Last Update'])
        self.excel_file = f"{user}_habits.xlsx"
        self.load_data()

    def load_data(self):
        if os.path.exists(self.excel_file):
            self.habits = pd.read_excel(self.excel_file)

    def save_data(self):
        self.habits.to_excel(self.excel_file, index=False)

    def add_habit(self, habit_name):
        if habit_name not in self.habits['Habit'].values:
            new_habit = pd.DataFrame({'Habit': [habit_name], 'Completed': [False], 'Last Update': [None]})
            self.habits = pd.concat([self.habits, new_habit], ignore_index=True)
            print(f"Habit '{habit_name}' added successfully.")
        else:
            print(f"Error! Habit '{habit_name}' already exists.")

    def mark_completed(self, habit_name):
        if habit_name in self.habits['Habit'].values:
            index = self.habits.index[self.habits['Habit'] == habit_name].tolist()[0]
            self.habits.loc[index, 'Completed'] = True
            self.habits.loc[index, 'Last Update'] = str(datetime.now())  # Convert to string
            print(f"Habit '{habit_name}' marked as completed.")
        else:
            print(f"Error! Habit '{habit_name}' does not exist.")

    def delete_habit(self, habit_name):
        if habit_name in self.habits['Habit'].values:
            self.habits = self.habits[self.habits['Habit'] != habit_name]
            print(f"Habit '{habit_name}' deleted successfully.")
        else:
            print(f"Error! Habit '{habit_name}' does not exist.")

    def show_habits(self):
        if self.habits.empty:
            print("No habits registered.")
        else:
            print("List of habits:")
            print(self.habits)

# Example of usage
user = "example_user"
manager = HabitsManager(user)

while True:
    print("\n=== Menu ===")
    print("1. Add Habit")
    print("2. Mark Habit as Completed")
    print("3. Delete Habit")
    print("4. Show Habits")
    print("5. Exit")

    option = input("Select an option: ")

    if option == '1':
        habit_name_new = input("Enter the name of the new habit: ")
        manager.add_habit(habit_name_new)
    elif option == '2':
        habit_name_completed = input("Enter the name of the completed habit: ")
        manager.mark_completed(habit_name_completed)
    elif option == '3':
        habit_name_delete = input("Enter the name of the habit to delete: ")
        manager.delete_habit(habit_name_delete)
    elif option == '4':
        manager.show_habits()
    elif option == '5':
        manager.save_data()
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")