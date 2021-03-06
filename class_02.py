""" Creatinf and unsing a class """

#The Car class 

class Car():
    """ A simple attempt to model a car. """
    def __init__(self, make, model, year):
        """Initialize car attribut."""
        self.make = make
        self.model = model
        self.year = year

        #fuel capacity and level in gallons.
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = self.fuel_capicity
        print("Fuel tank is full.")

    def drive(self):
        """Simulate driving."""
        print("The car is moving.")




class ElectricCar(Car):
    """A simple model of an electic car."""

    def __init__(self, make, model, year):
        """Inialize an electric car."""
        super().__init__(make, model,year)

        #attributes specific to electic cars. 
        #battery capacity in kwh.
        self.battery_size = 70
        #Charge level in %.
        self.charge_level = 0

    def charge(self):
        """Fully charge the vehicle."""

        self.charge_level = 100
        print("The vehicule is fully charge.")


    def fill_tank(self):
        """Display an error message. """
        print("This car has no fuel tank!")

my_ecar = ElectricCar('tesla', 'model s', 2016)


my_ecar.charge()

my_ecar.drive()



print(my_ecar.make)
print(my_ecar.model)
print(my_ecar.year)
