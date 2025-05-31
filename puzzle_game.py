"""
    CS5001
    Fall 2022
    final_project: puzzle_game
    Zhanpeng Tong
    This is a final project to creat a puzzle game by python

"""

import turtle
import os
import time
import math
import random
import glob

def screen_open():  # open the screen
    turtle.setup(800, 800)
    turtle.title("CS5001 Silding Puzzle Game by Zhanpeng Tong")
    draw_frame(-350, 320, 500, 450, 'black', 8)  # play area
    draw_frame(120, 320, 500, 230, 'blue', 6)  # leader board
    draw_frame(-350, -230, 100, 700, 'black', 8)  # Status area
    write(130, 290, 'Leaders:', 'blue', 25)  # show 'Leaders:' on screen
    turtle.up()
    turtle.ht()


def input_name():
    # use textinput let user input there name
    name = turtle.textinput('CS5001 Puzzle Slide', 'Your Name:')
    return str(name)


def input_moves():
    """
        let user input a int number between 5, 200
        that is the user max move time, if user can't win the game
        before that. the game will also lose.
    """
    info = 'CS5001 Puzzle Slide'
    info2 = 'Enter the number of move (chances) you want (5-200)'
    moves = turtle.numinput(info, info2, None, 5, 200)
    return int(moves)


def leader():
    # loading the rank on the leader board
    try:
        with open('leader.txt', "r") as file:
            lines = file.readlines()
            for i in range(len(lines)):
                if i > 10:  # keep the name on the rank is 10
                    break
                info = lines[i]
                location = (230 - 30 * i)  # change line location if name more that one.
                write(130, location, info, 'blue', 22)
    except FileNotFoundError:
        return None


def save_rank(name, step):
    f = open('leader.txt', mode='a')
    f.write(str(step) + ':' + str(name) + '\n')
    f.close()


def splash_screen():
    # display the splash_screen image for 3 seconds
    turtle.setup(800, 800)
    turtle.title("CS5001 Silding Puzzle Game by Zhanpeng Tong")
    current_directory = os.getcwd()
    os.chdir(current_directory + '/Resources')
    turtle.Screen().addshape('splash_screen.gif')
    turtle.shape('splash_screen.gif')
    time.sleep(3)
    turtle.clearscreen()
    os.chdir(current_directory)


def quit_button_image():
    # display the quit button image in right place and
    # calls exit_program when user clicks on the area show quit image
    current_directory = os.getcwd()
    os.chdir(current_directory + '/Resources')
    quits = turtle.Turtle()
    wn = turtle.Screen()
    quits.up()
    quits.ht()
    wn.addshape('quitbutton.gif')
    quits.goto(280, -275)
    quits.down()
    quits.st()
    quits.shape('quitbutton.gif')
    os.chdir(current_directory)
    quits.onclick(exit_program)


def load_button_image():
    # display the button on screen and return the turtle object
    # called load when user clicks on the area show load image
    current_directory = os.getcwd()
    os.chdir(current_directory + '/Resources')
    load = turtle.Turtle()
    wn = turtle.Screen()
    load.up()
    load.ht()
    wn.addshape('loadbutton.gif')
    load.goto(180, -275)
    load.down()
    load.st()
    load.shape('loadbutton.gif')
    os.chdir(current_directory)
    return load


def reset_button_image():
    # display the button on screen and return the turtle object
    # called reset when user clicks on the area show reset image
    current_directory = os.getcwd()
    os.chdir(current_directory + '/Resources')
    reset = turtle.Turtle()
    wn = turtle.Screen()
    reset.up()
    reset.ht()
    wn.addshape('resetbutton.gif')
    reset.goto(75, -275)
    reset.down()
    reset.st()
    reset.shape('resetbutton.gif')
    os.chdir(current_directory)
    return reset


def write(x, y, string, pen_color, font_size):
    # print string at (x,y) also can change pen_color and font size.
    writes = turtle.Turtle()
    writes.color(pen_color)
    writes.up()
    writes.ht()
    writes.goto(x, y)
    writes.down()
    writes.st()
    writes.write(string, font=('Arial', font_size, 'normal'))
    writes.up()
    writes.ht()


def write_move(x, y, string, pen_color, font_size, write_turtle):
    # show and update the total number of user success move the puzzle.
    write_turtle.color(pen_color)
    write_turtle.up()
    write_turtle.ht()
    write_turtle.goto(x, y)
    write_turtle.down()
    write_turtle.st()
    write_turtle.write(string, font=('Arial', font_size, 'normal'))
    write_turtle.up()
    write_turtle.ht()


def draw_frame(x, y, length, width, color, pensize):
    """
        draw a frame from left-top corner at point(x,y) with length and width
        pen's color and pensize can change.
    """
    turtle.up()
    turtle.ht()
    turtle.speed(0)
    turtle.pencolor(color)
    turtle.pensize(pensize)
    turtle.goto(x, y)
    turtle.down()
    turtle.st()
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
    turtle.up()
    turtle.ht()


