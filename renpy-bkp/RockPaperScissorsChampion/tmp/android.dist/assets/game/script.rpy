init python:
    import random
###############################
#MODEL
###############################
    if persistent.hi_score is None:
        persistent.hi_score = set()

    if persistent.ending is None:
        persistent.ending = set()

    def merge_hi_scores(old, new, current):
        current.update(old)
        current.update(new)
        
    def merge_endings(old, new, current):
        current.update(old)
        current.update(new)

    renpy.register_persistent('hi_score', merge_hi_scores)

    renpy.register_persistent('ending', merge_endings)

    if isinstance(persistent.hi_score, int):
        hi_score = persistent.hi_score
    else:
        hi_score = 0
        
    def rsp_game(player,opponent):
        evaluation = [player, opponent]
        evaluation.sort()
        rock_win=['rock','scissors']
        paper_win=['paper','rock']
        scissors_win=['paper','scissors']

        if evaluation == rock_win:
                winner = 'rock'
        elif evaluation == paper_win:
                winner = 'paper'
        elif evaluation == scissors_win:
                winner = 'scissors'
        else:
                winner = ''
        return winner
        
    def opponent_turn(lvl,enemy_combs, array):
        possible_choices=('rock','scissors','paper')
        move = random.choice(possible_choices)
        if lvl < 1:
            way = random.randint(0,1)
            if way == 0:
                move = 'rock'
            else:
                move = random.choice(possible_choices)
        elif lvl > 1:
            chk_len = len(enemy_combs)
            if chk_len >1:
                if enemy_combs[0] == enemy_combs[1]:
                    move = enemy_combs[1]
            else:
                mr = array.count('rock')
                ms = array.count('scissors')
                mp = array.count('paper')
                array_m=[mr,ms,mp]
                array_m.sort()
                array_m.reverse()
                for wm in possible_choices:
                    win = rsp_game(array_m[0],wm)
                    if wm == win:
                        move = win
        else:
            move = random.choice(possible_choices)
        return move
        
    def combo_manager(move, array):
        array.insert(0, move)
        x = len(array)
        if x > 3:
            array.pop(3)
            
    def check_combo(array):
        #combo definitions
        rock_combo = ['rock','rock','rock']
        scissors_combo = ['scissors','scissors','scissors']
        paper_combo = ['paper','paper','paper']

        #combo identification
        if array == rock_combo:
            return 'StoneWall'
        elif array == scissors_combo:
            return 'TwinBlades'
        elif array == paper_combo:
            return 'PaperThinMind'
        else:
            return ''
    def find_winner(plyr_move):
        move_list=['rock','scissors','paper']
        for move in move_list:
            win = rsp_game(plyr_move,move)
            if move == win:
                return move
###############################
#VIEW
###############################        
    def rsp_buttons():
        ui.hbox(xalign=0.2 , yalign=0.98)
        ui.imagebutton("img/btn-rock.png","img/btn-rock.png", clicked=ui.returns('rock'))
        ui.close()
        
        ui.hbox(xalign=0.5 , yalign=0.98)
        ui.imagebutton("img/btn-paper.png","img/btn-paper.png", clicked=ui.returns('paper'))
        ui.close()
        
        ui.hbox(xalign=0.8 , yalign=0.98)
        ui.imagebutton("img/btn-scissors.png","img/btn-scissors.png", clicked=ui.returns('scissors'))
        ui.close()
        
    def outcome_buttons():
        ui.hbox(xalign=0.5 , yalign=0.3)
        #ui.textbutton("[winner_text]\nUndefeated Streak:[undefeated]\nPoints for this Round:[point_bonus]", clicked=ui.returns(''))
        ui.text("{size=+24}[winner_text]{/size}")
        ui.close()
        
    def score():
        ui.vbox(xalign=0.1, yalign=0.0)
        ui.text("Score: [your_points]")
        ui.close()

        ui.vbox(xalign=0.9, yalign=0.0)
        ui.text("Hi Score: [hi_score]")
        ui.close()
        
        ui.vbox(xalign=0.05, yalign=0.11)
        ui.text("PLAYER")
        ui.close()

        ui.vbox(xalign=0.95, yalign=0.11)
        ui.text("[enemy_name]")
        ui.close()

#################################
#hero sprite
#################################
image hero:
    "img/hero.png"
    xalign 0.1
    yalign 0.35
