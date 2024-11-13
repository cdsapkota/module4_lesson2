class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = []

    def add_participant(self, participant_name):
        if participant_name and participant_name not in self.participants:
            self.participants.append(participant_name)
            print(f"{participant_name} added successfully.")
        else:
            print(f"Participant '{participant_name}' is either empty or already exists.")

    def delete_participant(self, participant_name):
        if participant_name in self.participants:
            self.participants.remove(participant_name)
            print(f"{participant_name} removed successfully.")
        else:
            print(f"Participant '{participant_name}' not found.")

    def get_participant_count(self):
        return len(self.participants)

    def __str__(self):
        return f"Event: {self.name}, Date: {self.date}, Participants: {len(self.participants)}"

events = []

while True:
    print("\nOptions:")
    print("1. Add a new event")
    print("2. Add participant to an event")
    print("3. Delete participant from an event")
    print("4. Get participant count for an event")
    print("5. List all events")
    print("6. Exit")
    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "6":
        print("Exiting program.")
        break

    try:
        if choice == "1":
            name = input("Enter event name: ").strip()
            date = input("Enter event date: ").strip()

            if any(event.name == name for event in events):
                print("Error: Event with this name already exists.")
            else:
                new_event = Event(name, date)
                events.append(new_event)
                print("Event added successfully.")

        elif choice == "2":
            event_name = input("Enter event name to add a participant: ").strip()
            participant_name = input("Enter participant name to add: ").strip()

            for event in events:
                if event.name == event_name:
                    event.add_participant(participant_name)
                    break
            else:
                print("Error: Event not found.")

        elif choice == "3":
            event_name = input("Enter event name to delete a participant: ").strip()
            participant_name = input("Enter participant name to delete: ").strip()

            for event in events:
                if event.name == event_name:
                    event.delete_participant(participant_name)
                    break
            else:
                print("Error: Event not found.")

        elif choice == "4":
            event_name = input("Enter event name to get participant count: ").strip()

            for event in events:
                if event.name == event_name:
                    count = event.get_participant_count()
                    print(f"Current participant count for '{event.name}': {count}")
                    break
            else:
                print("Error: Event not found.")

        elif choice == "5":
            print("\nListing all events:")
            if events:
                for event in events:
                    print(event)
            else:
                print("No events found.")

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

    except ValueError as e:
        print(f"Input error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
