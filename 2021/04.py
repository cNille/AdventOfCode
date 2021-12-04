import re
f = open('04.test', 'r')
f = open('04.input', 'r')
content = [x.strip() for x in f.readlines()]

numbers = map(int, content[0].split(','))
#print('Game numbers: %s', numbers)

board_data= content[1:]
nbr_boards = len(board_data) / 6

class Board:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.marked = []
        self.marked_number = []

    def check(self):
        columns = len(self.data)
        rows = len(self.data[0])

        # Check if column is complete
        for i in range(columns):
            marked_in_column = [n for n in self.marked if n[0] == i]
            if columns == len(marked_in_column): 
                return True

        # Check if row is complete
        for i in range(rows):
            marked_in_row = [n for n in self.marked if n[1] == i]
            if columns == len(marked_in_row): 
                return True
        return False

    def get_score(self):
        numbers_flatten = sum(self.data, []) # Flattens the lists
        unmarked = [n for n in numbers_flatten if n not in self.marked_number]
        score = sum(unmarked) * self.marked_number[-1]
        return score

    def draw(self, number):
        assert not self.check()
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                if(number == self.data[y][x]):
                    self.marked.append((x,y))

        self.marked_number.append(number)

# Create boards
boards = []
for idx in range(nbr_boards):
    offset = idx*6
    data = board_data[offset + 1: offset + 6]
    data = [map(int,re.split(r' +', x)) for x in data]
    board = Board(idx, data)
    boards.append(board)
    
# Start game!
leaderboard = []
for rnd, number in enumerate(numbers):
    #print('Round %d: %d' % (rnd, number))
    #print('Boards left: %d' % len(boards))
    
    for i, b in enumerate(boards):
        if(b.check()):
            continue
        b.draw(number)
        won = b.check()
        if won:
            #print('Board #%d has won' % b.id)
            leaderboard.append(b)
    if len(boards) == 0:
        break

winner = leaderboard[0] 
loser = leaderboard[-1] 
print('Winners score is: %d' % winner.get_score())
print('Losers score is: %d' % loser.get_score())