image hero2:
    "img/hero2.png"
    xalign 0.1
    yalign 0.35
image hero_pre:
    "img/hero-pre.png"
    xalign 0.24
    yalign 0.32
image hero_extend:
    "img/hero-extend.png"
    xalign 0.27
    yalign 0.4
image hero_arm:
    "img/hero-arm.png"
    xalign 0.27
    yalign 0.4
image hero_rock:
    "img/hero-rock.png"
    xalign 0.35
    yalign 0.4
image hero_paper:
    "img/hero-paper.png"
    xalign 0.35
    yalign 0.4
image hero_scissors:
    "img/hero-scissors.png"
    xalign 0.35
    yalign 0.4
#################################
#rocky sprite
#################################
image rocky:
    "img/rocky.png"
    xalign 0.9
    yalign 0.35
image rocky_pre:
    "img/rocky-pre.png"
    xalign 0.75
    yalign 0.33
image rocky_extend:
    "img/rocky-extend.png"
    xalign 0.75
    yalign 0.4
image rocky_arm:
    "img/rocky-arm.png"
    xalign 0.74
    yalign 0.4
image rocky_rock:
    "img/rocky-rock.png"
    xalign 0.66
    yalign 0.4
image rocky_paper:
    "img/rocky-paper.png"
    xalign 0.66
    yalign 0.4
image rocky_scissors:
    "img/rocky-scissors.png"
    xalign 0.66
    yalign 0.4
image rocky_sign:
    "img/rocky-sign.png"
    xalign 0.87
    yalign 0.22
#################################
#randy sprite
#################################
image randy:
    "img/randy.png"
    xalign 0.93
    yalign 0.35
image randy_pre:
    "img/randy-pre.png"
    xalign 0.77
    yalign 0.33
image randy_extend:
    "img/randy-extend.png"
    xalign 0.77
    yalign 0.4
image randy_arm:
    "img/randy-arm.png"
    xalign 0.74
    yalign 0.4
image randy_rock:
    "img/randy-rock.png"
    xalign 0.66
    yalign 0.4
image randy_paper:
    "img/randy-paper.png"
    xalign 0.66
    yalign 0.4
image randy_scissors:
    "img/randy-scissors.png"
    xalign 0.66
    yalign 0.4
image randy_sign:
    "img/randy-sign.png"
    xalign 0.87
    yalign 0.22
#################################
#ripley sprite
#################################
image ripley:
    "img/ripley.png"
    xalign 0.93
    yalign 0.35
image ripley_pre:
    "img/ripley-pre.png"
    xalign 0.71
    yalign 0.33
image ripley_extend:
    "img/ripley-extend.png"
    xalign 0.71
    yalign 0.4
image ripley_arm:
    "img/ripley-arm.png"
    xalign 0.69
    yalign 0.4
image ripley_rock:
    "img/ripley-rock.png"
    xalign 0.6
    yalign 0.38
image ripley_paper:
    "img/ripley-paper.png"
    xalign 0.6
    yalign 0.38
image ripley_scissors:
    "img/ripley-scissors.png"
    xalign 0.6
    yalign 0.38
image ripley_sign:
    "img/ripley-sign.png"
    xalign 0.7
    yalign 0.22
#################################
#combo markers
#################################
image combo_hero_0_r:
    "img/combo-hero-rock.png"
    xalign 0.05
    yalign 0.98
image combo_hero_0_p:
    "img/combo-hero-paper.png"
    xalign 0.05
    yalign 0.98
image combo_hero_0_s:
    "img/combo-hero-scissors.png"
    xalign 0.05
    yalign 0.98
image combo_hero_0_n:
    "img/combo-none.png"
    xalign 0.05
    yalign 0.98
image combo_hero_1_r:
    "img/combo-hero-rock.png"
    xalign 0.05
    yalign 0.88
image combo_hero_1_p:
    "img/combo-hero-paper.png"
    xalign 0.05
    yalign 0.88
image combo_hero_1_s:
    "img/combo-hero-scissors.png"
    xalign 0.05
    yalign 0.88
image combo_hero_1_n:
    "img/combo-none.png"
    xalign 0.05
    yalign 0.88
image combo_hero_2_r:
    "img/combo-hero-rock.png"
    xalign 0.05
    yalign 0.78
