import pygame
from PIL import ImageTk as PILImageTk, Image as PILImage
import datetime
import win32com.client as wincl
import win32gui
from pywinauto import application
import time
from tkinter import *
from tkinter.filedialog import *
import tkinter as tk
import tkinter.font as font
import pyautogui as pg


# app = application.Application()
# app.start("Notepad.exe")
# app.Notepad.edit.type_keys("")


# class Window(tk.Frame):
#     def __init__(self, master=None):
#         tk.Frame.__init__(self, master, takefocus="")
#         self.master = master


class HButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self["text"] = None

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground


root = Tk()
root.title("On-screen Keyboard")
root.iconbitmap("images/keyboard.ico")
root.configure(bg="Black")
root.resizable(0, 0)

myFont = font.Font(family="Jetbrains Mono", weight="bold", size=10)
smallFont = font.Font(family="Jetbrains Mono", weight="bold", size=8)
spaceFont = font.Font(family="", size=10)

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

speaker = wincl.Dispatch("Sapi.SpVoice")
wsh = wincl.Dispatch("WScript.Shell")

letters = 'abcdefghijklmnopqrstuvwxyz'
alphanumeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4',
                '5', '6', '7', '8', '9', '0']

timetoday = datetime.date.today()

pressed = False

Open = PILImage.open("images/winkey.png")

resized = Open.resize((60, 54), PILImage.ANTIALIAS)

win_key = PILImageTk.PhotoImage(resized)


# Commands
# user = input(": ")

def play():
    pygame.mixer.music.load("audio/keyboard.mp3")
    pygame.mixer.music.play(loops=0)


def button_click(char=None):
    hwnd = win32gui.FindWindowEx(0, 0, 0, "*Untitled - Notepad")
    win32gui.SetForegroundWindow(hwnd)
    # win32gui.SetFocus(hwnd)
    # wsh.SendKeys(char)
    pg.press(char)


def narrate(char=None):
    speaker.Speak(char)


def ctrl():
    button_left_ctrl.config(state=DISABLED, relief=SUNKEN)
    button_right_ctrl.config(state=DISABLED, relief=SUNKEN)


