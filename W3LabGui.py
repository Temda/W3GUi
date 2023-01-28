'''
Author  : Chaiyapon Sowanna
STD ID  : 1650702473
Week    : 3
Label   : Class Activity| Lab3 Home
Desc    : Basic GUI #2
Date    : 2023-01-24 / Due January 30, 2023 11:59 PM
'''
from tkinter import *
from tkinter import messagebox

COLOR_BLUE = '#D0E4FD'
COLOR_DARK_BLUE = '#133674'
COLOR_LIGHT_YELLOW = '#fef2cc'
COLOR_SEA_BLUE = '#66AAC3'
COLOR_WHITE = '#ffffff'
COLOR_GREEN = '#53A551'
COLOR_YELLOW = '#fec105'
COLOR_RED = '#db3444'
COLOR_BROWN = '#b89445'
COLOR_ORANGE = '#F1C397'

def mainwindow() :
    root = Tk()
    root.title("Dashboard by Chaiyapon Sowanna")
    root.geometry("950x650")
    root.configure(bg='lightgreen')
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=4)
    root.rowconfigure(2,weight=1)
    root.columnconfigure(0,weight=2)
    root.columnconfigure(1,weight=1)
    return(root)

def createframe(root) :
    fm_top = Frame(root,bg=COLOR_LIGHT_YELLOW)
    fm_top.grid_propagate(0)
    fm_top.rowconfigure(0,weight=1)
    fm_top.columnconfigure(0,weight=1)

    fm_left = Frame(root,bg=COLOR_WHITE)
    fm_left.rowconfigure(0,weight=3)
    fm_left.rowconfigure(1,weight=2)
    fm_left.columnconfigure((0,1,2,3), weight=1)
    fm_left.grid_propagate(0)

    fm_right = Frame(root,bg=COLOR_BLUE)
    fm_right.rowconfigure(0,weight=1)
    fm_right.columnconfigure(0,weight=1)
    fm_right.grid_propagate(0)

    fm_bottom = Frame(root, bg=COLOR_SEA_BLUE)
    fm_bottom.columnconfigure((0,1,2,3), weight=1)
    fm_bottom.rowconfigure((0,2), weight=1)
    fm_bottom.rowconfigure(1, weight=2)

    fm_top.grid(row=0,columnspan=2,sticky='news')
    fm_left.grid(row=1,column=0,sticky='news')
    fm_right.grid(row=1,column=1,sticky='news')
    fm_bottom.grid(row=2, column=0, columnspan=2, sticky=NSEW)
    return(root,fm_top,fm_left,fm_right, fm_bottom)

def widgettop(top):
    lbl_title = Label(top,text = 'Dashboard by Chaiyapon Sowanna', font='Tahoma 22', bg=COLOR_BLUE, fg=COLOR_DARK_BLUE)
    lbl_title.grid(row=0, column=0, sticky=NSEW, ipadx=10, ipady=10)

def widgetleft(left) :
    lbl_profile = Label(left, image=img_profile, bg=COLOR_WHITE, highlightbackground=COLOR_WHITE, height=300)
    lbl_profile.grid(row=0, column=0,columnspan=2, sticky=W, ipadx=5, ipady=5,padx=10,pady=10,rowspan=2)

    txt_info = Text(left, height=1, width=20, font='Tahoma 16', fg=COLOR_BROWN, bg=COLOR_LIGHT_YELLOW, background=COLOR_WHITE, borderwidth=0, border=0, relief=SOLID, highlightbackground=COLOR_WHITE)
    txt_info.grid(row=0,column=1,rowspan=2,sticky=NSEW,padx=42,pady=10,ipadx=100,ipady=100,columnspan=3)


    txt_skill1 = get_text_widget(fm_left, '28', 'Age', COLOR_GREEN)
    txt_skill1.grid(row=2,column=0, ipadx=10,ipady=30)

    txt_skill2 = get_text_widget(fm_left, '55', 'Weight', COLOR_YELLOW)
    txt_skill2.grid(row=2,column=1, ipadx=10,ipady=30)

    
    txt_skill3 = get_text_widget(fm_left, '160', 'Height', COLOR_SEA_BLUE)
    txt_skill3.grid(row=2,column=2, ipadx=10,ipady=30)

    txt_skill4 = get_text_widget(fm_left, '5', 'Skill', COLOR_RED)
    txt_skill4.grid(row=2,column=3, ipadx=10,ipady=30)


def widgetright(right) :

    text = Label(right, text = 'My English Skill', font='Tahoma 22', bg=COLOR_WHITE, fg=COLOR_DARK_BLUE)
    text.grid(row=2, column=1, padx=5,ipadx=50,ipady=5)
# sticky='w',padx=20,ipadx=30,ipady=200
    lbl_skill = Label(right, image=img_skill, background=COLOR_WHITE, borderwidth=0, border=0)
    lbl_skill.grid(row=3, column=1, padx=0,pady=5, ipady=30)

def widgetbottom(bottom) :
    click1 = Button(bottom,text="Click me 1",command=fnclick1, highlightbackground=COLOR_ORANGE, bg=COLOR_ORANGE, background=COLOR_ORANGE, height=3, width=10)
    click1.grid(row=1,column=0,padx=5,pady=5)

    click2 = Button(bottom,text="Click me 2",command=fnclick2, highlightbackground=COLOR_ORANGE, bg=COLOR_ORANGE, background=COLOR_ORANGE, height=3, width=10)
    click2.grid(row=1,column=1,padx=5,pady=5)

    click3 = Button(bottom,text="Click me 3",command=fnclick3, highlightbackground=COLOR_ORANGE, bg=COLOR_ORANGE, background=COLOR_ORANGE, height=3, width=10)
    click3.grid(row=1,column=2,padx=5,pady=5)


    click4 = Button(bottom,text="Exit Program",command=fnQuit, highlightbackground=COLOR_ORANGE, bg=COLOR_ORANGE, background=COLOR_ORANGE, height=3, width=10)
    click4.grid(row=1,column=3,padx=5,pady=5)



def get_text_widget(parent, key, value, color = COLOR_RED):
    txt = Text(parent, height=1, highlightbackground=COLOR_WHITE, bg=color, bd=1, border=1, borderwidth=1)
    txt.tag_config('value', font='Tahoma 22 bold', foreground='#fff', justify=CENTER)
    txt.tag_config('key', font='Tahoma 18', foreground='#fff', justify=CENTER)
    txt.insert(END, key, 'value')
    txt.insert(END, '\n' + value, 'key')
    txt.configure(state=DISABLED)
    return txt

def fnclick1() :
    messagebox.showinfo("Chaiyapon said:", "Click me 1 clicked")


def fnclick2() :
    messagebox.showinfo("Chaiyapon said:", "Click me 2 clicked")

def fnclick3() :
    messagebox.showinfo("Chaiyapon said:", "Click me 3 clicked")

def fnQuit():
    quit()

root = mainwindow()
root, fm_top, fm_left, fm_right, fm_bottom = createframe(root)

img_profile = PhotoImage(file='images/female.png').subsample(3,3)
img_skill = PhotoImage(file='images/skill.png')

widgettop(fm_top)
widgetleft(fm_left)
widgetright(fm_right)
widgetbottom(fm_bottom)

root.mainloop()