image combo_hero_2_p:
    "img/combo-hero-paper.png"
    xalign 0.05
    yalign 0.78
image combo_hero_2_s:
    "img/combo-hero-scissors.png"
    xalign 0.05
    yalign 0.78
image combo_hero_2_n:
    "img/combo-none.png"
    xalign 0.05
    yalign 0.78
########################################
image combo_enemy_0_r:
    "img/combo-enemy-rock.png"
    xalign 0.95
    yalign 0.98
image combo_enemy_0_p:
    "img/combo-enemy-paper.png"
    xalign 0.95
    yalign 0.98
image combo_enemy_0_s:
    "img/combo-enemy-scissors.png"
    xalign 0.95
    yalign 0.98
image combo_enemy_0_n:
    "img/combo-none.png"
    xalign 0.95
    yalign 0.98
image combo_enemy_1_r:
    "img/combo-enemy-rock.png"
    xalign 0.95
    yalign 0.88
image combo_enemy_1_p:
    "img/combo-enemy-paper.png"
    xalign 0.95
    yalign 0.88
image combo_enemy_1_s:
    "img/combo-enemy-scissors.png"
    xalign 0.95
    yalign 0.88
image combo_enemy_1_n:
    "img/combo-none.png"
    xalign 0.95
    yalign 0.88
image combo_enemy_2_r:
    "img/combo-enemy-rock.png"
    xalign 0.95
    yalign 0.78
image combo_enemy_2_p:
    "img/combo-enemy-paper.png"
    xalign 0.95
    yalign 0.78
image combo_enemy_2_s:
    "img/combo-enemy-scissors.png"
    xalign 0.95
    yalign 0.78
image combo_enemy_2_n:
    "img/combo-none.png"
    xalign 0.95
    yalign 0.78
#########################################
image energy_hero_bar:
    "img/life-bar.png"
    xalign 0.03
    yalign 0.045
image energy_hero_hp10:
    "img/life-unit.png"
    xalign 0.025
    yalign 0.05
image energy_hero_hp9:
    "img/life-unit.png"
    xalign 0.06
    yalign 0.05
image energy_hero_hp8:
    "img/life-unit.png"
    xalign 0.095
    yalign 0.05
image energy_hero_hp7:
    "img/life-unit.png"
    xalign 0.13
    yalign 0.05
image energy_hero_hp6:
    "img/life-unit.png"
    xalign 0.165
    yalign 0.05
image energy_hero_hp5:
    "img/life-unit.png"
    xalign 0.198
    yalign 0.05
image energy_hero_hp4:
    "img/life-unit.png"
    xalign 0.233
    yalign 0.05
image energy_hero_hp3:
    "img/life-unit.png"
    xalign 0.268
    yalign 0.05
image energy_hero_hp2:
    "img/life-unit.png"
    xalign 0.302
    yalign 0.05
image energy_hero_hp1:
    "img/life-unit.png"
    xalign 0.337
    yalign 0.05
#########################################
image energy_enemy_bar:
    "img/life-bar.png"
    xalign 0.95
    yalign 0.045
image energy_enemy_hp10:
    "img/life-unit.png"
    xalign 0.96
    yalign 0.05
image energy_enemy_hp9:
    "img/life-unit.png"
    xalign 0.925
    yalign 0.05
image energy_enemy_hp8:
    "img/life-unit.png"
    xalign 0.89
    yalign 0.05
image energy_enemy_hp7:
    "img/life-unit.png"
    xalign 0.855
    yalign 0.05
image energy_enemy_hp6:
    "img/life-unit.png"
    xalign 0.82
    yalign 0.05
image energy_enemy_hp5:
    "img/life-unit.png"
    xalign 0.785
    yalign 0.05
image energy_enemy_hp4:
    "img/life-unit.png"
    xalign 0.75
    yalign 0.05
image energy_enemy_hp3:
    "img/life-unit.png"
    xalign 0.715
    yalign 0.05
image energy_enemy_hp2:
    "img/life-unit.png"
    xalign 0.68
    yalign 0.05
image energy_enemy_hp1:
    "img/life-unit.png"
    xalign 0.647
    yalign 0.05
#########################################

screen btn:
    $rsp_buttons()

screen outcome:
    $outcome_buttons()

screen score:
    $score()
image bg arena="img/arena.png"
image bg rules="img/rules.png"