def narrate_on():
    button_narrate_on.config(state=DISABLED)
    button_narrate_off.config(state=NORMAL)
    # Row 1
    button_f1.config(command=lambda: [narrate("F1"), button_click("f1")])
    button_f2.config(command=lambda: [narrate("F2"), button_click("f2")])
    button_f3.config(command=lambda: [narrate("F3"), button_click("f3")])
    button_f4.config(command=lambda: [narrate("F4"), button_click("f4")])
    button_f5.config(command=lambda: [narrate("F5"), button_click("f5")])
    button_f6.config(command=lambda: [narrate("F6"), button_click("f6")])
    button_f7.config(command=lambda: [narrate("F7"), button_click("f7")])
    button_f8.config(command=lambda: [narrate("F8"), button_click("f8")])
    button_f9.config(command=lambda: [narrate("F9"), button_click("f9")])
    button_f10.config(command=lambda: [narrate("F10"), button_click("f10")])
    button_f11.config(command=lambda: [narrate("F11"), button_click("f11")])
    button_f12.config(command=lambda: [narrate("F12"), button_click("f12")])
    # # Row 2
    button_esc.config(command=lambda: [narrate("Escape"), button_click("escape")])
    button_backtick.config(command=lambda: [narrate("Backtick"), button_click("`")])
    button_1.config(command=lambda: [narrate("1"), button_click("1")])
    button_2.config(command=lambda: [narrate("2"), button_click("2")])
    button_3.config(command=lambda: [narrate("3"), button_click("3")])
    button_4.config(command=lambda: [narrate("4"), button_click("4")])
    button_5.config(command=lambda: [narrate("5"), button_click("5")])
    button_6.config(command=lambda: [narrate("6"), button_click("6")])
    button_7.config(command=lambda: [narrate("7"), button_click("7")])
    button_8.config(command=lambda: [narrate("8"), button_click("8")])
    button_9.config(command=lambda: [narrate("9"), button_click("9")])
    button_0.config(command=lambda: [narrate("0"), button_click("0")])
    button_minus_underscore.config(command=lambda: [narrate("minus"), button_click("-")])
    button_add_equal.config(command=lambda: [narrate("add"), button_click("+")])
    button_backspace.config(command=lambda: [narrate("backspace"), button_click("backspace")])
    # Row 3
    button_tab.config(command=lambda: [narrate("Tab"), button_click("tab")])
    button_q.config(command=lambda: [narrate("q"), button_click("q")])
    button_w.config(command=lambda: [narrate("w"), button_click("w")])
    button_e.config(command=lambda: [narrate("e"), button_click("e")])
    button_r.config(command=lambda: [narrate("r"), button_click("r")])
    button_t.config(command=lambda: [narrate("t"), button_click("t")])
    button_y.config(command=lambda: [narrate("y"), button_click("y")])
    button_u.config(command=lambda: [narrate("u"), button_click("u")])
    button_i.config(command=lambda: [narrate("i"), button_click("i")])
    button_o.config(command=lambda: [narrate("o"), button_click("o")])
    button_p.config(command=lambda: [narrate("p"), button_click("p")])
    button_square_curly_brackets_in.config(command=lambda: [narrate("square brackets in"), button_click("[")])
    button_square_curly_brackets_out.config(command=lambda: [narrate("square brackets out"), button_click("]")])
    button_backslash.config(command=lambda: [narrate("\\"), button_click("\\")])
    button_del.config(command=lambda: [narrate("del"), button_click("del")])
    # Row 4
    button_Caps.config(command=lambda: [narrate("Capslock"), button_click("capslock")])
    button_a.config(command=lambda: [narrate("a"), button_click("a")])
    button_s.config(command=lambda: [narrate("s"), button_click("s")])
    button_d.config(command=lambda: [narrate("d"), button_click("d")])
    button_f.config(command=lambda: [narrate("f"), button_click("f")])
    button_g.config(command=lambda: [narrate("g"), button_click("g")])
    button_h.config(command=lambda: [narrate("h"), button_click("h")])
    button_j.config(command=lambda: [narrate("j"), button_click("j")])
    button_k.config(command=lambda: [narrate("k"), button_click("k")])
    button_l.config(command=lambda: [narrate("l"), button_click("l")])
    button_semi_colon.config(command=lambda: [narrate("semicolon"), button_click(";")])
    button_quote.config(command=lambda: [narrate("quote"), button_click("'")])
    button_Enter.config(command=lambda: [narrate("enter"), button_click("enter")])
    # Row 5
    button_left_shift.config(command=lambda: [narrate("left shift"), button_click("shift")])
    button_z.config(command=lambda: [narrate("z"), button_click("z")])
    button_x.config(command=lambda: [narrate("x"), button_click("x")])
    button_c.config(command=lambda: [narrate("c"), button_click("c")])
    button_v.config(command=lambda: [narrate("v"), button_click("v")])
    button_b.config(command=lambda: [narrate("b"), button_click("b")])
    button_n.config(command=lambda: [narrate("n"), button_click("n")])
    button_m.config(command=lambda: [narrate("m"), button_click("m")])
    button_comma.config(command=lambda: [narrate("comma"), button_click(",")])
    button_dot.config(command=lambda: [narrate("dot"), button_click(".")])
    button_slash.config(command=lambda: [narrate("slash"), button_click("/")])
    button_up_arrow.config(command=lambda: [narrate("Up"), button_click("up")])
    button_right_shift.config(command=lambda: [narrate("right shift"), button_click("shift")])
    # Row 6
    button_fn.config(command=lambda: [narrate("fn"), button_click("fn")])
    button_left_ctrl.config(command=lambda: [narrate("left control"), button_click("ctrl")])
    button_win_key.config(command=lambda: [narrate("win key"), button_click("win")])
    button_left_alt.config(command=lambda: [narrate("left alt"), button_click("alt")])
    button_space.config(command=lambda: [narrate("space"), button_click("space")])
    button_right_alt.config(command=lambda: [narrate("right alt"), button_click("alt")])
    button_right_ctrl.config(command=lambda: [narrate("right control"), button_click("ctrl")])
    button_left_arrow.config(command=lambda: [narrate("Left"), button_click("left")])
    button_down_arrow.config(command=lambda: [narrate("Down"), button_click("down")])
    button_right_arrow.config(command=lambda: [narrate("Right"), button_click("right")])
    button_menu.config(command=lambda: [narrate("menu"), button_click("menu")])
    # if keyboard.is_pressed("a"):
    #     speaker.Speak("a")
    # if HButton['state'] == ACTIVE:
    #     speaker.speak(HButton['text'])


