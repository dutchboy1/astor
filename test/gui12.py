from tkinter import *
from collections import OrderedDict
from tkinter.scrolledtext import *


# CODE MULTIPLE OPTIONMENUS BETTER https://stackoverflow.com/questions/17056211/more-concise-way-to-configure-tkinter-option-menu 
# WRITE TO GUI: https://stackoverflow.com/questions/12351786/python-converting-cli-to-gui 

master = Tk()
master.title("Astrology App")
master.geometry("500x665")
#os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
master.lift()
master.attributes('-topmost', True)
#master.attributes('-topmost', False)
master["bg"] = "#eac1c1"

var = StringVar(master)
var.set("Sign")
var1 = StringVar(master)
var1.set("Sign")
var2= StringVar(master)
var2.set("Sign")
var3 = StringVar(master)
var3.set("Sign")
var4 = StringVar(master)
var4.set("Sign")
var5 = StringVar(master)
var5.set("Sign")
var6 = StringVar(master)
var6.set("Sign")
var7 = StringVar(master)
var7.set("Sign")
var8 = StringVar(master)
var8.set("Sign")
var9 = StringVar(master)
var9.set("Asc")

x = OptionMenu(master, var, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x.grid(column =1,row =1)

x1 = OptionMenu(master, var1, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x1.grid(column =1,row =2)

x2 = OptionMenu(master, var2, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x2.grid(column =1,row =3)

x3 = OptionMenu(master, var3, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x3.grid(column =1,row =4)

x4 = OptionMenu(master, var4, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x4.grid(column =1,row =5)

x5 = OptionMenu(master, var5, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x5.grid(column =1,row =6)
x6 = OptionMenu(master, var6, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x6.grid(column =1,row =7)

x7 = OptionMenu(master, var7, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x7.grid(column =1,row =8)

x8 = OptionMenu(master, var8, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x8.grid(column =1,row =9)

x9 = OptionMenu(master, var9, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x9.grid(column =1,row =10)



planets = ["Ma","Ve","Me","Mo","Su","Ju","Sa","Ra"]
signs = []
pslist = []
asc_house = {'Ar':'1', 'Ta':'2', 'Ge':'3','Can':'4','Le':'5', 'Vi':'6', 'Li':'7', 'Sc':'8', 'Sa':'9', 'Cap':'10', 'Aq':'11','Pi':'12'}
rotator = {'Ar':'12', 'Ta':'11', 'Ge':'10','Can':'9','Le':'8', 'Vi':'7', 'Li':'6', 'Sc':'5', 'Sa':'4', 'Cap':'3', 'Aq':'2','Pi':'1'}
houselist = []
planets_houses = []
asclist = []

def getasc():
    global asc
    asc = var9.get()
    return asc

#getasc()

def makesigns():
    signs.append(var.get())
    signs.append(var1.get())
    signs.append(var2.get())
    signs.append(var3.get())
    signs.append(var4.get())
    signs.append(var5.get())
    signs.append(var6.get())
    signs.append(var7.get()) 


def makepslist():
    y = 0
    for x in planets:
        pslist.append(x +' '+ signs[y])
        y+=1
    return(pslist)


def addHL():
    for i in signs:
        if i in asc_house.keys():
            houselist.append(asc_house[i])

def find_rotator():
    global rot
    if asc in rotator.keys():
        rot = rotator[asc]
        return(rot)       
       

def asc_rotator():
    global rot
    global houselist
    houselist = [str(int(x) + int(rot)) for x in houselist]
    houselist[:] = [int(x)-12 if int(x)>12 else x for x in houselist]
    houselist[:] = [1 if x==0 else x for x in houselist]
    return(houselist)


def planetshouses():
    y = 0
    for x in planets:
        planets_houses.append(x + " "+ str(houselist[y])+'H')
        y+=1
    return(planets_houses)


lord_base_list = ['Ma','Ve','Me','Mo','Su','Ju','Sa']
lords = [1,2,3,4,5,9,10]
lord_base_list2 = ['Me','Ve','Ma','Sa','Ju']
lords2 = [6,7,8,11,12]
lord_base_dict = dict(zip(lord_base_list,lords))
lord_base_dict2 = dict(zip(lord_base_list2,lords2))
#asc_rotator()
planet_houselist_dict = dict(zip(planets, houselist))


templords = []
for x in planets:
    if x in lord_base_dict.keys():
        templords.append(lord_base_dict[x])
    if x in lord_base_dict2.keys():
        templords.append(lord_base_dict2[x])


def rotate(l):
    global rot
    l = [(x + int(rot))for x in l]
    l[:] = [x-12 if x>12 else x for x in l]
    l[:] = [1 if x==0 else x for x in l]
       

def f(dict):
    for entry in dict.items():
        dict[entry[0]] = entry[1] + int(rot)
    for entry in dict.items():
        if entry[1] > 12:
            dict[entry[0]] = entry[1] -12
    for entry in dict.items():
        if entry[1] == 0:
            entry[0] ==1
    return dict


def lordinhouses():
    lordlist = []
    lordlist2 = []
    for x in planets:
        if x in lord_base_dict.keys():
            lordlist.append(int(lord_base_dict.get(x)))
    lord_in_houses_dict1 = dict(zip(lordlist, houselist))
    for x in planets:
        if x in lord_base_dict2.keys():
            lordlist2.append(int(lord_base_dict2.get(x)))

    lord_in_houses_dict2 = dict(zip(lordlist2, houselist))
    lord_in_houses_dict  = dict(list(lord_in_houses_dict1.items()) + list(lord_in_houses_dict2.items()))
    lh_list = (OrderedDict(sorted(lord_in_houses_dict.items(), key=lambda t: t[0])))
    print("Lords in houses:")
    for k, v in lh_list.items(): print(str(k)+'L in '+str(v)+'H')
    

"""
    lord_in_houses = []
    for x in planets:
        if x in lord_base_dict.keys():
            lord_in_houses.append((str(lord_base_dict.get(x))+'L in '+str(planet_houselist_dict.get(x))+'H'))

    for x in planets:
        if x in lord_base_dict2.keys():
            lord_in_houses.append((str(lord_base_dict2.get(x))+'L in '+str(planet_houselist_dict.get(x))+'H'))
    print("Lords in houses:")
    print(lord_in_houses)
    return lord_in_houses
"""


def planetsignchecker():
    print("Info based only on Planets and Signs:")
    if ('Su Ar') in pslist:
        print("Sun is exalted")
    if ('Mo Ta') in pslist:
        print("Moon is exalted")
    if ('Ju Cap') in pslist:
        print("Jupiter is false")
    if ('Sa Li') in pslist:
        print("Sa is exalted")

def redirector(inputStr):
    txt.insert(INSERT, inputStr)


sys.stdout.write = redirector #whenever sys.stdout.write is called, redirector is called.


def ok():
    global asc
    global rot
    global planet_houselist_dict
    global lord_in_houses
    makesigns()
    makepslist()
    asc = getasc()  
    addHL()
    rot = find_rotator() 
    asc_rotator()
    print("Planets in signs:")
    print(pslist)
    txt.insert(END, '\n')
    print("Planets in houses:")
    print(planetshouses())
    txt.insert(END, '\n')
    planet_houselist_dict = dict(zip(planets, houselist))
    f(lord_base_dict)
    f(lord_base_dict2)
    lordinhouses()
    txt.insert(END, '\n')
    planetsignchecker()
    txt.insert(END, '\n')
    redirector("Thanks for using the app")
    #textbox.configure(state="disabled")
    master.quit()

def cancel():
    print("The user clicked 'Cancel")
    master.destroy()


#Label
label1 = Label(text="  Welcome to Astrology App",bg="#fcffce",font=("Times New Roman",18))
label1.grid(column=0,row=0)

label2 = Label(text="Ma: ")
label2.grid(column=0,row=1)

label3 = Label(text="Ve: ")
label3.grid(column=0,row=2)
label4 = Label(text="Me: ")
label4.grid(column=0,row=3)
label5 = Label(text="Mo: ")
label5.grid(column=0,row=4)
label6 = Label(text="Su: ")
label6.grid(column=0,row=5)
label7 = Label(text="Ju: ")
label7.grid(column=0,row=6)
label8 = Label(text="Sa: ")
label8.grid(column=0,row=7)
label9 = Label(text="Ra: ")
label9.grid(column=0,row=8)
label10 = Label(text="Ke: ")
label10.grid(column=0,row=9)
labelasc = Label(text="What ascendent:",bg="#fcffce")
labelasc.grid(column=0,row=10)

txt = ScrolledText(master, bg="#C2DFFF", width = 80, height= 25, font = "Arial 11")
txt.grid(column = 0, row = 14, columnspan=2)
"""
textbox = Text(master, width = 93, height = 10, font = "Helvetica", bg="#C2DFFF")
textbox.grid(row = 13, column = 0, columnspan = 10)
"""
button = Button(master, text="OK", default ='active',command=ok).grid(column=1,row=11)
button = Button(master, text ="Cancel",command = cancel).grid(column=0,row=11)


master.mainloop()
