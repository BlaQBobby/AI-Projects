import numpy as np
import math

class Game():
    def __init__(self,board_size,players):
        self.board_size=board_size
        self.players=players
        self.game_state=None
        self.human_player='X'
        self.AI_player='O'
        self.current_player=None
        
        
    def initialize(self):
        self.game_state=['.'] * self.board_size
        
    def switch_player(self,player):
        self.current_player=self.human_player if player==self.AI_player else self.AI_player
        return self.current_player
        
    def set_current_player(self,player):
        if player == 'Human':
            self.current_player=self.human_player
        else:
            self.current_player=self.AI_player
            
    def play_move(self,move,player):
        move=int(move)-1
        self.game_state[move]=player
            

human='X'
AI='O'
#DEFINE THE SCORE DICTIONARY FOR HUMAN AND AI
SCORE_DICT={'X': -10, 'O':10}
WINPOS=[[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]

#if '__name__' == '__main__':

    
def winning_positions(game_state,player):
    win=False
    for position in WINPOS:
        if game_state[position[0]]==player and game_state[position[1]]==player and game_state[position[2]]==player:
            win=True
    return win
    
def printable_board(game_state):
    return np.array(game_state).reshape(3,3)

def get_user_move(possible_moves):
    valid_options=possible_moves
    validity = False
    while not (validity):
        decision=input('Make your move: (options 1 to 9)''\t')
        if decision not in valid_options:
              print('Not a valid move. Response should be between (1 & 9) and not currently played')
        else:
            validity=True
            return decision
            
def get_empty_cells(current_state):
    game_state=current_state
    potential_moves=[]
    for i,options in enumerate(game_state):
        if options=='.':
            potential_moves+=str(i+1)
    return potential_moves

def play_move(game_state, current_player, move):
    move=int(move)-1
    game_state[move]=current_player
    return game_state
        
                
def minimax_function(game_state,current_player,possible_moves):
    result=None
    moves=[]
    move_scores={}
    for potential_move in possible_moves:
        empty_cells=list(possible_moves)
        running_game_state=list(game_state)
        new_game_state=play_move(running_game_state, current_player,potential_move)
        #print(new_game_state,current_player)
        moves+=potential_move
        #print('Current moves list: %s' % str([x for x in moves]))
        is_win=winning_positions(new_game_state,current_player)
        if is_win:
            move_scores[potential_move]=SCORE_DICT[current_player]
            #print('After appending new score: Score Dictionary is: '); print(move_scores.items())
        elif not is_win:
            empty_cells.remove(potential_move)
            if len(empty_cells) == 0:
                move_scores[potential_move]=0
            elif len(empty_cells) != 0:
                next_player=AI if current_player==human else human
                potential_move=moves[(len(moves)-1)]
                move_scores[potential_move],_=minimax_function(new_game_state,next_player,empty_cells)
    if current_player==human:
        result=10000
        cell_return=''
        for cell,score in move_scores.items():
             if score < result:
                result=score
                cell_return=cell
                outcome=(result,cell_return)    
              
    elif current_player==AI:
        result=-10000
        for cell,score in move_scores.items():
            if score > result:
                result=score
                cell_return=cell
                outcome=(result,cell_return)
    #print(move_scores.items(),current_player)
    return outcome
    
def play_game(current_game, current_player):
    game_active=True
    game_play={}
    move_score=None
    move=None
    
    while game_active:
        possible_moves=[]
        possible_moves=get_empty_cells(current_game.game_state)
        print('Possible Moves: ');print(possible_moves)
        if len(possible_moves)==1:
            game_active=False
        if current_game.current_player==human:
            user_move=get_user_move(possible_moves)
            current_game.play_move(user_move,human)
            game_play[human]=user_move
            print('\n\n'); print(np.array(current_game.game_state).reshape(3,3))
        elif current_game.current_player==AI:
            AI_playground=list(current_game.game_state)
            move_score,move=minimax_function(AI_playground,AI,possible_moves)
            print('Move and score for AI: '); print(move,move_score)
            current_game.play_move(move,AI)
            print('After AI played, current game state: '); print(current_game.game_state)
            print('\n\n'); print(np.array(current_game.game_state).reshape(3,3))
            game_play[AI]=move
        is_win=winning_positions(current_game.game_state,current_game.current_player)
        if is_win and current_game.current_player==human:
            print('Never knew You Humans were this good.')
            break
        if is_win and current_game.current_player==AI:
            print('Humans are fickle. We\'ll dominate you lot soon. AI wins.')
            break
        current_game.switch_player(current_game.current_player)    
    if not is_win: 
        print('You managed a draw. Not bad for a human to be honest.')
    print("Game Over")
       

current_game=Game(9,2)
current_game.initialize()

decision_made=False

while not (decision_made):
    decision=input('Would you like to go first? (y/n)')
    if decision.upper()=='Y' or decision.upper()=='N':
        decision=decision.upper()
        decision_made=True
    else:
        print('Not a valid response. Response should be Y or N')
    current_game.set_current_player('Human') if decision=='Y' else current_game.set_current_player('AI')

play_game(current_game,current_game.current_player)

