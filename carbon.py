def carbon_absorption(area_m2, species="mangrove"):
    absorption_rates = {"mangrove": 8, "seagrass": 3}  # CO₂ absorption in kg/m² per year
    return area_m2 * absorption_rates.get(species, 5)  # Default 5 kg/m² if unknown species

# Example: 5000m² mangrove area
area = 5000
carbon_offset = carbon_absorption(area, "mangrove")
print(f"Estimated Carbon Offset: {carbon_offset} kg CO₂ per year")