def narrate_off():
    button_narrate_off.config(state=DISABLED)
    button_narrate_on.config(state=NORMAL)
    # Row 1
    button_f1.config(command=lambda: [play(), button_click("f1")])
    button_f2.config(command=lambda: [play(), button_click("f2")])
    button_f3.config(command=lambda: [play(), button_click("f3")])
    button_f4.config(command=lambda: [play(), button_click("f4")])
    button_f5.config(command=lambda: [play(), button_click("f5")])
    button_f6.config(command=lambda: [play(), button_click("f6")])
    button_f7.config(command=lambda: [play(), button_click("f7")])
    button_f8.config(command=lambda: [play(), button_click("f8")])
    button_f9.config(command=lambda: [play(), button_click("f9")])
    button_f10.config(command=lambda: [play(), button_click("f10")])
    button_f11.config(command=lambda: [play(), button_click("f11")])
    button_f12.config(command=lambda: [play(), button_click("f12")])
    # Row 2
    button_esc.config(command=lambda: [play(), button_click("escape")])
    button_backtick.config(command=lambda: [play(), button_click("`")])
    button_1.config(command=lambda: [play(), button_click("1")])
    button_2.config(command=lambda: [play(), button_click("2")])
    button_3.config(command=lambda: [play(), button_click("3")])
    button_4.config(command=lambda: [play(), button_click("4")])
    button_5.config(command=lambda: [play(), button_click("5")])
    button_6.config(command=lambda: [play(), button_click("6")])
    button_7.config(command=lambda: [play(), button_click("7")])
    button_8.config(command=lambda: [play(), button_click("8")])
    button_9.config(command=lambda: [play(), button_click("9")])
    button_0.config(command=lambda: [play(), button_click("0")])
    button_minus_underscore.config(command=lambda: [play(), button_click("-")])
    button_add_equal.config(command=lambda: [play(), button_click("+")])
    button_backspace.config(command=lambda: [play(), button_click("backspace")])
    # Row 3
    button_tab.config(command=lambda: [play(), button_click("tab")])
    button_q.config(command=lambda: [play(), button_click("q")])
    button_w.config(command=lambda: [play(), button_click("w")])
    button_e.config(command=lambda: [play(), button_click("e")])
    button_r.config(command=lambda: [play(), button_click("r")])
    button_t.config(command=lambda: [play(), button_click("t")])
    button_y.config(command=lambda: [play(), button_click("y")])
    button_u.config(command=lambda: [play(), button_click("u")])
    button_i.config(command=lambda: [play(), button_click("i")])
    button_o.config(command=lambda: [play(), button_click("o")])
    button_p.config(command=lambda: [play(), button_click("p")])
    button_square_curly_brackets_in.config(command=lambda: [play(), button_click("[")])
    button_square_curly_brackets_out.config(command=lambda: [play(), button_click("]")])
    button_backslash.config(command=lambda: [play(), button_click("\\")])
    button_del.config(command=lambda: [play(), button_click("del")])
    # Row 4
    button_Caps.config(command=lambda: [play(), button_click("capslock")])
    button_a.config(command=lambda: [play(), button_click("a")])
    button_s.config(command=lambda: [play(), button_click("s")])
    button_d.config(command=lambda: [play(), button_click("d")])
    button_f.config(command=lambda: [play(), button_click("f")])
    button_g.config(command=lambda: [play(), button_click("g")])
    button_h.config(command=lambda: [play(), button_click("h")])
    button_j.config(command=lambda: [play(), button_click("j")])
    button_k.config(command=lambda: [play(), button_click("k")])
    button_l.config(command=lambda: [play(), button_click("l")])
    button_semi_colon.config(command=lambda: [play(), button_click(";")])
    button_quote.config(command=lambda: [play(), button_click("'")])
    button_Enter.config(command=lambda: [play(), button_click("enter")])
    # Row 5
    button_left_shift.config(command=lambda: [play(), button_click("shift")])
    button_z.config(command=lambda: [play(), button_click("z")])
    button_x.config(command=lambda: [play(), button_click("x")])
    button_c.config(command=lambda: [play(), button_click("c")])
    button_v.config(command=lambda: [play(), button_click("v")])
    button_b.config(command=lambda: [play(), button_click("b")])
    button_n.config(command=lambda: [play(), button_click("n")])
    button_m.config(command=lambda: [play(), button_click("m")])
    button_comma.config(command=lambda: [play(), button_click(",")])
    button_dot.config(command=lambda: [play(), button_click(".")])
    button_slash.config(command=lambda: [play(), button_click("/")])
    button_up_arrow.config(command=lambda: [play(), button_click("up")])
    button_right_shift.config(command=lambda: [play(), button_click("shift")])
    # Row 6
    button_fn.config(command=lambda: [play(), button_click("fn")])
    button_left_ctrl.config(command=lambda: [play(), button_click("ctrl")])
    button_win_key.config(command=lambda: [play(), button_click("win")])
    button_left_alt.config(command=lambda: [play(), button_click("alt")])
    button_space.config(command=lambda: [play(), button_click("space")])
    button_right_alt.config(command=lambda: [play(), button_click("alt")])
    button_right_ctrl.config(command=lambda: [play(), button_click("ctrl")])
    button_menu.config(command=lambda: [play(), button_click("menu")])


