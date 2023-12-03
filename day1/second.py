numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def read_data(filename):
    f = open(filename, 'r')
    data = f.read()
    return data

def tansform_data(data):
    data = data.split("\n\n")
    remove_newlines = [elem.rstrip() for elem in data]
    grouped_data = [elem.split("\n") for elem in remove_newlines][0]
    return grouped_data

def map_to_int(string):
    if string == "one":
        return "1"
    elif string == "two":
        return "2"
    elif string == "three":
        return "3"
    elif string == "four":
        return "4"
    elif string == "five":
        return "5"
    elif string == "six":
        return "6"
    elif string == "seven":
        return "7"
    elif string == "eight":
        return "8"
    elif string == "nine":
        return "9"
    else:
        return "0"

def find_first_digit(string):
    while string != "":
        if string[0].isdigit():
            return string[0]
        else:
            for number in numbers:
                if string.startswith(number):
                    return map_to_int(number)
        string = string[1:]

def find_last_digit(string):
    new_numbers = [x[::-1] for x in numbers]
    string = string[::-1]
    while string != "":
        if string[0].isdigit():
            return string[0]
        else:
            for number in new_numbers:
                if string.startswith(number):
                    return map_to_int(number[::-1])
        string = string[1:]

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
