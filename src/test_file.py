
def load_file(filename):
    with open(filename) as file:
        content = file.read()
        return content

content = load_file("test.txt")
print(content)