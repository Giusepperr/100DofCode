travel_log = [
    {"Country":"France","timeVisited":6,"cities":["Paris","Nice"]},
    {"Country":"Italy","timeVisited":20,"cities":["Rome","Napoli"]}
    ]
def AddCountry(country,timeVisited,cities):
    country = {"Country":country,"timeVisited":timeVisited,"cities":cities}
    travel_log.append(country)

AddCountry('Russia', 2,["moscow","Vienna"])

print(travel_log)