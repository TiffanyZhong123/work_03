from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    r = open(fname,"r").read().strip().split('\n')
    print(r)
    x = 0
    while(x < len(r)):
        cmd = r[x]
        print(cmd)
        if(cmd == "line"):
            x+=1
            coords = map(int,r[x].split(' '))
            add_edge(points,coords[0],coords[1],coords[2],coords[3],coords[4],coords[5])
        elif(cmd == "ident"):
            ident(transform)
        elif(cmd == "scale"):
            x+=1
            coords = map(int,r[x].split(' '))
            matrix_mult(make_scale(coords[0],coords[1],coords[2]),transform)
        elif(cmd == "translate"):
            x+=1
            coords = map(int,r[x].split(' '))
            matrix_mult(make_translate(coords[0],coords[1],coords[2]),transform)
        elif(cmd == "rotate"):
            x+=1
            coords = r[x].split(' ')
            if(coords[0]=='x'):
                matrix_mult(make_rotX(int(coords[1])),transform)
            elif(coords[0]=='y'):
                matrix_mult(make_rotY(int(coords[1])),transform)
            else:
                matrix_mult(make_rotZ(int(coords[1])),transform)
        elif(cmd == "apply"):
            matrix_mult(transform,points)
        elif(cmd == "display"):
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
        elif(cmd == "save"):
            clear_screen(screen)
            draw_lines(points,screen,color)
            x+=1
            save_ppm(screen,r[x])
            save_extension(screen,r[x])
        elif(cmd == "quit"):
            return
        x += 1