image vs rocky ="img/VS1.png"
image vs randy ="img/VS2.png"
image vs ripley ="img/VS3.png"

image screen_bg="img/title2.png"

image combo_h_r:
    "img/hero-wall.png"
    xalign 0.3
    yalign 0.52
image combo_e_r:
    "img/enemy-wall.png"
    xalign 0.7
    yalign 0.52
image combo_e_p:
    "img/enemy-balloon.png"
    xalign 0.65
    yalign 0.15
image combo_e_p_p:
    "img/combo-enemy-paper.png"
    xalign 0.63
    yalign 0.17
image combo_e_p_s:
    "img/combo-enemy-scissors.png"
    xalign 0.63
    yalign 0.17
image combo_e_p_r:
    "img/combo-enemy-rock.png"
    xalign 0.63
    yalign 0.17
image combo_h_p:
    "img/hero-balloon.png"
    xalign 0.35
    yalign 0.15
image combo_h_p_p:
    "img/combo-hero-paper.png"
    xalign 0.37
    yalign 0.17
image combo_h_p_s:
    "img/combo-hero-scissors.png"
    xalign 0.37
    yalign 0.17
image combo_h_p_r:
    "img/combo-hero-rock.png"
    xalign 0.37
    yalign 0.17

image combo_h_s:
    "img/hero-cut.png"
    xalign 0.25 yalign 0.52
    linear 0.3 xalign 0.75
    "img/white.png"
    pause 0.3
    
image combo_e_s:
    "img/enemy-cut.png"
    xalign 0.75 yalign 0.52
    linear 0.3 xalign 0.25
    "img/white.png"
    pause 0.3
  
image white_flash:
    "img/white.png"
  
image end1:
    'img/end1.png'
    
image end2:
    'img/end2.png'
    
image end1zoom:
    'img/end1z.png'
    
image end2zoom:
    'img/end2z.png'
    
# The game starts here.
label start:
    scene bg rules
    python:
        is_music_playing = renpy.music.is_playing(channel='music')
        if is_music_playing == False:
            renpy.music.play('media/rpscLoop.ogg')
        if isinstance(persistent.hi_score, int):
            hi_score = persistent.hi_score
        else:
            hi_score = 0
        #disables right-click
        _game_menu_screen = None
        your_points = 0
        winner_text = "NO WINNERS!"
        undefeated = 0
        point_bonus = 0
        hero_hp = 10
        enemy_hp = 10
        ##
        opponent_level=0
        enemy_name = "ROCKY"
        ##
        hero_combo=[]
        enemy_combo=[]
        pre_fight_loop=0
        hero_dbl_atk = False
        enemy_dbl_atk = False
        enemy_reveal = False
        hero_reveal = False
        enemy_def = False
        hero_def = False
        is_hero_combo = ''
        is_enemy_combo = ''
        cnt_move=[]
    
label pre_fight:    
    scene black
    play sound 'media/win.wav'
    if opponent_level == 0:
        show vs rocky
        pause
    elif opponent_level == 1:
        show vs randy
        pause
    else:
        show vs ripley
        pause
    
