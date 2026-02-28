from pyscript import display, document
# python for project

def team_checker(e):
    document.getElementById('leader').innerHTML = ' '
    document.getElementById('output').innerHTML = ' '

    regiment_team = document.getElementById('Regiment').value
    leader = ['Keith Shadis', 'Dot Pixis', 'Erwin Smith', 'Nile Dok']
    training_corps = ['Samuel', 'Daz', 'Sandra', 'Gordon', 'Hanna', 'Ruth', 'Tom', 'Thomas', 'Milieus', 'Mina', 'Nack', 'Franz']
    garrison = ['Anka', 'Hugo', 'Rico', 'Ian', 'Mitabi', 'Hannes', 'Lobov', 'Gustav', 'Phil', 'Kitz', 'Carsten', 'Caleb Matig-a']
    scout = ['Eren', 'Mikasa', 'Armin', 'Sasha', 'Connie', 'Jean', 'Reiner', 'Bertholdt', 'Hange', 'Nanaba', 'Miche', 'Christa', 'Levi']
    mp = ['Annie', 'Marlo', 'Hitch', 'Djel', 'Traute', 'Ralph', 'Duran', 'Kenny', 'Boris', 'Waltz', 'Arianne Aguilar']

    #checks which regiment members should be displayed
    if regiment_team == "Train":
        #displays leader before loop to avoid looping the leader
        display('Your Commander is:', leader[0], target='leader')
        for team in training_corps:
            display(team, target='output')

    elif regiment_team == "Garrison":
        display('Your Commander is:', leader[1], target='leader')
        for team in garrison:
            display(team, target='output')
    
    elif regiment_team == "Scout":
        display('Your Commander is:', leader[2], target='leader')
        for team in scout:
            display(team, target='output')

    elif regiment_team == "MP":
        display('Your Commander is:', leader[3], target='leader')
        for team in mp:
            display(team, target='output')