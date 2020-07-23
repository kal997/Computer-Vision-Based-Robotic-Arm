import tkinter
import tkinter.font

circles_flag = False
squares_flag = False
triangles_flag = False
red_flag = False
green_flag = False
blue_flag = False


def user_input():
    """
    This function contains six function ready to be called from the user. When the user click on the desired button the
    corresponding function will be called and will change its flag to (True) then the function will destroy the GUI
    :return: Six boolean flags
    """
    def red():
        global red_flag
        red_flag = True
        print("Red")
        root.quit()

    def green():
        global green_flag
        green_flag = True
        print("Green")
        root.quit()

    def blue():
        global blue_flag
        blue_flag = True
        print("Blue")
        root.quit()

    def circles():
        global circles_flag
        circles_flag = True
        print("circles")
        root.quit()

    def squares():
        global squares_flag
        squares_flag = True
        print("squares")
        root.quit()

    def triangles():
        global triangles_flag
        triangles_flag = True
        print("triangles")
        root.quit()

    root = tkinter.Tk()
    root.title("Robotic Arm Control GUI")
    root.geometry("+890+5")
    main_label_font = tkinter.font.Font(root=root, family="Georgia", size=13, weight=tkinter.font.BOLD)
    labels_font = tkinter.font.Font(root=root,family="Georgia", size=12, weight=tkinter.font.BOLD)
    buttons_font = tkinter.font.Font(root=root,family="Georgia", size=10, weight=tkinter.font.BOLD)

    photo = tkinter.PhotoImage(file='/home/pi/Desktop/gui1.gif')
    photo_label = tkinter.Label(root,image=photo)

    space = tkinter.Label(root,text="")
    butt_tri = tkinter.Button(root, text="Triangles", bg="magenta", fg="white", command=triangles,font=buttons_font)
    butt_sq = tkinter.Button(root, text=" Squares ", bg="orange", fg="white", command=squares,font=buttons_font)
    butt_cir = tkinter.Button(root, text="  Circles  ", bg="purple", fg="white", command=circles,font=buttons_font)

    butt_red = tkinter.Button(root, text="   Red   ", bg="red", fg="white", command=red, font=buttons_font)
    butt_blue = tkinter.Button(root, text="   Blue  ", bg="blue", fg="white", command=blue, font=buttons_font)
    butt_green = tkinter.Button(root, text=" Green ", bg="green", fg="white", command=green, font=buttons_font)

    quit_button = tkinter.Button(root, text="Quit", bg="peachPuff", command=root.quit, font=buttons_font)

    general_label = tkinter.Label(root, text="\nAutonomous Sorting Robotic Arm\nPlease choose shape or color "
                                             "from the followings: \n", font=main_label_font)
    color_label = tkinter.Label(root, text="Color Sorting\n", font=labels_font)
    shape_label = tkinter.Label(root, text="Shape Sorting\n", font=labels_font)

    space.grid(row=9)
    general_label.grid(row=0, columnspan=3, ipadx=5)
    shape_label.grid(row=3, column=0, ipadx=5)
    color_label.grid(row=3, column=2, ipadx=5)

    photo_label.grid(row=2, columnspan=3)

    butt_cir.grid(row=4, column=0, ipadx=5, sticky="N"+"S"+"W"+"E")
    butt_sq.grid(row=5, column=0, ipadx=5, sticky="N"+"S"+"W"+"E")
    butt_tri.grid(row=6, column=0, ipadx=5, sticky="N"+"S"+"W"+"E")

    quit_button.grid(row=8, columnspan=3, ipadx=5)

    butt_red.grid(row=4, column=2, ipadx=5, sticky="N"+"S"+"W"+"E")
    butt_blue.grid(row=5, column=2, ipadx=5, sticky="N"+"S"+"W"+"E")
    butt_green.grid(row=6, column=2, ipadx=5, sticky="N"+"S"+"W"+"E")

    root.mainloop()
    return triangles_flag, squares_flag, circles_flag, red_flag, green_flag, blue_flag
