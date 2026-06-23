class Ticket:
    def __init__(self, movie, seats_available, seats_requested):
        self.movie = movie
        self.seats_available = seats_available
        self.seats_requested = seats_requested
        
        self.confirmed_seats = min(seats_available, seats_requested)
        
        if self.confirmed_seats == seats_requested:
            self.message = f"Success! All {seats_requested} requested seats have been booked."
        else:
            self.message = f"Partial booking. Only {self.confirmed_seats} out of {seats_requested} requested seats were available."

    def display_outcome(self):
        print(f"Movie: {self.movie}")
        print(f"Requested: {self.seats_requested} | Available: {self.seats_available}")
        print(f"Confirmed Seats: {self.confirmed_seats}")
        print(f"Status: {self.message}")
        print("-" * 50)

print("--- MOVIE TICKET BOOKING OUTCOMES ---\n")

ticket1 = Ticket("PharmaTrace: The Movie", 5, 5)
ticket1.display_outcome()

ticket2 = Ticket("Inception", 10, 3)
ticket2.display_outcome()

ticket3 = Ticket("Interstellar", 2, 6)
ticket3.display_outcome()