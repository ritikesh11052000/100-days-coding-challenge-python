travel_log = [
    {
        "country": "france",
        "cities_visited": ["paris", "axcb", "shdgs"],
        "total_visited": 12
    },
    {
        "country": "germany",
        "cities_visited": ["barline", "chiacgo", "maxico"],
        "total_visited": 4
    },
]
for item in travel_log:
    print("country:", item["country"])
    print("cities_visited: ", " ".join(item["cities_visited"]))
    print("total_visited : ",item["total_visited"])
    print(" ")
for item in travel_log:
    print("Country:", item["country"])
    print("Cities Visited:", ", ".join(item["cities_visited"]))
    print("Total Visited:", item["total_visited"])
    print()  # Adding an empty line for readability