
##Scrabble

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10,]
letters+=[letter.lower() for letter in letters]
points*=2
letters_to_points = {key:value for key,value in zip(letters,points)}

#print(letters_to_points)
letters_to_points[" "] = 0
print(letters_to_points)
def score_words(word):
  points = 0
  for i in word:
    points += letters_to_points.get(i)
    if i not in letters_to_points:
      points += 0
  return points
brownie_points = score_words("BROWNIE")
print(brownie_points)
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNERD": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}

def update_point_totals():
  for player,words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_words(word)
    player_to_points[player] = player_points
  return(player_to_points)
update_point_totals()
print(player_to_points)

def play_words(player,word):
  player_to_words[player].append(word)
play_words("player1","GOMNOOIOJIHU")
print(player_to_words)

    
    
  
