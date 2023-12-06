import re

def read_data(filename):
    f = open(filename, 'r')
    data = f.read()
    return data

def tansform_data(data):
    data = data.split("\n\n")
    remove_newlines = [elem.rstrip() for elem in data]
    grouped_data = [elem.split("\n") for elem in remove_newlines][0]
    return grouped_data

def check_red(game):
    init = re.findall(r"[0-9]+\s+red", game)
    reds = [int(x.split(" ")[0]) for x in init]
    return all([count <= 12 for count in reds])

def check_green(game):
    init = re.findall(r"[0-9]+\s+green", game)
    greens = [int(x.split(" ")[0]) for x in init]
    return all([count <= 13 for count in greens])

def check_blue(game):
    init = re.findall(r"[0-9]+\s+blue", game)
    blues = [int(x.split(" ")[0]) for x in init]
    return all([count <= 14 for count in blues])

def find_ok_games(data):
    kosher = []
    for game in data:
        if (check_red(game) and check_green(game) and check_blue(game)):
            kosher.append(game)
    return kosher

def sum_games(data):
    return sum([int(re.findall(r"[0-9]+", game)[0]) for game in data])

if __name__ == "__main__":
    data = read_data('data.txt')
    data = tansform_data(data)
    ok_games = find_ok_games(data)
    result = sum_games(ok_games)
    print(result)