label game_start:
    python:
        if len(hero_combo) == 2 and hero_reveal == False:
            if hero_combo[0]==hero_combo[1]:
                opponent = find_winner(hero_combo[1])
        else:
            opponent = opponent_turn(opponent_level,enemy_combo, cnt_move)
        #if enemy_reveal == True:
            #renpy.say(None, "[opponent]")
        #enemy_reveal = False
    scene bg arena
    if enemy_reveal == True:
        play sound 'media/mind.wav'
        show combo_e_p
        if opponent == 'paper':
            show combo_e_p_p
        elif opponent == 'rock':
            show combo_e_p_r
        else:
            show combo_e_p_s
    #hide screen outcome
    show screen score
    
    show hero_pre
    if not persistent.ending:
        show hero
    else:
        show hero2
    #################################
    #rocky sprite
    #################################
    if opponent_level==0:
        show rocky_pre
        show rocky
        #if opponent == "rock":
            #show rocky_sign
    #################################
    #randy sprite
    #################################
    elif opponent_level==1:
        show randy_pre
        show randy
        #if opponent == "paper":
            #show randy_sign
    #################################
    #ripley sprite
    #################################
    elif opponent_level==2:
        show ripley_pre
        show ripley
        #if opponent == "scissors":
            #show rocky_sign
    #show combos here
    if hero_def == True:
        play sound 'media/rock.wav'
        show combo_h_r
    if enemy_def == True:
        play sound 'media/rock.wav'
        show combo_e_r
    
    show screen btn
    ##############################
    $ len_hero_combo = len(hero_combo)
    show combo_hero_0_n
    show combo_hero_1_n
    show combo_hero_2_n
    if len_hero_combo >0:
        hide combo_hero_0_n
        if hero_combo[0]== 'rock':
            show combo_hero_0_r
        elif hero_combo[0]== 'scissors':
            show combo_hero_0_s
        elif hero_combo[0]== 'paper':
            show combo_hero_0_p
    if len_hero_combo >1:
        hide combo_hero_1_n
        if hero_combo[1]== 'rock':
            show combo_hero_1_r
        elif hero_combo[1]== 'scissors':
            show combo_hero_1_s
        elif hero_combo[1]== 'paper':
            show combo_hero_1_p
    if len_hero_combo >2:
        hide combo_hero_2_n
        if hero_combo[2]== 'rock':
            show combo_hero_2_r
        elif hero_combo[2]== 'scissors':
            show combo_hero_2_s
        elif hero_combo[2]== 'paper':
            show combo_hero_2_p
    $ len_enemy_combo = len(enemy_combo)
    show combo_enemy_0_n
    show combo_enemy_1_n
    show combo_enemy_2_n
    if len_enemy_combo >0:
        hide combo_enemy_0_n
        if enemy_combo[0]== 'rock':
            show combo_enemy_0_r
        elif enemy_combo[0]== 'scissors':
            show combo_enemy_0_s
        elif enemy_combo[0]== 'paper':
            show combo_enemy_0_p
    if len_enemy_combo >1:
        hide combo_enemy_1_n
        if enemy_combo[1]== 'rock':
            show combo_enemy_1_r
        elif enemy_combo[1]== 'scissors':
            show combo_enemy_1_s
        elif enemy_combo[1]== 'paper':
            show combo_enemy_1_p
    if len_enemy_combo >2:
        hide combo_enemy_2_n
        if enemy_combo[2]== 'rock':
            show combo_enemy_2_r
        elif enemy_combo[2]== 'scissors':
            show combo_enemy_2_s
        elif enemy_combo[2]== 'paper':
            show combo_enemy_2_p
    ##############################
    show energy_hero_bar
    if hero_hp > 9:
        show energy_hero_hp10
    if hero_hp > 8:
        show energy_hero_hp9
    if hero_hp > 7:
        show energy_hero_hp8
    if hero_hp > 6:
        show energy_hero_hp7
    if hero_hp > 5:
        show energy_hero_hp6
    if hero_hp > 4:
        show energy_hero_hp5
    if hero_hp > 3:
        show energy_hero_hp4
    if hero_hp > 2:
        show energy_hero_hp3
    if hero_hp > 1:
        show energy_hero_hp2
    if hero_hp > 0:
        show energy_hero_hp1
    ##########################
    show energy_enemy_bar
    if enemy_hp > 9:
        show energy_enemy_hp10
    if enemy_hp > 8:
        show energy_enemy_hp9
    if enemy_hp > 7:
        show energy_enemy_hp8
    if enemy_hp > 6:
        show energy_enemy_hp7
    if enemy_hp > 5:
        show energy_enemy_hp6
    if enemy_hp > 4:
        show energy_enemy_hp5
    if enemy_hp > 3:
        show energy_enemy_hp4
    if enemy_hp > 2:
        show energy_enemy_hp3
    if enemy_hp > 1:
        show energy_enemy_hp2
    if enemy_hp > 0:
        show energy_enemy_hp1
    ##############################
    python:
        player = ui.interact()
        if enemy_reveal == False and hero_dbl_atk == False and hero_def == False:
            combo_manager(player,hero_combo)
        if hero_reveal == False and enemy_dbl_atk == False and enemy_def == False:
            combo_manager(opponent,enemy_combo)
        if hero_reveal == True:
            renpy.sound.play('media/mind.wav')
            opponent = find_winner(player)
            if enemy_reveal == True:
                opponent = player
        #hero_reveal = False
        enemy_reveal = False
        pre_fight_loop=2
    
    if hero_reveal == True:
        show combo_h_p
        if player == 'rock':
            show combo_h_p_r
        elif player == 'paper':
            show combo_h_p_p
        else:
            show combo_h_p_s
        pause 2.0
        hide combo_h_p
        hide combo_h_p_p
        hide combo_h_p_r
        hide combo_h_p_s
        $hero_reveal = False
    
