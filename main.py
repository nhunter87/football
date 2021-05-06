# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Part 1
#spelers
player_0 = 'Ruud Gullit'
player_1 = 'Marco van Basten' 

#in welke minuut er gescored is
goal_0 = 32
goal_1 = 54

#wie scoorde er wanneer
scorers = player_0+''+str(goal_0)+', '+player_1+''+str(goal_1)
print(scorers)

report=f'{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute'
print(report)

#Part 2
player = 'Igor Belanov'
first_name = player [:4]
print(first_name)

last_name_len = player [5:12]
print(last_name_len)

name_short = player [0:1]+'. '+ player [5:12]
print(name_short)

chant = 'Igor! ' * 4
print(chant.strip(''))

good_chant = chant[12:] != 'Igor'
print(good_chant)