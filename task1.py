class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.reg_num = reg_num
        self.type = type
        self.owner = owner
    
    def update_owner(self, new_owner):
        self.owner = new_owner
    
    def __str__(self):
        return f"Registration: {self.reg_num}, Type: {self.type}, Owner: {self.owner}"
    
vehicles = []

while True:
    print("\nOptions:")
    print("1. Add a new vehicle")
    print("2. Update vehicle owner")
    print("3. List all vehicles")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "4":
        print("Exiting program.")
        break

    try:
        if choice == "1":
            reg_num = input("Enter registration number: ").lower()
            v_type = input("Enter vehicle type: ").lower()
            owner = input("Enter owner name: ")

            # Check if the vehicle already exists in the list
            if any(vehicle.reg_num == reg_num for vehicle in vehicles):
                print("Error: Vehicle with this registration number already exists.")
            else:
                new_vehicle = Vehicle(reg_num, v_type, owner)
                vehicles.append(new_vehicle)
                print("Vehicle added successfully.")

        elif choice == "2":
            reg_num = input("Enter registration number of the vehicle to update: ").lower()

            # Find the vehicle with the given registration number
            for vehicle in vehicles:
                if vehicle.reg_num == reg_num:
                    new_owner = input("Enter new owner's name: ")
                    vehicle.update_owner(new_owner)
                    print("Owner updated successfully.")
                    break
            else:
                print("Error: Vehicle not found.")

        elif choice == "3":
            print("\nListing all vehicles:")
            if vehicles:
                for vehicle in vehicles:
                    print(vehicle)
            else:
                print("No vehicles found.")

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

    except ValueError as e:
        print(f"Input error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")