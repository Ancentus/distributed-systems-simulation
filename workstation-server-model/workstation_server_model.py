from mimetypes import init


class FileServer:
    def __init__(self, server_id):
        self.server_id = server_id
        self.files = {}

    def add_file(self, file_name, content):
        self.files[file_name] = content
        print(f"File '{file_name}' added to File Server {self.server_id}")

    def delete_file(self, file_name):
        if file_name in self.files:
            del self.files[file_name]
            print(f"File '{file_name}' deleted from File Server {self.server_id}")
        else:
            print(f"File '{file_name}' not found in File Server {self.server_id}")

    def get_file(self, file_name):
        if file_name in self.files:
            return self.files[file_name]
        else:
            print(f"File '{file_name}' not found in File Server {self.server_id}")
            return None

class PrinterServer:
    def __init__(self, server_id):
        self.server_id = server_id
        self.print_queue = []

    def add_to_print_queue(self, file_name):
        self.print_queue.append(file_name)
        print(f"File '{file_name}' added to Printer Server {self.server_id} print queue.")

    def print_file(self):
        if self.print_queue:
            file_name = self.print_queue.pop(0)
            print(f"File '{file_name}' printed by Printer Server {self.server_id}.")
        else:
            print(f"No files in Printer Server {self.server_id} print queue")

class Workstation:
    def __init__(self, workstation_id, file_servers, printer_servers):
        self.workstation_id = workstation_id
        self. file_servers = file_servers
        self.printer_servers = printer_servers

    def access_file(self, file_name):
        for server in self.file_servers:
            content = server.get_file(file_name)
            if content:
                print(f"File '{file_name}' accessed from Workstation {self.workstation_id}")
                return content
        print(f"File {file_name} not found in any File Server")

    def add_file(self, file_name, content):
        for server in self.file_servers:
            server.add_file(file_name, content)

    def delete_file(self, file_name):
        for server in self.file_servers:
            server.delete_file(file_name)

    def print_file(self, file_name):
        for server in self.printer_servers:
            server.add_to_print_queue(file_name)

if __name__ == "__main__":
    # Create file servers
    file_server1 = FileServer(1)
    file_server2 = FileServer(2)

    # Create printer servers
    printer_server1 = PrinterServer(1)
    printer_server2 = PrinterServer(2)

    # Create workstations
    workstation1 =  Workstation(1,[file_server1, file_server2], [printer_server1])
    workstation2 =  Workstation(2,[file_server1, file_server2], [printer_server2])

    # Add files to file servers
    file_server1.add_file("file1.txt", "This is file 1 content")
    file_server2.add_file("file2.txt", "This is file 2 content")

    # Access files from workstations
    workstation1.access_file("file1.txt")
    workstation2.access_file("file2.txt")

    # Add and delete files from workstations
    workstation1.add_file("file3.txt", "This is file 3 content")
    workstation1.delete_file("file.txt")

    # Print files from workstations
    workstation1.print_file("file1.txt")
    workstation2.print_file("file2.txt")