# Buttons


# Row 1
Date = Label(root, text=timetoday, padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
             state=DISABLED)
button_f1 = HButton(root, text="F1", padx=20, pady=13, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                    activebackground="#4e5154", takefocus=False, command=lambda: [play()])
button_f2 = HButton(root, text="F2", padx=20, pady=13, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                    activebackground="#4e5154", takefocus=False, command=lambda: [play()])
button_f3 = HButton(root, text="F3", padx=20, pady=13, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                    activebackground="#4e5154", takefocus=False, command=lambda: [play()])
button_f4 = HButton(root, text="F4", padx=20, pady=13, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                    activebackground="#4e5154", takefocus=False, command=lambda: [play()])
button_f5 = HButton(root, text="F5", padx=20, pady=13, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                    activebackground="#4e5154", takefocus=False, command=lambda: [play()])
button_f6 = HButton(root, text="F6", padx=20, pady=13, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                    activebackground="#4e5154", takefocus=False, command=lambda: [play()])
button_f7 = HButton(root, text="F7", padx=20, pady=13, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                    activebackground="#4e5154", takefocus=False, command=lambda: [play()])
button_f8 = HButton(root, text="F8", padx=20, pady=13, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                    activebackground="#4e5154", takefocus=False, command=lambda: [play()])
button_f9 = HButton(root, text="F9", padx=20, pady=13, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                    activebackground="#4e5154", takefocus=False, command=lambda: [play()])
button_f10 = HButton(root, text="F10", padx=20, pady=13, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                     activebackground="#4e5154", takefocus=False, command=lambda: [play()])
button_f11 = HButton(root, text="F11", padx=20, pady=13, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                     activebackground="#4e5154", takefocus=False, command=lambda: [play()])
button_f12 = HButton(root, text="F12", padx=20, pady=13, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                     activebackground="#4e5154", takefocus=False, command=lambda: [play()])

# Row 2
button_esc = HButton(root, text="Esc", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                     activebackground="#4e5154", takefocus=False, command=lambda: [play()])
button_backtick = HButton(root, text="~\n`", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                          activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("`")])
button_1 = HButton(root, text="!\n1", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [button_click("1"), play()])
button_2 = HButton(root, text="@\n2", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("2")])

button_3 = HButton(root, text="#\n3", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("3")])

button_4 = HButton(root, text="$\n4", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("4")])

button_5 = HButton(root, text="%\n5", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("5")])

button_6 = HButton(root, text="^\n6", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("6")])

button_7 = HButton(root, text="&\n7", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("7")])

button_8 = HButton(root, text="*\n8", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("8")])

button_9 = HButton(root, text="(\n9", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("9")])

button_0 = HButton(root, text=")\n0", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("0")])

button_minus_underscore = HButton(root, text="_\n-", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont,
                                  borderwidth=6,
                                  activebackground="#4e5154", takefocus=False,
                                  command=lambda: [play(), button_click("-")])
