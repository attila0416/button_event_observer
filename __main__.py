ACTIVATE_FORMAT = "activate_{}"
DEACTIVATE_FORMAT = "deactivate_{}"


class Button:
    def __init__(self, id):
        self.id = id
        self.events_map = None

    def activate(self):
        print()
        print(f"Activating {self.id}")
        current_event = ACTIVATE_FORMAT.format(self.id)
        subscribed_actions = self.events_map[current_event]
        for subscribed_action in subscribed_actions:
            subscribed_action()

    def deactivate(self):
        print(f"Deactivating {self.id}")


def main():
    button1 = Button(1)
    button2 = Button(2)
    button3 = Button(3)
    events_map = {
        ACTIVATE_FORMAT.format(button1.id): [button2.deactivate, button3.deactivate],
        ACTIVATE_FORMAT.format(button2.id): [button1.deactivate, button3.deactivate],
        ACTIVATE_FORMAT.format(button3.id): [button1.deactivate, button2.deactivate],
    }
    button1.events_map = events_map
    button2.events_map = events_map
    button3.events_map = events_map

    button1.activate()
    button3.activate()


if __name__ == "__main__":
    main()
