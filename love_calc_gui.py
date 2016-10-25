import Tkinter
import tkMessageBox

from pyllist import sllist


win = Tkinter.Tk()
win.title('Love Calculator')

r1 = Tkinter.Frame(win)
# Entry box for first person's name. 
label = Tkinter.Label(r1, text='Person 1: ', font=("Courier New",10))
entry1 = Tkinter.Entry(r1)

r2 = Tkinter.Frame(win)
# Entry box for second person's name. 
label2 = Tkinter.Label(r2, text='Person 2: ', font=("Courier New",10))
entry2 = Tkinter.Entry(r2)

r3 = Tkinter.Frame(win)

r4 = Tkinter.Frame(win)
chancesLabel = Tkinter.Label(r4, text='')
r5 = Tkinter.Frame(win)
resultsLabel = Tkinter.Label(r5, text='')

chancesLabel.config(text='Enter Two Names', font=("Courier New",10))
resultsLabel.config(text=" Click 'CALCULATE'", font=("Courier New",10))

def _count(name1, name2):
    letters = (name1+name2).lower()

    counts = {char: letters.count(char) for char in 'loves'}
    result = [counts[char] for char in 'loves']
    return sllist(result)


def _add(letters):
    def step(sll):
        for node in sll.iternodes():
            try:
                node.value += node.next()
                if node.value >= 10:
                    sll.insertbefore(node, node.value/10)
                    node.value %= 10
            except TypeError:
                'reached end of sllist'
                sll.popright()

    visited = set()
    while len(letters) > 2:
        curr = str(letters)  # stringify the Sllist since you cannot hash a mutable object 
        if curr in visited:
            return sllist([1])
        visited.add(curr)

        step(letters)

    return letters


def love_algorithm(name1, name2):
    result = _add(_count(name1, name2))

    if len(result) == 2:
        return 10*result[0] + result[1]
    return result[0]


def get_text(percent):
    if percent >= 90:
        return "Extremely favorable!"
    elif percent > 80:
        return "Very favorable!"
    elif percent >= 70:
        return "Favorable!"
    elif percent > 50:
        return "slightly favorable"
    elif percent > 40:
        return "slightly unfavorable"
    elif percent > 25:
        return "unfavorable"
    else:
        return "very unfavorable"


def label_spacer(parent):
    label = Tkinter.Label(parent, text="    ", font=("Courier New",10))
    label.pack(side='left')


def row_spacer():
    new_row = Tkinter.Frame(win)
    label = Tkinter.Label(text=" ")
    label.pack()
    new_row.pack()


def calculate():
    percent = love_algorithm(entry1.get(), entry2.get())
    results = get_text(percent)
    chancesLabel.config(text="Chances of Success: "+str(percent)+"%")
    resultsLabel.config(text="Results: "+results)

button = Tkinter.Button(r3,text=" CALCULATE ", command=calculate, font=("Courier New", 10))

row_spacer()
label_spacer(r1)
label.pack(side='left')
entry1.pack(side='left')
label_spacer(r1)
r1.pack()

label2.pack(side='left')
entry2.pack(side='right')
r2.pack()

row_spacer()
label_spacer(r3)
button.pack(side='right')
r3.pack()

row_spacer()
chancesLabel.pack()
r4.pack()

resultsLabel.pack()
r5.pack()
row_spacer()

win.mainloop()