button_add_equal = HButton(root, text="+\n=", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                           activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("=")])
button_backspace = HButton(root, text="<--", padx=20, pady=18, bg="#2e2a2a", fg="#FFFFFF", font=smallFont,
                           borderwidth=6,
                           activebackground="#4e5154", takefocus=False,
                           command=lambda: [play(), button_click("backspace")])

# Row 3
button_tab = HButton(root, text="Tab", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                     activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("tab")])
button_q = HButton(root, text="q", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("q")])
button_w = HButton(root, text="w", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("w")])
button_e = HButton(root, text="e", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("e")])
button_r = HButton(root, text="r", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("r")])
button_t = HButton(root, text="t", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("t")])
button_y = HButton(root, text="y", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("y")])
button_u = HButton(root, text="u", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("u")])
button_i = HButton(root, text="i", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("i")])
button_o = HButton(root, text="o", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("o")])
button_p = HButton(root, text="p", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("p")])
button_square_curly_brackets_in = HButton(root, text="{\n[", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont,
                                          borderwidth=6,
                                          activebackground="#4e5154", takefocus=False,
                                          command=lambda: [play(), button_click("{")])
button_square_curly_brackets_out = HButton(root, text="}\n]", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont,
                                           borderwidth=6,
                                           activebackground="#4e5154", takefocus=False,
                                           command=lambda: [play(), button_click("}")])
button_backslash = HButton(root, text=str("|\n\\"), padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont,
                           borderwidth=6,
                           activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("\\")])
button_del = HButton(root, text="Del", padx=20, pady=18, bg="#2e2a2a", fg="#FFFFFF", font=smallFont, borderwidth=6,
                     activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("del")])

# Row 4
button_Caps = HButton(root, text="Caps", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                      activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("capslock")])
button_a = HButton(root, text="a", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("a")])
button_s = HButton(root, text="s", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("s")])
button_d = HButton(root, text="d", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("d")])
button_f = HButton(root, text="f", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("f")])
button_g = HButton(root, text="g", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("g")])
button_h = HButton(root, text="h", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("h")])
button_j = HButton(root, text="j", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("j")])
button_k = HButton(root, text="k", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("k")])
button_l = HButton(root, text="l", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("l")])
button_semi_colon = HButton(root, text=":\n;", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                            activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click(";")])
button_quote = HButton(root, text="''\n'", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                       activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("'")])
button_Enter = HButton(root, text="Enter", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                       activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("enter")])

# Row 5
button_left_shift = HButton(root, text="Shift", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont,
                            borderwidth=6,
                            activebackground="#4e5154", takefocus=False,
                            command=lambda: [play(), button_click("shift")])
button_z = HButton(root, text="z", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("z")])
button_x = HButton(root, text="x", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("x")])
button_c = HButton(root, text="c", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("c")])
button_v = HButton(root, text="v", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("v")])
button_b = HButton(root, text="b", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("b")])
button_n = HButton(root, text="n", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("n")])
button_m = HButton(root, text="m", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                   activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("m")])
button_comma = HButton(root, text="<\n,", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                       activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click(",")])
button_dot = HButton(root, text=">\n.", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                     activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click(".")])
button_slash = HButton(root, text="?\n/", padx=25, pady=6, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                       activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("/")])
button_up_arrow = HButton(root, text="↑", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                          activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("up")])
button_right_shift = HButton(root, text="Shift", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont,
                             borderwidth=6,
                             activebackground="#4e5154", takefocus=False,
                             command=lambda: [play(), button_click("shift")])

# Row 6
button_fn = HButton(root, text="fn", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                    activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("fn")])
button_left_ctrl = HButton(root, text="Ctrl", padx=17, pady=18, bg="#2e2a2a", fg="#FFFFFF", font=smallFont,
                           borderwidth=6,
                           activebackground="#4e5154", takefocus=False,
                           command=lambda: [play(), button_click("ctrl"), ctrl()])
button_win_key = HButton(root, image=win_key, padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                         activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("win")])
button_left_alt = HButton(root, text="Alt", padx=20, pady=18, bg="#2e2a2a", fg="#FFFFFF", font=smallFont, borderwidth=6,
                          activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click()])
