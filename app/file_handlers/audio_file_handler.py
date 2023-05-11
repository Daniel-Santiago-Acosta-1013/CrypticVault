def read_file(path):
    with open(path, "rb") as file:
        return file.read()

def write_file(path, data):
    with open(path, "wb") as file:
        file.write(data)