white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]
hello= {1:2,2:3,3:4,4:5,6:7,7:8} 
dis = pygame_display_set_mode(800, 600)
game_over = False
 
x1 = 300
y1 = 300
 
x1_change = 0       
y1_change = 0
 
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
 