label pre_throw:
    while pre_fight_loop > 0:
        hide hero
        hide hero_pre
        show hero_extend
        if not persistent.ending:
            show hero
        else:
            show hero2
        #################################
        #rocky sprite
        #################################
        if opponent_level==0:
            hide rocky_pre
            hide rocky
            show rocky_extend
            show rocky
        #################################
        #randy sprite
        #################################
        elif opponent_level==1:
            hide randy_pre
            hide randy
            show randy_extend
            show randy
        #################################
        #ripley sprite
        #################################
        elif opponent_level==2:
            hide ripley_pre
            hide ripley
            show ripley_extend
            show ripley
        pause 0.1
        
        hide hero
        hide hero_extend
        show hero_pre
        if not persistent.ending:
            show hero
        else:
            show hero2
        #################################
        #rocky sprite
        #################################
        if opponent_level==0:
            hide rocky_extend
            hide rocky
            show rocky_pre
            show rocky
        #################################
        #randy sprite
        #################################
        elif opponent_level==1:
            hide randy_extend
            hide randy
            show randy_pre
            show randy
        #################################
        #ripley sprite
        #################################
        elif opponent_level==2:
            hide ripley_extend
            hide ripley
            show ripley_pre
            show ripley
        pause 0.1
        
        $pre_fight_loop-=1

label hero_throw:
        
    hide hero
    hide hero_pre
    show hero_arm
    if not persistent.ending:
        show hero
    else:
        show hero2
    if player == "rock":
        show hero_rock
    elif player == "scissors":
        show hero_scissors
    elif player == "paper":
        show hero_paper
    
    pause 0.1
    hide ripley_pre
    hide rocky_pre
    hide randy_pre
    #################################
    #rocky sprite
    #################################
    if opponent_level==0:
        show rocky_arm
        if opponent == "rock":
            show rocky_rock
        elif opponent == "scissors":
            show rocky_scissors
        elif opponent == "paper":
            show rocky_paper
    #################################
    #randy sprite
    #################################
    elif opponent_level==1:
        show randy_arm
        if opponent == "rock":
            show randy_rock
        elif opponent == "scissors":
            show randy_scissors
        elif opponent == "paper":
            show randy_paper
    #################################
    #ripley sprite
    #################################
    elif opponent_level==2:
        show ripley_arm
        if opponent == "rock":
            show ripley_rock
        elif opponent == "scissors":
            show ripley_scissors
        elif opponent == "paper":
            show ripley_paper
    pause 0.2
    
