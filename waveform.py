import sys
import os

if len(sys.argv)<2:
      print("No score file specified.")
      sys.exit()

instrument_line = ()
instrument_score = ()

if len(sys.argv)==2:
    path = sys.argv[1]
    if (os.path.isfile(path)) == False:
        if 'character' in path:
            print("No score file specified.")
        else:
            print("Invalid path to score file.")
        exit()
    if (os.path.isfile(path)) == True:
        with open(sys.argv[1], 'r') as f:
            line_score = f.read().splitlines()
            instrument_name = (line_score[0].strip(" "))
            wave_characters = (line_score[1].strip(" "))
            wave_amount = int(len((wave_characters)) - 2)
        try:
            with open(os.path.join('instruments',instrument_name)) as f:
                    instrument_line = f.readlines()
            with open(sys.argv[1]) as f:
                    instrument_score = f.readlines()
                    instrument_line = [x.strip() for x in instrument_line]
                    instrument_score = [x.strip() for x in instrument_score]
                    instrument_score = [x.strip('|') for x in instrument_score]
        except FileNotFoundError:
                print("Unknown source.")
                sys.exit()




# creating an array which represents an initial wave for the given instrument:
# geting rid of \t and store the position of any symbols but spaces
def generate_initial_wave(content):
    array = []
    j = 0
    for line in content:
        tab_index = line.find("\t")
        new_line = line[tab_index + 1:]
        i = 0
        for character in new_line:
            if character != ' ':
                array.append((i, j))
            i = i + 1
        j = j + 1

    array.sort(key=lambda x: x[0], reverse=False)
    return array


# method for drawing wave using given character as parameter
def draw_wave(points, character, length):
        array = [' '] * length
        for point in points:
            array[point[0]] = character
        new_wave = ''.join(array)
        print(new_wave)

# generating the wave: walking through score array looking for - and *
# when it's * - wave goes as usual, but if it's - wave drops to x-axis and moves on x-axis until meets next *
# after that it restarts from the beginning
def generate_wave(score, line):
    index = 0
    instrument_wave_line = []
    overflow = 0
    for symbol in score[1]:
        if index >= len(line):
            index = 0
            overflow = overflow + len(line)
        if symbol == '*':
            point_to_add = (line[index][0] + overflow, line[index][1])
            instrument_wave_line.append(point_to_add)
            index = index + 1
        else:
            overflow = index + overflow
            min_val = min(line[0][1],line[index][1])
            max_val = max(line[0][1],line[index][1])
            for new_y in range(min_val,max_val+1):
                point_to_add = (overflow, new_y)
                instrument_wave_line.append(point_to_add)
            overflow = overflow + 1
            index = 0
    return instrument_wave_line

wave = generate_initial_wave(instrument_line)

generated_wave = generate_wave(instrument_score,wave)
values = set(map(lambda i: i[1], generated_wave))
groups = [[j for j in generated_wave if j[1] == i] for i in values]

for points in groups:
    draw_wave(points, '*', wave_amount)
