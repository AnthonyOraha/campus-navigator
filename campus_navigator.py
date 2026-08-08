from collections import deque

buildings = [
    "Library",
    "Student Union",
    "Engineering Building",
    "Science Building",
    "Gym"
]

building_info = {
    "Library": "Study and research",
    "Student Union": "Food and student activities",
    "Engineering Building": "Engineering classes",
    "Science Building": "Science classes and labs",
    "Gym": "Fitness and recreation"
}

campus_graph = {
    "Library": ["Student Union", "Science Building"],
    "Student Union": ["Library", "Gym"],
    "Engineering Building": ["Science Building", "Gym"],
    "Science Building": ["Library", "Engineering Building"],
    "Gym": ["Student Union", "Engineering Building"]
}

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = []

    while queue:
        path = queue.popleft()
        building = path[-1]

        if building == goal:
            return path

        if building not in visited:
            visited.append(building)

            for neighbor in graph[building]:
                new_path = path + [neighbor]
                queue.append(new_path)

    return None

campus_tree = {
    "Campus": {
        "Academic": [
            "Engineering Building",
            "Science Building"
        ],
        "Student Services": [
            "Library",
            "Student Union"
        ],
        "Recreation": [
            "Gym"
        ]
    }
}

while True:
    print("\n--- Campus Navigator ---")
    print("1. View Buildings")
    print("2. Search Building")
    print("3. Find Route")
    print("4. View Building Categories")
    print("5. View Buildings Alphabetically")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\nCampus Buildings:")
        for building in buildings:
            print("-", building)

    elif choice == "2":
        search_name = input("Enter building name: ")

        if search_name in building_info:
            print(search_name + ":", building_info[search_name])
        else:
            print("Building not found.")

    elif choice == "3":
        start = input("Enter starting building: ")
        goal = input("Enter destination building: ")

        if start in campus_graph and goal in campus_graph:
            route = bfs(campus_graph, start, goal)

            if route:
                print("Route:", " -> ".join(route))
            else:
                print("No route found.")
        else:
            print("Invalid building name.")

    elif choice == "4":
        print("\nBuilding Categories:")

        for category, locations in campus_tree["Campus"].items():
            print(category + ":")
            for location in locations:
                print("  -", location)

    elif choice == "5":
        print("\nBuildings in Alphabetical Order:")

        for building in sorted(buildings):
            print("-", building)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")