button_space = HButton(root, text="Space", padx=124, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                       activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("space")])
button_right_alt = HButton(root, text="Alt", padx=20, pady=18, bg="#2e2a2a", fg="#FFFFFF", font=smallFont,
                           borderwidth=6,
                           activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click()])
button_right_ctrl = HButton(root, text="Ctrl", padx=17, pady=18, bg="#2e2a2a", fg="#FFFFFF", font=smallFont,
                            borderwidth=6,
                            activebackground="#4e5154", takefocus=False,
                            command=lambda: [play(), button_click("ctrl"), ctrl()])
button_left_arrow = HButton(root, text="←", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                            activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("left")])
button_down_arrow = HButton(root, text="↓", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                            activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("down")])
button_right_arrow = HButton(root, text="→", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                             activebackground="#4e5154", takefocus=False,
                             command=lambda: [play(), button_click("right")])
button_menu = HButton(root, text="≣", padx=25, pady=15, bg="#2e2a2a", fg="#FFFFFF", font=myFont, borderwidth=6,
                      activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click()])

# Navigation buttons
button_insert = HButton(root, text="Insert", padx=15, pady=18, bg="#2e2a2a", fg="#FFFFFF", font=smallFont,
                        borderwidth=6,
                        activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("insert")])
button_home = HButton(root, text="Home", padx=18, pady=18, bg="#2e2a2a", fg="#FFFFFF", font=smallFont, borderwidth=6,
                      activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("home")])
button_pg_up = HButton(root, text="Page\nup", padx=18, pady=10, bg="#2e2a2a", fg="#FFFFFF", font=smallFont,
                       borderwidth=6,
                       activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("pgup")])
button_prt_scn = HButton(root, text="Prt\nScn", padx=15, pady=10, bg="#2e2a2a", fg="#FFFFFF", font=smallFont,
                         borderwidth=6,
                         activebackground="#4e5154", takefocus=False,
                         command=lambda: [play(), button_click("prntscrn")])
button_end = HButton(root, text="End", padx=20, pady=18, bg="#2e2a2a", fg="#FFFFFF", font=smallFont, borderwidth=6,
                     activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("end")])
button_pg_down = HButton(root, text="Page\ndown", padx=18, pady=10, bg="#2e2a2a", fg="#FFFFFF", font=smallFont,
                         borderwidth=6,
                         activebackground="#4e5154", takefocus=False, command=lambda: [play(), button_click("pgdown")])
space = Label(root, text="", bg="black", font=spaceFont)

button_narrate_on = HButton(root, text="Narrate\nOn", padx=10, pady=8, bg="#2e2a2a", fg="#FFFFFF", font=smallFont,
                            borderwidth=6,
                            activebackground="#4e5154", takefocus=False, command=lambda: [play(), narrate_on()])
button_narrate_off = HButton(root, text="Narrate\nOff", padx=10, pady=8, bg="#2e2a2a", fg="#FFFFFF", font=smallFont,
                             borderwidth=6, state=DISABLED,
                             activebackground="#4e5154", takefocus=False, command=lambda: [play(), narrate_off()])

# Grid 1
Date.grid(row=1, column=0, columnspan=3, sticky="ew")
button_f1.grid(row=1, column=3, sticky="ew")
button_f2.grid(row=1, column=4, sticky="ew")
button_f3.grid(row=1, column=5, sticky="ew")
button_f4.grid(row=1, column=6)
button_f5.grid(row=1, column=7)
button_f6.grid(row=1, column=8, sticky="ew")
button_f7.grid(row=1, column=9, sticky="ew")
button_f8.grid(row=1, column=10)
button_f9.grid(row=1, column=11)
button_f10.grid(row=1, column=12, sticky="ew")
button_f11.grid(row=1, column=13, sticky="ew")
button_f12.grid(row=1, column=14, sticky="ew")

# Grid 2
button_esc.grid(row=2, column=0, sticky="ew")
button_backtick.grid(row=2, column=2, sticky="ew")
button_1.grid(row=2, column=3, sticky="ew")
button_2.grid(row=2, column=4, sticky="ew")
button_3.grid(row=2, column=5, sticky="ew")
button_4.grid(row=2, column=6, sticky="ew")
button_5.grid(row=2, column=7, sticky="ew")
button_6.grid(row=2, column=8, sticky="ew")
button_7.grid(row=2, column=9, sticky="ew")
button_8.grid(row=2, column=10, sticky="ew")
button_9.grid(row=2, column=11, sticky="ew")
button_0.grid(row=2, column=12, sticky="ew")
button_minus_underscore.grid(row=2, column=13, sticky="ew")
button_add_equal.grid(row=2, column=14, sticky="ew")
button_backspace.grid(row=2, column=15, sticky="ew")

