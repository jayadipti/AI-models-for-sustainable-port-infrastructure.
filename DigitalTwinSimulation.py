class DigitalTwin:
    def __init__(self, name):
        self.name = name
        self.parameters = {"energy_usage": 10000, "waste_generation": 500}

    def update_parameters(self, energy_usage, waste_generation):
        self.parameters["energy_usage"] = energy_usage
        self.parameters["waste_generation"] = waste_generation

    def display_status(self):
        print(f"Port: {self.name}")
        print(f"Energy Usage: {self.parameters['energy_usage']} kW")
        print(f"Waste Generation: {self.parameters['waste_generation']} kg")


port_twin = DigitalTwin("GreenPort")
port_twin.update_parameters(8000, 300)
port_twin.display_status()
