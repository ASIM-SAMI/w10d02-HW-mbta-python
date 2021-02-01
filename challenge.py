red_line  = ['south station', 'park st',
 'kendall', 'central', 'harvard' ,'porter','davis','alewife']

green_line = ['haymarket', 'government center', 'park st', 'bolyston', 'arlington','copley']

orange_line = ['north station', 'haymarket', 'park st',
'state', 'downtown crossing', 'chinatown','back bay','forest hills']

stops_total = 0
final_string = ['','','','']

def planTrip(line, start, change, target):
    line = line.lower()
    if line == 'red_line' :
        findTheWay(line, red_line, start, red_line[1])
    elif line == 'green_line' :
        findTheWay(line, green_line, start, green_line[2])
    elif line == 'orange_line' :
        findTheWay(line, orange_line, start, orange_line[2])
    pass

    changeWay(change, target)
    console.log(f'{stops_total} stops in total.')
    final_string[3] = f'{stops_total} stops in total.'   



def changeWay(change, target):
    print('Change at park st.')
    final_string[1] = 'Change at park st.'
    change = change.lower()
    if change == 'red_line' :
        newWay(red_line, target)
    elif change == 'green_line' :
        newWay(green_line, target)
    elif change == 'orange_line' :
        newWay(orange_line, target)
    pass


def newWay(newLine,target):
    string = 'Your journey continues through the following stops:'
    us_index = newLine.index('park st')
    if(newLine.index(target) > us_index):
        us_index += 1
    elif (newLine.index(target) < us_index):
        us_index -= 1
    pass
    i = us_index
    while i >= 0 :
        if newLine[i] != target : 
            string += f' {i} '
            stops_total +=1
        else :
            string += f' {i} '
            stops_total += 1
            i = -1
        pass
        i += 1
    print(string)
    final_string[2] = f'{string}'

       
def findTheWay(li, line , start, stop):
    us_index = line.index('park st')
    start = line.index(start)
    if start > us_index:
        start -= 1
    elif start < us_index:
        start += 1
    string = f'You must travel through the following stops on the {li.upper()} line:'
    i = start
    while i < len(line) :
        if line[i] != stop:
            string += f' {line[i]}, '
            stops_total += 1
        else:
            string += f' {line[i]}, '
            stops_total += 1
            i = 50
        pass
        i += 1
        print(f' {string}')
        final_string[0] = f' {string} '



planTrip('red_line', 'south station', 'orange_line', 'haymarket')