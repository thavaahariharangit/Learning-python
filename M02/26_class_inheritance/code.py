class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"
    
    def disconnect(self):
        self.connected = False
        print("Disconnected")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity
    
    def __str__(self):
        return f"Printer {self.name!r} ({self.connected_by}) with capacity {self.capacity} and {self.remaining_pages} remaining pages"

    def print(self, pages):
        if not self.connected:
            print("Printer is not connected")
            return
        if pages > self.remaining_pages:
            print("Not enough paper to print")
            return
        self.remaining_pages -= pages
        print(f"Printed {pages} pages, {self.remaining_pages} remaining")



# printer = Device("Printer", "USB")
# print(printer)
# printer.disconnect()

printer = Printer("Printer", "USB", 100)
print(printer)
printer.print(10)
print(printer)
printer.disconnect()
printer.print(10)