# Grid 3
button_tab.grid(row=3, column=0, sticky="ew")
button_q.grid(row=3, column=2, sticky="ew")
button_w.grid(row=3, column=3, sticky="ew")
button_e.grid(row=3, column=4, sticky="ew")
button_r.grid(row=3, column=5, sticky="ew")
button_t.grid(row=3, column=6, sticky="ew")
button_y.grid(row=3, column=7, sticky="ew")
button_u.grid(row=3, column=8, sticky="ew")
button_i.grid(row=3, column=9, sticky="ew")
button_o.grid(row=3, column=10, sticky="ew")
button_p.grid(row=3, column=11, sticky="ew")
button_square_curly_brackets_in.grid(row=3, column=12, sticky="ew")
button_square_curly_brackets_out.grid(row=3, column=13, sticky="ew")
button_backslash.grid(row=3, column=14, sticky="ew")
button_del.grid(row=3, column=15, sticky="ew")

# Grid 4
button_Caps.grid(row=4, column=0, sticky="ew")
button_a.grid(row=4, column=2, sticky="ew")
button_s.grid(row=4, column=3, sticky="ew")
button_d.grid(row=4, column=4, sticky="ew")
button_f.grid(row=4, column=5, sticky="ew")
button_g.grid(row=4, column=6, sticky="ew")
button_h.grid(row=4, column=7, sticky="ew")
button_j.grid(row=4, column=8, sticky="ew")
button_k.grid(row=4, column=9, sticky="ew")
button_l.grid(row=4, column=10, sticky="ew")
button_semi_colon.grid(row=4, column=11, sticky="ew")
button_quote.grid(row=4, column=12, sticky="ew")
button_Enter.grid(row=4, column=13, sticky="ew", columnspan=3)

# Grid 5
button_left_shift.grid(row=5, column=0, sticky="ew")
button_z.grid(row=5, column=2, sticky="ew")
button_x.grid(row=5, column=3, sticky="ew")
button_c.grid(row=5, column=4, sticky="ew")
button_v.grid(row=5, column=5, sticky="ew")
button_b.grid(row=5, column=6, sticky="ew")
button_n.grid(row=5, column=7, sticky="ew")
button_m.grid(row=5, column=8, sticky="ew")
button_comma.grid(row=5, column=9, sticky="ew")
button_dot.grid(row=5, column=10, sticky="ew")
button_slash.grid(row=5, column=11, sticky="ew")
button_up_arrow.grid(row=5, column=12, sticky="ew")
button_right_shift.grid(row=5, column=13, sticky="ew", columnspan=3)

# Grid 6
button_fn.grid(row=6, column=0, sticky="ew")
button_left_ctrl.grid(row=6, column=2)
button_win_key.grid(row=6, column=3, sticky="ew")
button_left_alt.grid(row=6, column=4)
button_space.grid(row=6, column=5, columnspan=4)
button_right_alt.grid(row=6, column=9)
button_right_ctrl.grid(row=6, column=10)
button_left_arrow.grid(row=6, column=11, sticky="ew")
button_down_arrow.grid(row=6, column=12, sticky="ew")
button_right_arrow.grid(row=6, column=13, sticky="ew")
button_menu.grid(row=6, column=14, columnspan=2, sticky="ew")

# Navigation
space.grid(row=1, column=16, rowspan=3, sticky="ew")
button_insert.grid(row=2, column=17, sticky="ew")
button_home.grid(row=2, column=18, sticky="ew")
button_pg_up.grid(row=2, column=19, sticky="nsew")
button_prt_scn.grid(row=3, column=17, sticky="ew")
button_end.grid(row=3, column=18, sticky="ew")
button_pg_down.grid(row=3, column=19, sticky="new")
button_narrate_on.grid(row=1, column=18, sticky="nsew")
button_narrate_off.grid(row=1, column=19, sticky="nsew")

root.mainloop()
