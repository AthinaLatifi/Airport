from queue import Queue, PriorityQueue

class Airport:
    def __init__(self):
        self.landing_queue = Queue()
        self.takeoff_queue = Queue()
        self.emergency_landing_queue = PriorityQueue()

    def request_landing(self, flight_number):
        print(f"Flight {flight_number} requests landing")
        # Assuming flight_number is a unique identifier for each flight
        self.landing_queue.put(flight_number)

    def request_takeoff(self, flight_number):
        print(f"Flight {flight_number} requests takeoff")
        self.takeoff_queue.put(flight_number)

    def request_emergency_landing(self, flight_number):
        print(f"Flight {flight_number} requests emergency landing")
        # Priority is set to a negative value to ensure higher priority
        self.emergency_landing_queue.put((-1, flight_number))

    def allow_action(self):
        # Check for emergency landings first
        if not self.emergency_landing_queue.empty():
            priority, flight_number = self.emergency_landing_queue.get()
            print(f"CONTROL: {flight_number} land")
        # Check for normal landings
        elif not self.landing_queue.empty():
            flight_number = self.landing_queue.get()
            print(f"CONTROL: {flight_number} land")
        # Check for takeoffs
        elif not self.takeoff_queue.empty():
            flight_number = self.takeoff_queue.get()
            print(f"CONTROL: {flight_number} takeoff")

# Usage
airport = Airport()

# Simulation
airport.request_landing(345)
airport.request_landing(190)
airport.request_takeoff(188)
airport.allow_action()
airport.request_emergency_landing(621)
airport.allow_action()
airport.request_takeoff(511)
airport.allow_action()
airport.allow_action()
airport.request_takeoff(810)
airport.allow_action()