label combo_anima:
    ##############################
    $ len_hero_combo = len(hero_combo)
    if len_hero_combo >0:
        if hero_combo[0]== 'rock':
            show combo_hero_0_r
        elif hero_combo[0]== 'scissors':
            show combo_hero_0_s
        elif hero_combo[0]== 'paper':
            show combo_hero_0_p
    if len_hero_combo >1:
        if hero_combo[1]== 'rock':
            show combo_hero_1_r
        elif hero_combo[1]== 'scissors':
            show combo_hero_1_s
        elif hero_combo[1]== 'paper':
            show combo_hero_1_p
    if len_hero_combo >2:
        if hero_combo[2]== 'rock':
            show combo_hero_2_r
        elif hero_combo[2]== 'scissors':
            show combo_hero_2_s
        elif hero_combo[2]== 'paper':
            show combo_hero_2_p
    $ len_enemy_combo = len(enemy_combo)
    if len_enemy_combo >0:
        if enemy_combo[0]== 'rock':
            show combo_enemy_0_r
        elif enemy_combo[0]== 'scissors':
            show combo_enemy_0_s
        elif enemy_combo[0]== 'paper':
            show combo_enemy_0_p
    if len_enemy_combo >1:
        if enemy_combo[1]== 'rock':
            show combo_enemy_1_r
        elif enemy_combo[1]== 'scissors':
            show combo_enemy_1_s
        elif enemy_combo[1]== 'paper':
            show combo_enemy_1_p
    if len_enemy_combo >2:
        if enemy_combo[2]== 'rock':
            show combo_enemy_2_r
        elif enemy_combo[2]== 'scissors':
            show combo_enemy_2_s
        elif enemy_combo[2]== 'paper':
            show combo_enemy_2_p
    ##############################
    $is_hero_combo = check_combo(hero_combo)
    $is_enemy_combo = check_combo(enemy_combo)
    if is_hero_combo == 'StoneWall':
        show combo_h_r
    if is_hero_combo != '':
        $point_bonus = 200
        play sound 'media/combo.wav'
        centered "{size=+24}PLAYER'S COMBO:\n[is_hero_combo]\n\n\n\n\n\n{/size}"
    if is_enemy_combo == 'StoneWall':
        show combo_e_r
    if is_enemy_combo != '':
        play sound 'media/combo.wav'
        centered "{size=+24}[enemy_name]'S COMBO:\n[is_enemy_combo]\n\n\n\n\n\n{/size}"
    python:
        if is_hero_combo != '':
            hero_combo=[]
            if is_hero_combo == 'StoneWall':
                hero_def = True
            elif is_hero_combo == 'TwinBlades':
                hero_dbl_atk = True
            elif is_hero_combo == 'PaperThinMind':
                enemy_reveal = True
            is_hero_combo = ''
        if is_enemy_combo != '':
            enemy_combo=[]
            if is_enemy_combo == 'StoneWall':
                enemy_def = True
            elif is_enemy_combo == 'TwinBlades':
                enemy_dbl_atk = True
            elif is_enemy_combo == 'PaperThinMind':
                hero_reveal = True
            is_enemy_combo = ''
            
label combo_anima_intro:
    if hero_dbl_atk == True:
        show combo_h_s
        play sound 'media/fire.wav'
        pause 1.5
        hide combo_h_s
    if enemy_dbl_atk == True:
        show combo_e_s
        play sound 'media/fire.wav'
        pause 1.5
        hide combo_e_s