def directive_info(filename='mario.puz'):
    """
        function will return all information about puzzle.
        user can choose puzzle that user choose.
        default puzzle is 'mario.puz'
    """
    try:
        with open(filename, mode='r') as file:
            puz_list = []
            info_list = []
            list_ = []
            turtle_name = []
            tile_location = []
            for each in file:
                new_list = []
                x = each.split(': ')
                for element in x:
                    new_list.append(element)
                for i in range(len(new_list)):
                    new_list[i] = new_list[i].strip('\n')
                list_.append(new_list)
            for i in range(len(list_)):
                if i <= 3:
                    info_list.append(list_[i])
                else:
                    puz_list.append(list_[i])
            i_num = 0  # is the real num of image's name on file.
            for i in range(len(puz_list)):
                i_num += 1
                turtle_name.append(puz_list[i][0])
                tile_location.append(puz_list[i][1])
            # size = the area for one piece of puzzle(tile)
            size = int(info_list[2][1])
            # Add a small gap of width 2 between each tiles
            resize = size + 2
            number = int(info_list[1][1])
            number_of_images = math.sqrt(number)
            # checks image_filenames's number is equal number provide on file.
            # also check the number of images is 4, 9, 16.
            if int(number_of_images + 0.5) ** 2 != number or number != i_num:
                display_file_error()
            return puz_list, info_list, turtle_name, tile_location, size, resize
    except Exception as msg:  # Save Error info
        display_file_error()
        f = open("5001_puzzle.err.txt", "a")
        f.write(str(msg) + '\n')
        f.close()


def display_file_error():
    '''
        display the file_error.gif to the user
    '''
    current_directory = os.getcwd()
    os.chdir(current_directory + '/Resources')
    error = turtle.Turtle()
    wn = turtle.Screen()
    error.up()
    error.ht()
    error.goto(0, 0)
    error.down()
    error.st()
    wn.addshape('file_error.gif')
    error.shape('file_error.gif')
    time.sleep(3)
    error.ht()
    os.chdir(current_directory)


def load_puz(turtles, tile_location, pic, move_list):
    """
        the function load the puzzle pieces that user picked
    """
    puz_list = []
    current_directory = os.getcwd()
    # add files ends with .puz to puz_list
    for name in glob.glob(current_directory + '/*.puz'):
        puz_list.append(name.split('/')[-1])
    # if there are more than 10 files show the warning
    if len(puz_list) > 10:
        os.chdir(current_directory + '/Resources')
        turtle.up()
        turtle.ht()
        turtle.goto(0, 0)
        turtle.down()
        turtle.st()
        turtle.Screen().addshape('file_warning.gif')
        turtle.shape('file_warning.gif')
        time.sleep(3)
    info_t = 'Load Puzzle'
    info_c = 'Enter the name of puzzle of choice: ' + '\n' + '\n'.join(puz_list)
    puz_of_choice = turtle.textinput(info_t, info_c)
    os.chdir(current_directory)
    # hide the previous thumbnail gif
    pic.ht()
    # turtle.clear()
    # hide the previous puzzle pieces
    for each in turtles:
        each.ht()
    # reinitialize player move to 0
    move_list[0] = 0
    puz, info, turtle_name, tile_location, size, resize = directive_info(puz_of_choice)
    pic = attach_thumbnail(info[3][1])
    turtles = shuffled_tiles(tile_location, turtle_name, size, resize, move_list)
    load = load_button_image()
    load_button(turtles, tile_location, load, pic, move_list)
    reset = reset_button_image()
    reset_button(turtles, tile_location, reset)


def attach_thumbnail(thumbnail):
    # the function attach the thumbnail gif
    thumbnail_location = str(thumbnail)
    pic = turtle.Turtle()
    wn = turtle.Screen()
    pic.up()
    pic.ht()
    wn.addshape(thumbnail_location)
    pic.goto(330, 280)
    pic.down()
    pic.st()
    pic.shape(thumbnail_location)
    return pic


def check_blank(current, neighbor, move_list):
    # the function checks if the tile's neighbors is blank, if yes then swap places
    if "blank.gif" in neighbor.shape():
        target_shape = current.shape()
        current.shape(neighbor.shape())
        neighbor.shape(target_shape)
        move_list[1].clear()
        move_list[0] += 1
        # when swap is successful then add the move by 1
        write_move(-310, -290, f'player moves: {move_list[0]} / ' + \
                   f'{move_list[2]}', 'black', 20, move_list[1])


