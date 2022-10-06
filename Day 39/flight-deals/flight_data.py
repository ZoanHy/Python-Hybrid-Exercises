class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, start_port, start_city, destination_port, destination_city, out_date, return_date):
        self.price = price
        self.start_port = start_port
        self.start_city = start_city
        self.destination_port = destination_port
        self.destination_city = destination_city
        self.out_date = out_date
        self.return_date = return_date


