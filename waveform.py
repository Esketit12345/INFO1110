import sys
import os

if len(sys.argv)<2:
      print("No score file specified.")

if len(sys.argv)==2:
    path = sys.argv[1]
    if (os.path.isfile(path)) == False:
        if 'character' in path:
            print("No score file specified.")
        else:
            print("Invalid path to score file.")
        exit()
    if (os.path.isfile(path)) == True:
        with open(sys.argv[1], 'r') as file:
            line_score = file.read().splitlines()
            instrument_name = (line_score[0].strip(" "))
            wave_characters = (line_score[1].strip(" "))

        f = open(os.path.join('instruments',line_score[0].strip(" ")), 'r')
        contents = f.read()
        newcontents = contents.replace('-','*').replace('/','*').replace('\\','*').replace('*1','-1').replace('*2','-2').replace('*3','-3')
        print(newcontents)
       
