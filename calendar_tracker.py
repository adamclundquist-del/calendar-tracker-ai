events = []

def add_event():
    event = input("Enter event name: ")
    events.append(event)
    print("Event added.")

def delete_event():
    event = input("Enter event name to delete: ")

    if event in events:
        events.remove(event)
        print("Event deleted.")
    else:
        print("Event not found.")

add_event()
delete_event()

print("\nCurrent Events:")
print(events)
