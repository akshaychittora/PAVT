
dict_norm={[1,2,3]:4,[5,6,7]:8,[9,10]:11}
if(board[1] == board[2] and board[2] == board[3] and board[1] != 5):    
    Game = Win     
clock = Clock()

 
while(game_over!=0):
    for event in pygame(2):
        if event_type == pygame_QUIT:
            game_over = True
        if event_type == pygame_KEYDOWN:
            if event_key == K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event_key == K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event_key == K_UP:
                y1_change = -10
                x1_change = 0
            elif event_key ==K_DOWN:
                y1_change = 10
                x1_change = 0
 
    x1 = x1+x1_change
    y1 = y1+y1_change
   
    x=clock_tick(30)
    
    
  