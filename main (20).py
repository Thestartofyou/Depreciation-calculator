def calculate_depreciation_expense(cost, salvage_value, useful_life_years):
    depreciation_per_year = (cost - salvage_value) / useful_life_years
    return depreciation_per_year

def depreciate_assets():
    building_components = calculate_depreciation_expense(50000, 10000, 20)
    electrical_and_lighting = calculate_depreciation_expense(20000, 4000, 10)
    plumbing = calculate_depreciation_expense(10000, 2000, 15)
    flooring = calculate_depreciation_expense(15000, 3000, 12)
    fixtures_and_equipment = calculate_depreciation_expense(25000, 5000, 8)
    furniture_and_fittings = calculate_depreciation_expense(20000, 4000, 10)

    return {
        "Building components": building_components,
        "Electrical and lighting": electrical_and_lighting,
        "Plumbing": plumbing,
        "Flooring": flooring,
        "Fixtures and equipment": fixtures_and_equipment,
        "Furniture and fittings": furniture_and_fittings
    }

assets_depreciation_expense = depreciate_assets()

for category, expense in assets_depreciation_expense.items():
    print(f"{category}: ${expense:.2f} per year")
