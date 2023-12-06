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

def max_red(game):
    init = re.findall(r"[0-9]+\s+red", game)
    reds = [int(x.split(" ")[0]) for x in init]
    return max(reds)

def max_green(game):
    init = re.findall(r"[0-9]+\s+green", game)
    greens = [int(x.split(" ")[0]) for x in init]
    return max(greens)
    #return all([count <= 13 for count in greens])

def max_blue(game):
    init = re.findall(r"[0-9]+\s+blue", game)
    blues = [int(x.split(" ")[0]) for x in init]
    return max(blues)

def power_of_games(data):
    return sum([max_red(game) * max_blue(game) * max_green(game) for game in data])

if __name__ == "__main__":
    data = read_data('data.txt')
    data = tansform_data(data)
    print(power_of_games(data))
