def read_data(filename):
    f = open(filename, 'r')
    data = f.read()
    return data

def tansform_data(data):
    data = data.split("\n\n")
    remove_newlines = [elem.rstrip() for elem in data]
    grouped_data = [elem.split("\n") for elem in remove_newlines][0]
    return grouped_data

def find_first_digit(string):
    for c in string:
        if c.isdigit():
            return c

def find_last_digit(string):
    for c in string[::-1]:
        if c.isdigit():
            return c

def find_digits(data):
    return [int(find_first_digit(x) + find_last_digit(x)) for x in data]

def sum_digits(data):
    return sum(data)

if __name__ == "__main__":
    data = read_data('data.txt')
    data = tansform_data(data)
    data = find_digits(data)
    data = sum_digits(data)
    print(data)
