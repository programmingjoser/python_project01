import csv

def players():
    ''' create and return 2 lists of players(experienced and inexperienced) '''
    with open('soccer_players.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rows = list(reader)
        experienced_players = []
        inexperienced_players = []
        for line in rows[:]:
            if line[2] == 'YES':
                experienced_players += line
            else:
                inexperienced_players += line

    return experienced_players, inexperienced_players

def create_teams(teams, experienced, notexperienced):

    count = 0
    for team in teams:
        for player in experienced:
            print(player)
  #          if len(teams[team]) < len(experienced) / len(teams):
#                teams[team] += player

    print(teams)
            
if __name__ == "__main__":
    
    teams = {
        "Sharks":"",
        "Dragons":"",
        "Raptors":""
    }

    players1, players2 = players()

    tdict = create_teams(teams, players1, players2)

'''
# list
with open('soccer_players.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # object is generator print(reader)
    rows = list(reader)
#    print(rows)
    for line in rows:
        print(line)
        print(line[2])

Dragons = []
Sharks = []
Raptors = []
experienced_players = 0

# dict
with open('soccer_players.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    rows = list(reader)
    for line in rows[:]:
        print(line)
        # only works with dict, key value
        # print(line['Name'])
        # print(line['Height (inches)'])
        if line['Soccer Experience'] == 'YES':
            experienced_players += 1

    print(experienced_players)
'''