label results:
    hide screen btn
    python:
        winner=rsp_game(player,opponent)
        cnt_move.append(player)
        if player==winner:
            undefeated += 1
            point_bonus = 100 * undefeated
            your_points += point_bonus
            if your_points > hi_score:
                hi_score = your_points
            renpy.sound.play('media/win.wav')
            winner_text = "YOU WIN!"
            if enemy_def != True:
                enemy_hp -= 1
            enemy_def = False
            if enemy_dbl_atk == True:
                if hero_def == True:
                    hero_def = False
                else:
                    hero_hp -= 1
                enemy_dbl_atk = False
            if hero_dbl_atk == True:
                enemy_hp -= 1
                hero_dbl_atk = False
        elif opponent==winner:
            undefeated = 0
            point_bonus = 0
            renpy.sound.play('media/lose.wav')
            winner_text = "YOU LOSE!"
            if hero_def != True:
                hero_hp -= 1
            hero_def = False
            if hero_dbl_atk == True:
                if enemy_def == True:
                    enemy_def = False
                else:
                    enemy_hp -= 1
                hero_dbl_atk = False
            if enemy_dbl_atk == True:
                hero_hp -= 1
                enemy_dbl_atk = False
        else:
            point_bonus = 0
            renpy.sound.play('media/lose.wav')
            winner_text = "NO WINNERS..."
            if hero_def != True:
                hero_hp -= 1
            hero_def = False
            if enemy_def != True:
                enemy_hp -= 1
            enemy_def = False
            if hero_dbl_atk == True:
                if enemy_def == True:
                    enemy_hp -= 1
                    enemy_def = False
                else:
                    enemy_hp -= 2
                hero_dbl_atk = False
            if enemy_dbl_atk == True:
                if hero_def == True:
                    hero_hp -= 1
                    hero_def = False
                else:
                    hero_hp -= 2
                enemy_dbl_atk = False
                
    ##############################
    show energy_hero_bar
    hide energy_hero_hp10
    hide energy_hero_hp9
    hide energy_hero_hp8
    hide energy_hero_hp7
    hide energy_hero_hp6
    hide energy_hero_hp5
    hide energy_hero_hp4
    hide energy_hero_hp3
    hide energy_hero_hp2
    hide energy_hero_hp1
    if hero_hp > 9:
        show energy_hero_hp10
    if hero_hp > 8:
        show energy_hero_hp9
    if hero_hp > 7:
        show energy_hero_hp8
    if hero_hp > 6:
        show energy_hero_hp7
    if hero_hp > 5:
        show energy_hero_hp6
    if hero_hp > 4:
        show energy_hero_hp5
    if hero_hp > 3:
        show energy_hero_hp4
    if hero_hp > 2:
        show energy_hero_hp3
    if hero_hp > 1:
        show energy_hero_hp2
    if hero_hp > 0:
        show energy_hero_hp1
    ##############################
    show energy_enemy_bar
    hide energy_enemy_hp10
    hide energy_enemy_hp9
    hide energy_enemy_hp8
    hide energy_enemy_hp7
    hide energy_enemy_hp6
    hide energy_enemy_hp5
    hide energy_enemy_hp4
    hide energy_enemy_hp3
    hide energy_enemy_hp2
    hide energy_enemy_hp1
    if enemy_hp > 9:
        show energy_enemy_hp10
    if enemy_hp > 8:
        show energy_enemy_hp9
    if enemy_hp > 7:
        show energy_enemy_hp8
    if enemy_hp > 6:
        show energy_enemy_hp7
    if enemy_hp > 5:
        show energy_enemy_hp6
    if enemy_hp > 4:
        show energy_enemy_hp5
    if enemy_hp > 3:
        show energy_enemy_hp4
    if enemy_hp > 2:
        show energy_enemy_hp3
    if enemy_hp > 1:
        show energy_enemy_hp2
    if enemy_hp > 0:
        show energy_enemy_hp1
    ##############################
    show screen outcome
    pause
    $game_win = False
    if enemy_hp <= 0:
        python:
            opponent_level+=1
            hero_hp = 10
            if opponent_level== 1:
                enemy_name = "RANDY"
                #enemy_name = "ANDY"
            elif opponent_level== 2:
                enemy_name = "RIPLEY"
            elif opponent_level > 2:
                game_win = True
            is_enemy_combo = ''
            is_hero_combo = ''
            enemy_combo = []
            hero_combo = []
            hero_dbl_atk = False
            enemy_dbl_atk = False
            enemy_reveal = False
            hero_reveal = False
            enemy_def = False
            hero_def = False
    elif hero_hp <= 0:
        jump ending
        #pass
        
label combo_anima_end:
    if hero_def == False:
        hide combo_h_r
    if enemy_def == False:
        hide combo_e_r
        
    hide screen outcome
    hide screen score
    if game_win == True:
        jump end_screen
    elif enemy_hp <= 0:
        $enemy_hp = 10
        jump pre_fight
    else:
        jump game_start

label ending:
    $ persistent.hi_score = hi_score
    hide screen outcome
    hide screen score
    show screen_bg  
    play sound 'media/end.wav'
    menu:
        "{size=+32}GAME OVER{/size}":
            jump start
        "START AGAIN?":
            jump start
        "QUIT":
            return
            #renpy.full_restart()
    
label end_screen:
    $ persistent.hi_score = hi_score
    hide screen outcome
    hide screen score
    if not persistent.ending:
        show end1
        "{size=+10}YOU ARE THE TRUE ROCK PAPER SCISSORS CHAMPION{/size}"
        "{size=+10}You've proved once and for all your superiority over the Triple R Gang by beating them in their own game!{/size}"
        show end1zoom
        "{size=+10}After collecting the prize money, you decide to spend it all...{/size}"
        show end2zoom
        "{size=+10}...in reconstructive plastic surgery. Now you've got your old looks back! Now play the game again, you sexy fellow!{/size}"
        $ persistent.ending = True
    else:
        show end2
        "{size=+10}YOU ARE THE TRUE ROCK PAPER SCISSORS CHAMPION AGAIN!{/size}"
        "{size=+10}Once again, you have proved your superiority. However, you feel hollow inside.{/size}"
        show end2zoom
        "{size=+10}Attributing the malady inside your soul to vanity...{/size}"
        show end1zoom
        "{size=+10}...you self-harm till you go back to your old looks. Now play the game again, you ascetic hero!{/size}"
        $ persistent.ending = False
    return

label splashscreen:   
    $ renpy.movie_cutscene('media/intro.mkv')
    return