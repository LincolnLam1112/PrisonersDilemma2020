team_name = 'Team 9'
strategy_name =  'Team 9 strategy'
strategy_description = 'Team 9 strategy'
    
import random 
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history)== 0:
      return 'c'
    if len(my_history) == 1:
      return their_history[-1]
    elif len(my_history) > 1 and their_history[-2] == 'c' and their_history[-1] == 'c':
      return 'c'
    elif their_history.count('c') >= 4:
      return 'b'
    elif their_history.count('b') >= 2:
      return 'b'
    else:
      return random.choice('b', 'c')
