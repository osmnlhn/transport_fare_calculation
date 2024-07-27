FARE_PER_ZONE = {
    "adult": 2105,
    "child": 1410,
    "senior": 1025,
    "student": 1750,
}

def calculate_total_zones(start_zone, end_zone):
    return abs(end_zone - start_zone) + 1

def calculate_fare(zones, adults, children, seniors, students):
    return {
        "adults": zones * FARE_PER_ZONE["adult"] * adults,
        "children": zones * FARE_PER_ZONE["child"] * children,
        "seniors": zones * FARE_PER_ZONE["senior"] * seniors,
        "students": zones * FARE_PER_ZONE["student"] * students,
    }