def swap_tile(turtl, resize, turtles, tile_location, move_list):
    """
        the function provide information: neighbor of the tiles user choose
        then run check_blank().
    """
    pair = turtl.pos()  # use one turtle that carries the image(x, y)
    # defines the "neighbors" for the click point
    left = (pair[0] - resize, pair[1])
    right = (pair[0] + resize, pair[1])
    top = (pair[0], pair[1] + resize)
    down = (pair[0], pair[1] - resize)
    for each in turtles:
        # check do have blank in those 'neighbors'
        if each.pos() == right:
            check_blank(turtl, each, move_list)
        elif each.pos() == left:
            check_blank(turtl, each, move_list)
        elif each.pos() == top:
            check_blank(turtl, each, move_list)
        elif each.pos() == down:
            check_blank(turtl, each, move_list)
    i = 0
    for i in range(len(turtles)):
        # compare the pattern to the ordered pattern if not the same break
        if turtles[i].shape() != tile_location[i]:
            break
        # continue otherwise
        else:
            i += 1
    # if puzzle is solved then display winner.gif
    if i == len(turtles):
        save_rank(move_list[3], move_list[0])
        current_directory = os.getcwd()
        os.chdir(current_directory + '/Resources')
        turtle.goto(0, 0)
        turtle.down()
        turtle.st()
        turtle.Screen().addshape('winner.gif')
        turtle.shape('winner.gif')
        time.sleep(3)
        os.chdir(current_directory)
        turtle.clearscreen()
        turtle.bye()
    # if puzzle is unsolved within the move specified, then display lose.gif
    if move_list[0] == move_list[2]:
        current_directory = os.getcwd()
        os.chdir(current_directory + '/Resources')
        turtle.goto(0, 0)
        turtle.down()
        turtle.st()
        turtle.Screen().addshape('Lose.gif')
        turtle.shape('Lose.gif')
        time.sleep(2)
        turtle.Screen().addshape('credits.gif')
        turtle.shape('credits.gif')
        time.sleep(3)
        os.chdir(current_directory)
        turtle.clearscreen()
        turtle.bye()


def shuffled_tiles(tile_location, turtle_name, size, resize, move_list):
    # shuffle the tiles and display the shuffled puzzle pieces for user to play.
    wn = turtle.Screen()
    turtles = []  # different turtle objects
    shuffled_tile = tile_location.copy()  # made a copy, so OG dont get changed
    random.shuffle(shuffled_tile)  # shuffle the list
    length = int(math.sqrt(len(shuffled_tile)))
    for each in tile_location:
        wn.addshape(each)
    for each in turtle_name:
        each = turtle.Turtle()
        turtles.append(each)
    x_pos = -280
    y_pos = 250
    a = 0
    # the two for loops gives the layers of the puzzle 4x4 3x3 or 2x2
    for i in range(length):
        turtles[a].up()
        turtles[a].ht()
        turtles[a].goto(0, y_pos)
        turtles[a].down()
        turtles[a].st()
        for j in range(length):
            turtles[a].speed(0)
            turtles[a].up()
            turtles[a].ht()
            turtles[a].goto(x_pos, y_pos)
            turtles[a].down()
            turtles[a].st()
            turtles[a].shape(shuffled_tile[a])  # Attach image

            def click(x, y, tile=turtles[a]):
                return swap_tile(tile, resize, turtles, tile_location, \
                                 move_list)

            turtles[a].onclick(click)
            # draw broders around the tiles
            a += 1
            x_pos += resize
        x_pos = -280
        y_pos -= resize
    turtle.up()
    turtle.ht()
    return turtles


def reset_button(turtles, tile_location, reset):
    # run reset function when user clicks on the reset image
    reset.onclick(lambda x, y: resets(turtles, tile_location))


def resets(turtles, tile_location):
    # unscramble the puzzle
    i = 0
    # attach the image in a ordered pattern
    for each in turtles:
        each.shape(tile_location[i])
        i += 1


def load_button(turtles, tile_location, load, pic, move_list):
    # run the function load_puz when user click on load image
    # load.onclick(lambda x, y: open_clean())
    load.onclick(lambda x, y: load_puz(turtles, tile_location, pic, move_list))

                 
def exit_program(x, y):
    # show 'quitmsg' image on screen and quit game.
    current_directory = os.getcwd()
    os.chdir(current_directory + '/Resources')
    wn = turtle.Screen()
    turtle.up()
    turtle.ht()
    turtle.goto(0, 0)
    turtle.down()
    turtle.st()
    wn.addshape('quitmsg.gif')
    turtle.shape('quitmsg.gif')
    time.sleep(3)
    os.chdir(current_directory)
    turtle.clearscreen()
    turtle.bye()


def main():
    splash_screen()
    name = input_name()
    write_turtle = turtle.Turtle()
    moves = input_moves()
    move_list = [0, write_turtle, moves, name]
    screen_open()
    leader()
    quit_button_image()
    load = load_button_image()
    reset = reset_button_image()
    puz, info, turtle_name, tile_location, size, resize = directive_info()
    pic = attach_thumbnail(info[3][1])
    turtles = shuffled_tiles(tile_location, turtle_name, size, resize, move_list)
    load_button(turtles, tile_location, load, pic, move_list)
    reset_button(turtles, tile_location, reset)


if __name__ == "__main__":
    main()
