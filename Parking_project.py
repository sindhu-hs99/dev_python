import datetime
#import json
class Parking_system:
    #Attributes
    def __init__(self, total_slot):                     ##--> Constructor
        self.total_slot=total_slot
        self.available_slot=list(range(1,total_slot+1))
        self.parked_vehicle={}
        #self.load_data()

    #Methods
    def park_vehicle(self,vehicle_number):
        vehicle_number = vehicle_number.upper()
        if not self.available_slot:
            return f"Parking is Full!! No slots available."
        
        if vehicle_number in self.parked_vehicle:
            return f"Vehicle already parked!!"
        
        slot = self.available_slot.pop(0)
        entry_time=datetime.datetime.now()

        self.parked_vehicle[vehicle_number]={
            "slot" : slot,
            "entry_time" : entry_time
        }

        return f"Vehicle {vehicle_number} parked at slot {slot} at {entry_time} "
        #self.save_data()
    

    def parked_veh_remove(self,vehicle_number):
        vehicle_number = vehicle_number.upper()
        if vehicle_number not in self.parked_vehicle:
            return f"Vehicle not found"
        
        details = self.parked_vehicle.pop(vehicle_number)
        exit_time = datetime.datetime.now()
        exit_time_str = exit_time.strftime("%d-%m-%y %H:%M:%S")

        duration = exit_time - details["entry_time"]
        hours = duration.total_seconds()/3600

        fee=self.calculate(hours)
        self.available_slot.append(details["slot"])
        self.available_slot.sort()

        return(
            f"\nVehicle {vehicle_number} exited!!\n"
            f"\nExit Time: {exit_time_str}\n"
            f"\nParking Duration: {hours}hr \n"
            f"\nFee: Rs{fee} \n"
            f"\nFree slots available : {self.available_slot}\n"
        )
        
        #self.save_data()
    
    def calculate(self,hours):
        fee_per_hour = 20
        return (max(20, int(fee_per_hour * (hours))))

    '''
    def show_status(self):
        return f"Available slot: {self.available_slot}")
        return f"Parked slots: {self.parked_vehicle}")
    '''
    def park_vehicle_details(self):
        print("\n--------------Parking Summary----------")
        print( f"Total slots: {self.total_slot}")
        print( f"Available Slots: {len(self.available_slot)} slots")
        print(f"Available Slots name: {self.available_slot if self.available_slot else 'NA'} ")
        print( f"Occupied Slots: {len(self.parked_vehicle) if self.parked_vehicle else 'NA'}")
        for vehicle, info in self.parked_vehicle.items():   
            entry_time = info["entry_time"].strftime("%d-%m-%y %H:%M:%S")

            print(f"\nVehicle_number : {vehicle}")
            print( f"Slot : {info['slot']}")
            print( f"Entry Time: {entry_time}")
            
            #return f"vehicle: {vehicle}, slot: {info['slot']}, entry:{info['entry_time']}")

if __name__ == "__main__":
    a=Parking_system(3)

    while True:
        print("\n******************* SMART PARKING SYSTEM **********************")
        print("\n1. Park Vehicle")
        print("2. Remove Vehicle")
        print("3. show status")
        print("4. Exit")

        try:
            choice=int(input("\n Enter your choice: "))
        except ValueError:
            print(f"Please enter values only!!!")
            continue

        if choice == 1:
            vehicle=input("\nEnter the vehicle number:")
            if not vehicle.strip():
                print("Vehicle number can't be empty")
                continue
            print(a.park_vehicle(vehicle))
        elif choice == 2:
            vehicle=input("\nEnter the vehicle num: ")
            if not vehicle.strip():
                print("Vehicle number can't be empty")
                continue
            print(a.parked_veh_remove(vehicle))
        elif choice == 3:
            a.park_vehicle_details()
        elif choice == 4:
            print("\nExiting the system...... ")
            break
        else:
            print("\nInvalid Choice..... ")