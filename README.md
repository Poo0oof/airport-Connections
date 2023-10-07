# Airport Connections

# Question

You have been provided with a list of airport codes (e.g., 'JFK'), a list of routes (one-way flights from one airport to another, such as ['JFK', 'SFO']), and a designated starting airport. Your task is to create a function that calculates the minimum number of additional airport connections (one-way flights) required for someone to reach any airport on the list, starting from the specified starting airport. It's important to note that these connections do not have to be direct; it's acceptable if an airport can only be reached from the starting airport by making intermediate stops at other airports.

# Sample input: 

```
ListOfAirports = [ 
"BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD", 
],
```

```
ListOfRoutes = [ 
["DSM", "ORD"], ["ORD", "BGI"], ["BGI", "LGA"], ["SIN", "CDG"], ["CDG", "SIN"], ["CDG", "BUD"], ["DEL", "DOH"], ["DEL", "CDG"], ["TLV", "DEL"], ["EWR", "HND"], ["1-IND", "ICN"], ["HND", "JFK"] ["ICN", "JFK"], ["JFK", "LGA"], ["EYW", "LHR"], ["LHR", "SFO"], ["SFO", "SAN"], ["SFO", "DSM"], ["SAN", "EYVV"],
 ],
```

```
StartPoint = "LGA" 
```

# Sample output:
3
