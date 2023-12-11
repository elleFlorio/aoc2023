def read_input(filename):
    with open("input/" + filename, 'r') as f:
        return f.read().splitlines()
