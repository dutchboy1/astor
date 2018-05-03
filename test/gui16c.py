# latest version including check for fullmoon and extra lines Cap asc, also update periodinfo Cap
#!/usr/bin/env python
from tkinter import *
from collections import OrderedDict
from tkinter.scrolledtext import *
from collections import Counter


#from lords import *
#from check import retrochecker


# if no asc selected give this info
# CODE MULTIPLE OPTIONMENUS BETTER https://stackoverflow.com/questions/17056211/more-concise-way-to-configure-tkinter-option-menu
# WRITE TO GUI: https://stackoverflow.com/questions/12351786/python-converting-cli-to-gui

master = Tk()
master.title("Astrology App")
master.geometry("700x620")
#master.geometry("600x665")
#os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
master.lift()
master.attributes('-topmost', True)
#master.attributes('-topmost', False)
master["bg"] = "#eac1c1"

mvar = IntVar()
mvar1 = IntVar()
mvar2 = IntVar()
mvar3 = IntVar()
mvar4 = IntVar()


# I put default on Ar instead of Sign to make testing faster..
var = StringVar(master)
var.set("Asc")
var1 = StringVar(master)
var1.set("Ar")
var2= StringVar(master)
var2.set("Ar")
var3 = StringVar(master)
var3.set("Ar")
var4 = StringVar(master)
var4.set("Ar")
var5 = StringVar(master)
var5.set("Ar")
var6 = StringVar(master)
var6.set("Ar")
var7 = StringVar(master)
var7.set("Ar")
var8 = StringVar(master)
var8.set("Ar")
var9 = StringVar(master)
var9.set("Ar")

x = OptionMenu(master, var, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x.grid(column =2,row =1)

x1 = OptionMenu(master, var1, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x1.grid(column =2,row =2)

x2 = OptionMenu(master, var2, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x2.grid(column =2,row =3)

x3 = OptionMenu(master, var3, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x3.grid(column =2,row =4)

x4 = OptionMenu(master, var4, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x4.grid(column =2,row =5)

x5 = OptionMenu(master, var5, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x5.grid(column =2,row =6)
x6 = OptionMenu(master, var6, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x6.grid(column =2,row =7)

x7 = OptionMenu(master, var7, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x7.grid(column =2,row =8)

x8 = OptionMenu(master, var8, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x8.grid(column =2,row =9)

x9 = OptionMenu(master, var9, "Ar", "Ta", "Ge","Can","Le","Vi","Li","Sc","Sa","Cap","Aq","Pi")
x9.grid(column =2,row =10)



planets = ["Ma","Ve","Me","Mo","Su","Ju","Sa","Ra","Ke"]
signs = []
pslist = []
asc_house = {'Ar':'1', 'Ta':'2', 'Ge':'3','Can':'4','Le':'5', 'Vi':'6', 'Li':'7', 'Sc':'8', 'Sa':'9', 'Cap':'10', 'Aq':'11','Pi':'12'}
rotator = {'Ar':'12', 'Ta':'11', 'Ge':'10','Can':'9','Le':'8', 'Vi':'7', 'Li':'6', 'Sc':'5', 'Sa':'4', 'Cap':'3', 'Aq':'2','Pi':'1'}
houselist = []
planets_houses = []
asclist = []

def getasc():
    global asc
    asc = var.get()
    return asc



def makesigns():
    signs.append(var1.get())
    signs.append(var2.get())
    signs.append(var3.get())
    signs.append(var4.get())
    signs.append(var5.get())
    signs.append(var6.get())
    signs.append(var7.get())
    signs.append(var8.get())
    signs.append(var9.get())




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

# In houselist I can check if Ke is Ra +6 for correct input

def find_rotator():
    global rot
    if asc in rotator.keys():
        rot = rotator[asc]
        return(rot)


def asc_rotator():
    global rot
    global houselist
    houselist = [(int(x) + int(rot)) for x in houselist]
    houselist[:] = [int(x)-12 if int(x)>12 else x for x in houselist]
    houselist[:] = [1 if x==0 else x for x in houselist]
    return(houselist)

RaKeCheck= []





def planetshouses():
    y = 0
    for x in planets:
        planets_houses.append(x + " "+ str(houselist[y])+'H')
        if x == 'Ra':
            RaKeCheck.append(houselist[y])
        if x == 'Ke':
            RaKeCheck.append(houselist[y])
        y+=1
    return(planets_houses)


def RKcheck():
        if (RaKeCheck[0] -RaKeCheck[1] !=6) and (RaKeCheck[0] -RaKeCheck[1] !=-6):
            print("Ra Ke NOT CORRECT INPUT!! Rahu should be opposite of Ketu")


#planet_houselist_dict

lord_base_list = ['Ma','Ve','Me','Mo','Su','Ju','Sa']
lords = [1,2,3,4,5,9,10]
lord_base_list2 = ['Me','Ve','Ma','Sa','Ju']
lords2 = [6,7,8,11,12]
lord_base_dict = dict(zip(lord_base_list,lords))
lord_base_dict2 = dict(zip(lord_base_list2,lords2))
phd = dict(zip(planets, houselist))



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


lord_in_houses_dict = {}
lord_in_houses_dict2 = {}
lordlist = []
lordlist2 = []
nhouselist = []
nhouselist2 = []

def lordinhouses():
    global lordlist
    global lordlist2
    global nhouselist
    global nhouselist2
    global lord_in_houses_dict
    global lh_list
    for x in planets:
        if x in lord_base_dict.keys():
            lordlist.append(int(lord_base_dict.get(x)))
            nhouselist.append(phd.get(x))
    lord_in_houses_dict1 = dict(zip(lordlist, nhouselist))
    for x in planets:
        if x in lord_base_dict2.keys():
            lordlist2.append(int(lord_base_dict2.get(x)))
            nhouselist2.append(phd.get(x))
    lord_in_houses_dict2 = dict(zip(lordlist2, nhouselist2))

    lord_in_houses_dict  = dict(list(lord_in_houses_dict1.items()) + list(lord_in_houses_dict2.items()))
    lh_list = (OrderedDict(sorted(lord_in_houses_dict.items(), key=lambda t: t[0])))
    print("Lords in houses:")
    for k, v in lh_list.items(): print(str(k)+'L in '+str(v)+'H')

# finds 8L, but has to check 2 dicts..
#print(list(lord_base_dict2.keys())[list(lord_base_dict2.values()).index(8)])

lord_planet = {}
# Dict: 1L = 'planet, 2L = 'planet' etc..
def findlordisplanet():
    global lord_planet
    lordisplanet = []
    lordisplanet2 = [1,2,3,4,5,6,7,8,9,10,11,12]
    for x in range (13):
        if (x in lord_base_dict.values()) == True:
            lordisplanet.append(list(lord_base_dict.keys())[list(lord_base_dict.values()).index(x)])
        if (x in lord_base_dict2.values()) == True:
            lordisplanet.append(list(lord_base_dict2.keys())[list(lord_base_dict2.values()).index(x)])
    lord_planet = dict(zip(lordisplanet2,lordisplanet))
    return(lord_planet)




exchangel = []

#Checks for exchanges
def exchange(lord_in_houses_dict):
    for k,v in lord_in_houses_dict.items():
        x=k,v
        if (k,v) and (v,k) in lord_in_houses_dict.items():
            if k<v:
                exchangel.append(x)
    return(exchangel)


# prints exchanges
def printexchange():
    for k,v in exchangel:
        print(str(k)+"-"+str(v)+" exchange")

def ascinfo():
    if asc == 'Ar':
        print("AR ASC\nSu karaka very good, Mo also karaka, Ma most of time karaka, Me totally akaraka, Ju karaka and akaraka both, Sa karaka and akarkara both, Ve is markesh. S: Marrkesh can be also karaka? P. No, can give death in its period. \nMa because 1L doesn’t give results of 8H, also gives good promotions, good agriculture, good land. \nMe, 3L and 6L gives very much ups and down in life, bad business if people are business people, and increases enemies, gives also depression.\nVe gives very bad physical health. Ve becomes bit crazy. Which planet it sits with it gives results of this planet. S: If it sits with Me? P. Gives ups and down, and healthwise not good.\nSa gives very good results, lots of progress in the life, ups and downs come, but people get good results this period. Ra and Ke which house they sit they give results of this house.\n   ")
    if asc == 'Ar' and (phd.get('Ju') == phd.get('Sa')) == True:
        print("Ju and Sa don't give very strong raj yoga, even 9L and 10L. Sa and Ju together make person a little bit layman, simple person, not high Raj yoga. Can work government job, something simple. S: 9L and 10L? P. Also 11L and 12L. S: Even if sitting 9H? If Ju and Sa are associated, during this period they can become simple layman lose many things. Ju/Sa also not so good. S: Sa mahadasha? P. Better then Ju. \n")
    if asc == 'Ar' and ((("Ma 2H") in planets_houses or ("Ma 10H") in planets_houses or ("Ma 11H") in planets_houses) or (phd.get('Ma') == phd.get('Su')) or ((phd['Ma'] in suA) and (phd['Su'] in maA))):
        print("Ma 2H/10H/11H or Su connects with Ma: Sure can be very good doctors, can study medical science very good way, because from these houses Ma aspects 5H and connectivity with 5L. Ma is medicine, and 5H of education. \n")
    if asc == 'Ar' and ("Ju 10H") in planets_houses and ("Ju" in (sorted(k for k,v in phd.items() if cn[v] == 1))):
        print("Sometimes alone Ju 10H can give sometime heart problems in Aries sign, 12L 10H aspecting 4H a little bit becomes like marrkesh. \n")
    if asc == 'Ar' and ("Ve 12H") in planets_houses:
        print("Ve 12H gives very positive results. S: Like what? P. Prosperity. \n")
    if asc == 'Ar' and ("Ve 6H") in planets_houses and ("Me 7H") in planets_houses:
        print("Ve 6H and Me 7H very bad, always brings illness to wife. \n")
    if asc == 'Ar' and (phd.get('Ma') == phd.get('Me')):
        print("Ma and Me together, always have problem with the head, and sometime stroke.\n")
    if asc == 'Ar' and (set([("Ma 2H"),("Ju 2H"),("Ve 2H")]) <= set(planets_houses)):
        print("If Ma, Ju and Ve all in 2H, very big merchant, can make lots of money by business, sutra from Bhavat Ratnaka (min 45). S: Good book? P. So, so. But person will get money only after working very hard, family will not support him, will go by his own efforts. \n")
    if asc == 'Ar' and (set([("Ma 11H"),("Me 11H")]) <= set(planets_houses)):
        print("If Ma 11H with Me sure abortion will come to woman. \n")
    if asc == 'Ar' and (set([("Ma 11H"),("Ju 11H")]) <= set(planets_houses)):
        print("If Ma 11H with Ju sometimes abortion will come. \n")
    if asc == 'Ar' and (set([("Su 1H"),("Mo 4H"),("Ma 10H")]) <= set(planets_houses)):
        print("Su 1H, Mo 4H and Ma 10H very good person, and good administrator, will be very successful in civil services, can become very high level diplomat.\n")
    if asc == 'Ar' and (set([("Ve 2H"),("Su 2H")]) <= set(planets_houses)) and (2 in juA):
        print("Ve with Su 2H aspected by Ju, can get very good position. Very good person, and good administrator, will be very successful in civil services, can become very high level diplomat.  \n")
    if asc == 'Ar' and ("Ve" in (sorted(k for k,v in phd.items() if cn[v] == 1))):
        print("If Ve alone anywhere not good. S: Ve alone markesh? P. Becomes lusty and dusty in the mind.\n")
    if asc == 'Ar' and ("Ve" in (sorted(k for k,v in phd.items() if cn[v] == 1))) and (("Ve 6H") in planets_houses or ("Ve 8H") in planets_houses):
        print("This asc Ve alone, especially 6 and 8 house very bad.\n")
    if asc == 'Ar' and ("Ve" in (sorted(k for k,v in phd.items() if cn[v] == 1))) and ("Ve 12H") in planets_houses:
        print("S: If Ve alone 12H? P. Not much prosperity. \n")
    if asc == 'Ar' and (phd.get('Ve') == phd.get('Su')):
        print("If Ve connects with Su, very good.\n")
    if asc == 'Ar' and (set([("Ma 4H"),("Ju 4H")]) <= set(planets_houses)):
        print("Ma with Ju 4H Neech Bhangra yoga. Totally cancels debilitation of Ma. \n")
    if asc == 'Ar' and ("Ma 7H") in planets_houses:
        print("Ma 7H bad situation for happy marriage life. \n")
    if asc == 'Ar' and ("Ve 8H") in planets_houses:
        print("Ve 8H (Ma sign) bad situation for happy marriage life. \n")
    if asc == 'Ar' and ("Ma 2H") in planets_houses:
        print("Ma in Ve sign not happy for marriage life.  \n")
    if asc == 'Ar' and ("Ve 1H") in planets_houses:
        print("Ve in Ma sign not happy for marriage life.  \n")
    if asc == 'Ta':
        print("TA ASC:\nSu, Purna karaka, Su 4L gives good results. If good in horoscope gives good name and fame to father. Mo neutral (education good, but health wise can give problem 2L), Mo 3L akaraka not good. Ma big marrkesh, 7L and 12L. Me neutral, Ju big marrkesh or big akaraka, worst planet for this asc, Ve karaka, Sa purna karaka. Sa gives very good results. If only Sa very good in horoscope can make person king. Me main sign is 5H so 80-90% positive. Ve most of time gives good results if Ve good, but sometime can give results of 6H, physical health. Ra and Ke give good very results Ta asc. Always give good energy even they are the worse house rulers.\n")
    if asc == 'Ta' and (phd.get('Ve') == phd.get('Sa')):
        print("Ve and Sa combination make person very very positive, 100% better if they are in good house. If this combination comes in 1H and 10H really very good. \n")
    if asc == 'Ta' and (phd.get('Su') == phd.get('Me')):
        print("Su and Me together also very good. \n")
    if asc == 'Ta' and ("Ju 8H") in planets_houses:
        print("Ju 8H destroys quality of this house, but many times I found gives very good results, very strange. Usually should give very bad results. Bhavat Ratnaka also says Ju 8H gives good results for this asc. \n")
    if asc == 'Ta' and (("Me 2H") in planets_houses or ("Me 5H") in planets_houses):
        print("Me 2H or 5H very good talker, orator, or exchange 3-5 very big talkers, can talk very good way. Prateek’s bigger son has this combination he goes to shop asks so many questions. \n")
    if asc == 'Ta' and (phd.get('Ma') == phd.get('Su')):
        print("1L and 5L together can be good astrologer.\n")
    if asc == 'Ta' and (phd.get('Me') == phd.get('Ve')):
        print("Ve and Me together can be very good astrologer.\n")
    if asc == 'Ta' and (phd.get('Me') == phd.get('Ra') == phd.get('Sa')):
        print("Me, Sa and Ra sit anywhere these people live far away from family, especially if 2H, live far away from family, never go near them. \n")
    if asc == 'Ta' and (phd.get('Ra') == phd.get('Ve')):
        print("If Ve and Ra together all life problem with ear and throat. A story behind it, when Ra went to drink nectar the guru said don’t listen what Vishnu says, just go and bring the... He didn’t listen to guru so guru gave cursing to him, so he doesn’t have ear, he won’t listen to anybody, so when Ve goes with Ra, people can have problem with ears. S: Other asc? P. Tau asc, Ve here 1L and 6L\n")
    if asc == 'Ta' and (phd.get('Me') == phd.get('Ju')) and (phd.get('Me')) in maA :
        print("Me and Ju together aspected by Ma very good for money. \n")
    if asc == 'Ta' and ( ( phd.get('Mo') in (set(saA).intersection(raA))) or (phd.get('Mo') in (set(saA).intersection(maA)))):
        print("Mo aspected by Sa and Ra or Ma, can give all the time problem with brother, fighting with brother.\n ")
    if asc == 'Ta' and ( ( 3 in (set(saA).intersection(raA))) or (3 in (set(saA).intersection(maA)))):
        print("3H aspected by Sa and Ra or Ma, can give all the time problem with brother, fighting with brother.\n ")
    if asc == 'Ta' and (( phd.get('Su') in (set(saA).intersection(raA))) or (phd.get('Su') == phd.get('Sa') == phd.get('Ra'))):
        print("Su influenced by Sa and Ra: This person changes many time his job, goes here and there. S: Ra plays a lot in the combinations for this asc? P. Ra student of Ve. “If you are my student you will have a lot of influence on my life”. \n")
    if asc == 'Ta' and (("Mo 1H") in planets_houses) and ("Mo" in (sorted(k for k,v in phd.items() if cn[v] == 1))) :
        print("Exalted Mo 1H, alone and kemadruma, can be very poor\n")
    if asc == 'Ta' and (("Mo 1H") in planets_houses) and ("Mo" in (sorted(k for k,v in phd.items() if cn[v] == 1))) and (("Ma 7H") in planets_houses):
        print("If Mo 1H, alone and same time if Ma 7H can get lots of money from wife side.\n")
    if asc == 'Ta' and  ("Mo" in (sorted(k for k,v in phd.items() if cn[v] == 1))) and (phd.get('Mo') in juA ):
        print("S. If Ju opposite Mo, and Mo alone? P. Very bad Gaja Keshari, 8L and 3L (8 from 8) in front of asc. \n")
    if asc == 'Ta' and (set([("Su 11H"),("Sa 11H")]) <= set(planets_houses)):
        print("Sa and Su 11H gives long life. Su goes weaker. Sa will go stronger there, looking 1H, 5H, 8H, good houses increase the life, Sa yogakaraka, when opposite planet goes weaker, yoga karaka goes stronger. \n")
    if asc == 'Ta' and (("Su 11H") in planets_houses) and ("Su" in (sorted(k for k,v in phd.items() if cn[v] == 1))):
        print("S: Su alone 11H? P. Not good, 8 from his house. \n")
    if asc == 'Ta' and ("Ma 6H") in planets_houses:
        print("6H Ma all life fighting with wife, sometime fight with wife, sometime wife will fight with him.\n")
    if asc == 'Ta' and ("Ve" in (sorted(k for k,v in phd.items() if cn[v] == 1))):
        print("Ve alone 7H all life very good vehicles. \n")
    if asc == 'Ge':
        print("GE ASC:\nGe asc. Strange only Ve has the power to give pleasure. Su is akaraka, not good karaka. Mo is markesh. Ma is very very bad. Which house Ma sits destroys quality of this house. Me neutral, langesha but master or two Kendras. Me is like an impotent person, doesn’t play big role, ruler of two Kendras, Ju same two Kendra rulers. Ju akaraka, sometime marrkesh also.  Ve very good karaka. Sa totally akaraka, 8L and 9L. If offered milk and wine, will take wine first. The weaker Ma the stronger the chart. Sa is 8H indicator, first will take indications of 8H. Marrkesh planet is killer not only of the life, of say wife and children. It can kill also money, reputation, relationships. \n")
    if asc == 'Ge' and ("Me 11H") in planets_houses:
        print("S: For Ge asc, Me sitting 11H, not good for 4H? P. Not good. \n")
    if asc == 'Ge' and (set([("Su 3H"),("Me 3H")]) <= set(planets_houses)):
        print("Su and Me 3H very powerful person, big yoga karaka, Me goes out of Kendra in friendly sign, gives lots of money its own period. Prateek mentions 15 types of money.\n")
    if asc == 'Ge' and (set([("Mo 2H"),("Ma 2H"),("Ve 2H")]) <= set(planets_houses)):
        print("Mo, Ma and Ve 2H very big money, chandra mangala yoga with Ve. \n")
    if asc == 'Ge' and ("Sa 8H") in planets_houses:
        print("8H Sa gives very long life. Indian prime minister Deshai Ge asc Sa 8H died 107 years old. \n")
    if asc == 'Ge'and (set([("Su 11H"),("Me 11H"),("Sa 9H")]) <= set(planets_houses)):
        print("Sa 9H, Su and Me 11H world famous people, even Sa aspecting Su 11H, false aspect, but Su exalted here, 3L with Me. S: Sa in 11 from 11? P. Yes, and Me 1L also in 11. \n")
    if asc == 'Ge'and (set([("Mo 6H"),("Me 6H"),("Su 6H")]) <= set(planets_houses)):
        print("6H Su, Me and Mo, always lie and hide a lot of things. \n")
    if asc == 'Ge'and (phd.get('Ju') in (1,3,5)) and (phd.get('Sa') in (12,3,7)):
        print("If Ju and Sa influence 9H they often travel spiritual places. \n")
    if asc == 'Ge'and ("Me 11H") in planets_houses:
        print("11H Me always doubtful, make kind of mysterious person, usually Ar not good sign for Me, behaves strange sometime. \n")
    if asc == 'Ge' and (set([("Mo 5H"),("Ve 5H")]) <= set(planets_houses)):
        print("5H Mo and Ve together, sexual relationship with many women. \n")
    if asc == 'Ge' and (set([("Ma 12H"),("Ju 12H")]) <= set(planets_houses)):
        print("Ma and Ju 12H will not be good with wife.\n")
    if asc == 'Ge' and (set([("Ma 9H"),("Ju 9H")]) <= set(planets_houses)):
        print("If Ju 9H with Ma sometime bisexual, or tries to make sex with wife backside.\n")
    if asc == 'Ge' and ("Ma 11H") in planets_houses:
        print("S: Ma 11H? P. Ok, other than problem with older brother. \n")
    if asc == 'Ge' and ("Ra 9H") in planets_houses:
        print("9H Ra person becomes intelligent. \n")
    if asc == 'Ge' and ("Sa 5H") in planets_houses:
        print("Sa 5H brings lots of disease and sometime abortion. Exalted Sa not good for this asc. S: Exalted and retrograde? P. Better. \n")
    if asc == 'Ge' and ("Su 5H") in planets_houses:
        print("Su 5H can break many times bones.\n")
    if asc == 'Ge' and ("Mo 6H") in planets_houses:
        print("6H Mo are doing a lot of prostitution. Prateek mentions Russian girls from Goa who offers so called tantra classes in Rishikesh. \n")
    if asc == 'Ge' and (phd.get('Mo') in (4,7,10)) and ("Mo" in (sorted(k for k,v in phd.items() if cn[v] == 1))):
        print("Mo alone Ke in Kendra, 4, 7, 10, gives very good results. ")
    if asc == 'Ge' and (phd.get('Mo') in maA):
        print("If Ma aspects the Mo they can do anything for money, very angry, can kill people. Ma aspecting the Mo can become very good (not clear**) and police, and these kind of things, makes person more aggressive, if he uses his abilities can be very good. \n")
    if asc == 'Ge' and ((phd.get('Me') in maA) or (phd.get('Me') == phd.get('Ma')) ):
        print("Me influenced by Ma can spend a lot of money on bad habits, wine, drugs etc. \n")
    if asc == 'Ge' and (phd.get('Me') in saA) and (phd.get('Me') in raA):
        print("Me aspected by Sa and Ra skin problems can come. \n")
    if asc == 'Ge' and (phd.get('Me') == phd.get('Mo') == phd.get('Ve')) and  (phd.get('Me') in maA):
        print("Ve and Mo and Me influenced by Ma old age they can go crazy and lose their memory. \n")
    if asc == 'Ge' and (("Ma 2H") in planets_houses) and ("Ma" in (sorted(k for k,v in phd.items() if cn[v] == 1))):
        print("Ma alone 2H can be adopted different family. \n")
    if asc == 'Ge' and ("Mo 12H") in planets_houses:
        print("12H Mo always positive, brings person lots of good traveling in life. \n")
    if asc == 'Ge' and ((phd.get('Su') in moA) or (phd.get('Su') == (phd.get('Mo')))) and ((phd.get('Su') in meA) or (phd.get('Su') == (phd.get('Me')))):
        print("Su influenced by Mo and Me, these people like a lot writing. \n")
    if asc == 'Ge' and (phd.get('Me') == phd.get('Su')) and (phd.get('Su') in (10,11)):
        print("Su and Me together 10H and 11H are very ambitious, for their ambition can use any means. \n")
    if asc == 'Ge' and (set([("Ma 8H"),("Me 11H")]) <= set(planets_houses)):
        print("Ma 8H and Me 11H big thieves, they cannot be catched immediately. \n")
    if asc == 'Ge' and (("Ju 2H") in planets_houses) and (("Ju R") in retrolist):
        print("JuR 2H like Osho\n")
    if asc == 'Ge' and (set([("Mo 3H"),("Ra 3H")]) <= set(planets_houses)):
        print("S: Mo and Ra 3H for Ge asc? P. Very good position for Mo, but traveling a lot, if they stay same country they will not progress, become more down and more down, and depressed. 3H is traveling, Mo is traveling, 12 from 4H. \n")
    if asc == 'Can':
        print("CAN ASC:\nSu is akaraka, little marrkesh. Mo totally karaka. Ma totally karaka. Me totally akaraka. Ju akaraka. Ve akaraka. Sa neutral. Me and Ju don’t give good results. \n")
    if asc == 'Can' and ("Ju 1H") in planets_houses:
        print("Sometime Ju 1H can go crazy, but very religious people.\n")
    if asc == 'Can' and ("Ju 6H") in planets_houses:
        print("S: Ju 6H? P. kills the disease. Will always attract other religion. Sometime they are not born in good place, good family, but when they grow up they do very well. Krishna was born in jail, Tau asc, Mo 1H, very strong 6H, lots of problems with snakes, Sarpa dosha.\n")
    if asc == 'Can' and (phd.get('Ma') == (phd.get('Mo'))):
        print("When Ma and Mo together they bring a lot of positive energy. \n")
    if asc == 'Can' and ("Mo 1H") in planets_houses:
        print("S: Mo 1H? P. Very emotional people. \n")
    if asc == 'Can' and phd.get('Ve') in (2,12):
        print("Ve not good karaka for Can asc, but sitting 2H or 12H brings lots of money. \n")
    if asc == 'Can' and ("Ju 12H") in planets_houses:
        print("S: Ju good in Sag, 6 and 8H, also in 12H? P. Yes, this is Brahmin quality.\n")
    if asc == 'Can' and  (set([("Ma 2H"),("Mo 2H"),("Su 5H")]) <= set(planets_houses)) and (("Me 5H") in planets_houses or ("Ve 5H") in planets_houses) :
        print("Chandra mangala 2H with Ju, and Su and Me, Su and Ve 5H these people can become billioners. \n")
    if asc == 'Can' and  (set([("Me 11H"),("Mo 10H"),("Ve 10H"),("Ju 1H")]) <= set(planets_houses)):
        print("11H Me, Mo, and Ve, 10H Su, Ju asc, very strong horoscope, can be very good professor in university.\n")
    if asc == 'Can' and (phd.get('Ju') == phd.get('Mo')):
        print("Chandra and Ju make very big Raj yoga. \n")
    if asc == 'Can' and (set([("Me 12H"),("Ve 12H")]) <= set(planets_houses)):
        print("Ve and Me very good 12H. \n")
    if asc == 'Can' and  (set([("Ma 7H"),("Sa 4H"),("Ju 1H")]) <= set(planets_houses)):
        print("Ma 7H, Sa 4H, Ju 1H very good, lots of money, but only for man. \n")
    if asc == 'Can' and (set([("Me 12H"),("Ve 12H")]) <= set(planets_houses)):
        print("10H Su and Mo very big raj yoga. \n")
    if asc == 'Can' and (("Mo 1H") in planets_houses) and ("Mo" in (sorted(k for k,v in phd.items() if cn[v] == 1))):
        print("Only Mo 1H very good, emotional person. \n")
    if asc == 'Can' and (("Mo 7H") in planets_houses) and ("Mo" in (sorted(k for k,v in phd.items() if cn[v] == 1))):
        print("If 7H these people are very quick, want to do everything quick, sometimes sexually also. \n")
    if asc == 'Can' and (phd.get('Ve') in (7,12)):
        print("Ve 12H or 7H mother can have lots of physical problems. Sometime Ve in these houses, Ra dasha can be very difficult for them. S: No matter where Ra? P. Ya.\n")
    if asc == 'Can' and (phd.get('Sa') in (7,8)):
        print("Sa 7H or 8H wife will have very sharp tongue, all the time can say bad things. \n")
    if asc == 'Can' and (phd.get('Ma') in (5,7,10)):
        print("Ma 5H, 7H, 10H, makes very good Raj yoga.\n")
    if asc == 'Can' and phd.get('Sa') == 4:
        print(" S: Sa exalted 4H? P. Good for man, not for woman. \n")
    if asc == 'Can' and (set([("Me 2H"),("Ve 2H"),("Su 2H")]) <= set(planets_houses)):
        print("S: Su, Me and Ve 2H? P. Su in Leo very good.\n")
    if asc == 'Le':
        print("LE ASC:\nLeo Su purna (full) karaka, Mo akaraka, Ma purna karaka, Me simple karaka, Ju 8L akaraka. If Ju very bad, retrograde or combust, gives lots of journeys to foreign countries. Ve akaraka, the weaker Ve is, the stronger the horoscope. Sa akaraka. \n")
    if asc == 'Le' and phd.get('Su') == 1:
        print("Su 1H person becomes egoistic, but very good for management. \n")
    if asc == 'Le' and (phd.get('Me') == phd.get('Ma') == phd.get('Su')) :
        print("Su, Ma, Me together, make very good combination for money-wise. \n")
    if asc == 'Le' and (phd.get('Me') == phd.get('Ju') == phd.get('Su')) :
        print("When Su, Ju, Me go together, very good combination money-wise, because 1L, Me, 2L and Ju 5L.\n")
    if asc == 'Le' and (phd.get('Me') in (2,5,11)):
        print("Me 5H, 11H or 2H gives all the time good money. \n")
    if asc == 'Le' and (phd.get('Ve') == phd.get('Ma')):
        print("Ve and Ma together don’t make Raj yoga, even though 9L and 10L. S: Why? P. This by experience.\n")
    if asc == 'Le' and (phd.get('Sa') == phd.get('Ma')) or (phd.get('Ra') == phd.get('Ma')):
        print("Sa and Ma together or Ma and Ra together they can have prostate (uterus) problems or father can have such problem. \n")
    if asc == 'Le' and phd.get('Ra') == 11:
        print("Ju and Ra 11H or Ra 11H they usually don’t have son, or if they have son he won’t be useful for them. \n")
    if asc == 'Le' and (phd.get('Sa') == phd.get('Ju')):
        print("Ju and Sa together, wife comes from simple family, makes a lot of trouble in family. S: Why? P. 6L and 8L. S: More for man? P. Yes. \n")
    if asc == 'Le' and (phd.get('Mo') == phd.get('Ju')) and (phd.get('Mo') in (3,6,8,12)):
        print("Ju and Mo 3, 6, 8 or 12 also give travels to foreign countries. \n")
    if asc == 'Le' and (((phd.get('Me') == 5) and ((5 in (juA)) or (5 in (veA)) or (5 in (moA)) ))) or  (((phd.get('Me') == 9) and ((9 in (juA)) or (9 in (veA)) or (9 in (moA)) ))) :
        print("Me 5H or 9H aspected by benefic (S: if aspected by Ma? P. Not good)\n")
    if asc == 'Le' and (phd.get('Ra') in (5,11)):
        print("Ra or Ke 11H these people can get lots of money by lottery or stock market. \n")
    if asc == 'Le' and (phd.get('Ve') == phd.get('Ju')):
        print("Ju and Ve together any house make person down money down. \n")
    if asc == 'Le' and (phd.get('Ve') == phd.get('Ju') == phd.get('Me')):
        print("Ju, Ve, and Me together can go bankrupt, even though benefics. \n")
    if asc == 'Le' and phd.get('Sa') == 9:
        print("Sa Ar sign very good Raj yoga, but if they get married trouble, they can become very successful other countries. \n")
    if asc == 'Le' and phd.get('Ju') == 7:
        print("Ju 7H? P. Late marriage \n")
    if asc == 'Vi':
        print("VI ASC:\nSu sometime karaka, sometime akaraka. Mo very little karaka. Ma very akaraka. Me karaka. Ju akaraka. Ve sometime karaka, sometime akaraka, Sa not good karaka. \n")
    if asc == 'Vi' and (set([("Ve 2H"),("Ke 2H")]) <= set(planets_houses)):
        print("Ke and Ve very good for money 2H, Ve own sign with Ke 4 times more better. \n")
    if asc == 'Vi' and phd.get('Ma') == 5:
        print("If Ma very very strong 5H Cap doesn’t give education, or they don’t use education. S: Destroys also children? P. Yes, the weaker Ma is the stronger the horoscope. \n")
    if asc == 'Vi' and phd.get('Ju') == 7:
        print("Ju 7H sometime kills the mother, kendradipathi dosha. \n")
    if asc == 'Vi' and (phd.get('Sa') in (5,11)):
        print("Sa 5 or 11, if first daughter the rest will be daughters, same for sons. Sa is snake, eats own eggs, quality of snake if gives female, female follow, similarly male. S: Ra also snake? P. Mainly Sa snake in 5H. Ra snake in 6, 8 and 2. 1 and 7 become kundalini, because 1H is sahasrara chakra, and 7H is 2nd chakra.\n")
    if asc == 'Vi' and (phd.get('Ju') in (2,6,8,12)):
        print("Ju 2,6,8,12 doesn't give very happy marriage life. \n")
    if asc == 'Vi' and phd.get('Ve') == 12:
        print("Ve 12H gives very good results. \n")
    if asc == 'Vi' and phd.get('Ve') == 7:
        print("7H Ve gives lots of women, and sometime they can become very rich business wise. S: False aspect to 1H? P. Usually these people use their sperm a lot. \n")
    if asc == 'Vi' and (set([("Me 1H"),("Ve 2H")]) <= set(planets_houses)):
        print("Me 1H, Ve 2H great raj yoga. Very good money wise and can be very good actors, beautiful people, by acting can make lots of money. \n")
    if asc == 'Vi' and (set([("Mo 7H"),("Ve 7H"),("Ju 11H"),("Su 8H")]) <= set(planets_houses)):
        print("Mo, Ve 7, Ju 11, and Su 8H they have very beautiful wife, the wife provides service to them, but they don’t care about the wife..\n")
    if asc == 'Vi' and (set([("Ve 4H"),("Ju 4H")]) <= set(planets_houses)):
        print(" Ju and Ve 4H brings a lot of property. Usually I don’t like Ju and Ve together, two Brahmins sitting, one preaches sex, other preaches chant mantras, but for this asc they support very good materialistic life, car and everything.\n")
    if asc == 'Vi' and phd.get('Sa') == 2:
        print("2H Sa not retrograde brings lots of prosperity. \n")
    if asc == 'Vi' and (set([("Ve 1H"),("Me 1H"),("Mo 1H")]) <= set(planets_houses)):
        print("Me, Mo, and Ve, even Ve fallen, very good relationship with wife, and lots of money. \n")
    if asc == 'Vi' and (set([("Ve 1H"),("Me 1H")]) <= set(planets_houses)):
        print("Me and Ve alone 1H still good for wife and money? P. Very good")
    if asc == 'Vi' and phd.get('Ra') == 9:
        print("9H Ra many travels to many place. \n")
    if asc == 'Vi' and phd.get('Ra') == 1:
        print("1H Ra big raj yoga. \n")
    if asc == 'Li':
        print("LI ASC:\nSu karaka and akaraka. Mars strong markesh. Me sometime karaka sometime akaraka. Ju totally akaraka, brings lots of problems. The weaker Ju is the better the results, Ve purna karkaka (very good karaka). Ve fallen, weak, or zero (low degree)  makes not so long life because Ve is 1L and 8L. Mo karaka. Sa very good karaka. Where Sa sits improves the life.Ra and Ke give good results Li asc. Always give good energy even they are the worse house rulers.\n")
    if asc == 'Li' and (phd.get('Ma') in (6,8,12)):
        print("Ma 6, 8, 12 houses can get lots of trouble in their life. \n")
    if asc == 'Li' and phd.get('Ju') == 9:
        print("Ju 9H they go to different gurus, sadhus, move here and there all their life.\n")
    if asc == 'Li' and phd.get('Ju') == 4:
        print("Ju 4H good luck\n")
    if asc == 'Li' and phd.get('Ju') == 10:
        print("Ju 10H very bad results.\n")
    if asc == 'Li' and phd.get('Ju') == 8:
        print("Ju 8H gives lots of money. \n")
    if asc == 'Li' and ((phd.get('Sa') == phd.get('Su')) or (phd.get('Sa') == phd.get('Ma')) ) :
        print("Sa and Su together or Sa and Ma together get a lot of trouble from son. \n")
    if asc == 'Li' and phd.get('Ve') == 12:
        print("Ve false makes not so long life because Ve is 1L and 8L. \n")
    if asc == 'Li' and phd.get('Su') == 1:
        print("Su 1H very bad, but can be very good medical science, I don’t know how. \n")
    if asc == 'Li' and phd.get('Su') == 7:
        print("Su in 7H is very good for business, 11L 7H, but very bad relationship with woman, and for health, too much agni. Sometimes if Ve also goes there, combust or very weak, can go very very bad for 1H. But from business, money point of view, Su 7H best position for business. \n")
    if asc == 'Li' and (set([("Ve 7H"),("Me 7H"),("Su 7H")]) <= set(planets_houses)):
        print("If Ve and Me come together they can kill themselves also, Hitler’s horoscope, Su, Me and Ve 7H go very high but kill himself, 12L and 11L together. \n")
    if asc == 'Li'and phd.get('Su') == 3:
        print("S: If Su in 3H? P. Not a problem, very good. Good raj yoga, very good alone, even with Sa or Ju very good.\n")
    if asc == 'Li'and phd.get('Su') == 6:
        print("Su 6H also very good.\n ")
    if asc == 'Li' and (set([("Ve 9H"),("Me 9H")]) <= set(planets_houses)):
        print("Me and Ve 9H brings big raj yoga. \n")
    if asc == 'Li' and (set([("Ve 10H"),("M0 10H")]) <= set(planets_houses)):
        print("Ve and Mo 10H also big raj yoga. \n")
    if asc == 'Li'and phd.get('Mo') == 4:
        print("4H Mo very good for working other country. S: Also own country? P. Ya, own country.\n")
    if asc == 'Li' and phd.get('Me') == 12:
        print("12H Me very strong for good luck. \n")
    if asc == 'Li' and phd.get('Sa') == 1:
        print("S: Sa 1H? P. Great raj yoga, but not good for women. They go corrupted by man, many men can have bhoga, sex with them, false aspect 7H. \n")
    if asc == 'Li' and phd.get('Mo') == 12:
        print("S: Mo 12H? P. Good for traveling and job other countries.\n")
    if asc == 'Li' and phd.get('Mo') == 11:
        print("S: Mo 11H? P. Sometime trouble with mother father. \n")
    if asc == 'Li' and (set([("Su 12H"),("Me 12H")]) <= set(planets_houses)) and (phd.get('Sa') in (3,6,10,12)):
        print("12H Su, Me and Sa, or Su and Me aspected by Sa, very very good, very good researchers. Me 12L own sign, with yogakaraka Sa, and 11L. S: Why 11L? P. Goes weaker in 12H.  \n")
    if asc == 'Li' and (set([("Sa 9H"),("Ju 8H"),("Ma 11H"),("Me 11H")]) <= set(planets_houses)):
        print("Ju 8H, Sa 9H, Ma and Me 11H go very high position of life, really very high life. \n")
    if asc == 'Li' and phd.get('Ve') == 1:
        print("Ve 1H sometime Ve can kill the person, even 1L. \n")
    if asc == 'Li' and phd.get('Ra') == 11:
        print("Ra 11H and Ke 5H give lots of money.\n")
    if asc == 'Li' and phd.get('Ju') == 10:
        print("S: Ju exalted here not good for children? P. Not good.\n")
    if asc == 'Li' and phd.get('Ju') == 4:
        print("S: Ju 4H fallen? P. Can be better.\n")
    if asc == 'Sc':
        print("Su very good karaka. Mo very good karaka. Ma karaka. Me akaraka. Ju is neutral, a little bit karaka. Ve very strong Markesh and Sa akaraka. S: Sa rules Kendra? P. But also 3L not good. \n")
    if asc == 'Sc' and (phd.get('Ju') == phd.get('Me')) or (phd.get('Ju') in meA):
        print("Ju and Me combinations and opposition very good for money, usually Me akaraka, but brings very good money 11H, other places they also make good money, but this person becomes very miser, don’t expend money. \n")
    if asc == 'Sc' and phd.get('Ju') == 3:
        print("Ju 3H makes person very beautiful, happy and very good, good healing power. S: Fallen? P. Exalted aspect to 4H. \n")
    if asc == 'Sc' and (set([("Ju 5H"),("Me 5H"),("Mo 11H")]) <= set(planets_houses)):
        print("Ju and Me 5H and Mo 11H people make billions of money. Gaja Keshari combinations brings very nice energy, Ju and Mo together or in Kendra from each other. Ju 5H and Mo 2H in mula 4 pada becomes a king, very high position, very very powerful combination, because 4th pada of Mula very good. 1st 3 padas are not good, one is not good for father, 2nd pada not good for mother and 3rd not good for self, but 4th pada good for prosperity and everything. \n")
    if asc == 'Sc' and (set([("Ju 5H"),("Me 5H")]) <= set(planets_houses)):
        print("Me fallen 5H with Ju also brings lots of money and lots of children, and good children also. Me alone here?**** (also karaka and akaraka for Ar and Tau asc). \n")
    if asc == 'Sc' and (set([("Ju 9H"),("Mo 9H"),("Ke 9H")]) <= set(planets_houses)):
        print("Mo, Ju and Ke 9H they become very spiritual, religious very strong. S: If only Mo and Ke? P. Will make but less strong. Ju is main planet exalted with Ke, gives more energy to Ju.\n")
    if asc == 'Sc' and (phd.get('Ju') in meA):
        print("If Me and Ju in opposition brings very good in laws, can get very good money from in laws.\n")
    if asc == 'Sc' and (set([("Ju 3H"),("Ve 3H")]) <= set(planets_houses)):
        print("Ju and Ve 3H all the money  collected by this person is expended by son gambling and wine. \n")
    if asc == 'Sc' and phd.get('Ju') == 9:
        print("9H Ju gives very good energy for the children, make good name and fame for father.\n")
    if asc == 'Sc' and (phd.get('Sa') == 4) and  ("Sa" in (sorted(k for k,v in phd.items() if cn[v] == 1))):
        print("Alone Sa 4H people can go impotency, or they can have less sperm in semen, or wife or partner can be stronger than this person, person can go weaker. S: Why, Sa own house? P. Gets a lot female, mother energy, if in 10H get a lot from father, no female. Sa gets all energy from house it sits in. S: If female? P. Can be lesbian. S: If male? P. More female, not male. \n")
    if asc == 'Sc' and (phd.get('Ju') in saA) and (phd.get('Sa') in juA):
        print("Ju and Sa opposition can make a lot of money by investment in property. \n")
    if asc == 'Sc' and (set([("Sa 6H"),("Ma 6H")]) <= set(planets_houses)):
        print("Sa and Ma 6H can be very good thieves, sometime father can give money to them, they will put some of it in pocket. One false one own sign, 4L goes much weaker, so no higher level honesty. S: Honesty not from 2H? P. Different honesty. 4H honesty to self, 2H honesty to others. \n")
    if asc == 'Sc' and (set([("Su 11H"),("Me 11H"),("Ke 11H")]) <= set(planets_houses)):
        print("S: Su, Me and Ke 11H? P. Very good. Woman or man? X. Woman. P. She should be careful people can give her money to sleep with her, she should honor herself, otherwise nothing happens and they can go very high level, very good. \n")
    if asc == 'Sc' and (phd.get('Ve') == 7) and  ("Ve" in (sorted(k for k,v in phd.items() if cn[v] == 1))):
        print("Ve alone 7H not good for marriage life. People can have attraction with many other woman. \n")
    if asc == 'Sc' and (set([("Sa 7H"),("Ve 7H"),("Ra 7H")]) <= set(planets_houses)):
        print("7H Sa, Ve and Ra, very very bad, can have many other women, and sometime very strong sexual energy, not true, many things happen about this. area. \n")
    if asc == 'Sc' and (phd.get('Me') == 5) and  ("Me" in (sorted(k for k,v in phd.items() if cn[v] == 1))):
        print("Alone Me 5H gives a lot of traveling in other countries.\n")
    if asc == 'Sc' and phd.get('Me') == 6:
        print("6H Me go very rich but also very sick. The sicker the richer and vice versa. 6H disease and 11H is 6 from 6, and 6H 8 from 11H. S: If they are rich and let go of all money they become healthy? P. Very good. \n")
    if asc == 'Sc' and (phd.get('Su')) in (6,10):
        print("6H Su or 10H Su can go very rich and very good name and fame for father. \n")
    if asc == 'Sc' and (phd.get('Me')) == (phd.get('Ma')):
        print("Me and Ma together very angry people. Can have lots of surgery sometime, or mark in knee or leg area. \n")
    if asc == 'Sc' and phd.get('Ve') == 12:
        print("12H Ve can love a lot to wives, and have many wives, loves every wife. \n")
    if asc == 'Sc' and phd.get('Ma') == 6:
        print("6H Ma very strong brings lots of positive energy in life. \n")
    if asc == 'Sc' and (phd.get('Mo') == 7) and  ("Mo" in (sorted(k for k,v in phd.items() if cn[v] == 1))):
        print("S: Mo alone 7H? P. If alone sometime good, sometime not good, depending also on whether Mo is waxing or waning. If Shukla (waxing) paksha very good, if Krishna (waning) paksha, not good.\n")
    if asc == 'Sa':
        print("SA ASC:\nSu purna karaka. Bhakesh, not marrkesh. Mo neutral. Ma half karaka, half akaraka. Me sometime good, sometime bad, sometime neutral. Ju karaka. Ve very bad. The weaker Ve goes, near the Su, false, or enemy sign, the horoscope goes stronger.  Sa also akaraka. Not many planets are marrkesh, so Sa people usually live long life. Ra and Ke for Sag asc, bring very good results in 9, 10, 11 houses, also 7H. But 5, 4, make very bad results. Ra 3H big raja yoga, and Ke 9H very good.\n ")
    if asc == 'Sa' and phd.get('Sa') == 5:
        print("Sa 5H gives lots of money during its period. Person goes very healthy and long life, very good things.  S: And wife? P. Not so long life, and she always becomes ill. \n")
    if asc == 'Sa' and phd.get('Sa') == 11:
        print("Sa exalted 11H good for money, but sometime accident can come. Sa 11H wife goes very healthy and long life.\n")
    if asc == 'Sa' and phd.get('Sa') == 3:
        print("Not good placement for Sa this asc. Simple work. \n")
    if asc == 'Sa' and phd.get('Ju') == 5:
        print("Only for this asc Ju 5H gives very good qualities, not any other asc, because he is here 1L and 4L, becomes big Raj yoga, doesn’t happen Pi asc when Ju 5H. \n")
    if asc == 'Sa' and phd.get('Ma') == 7:
        print("7H Ma many women relationship. \n")
    if asc == 'Sa' and phd.get('Ma') == 8:
        print("8H Ma gives long life, but gives surgery also a lot. \n")
    if asc == 'Sa'and (set([("Ra 9H"),("Ma 9H")]) <= set(planets_houses)):
        print("9H Ra and Ma the son goes very critical conditi\n")
    if asc == 'Sa' and (set([("Ve 7H"),("Ma 7H")]) <= set(planets_houses)):
        print("7H Ma and Ve, sometime wife dies by mistake of doctor. \n")
    if asc == 'Sa' and (set([("Ve 8H"),("Ma 8H")]) <= set(planets_houses)):
        print("Ma and Ve 8H unnatural death.\n")
    if asc == 'Sa' and phd.get('Ve') == 10:
        print("Only for Sag asc Ve 10H brings the money, because akaraka fallen and 12 from 11. \n")
    if asc == 'Sa' and (set([("Ve 5H"),("Sa 5H")]) <= set(planets_houses)):
        print("Sa and Ve 5H always stomach problem. \n")
    if asc == 'Sa' and (set([("Sa 1H"),("Ju 7H"),("Ra 1H")]) <= set(planets_houses)):
        print("Ju 7H, Sa and Ra 1H this woman can become widow. In woman horoscope, Ra false sign 1H, and Ju kills the husband. S: For man? P. Man can have problem with wife. \n")
    if asc == 'Sa' and phd.get('Me') == 7:
        print("7H Me can give very early marriage, in Russian horoscope can marry 16 years old. \n")
    if asc == 'Sa' and (set([("Ju 10H"),("Su 10H")]) <= set(planets_houses)):
        print("10H Su with Ju, can be very good academic field. \n")
    if asc == 'Sa' and (set([("Me 10H"),("Ra 4H")]) <= set(planets_houses)) and ((phd.get('Sa') == 4) or (phd.get('Ma') == 4)) :
        print("10H Me, 4H Ra, Sa, or Ra and Ma, go very high and after that very down, perhaps corruption or something like that. \n")
    if asc == 'Sa' and phd.get('Ju') == 8:
        print("S: 1L 8H causes problems? P. He doesn’t like his father, he will have differences from father. \n")
    if asc == 'Sa' and phd.get('Me') in (6,8):
        print("Me 6H or 8H Me always makes some skin problem. \n")
    if asc == 'Sa' and (phd.get('Ma') == phd.get('Ve')) or (phd.get('Ma') in veA):
        print("Ma and Ve combinations always bring ups and down in the life. \n")
    if asc == 'Cap':
        print("CAP ASC\nSu neutral. Mo karaka. Usually full Mo not good for marriage life, but for this asc as much as Mo is far from Su marriage life will be very good. S: 7L and 8L? P. Yes. P. Ma akaraka. Me akaraka sometimes. Ju purna akaraka. The weaker Ju is the stronger the horoscope. Ve purna karaka. Often they don’t live long life \n")
    if asc == 'Cap' and phd.get('Ju') == 1:
        print("If Ju 1H really gives very bad results, these people don’t live long life. \n")
    if asc == 'Cap' and (set([("Ve 7H"),("Ju 1H"),("Me 8H")]) <= set(planets_houses)):
        print("But if Ju 1H and Ve 7H, Me 8H then they live long life but they are poor people. \n")
    if asc == 'Cap' and phd.get('Ve') in (5,10):
        print("Ve can give very good results 5H not 10H. S: Because 10H male by house and sign? P. Yes. \n")
    if asc == 'Cap' and phd.get('Sa') == 10:
        print("Sa 10H gives long life wife. \n")
    if asc == 'Cap' and phd.get('Ju') == 9:
        print("9H Ju very sattvic person, travels a lot here and there, and sometime many Saddhu people go here and there. S: Because Ju aspects own sign 3H? P. Yes, traveling. \n")
    if asc == 'Cap' and phd.get('Ma') == 1:
        print("Ma 1H can go easily angry, if he can invest in property can get good money and lots of property. \n")
    if asc == 'Cap' and phd.get('Sa') == 4:
        print("S: Sa 4H? P. Not good for mental peace. Good for ten house, good for 1H, but not good for 1H, for the mother especially. \n")
    if asc == 'Cap' and phd.get('Ma') == 10:
        print("S: Ma 10H? P. Very good. \n")
    if asc == 'Cap' and (set([("Ma 10H"),("Ra 10H")]) <= set(planets_houses)):
        print("S: Ma with Ra 10H? P. Good but sometime bad karma. S: For relationship? P. Not so easy, but no connectivity with relationship with the man. S: Fighter? P. Boxer fighter, or beating the wife. S: Girl has combination 10H Ma and Ra? P. Not good. \n")
#5H Mo, 9H Ju, and Ve and Me asc big Raj yoga, can be very good administrative job, very high position.
    if asc == 'Cap' and (set([("Ve 3H"),("Me 3H")]) <= set(planets_houses)):
        print("Ve and Me 3H very good combination for creativity, good architect, and good wood work. \n")
    if asc == 'Cap' and phd.get('Ra') == 10:
        print("10H Ra, brings very good diplomat. \n")
    if asc == 'Cap' and (phd.get('Ve') == 10) and ("Ve" in (sorted(k for k,v in phd.items() if cn[v] == 1))):
        print("Alone Ve 10H sometime children are not good, they can take money after death of father, and expend all money negative way. \n")
    if asc == 'Cap' and (set([("Ma 11H"),("Ve 11H"),("Ju 1H")]) <= set(planets_houses)):
        print("Ma and Ve 11H and Ju 1H sometime can take money of brother, after brother dies. S: Steal also or just after death? P. After death. \n")
    if asc == 'Cap' and (phd.get('Me')) == (phd.get('Ju')) and ((phd.get('Me')) in juA) and ((phd.get('Me')) in raA) :
        print("Me and Ju together aspected by Sa and Ra, so older brother not so long life. \n")

    if asc == 'Cap' and phd.get('Mo') == 12:
        print("Mo 12H traveling a lot and sleeping with many women. \n")
    if asc == 'Cap' and (set([("Ve 12H"),("Su 1H"),("Mo 1H"),("Me 1H"),("Ma 12H")]) <= set(planets_houses)):
        print("Su and Mo 1H with Me, 12H Ma and Ve so brother helps a lot. \n")
    if asc == 'Cap' and (set([("Me 9H"),("Sa 9H")]) <= set(planets_houses)):
        print("Me, Sa 9H even born simple family reaches very high level. 1L and 9L together big combination for this asc. \n")
    if asc == 'Cap' and (set([("Me 7H"),("Ju 7H")]) <= set(planets_houses)):
        print("Me and Ju 7H wife can have big trouble. \n")
    if asc == 'Cap' and phd.get('Ve') == 1:
        print("But 1H Ve brings good money. \n")
    if asc == 'Cap' and (set([("Ma 1H"),("Mo 7H")]) <= set(planets_houses)):
        print("1H Ma, 7H Mo brings very good money. \n")
    if asc == 'Cap' and (set([("Ve 11H"),("Ma 5H"),("Su 10H"),("Me 10H")]) <= set(planets_houses)):
        print("5H Ma 11H Ve and 10H Me and Su, very good money. \n")
    if asc == 'Aq':
        print("AQ ASC:\nSu is karaka. Mo neutral, sometime not karaka. Ma akaraka. If Ma very weak little brother doesn’t have long life.  Me akaraka and sometime karaka, Ju marrkesh. Where Ju aspects the house gets some value, because 2H and 11H are houses of value, like gold is valuable. S: And where Ju sits? P. This is different thing.. , Ve purna karaka. Ve stronger makes very good money, lots of cars and things, even combust, or retrograde sometime will give less results but good results. Sa karaka. \n")
    if asc == 'Aq' and phd.get('Ju') in (2,11):
        print("Good Ju makes lots of money, 2L 2H, 11L 11H \n")
    if asc == 'Aq' and (set([("Ra 11H"),("Ju 11H")]) <= set(planets_houses)):
        print("Ra 11H with Ju, chandal yoga, makes very good money by negative work. \n")
    if asc == 'Aq' and phd.get('Ju') == 9:
        print("Ju 9H aspecting 3H the brother will be rich person, like that, aspecting 6H enemies can be more successful than him.\n")
    if asc == 'Aq' and (set([("Ve 11H"),("Ju 2H")]) <= set(planets_houses)):
        print("Ju in 2H and Ve 11H born in very low family but become very rich later. Even they have very bad combinations they can become very rich. 2L and 11L 2H, and 4L and 9L 11H, very very good.  \n")

    #    print("Same thing Ma and Ve should give good results but they don’t give results, same as Leo asc, they give only blood sugar sometime, laughing.. \n")
    if asc == 'Aq' and (set([("Ve 10H"),("Ju 9H")]) <= set(planets_houses)) and (10 in saA):
        print("Ju 9H and Ve 10H, and Ve aspected by Sa good combination for money, can gets lots of money, sometime can get money for spirituality, like prem baba and shanti mai. S: Is it enough that Sa one side aspects Ve? P. 1L aspect very good, and Ve is very good friend. 11L 9H and Ve 10H aspected by Sa, 11L 11 from 11, Ve in 2nd to 9H, money place for 9H, aspected by 1L very good combination for money, can make billions of dollars, can get lots of money from family. Bill Gate’s son, Roger, got lots of money from his father. \n")
    if asc == 'Aq' and phd.get('Ma') == 3:
        print("Ma 3H can have lots of brothers. Ma 3L younger brothers, \n")
    if asc == 'Aq' and phd.get('Ma') in (2,11):
         print("Ma 11H or 2H so no brother. Nobody can be brother if he goes family house or 11H. If Mo very weak, 2H 12 from 3rd, and 11H nobody can be brother, because 11H is older. \n")
    if asc == 'Aq' and phd.get('Ve') == 12:
         print("12H Ve doesn’t give good results. S: Why? P. 4L and 9L in sign of Cap. S: Cap fallen sign of Ve? P. Ya, ya. \n")
    if asc == 'Aq' and (set([("Me 5H"),("Ju 5H"),("Sa 11H")]) <= set(planets_houses)):
         print("Me and Ju 5H, 11H Sa difficulty to getting babies sometime. \n")
    if asc == 'Aq' and (set([("Sa 2H"),("Ju 1H")]) <= set(planets_houses)):
         print("1L 2H and 2L 1H not good Raj yoga, they live very simple life all the life, or they can have lots of money but they don’t show, like miser. \n")
    if asc == 'Aq' and (set([("Sa 11H"),("Ve 11H")]) <= set(planets_houses)):
         print("Sa and Ve 11H very very good. \n")
    if asc == 'Aq' and phd.get('Mo') == 4:
         print("4H Mo also loves his enemies, 6L 4H. \n")
    if asc == 'Aq' and phd.get('Su') == 7:
         print("Su 7H the wife will be courageous, fighter, can be stronger than her husband.\n")
    if asc == 'Aq' and phd.get('Su') == 9:
         print("Same thing if 7L goes 9H, the wife lives doesn’t live long life (false sign). \n")
    if asc == 'Aq' and phd.get('Su') == 3:
         print("3H Su brings very high thinking and very nice energy.  \n")
    if asc == 'Aq' and phd.get('Me') == 8:
         print("8H Me brings long life. \n")
    if asc == 'Aq' and phd.get('Me') == 2:
         print("2H Me lives far from family, and gets problem from son. \n")
    if asc == 'Aq' and (phd.get('Sa') == 10) and ("Sa" in (sorted(k for k,v in phd.items() if cn[v] == 1))):
         print("Alone Sa 10H very very good, can make millions of money, and very strong power.\n")
    if asc == 'Aq' and phd.get('Me') == 8:
         print("S. Me 8H good for children? P. Yes. S: Still 8 from 1H. P. Good for long life of person, will trouble to children. \n")
    if asc == 'Pi':
         print("PI ASC:\nSu neutral, Mo karaka, Ma bit karaka and bit akaraka, Me neutral, Ju karaka, Ve Purn akaraka. S: Ve combust? P. Very good. Sa akaraka. Ma stronger aspected by Ju or good planet horoscope goes stronger. The more Ve goes down, horoscope goes stronger. As much as Su and Mo would be far good for children and family, but not full Mo. \n")
    if asc == 'Pi' and phd.get('Ve') == 12:
         print("Ve 12H doesn’t bring very good energy, during its inter period people can take loan but will be difficult for them to return. \n")
    if asc == 'Pi' and phd.get('Mo') == 12:
         print("Mo 5L 12H also not so good.\n")
    if asc == 'Pi' and phd.get('Sa') == 12:
         print("Sa 12H brings very good energy, very good life. 11L own sign 12H and 11 from 2H gives very good money.  \n")
    if asc == 'Pi' and phd.get('Ma') == 11:
         print("Ma 11H really really great, lots of positive energy for the life, lots of energy money-wise, can make lots of money in their life, 2L and 9L exalted 11H really great combination.\n")
    if asc == 'Pi' and phd.get('Ma') == 5:
         print("5H Ma, sometime wife or brother of wife can destroy all the money. \n")
    if asc == 'Pi' and phd.get('Ve') == 1:
         print("Ve 1H if they go Bhakti yoga can go very high. \n")
    if asc == 'Pi' and phd.get('Ju') == 12:
         print("S: Ju 12H? P. Physical problems it gives, and sometime mother father don’t stay together, sometime they can leave their country and live there. Physical problems because Sa sign and aspecting 6H, more diseases enemies will come. \n")
    if asc == 'Pi' and phd.get('Me') == 8:
         print("8H Me father can die very early. \n")
    if asc == 'Pi' and (phd.get('Ke') == 7) and (phd.get('Ve') in (1,7)):
         print("Ke 7H and Ve 1 or 7 house can have very strong sexual energy, can see all the objects for sex (not clear). \n")
    if asc == 'Pi' and (phd.get('Me') == 1) and ("Me" in (sorted(k for k,v in phd.items() if cn[v] == 1))):
         print("Alone Me 1H sometime don’t get energy from father, 10 from 10, 7L 1H kendradipathi dosha stronger, don’t connect with father. Me and Ju like father and son, illegal child of father. \n")
    if asc == 'Pi' and phd.get('Me') == 2:
         print("2H Me during childhood, this person doesn’t get pleasure, gets sadness, weaker than wife in man’s chart.\n")
    if asc == 'Pi' and phd.get('Ju') == 5:
         print("5H Ju sometime problem to father, can become handicapped. \n")
    if asc == 'Pi' and (set([("Su 11H"),("Ve 11H"),("Me 11H")]) <= set(planets_houses)):
         print("S: Su, Ve and Me 11H? P. A little bit problem moneywise, because Su 6 from 6 and aspecting the mind, they try to do best but mind can make them problem, they can be their own enemy, where they can get profit their mind can say no, no, no, they miss the opportunity. S: Aspect 5H? P. Problem woman area, and stomach area. S: Why woman area? P. Woman area and children house.\n")
    if asc == 'Pi' and (set([("Su 1H"),("Ju 1H"),("Me 1H")]) <= set(planets_houses)):
         print("S: Su, Ju and Me 1H? P. Ju very good 1H. P.  S: And together with Su and Me? P. Not problem. Me fall but Ju will make them very positive. Tricky person, very tricky know how to make tricks, very technical mind, very practical, 1H very good combination. \n")
    if asc == 'Pi' and (set([("Su 1H"),("Ve 1H"),("Ma 1H"),("Ju 8H")]) <= set(planets_houses)):
         print("Same like Sag asc and Sa 5H. Su Ma Ve 1H and Ju 8H, Ju/Ma period can go to jail even for one night. \n")
    if asc == 'Pi' and (set([("Ju 6H"),("Ve 8H"),("Sa 9H")]) <= set(planets_houses)):
         print("Ju 6H, Ve 8H and Sa 9H, very good for money. S: Why Ju 6H? P. 6H Ju can give very good money sometime this asc, where it sits destroys quality of this house, 6H. S: Can also cause health problems? P. Yes health problems. S: Destroys enemies. P. Very good destroys enemies and this.\n")
    if asc == 'Pi' and (set([("Ma 11H"),("Sa 11H")]) <= set(planets_houses)):
         print("If Ma and Sa 11H best for money. \n")
    if asc == 'Pi' and (set([("Ma 9H"),("Sa 9H")]) <= set(planets_houses)):
         print("Sa and Ma 9H can do negative bad karma young age then they suffer. S: Why young age? P. Ma young age planet, ear can be problematic, they cannot hear very good way, when Sa and Ma 9H. \n")
    if asc == 'Pi' and (set([("Ma 3H"),("Sa 3H")]) <= set(planets_houses)):
         print("They cannot hear very good way, when Sa and Ma 3H. \n")
    if asc == 'Pi' and (set([("Ma 11H"),("Mo 11H"),("Me 11H")]) <= set(planets_houses)):
         print("Ma, Mo and Me 11H, all life they have very good car.\n")
    if asc == 'Pi' and phd.get('Mo') == 9:
         print("9H Mo son always goes sick, pneumonia or some lungs problem.\n")
    if asc == 'Pi' and (set([("Ma 4H"),("Mo 4H"),("Me 4H"),("Ju 4H")]) <= set(planets_houses)):
         print("Ma, Mo, Me, Ju 4H lots of property, can make lots of money by property work and buying and selling. \n")
    if asc == 'Pi' and (set([("Sa 7H"),("Su 7H"),("Me 12H")]) <= set(planets_houses)):
         print("Su and Sa 7H and 12H Me, all life can have very bad marriage life.\n")
    if asc == 'Pi' and phd.get('Me') == 12:
         print("S. I know person with Me 12H very good poet and artist. P. But marriage life not so good. S: But good otherwise? P. Ya, ya. \n")
    if asc == 'Pi' and phd.get('Me') == 11:
         print("S: Me 11H for marriage? P. Ok. S. If combust. P. Then they should be very careful with whom they marry, sometime they can be cheated by man, need to choose man carefully. \n")
    if asc == 'Pi' and phd.get('Sa') == 11:
         print("S: Sa 11H? P. Very good. But 11H Sa big brother drinks alcohol, and has very sharp voice. S: Older brother or him? P. Older brother. \n")
    if asc == 'Pi' and phd.get('Sa') == 2:
         print("2H Sa sometime family members use all their money, destroy all money, or sometime he gives money to family member and doesn’t get back. S: Also get money from family? P. Get money but false go down. S: 11L and 12L 2H. P. Mixed results. \n")
    if asc == 'Pi' and (set([("Sa 12H"),("Ju 1H"),("Ma 9H")]) <= set(planets_houses)):
         print("Aq Sa 12H, Ju 1H 9H Ma very good person, very spiritual and very good enlightened path. 9H Ma always keeps person alert, and sometime too much alertness can make mind crazy.\n")
"""

    if asc == 'Cap' and
        print("\n")
    if asc == 'Cap' and
        print("\n")
"""



def periodinfo():
    print("PERIOD INFO:")
    if asc == 'Ar':
        print("Period info:\nMo 4L gives during its period all kind of pleasure and joy. If sitting 6, 8, 12 they will give less result.\nSu 5L master of trikona, so during its period gives very very good results. Always give raj yoga, promotion, good child, good income.\nJu 9L and 12L starting of dasha, antar dasha gives very good results but later bad results, mixed results, but most of time positive results, depends on where Ju is sitting. If Ju 9H sure good results. 12H little bit bad results. \n")
    if asc == 'Ar' and ("Ma 5H") in planets_houses:
        print("Ma 5H gives very good progress in its dasha.\n ")
    if asc == 'Ar' and ("Ju 11H") in planets_houses:
        print("Ju 11H not good dasha.\n ")
    if asc == 'Ta':
        print("Period info:\nDuring Mo period sometime fighting with brother and depression can come, if Mo not good in horoscope, if good in horoscope gives love to brother. Ma gives in its period not good for family, health issues. If not good fire can come to house. Me starting gives good results but later not good results, because 2L and 5L. Ju gives physical health problems during its dasha. Sa gives very good results, dasha and antardasha can give very positive results. \n")
    if asc == 'Ta' and (phd.get('Me') == phd.get('Ve')):
        print("Me and Ve together then dasha of Me will be very very good.\n")
    if asc == 'Ta' and (set([("Ma 1H"),("Ve 1H")]) <= set(planets_houses)) and ((1 in juA) or (1 in meA)):
        print("Ma and Ve in asc, and Ju or Me, one of them, aspect them, then Me period will be very very good. \n")
    if asc == 'Ta':
        print("Ve period always good, good money good energy. \n")
    if asc == 'Ge'and (set([("Mo 8H"),("Ma 2H"),("Sa 2H")]) <= set(planets_houses)):
        print("If 8H Mo, and Sa and Ma 2H even born rich family, during Sa period can become very very poor. \n")
    if asc == 'Le':
        print("Sometime Ve period gives the person transfer from one job to another. Su period Leo asc, very good dasha. Mo period, best period is Mo/Me and Mo/Ke, also Mo/Su, and Mo/Ma very good. Ju/Sa and Ju/Mo, Ju/Ra not good periods, Ju/Su, Ju/Ma, Ju/Me very good. Sa/Ke and Sa/Me very very good, Sa/Ve good, Sa/Ra not good, but Me/Ju not good. S: Why? P.8L, 2L always gives some trouble. 8L 2H is ok. Ju always think Me is enemy, Me doesn’t think Ju is enemy. Ke dasha good other than Ke/Ra. \n")
    if asc == 'Le' and (phd.get('Sa') in (2,8)):
        print("Sa 2H or 8H, Sa period sometime not good period, but if they work mines, coal, gas, oil, can make lots of money. \n")
    if asc == 'Li':
        print("Ma period problems. \n")
    if asc == 'Li' and (set([("Sa 1H"),("Mo 10H")]) <= set(planets_houses)):
        print("Sa 1H and 10H Mo period goes very good, gives lots of money and lots of prosperity. \n")
    if asc == 'Sc' and (set([("Su 7H"),("Me 7H"),("Ve 7H")]) <= set(planets_houses)):
        print("Su, Me and Ve 7H. Me period very good, even though Me akaraka, brings name and fame, good position, good energy.  S: Su makes Me weaker? P. 11L 7H very good and Me indicator for money. 7H house of finance and business. S: And Su? P. Su is karma. S: Ve and Me akaraka? P. Sometime akaraka make very good combinations with Su, experience says so. S: This exeperience from your tradition or Gotham? X. Tradition. \n")
    if asc == 'Sa' and (set([("Sa 3H"),("Su 9H"),("Ve 9H")]) <= set(planets_houses)):
        print("3H Sa, and 9H Su and Ve, also brings Sa period very strong. \n")
    if asc == 'Cap':
        print("Usually Me is not so much indicator, 6L but own dasha and period gives very good results. Ju period gives very bad results. Usually Su period is good for this asc even 8L.  \n")
    if asc == 'Cap' and (set([("Ju 12H"),("Ra 12H")]) <= set(planets_houses)):
        print("Ra and Ju 12H usually Ju period very good can go very high level, but whatever money made during Ju period will be lost after Ju. Ju and Ra become same planet Ra Ra, but after Sa begins all money is lost. S: Positive money? P. Not positive money. \n")
    if asc == 'Aq':
        print("Ve/Ve doesn’t give good results. \n")
    if asc == 'Aq' and (set([("Su 1H"),("Ve 1H"),("Ra 10H")]) <= set(planets_houses)):
        print("If asc has Su and Ve, 10H Ra the dasha of Ra goes very very good and also Ju dasha goes very good. S: No matter where Ju sits? P. Ya. \n")
    if asc == 'Aq':
        print("Me period very good especially the first 10 years. Me/Me, Me/Ke, Me/Ve, Me/Su positive but when Me/Ra (Me/Mo?) comes problem starts. \n")
    if asc == 'Aq' and (set([("Su 8H"),("Ma 8H")]) <= set(planets_houses)):
        print("Su and Ma 8H both dashas go very bad. Even born very rich family can go very low. \n")
    if asc == 'Aq' and (set([("Su 3H"),("Me 3H"),("Ju 3H")]) <= set(planets_houses)):
        print("Su, Ju, and Me 3H, then Su period very good and can make lots of money. \n")
    if asc == 'Pi':
        print("Su dasha most of time good dasha, Su/Su Su/Ra not good. Mo dasha very very good, only Mo/Ve can cause some trouble. Ma dasha very very good, other than Ma/Su. Ra dasha most of time good, but Ra/Ve and Ra/Su give some trouble also. Ju dasha very good, but Ju/Su gives problem in body. Sa dasha good other than Sa/Su, Sa/Ve. S: Even though Sa akaraka? P. No problem. Me dasha very good other than Me/Ra and Me/Ve normal, but need to see also where they are sitting. S: Because Me and Ra both rule 7H? P. Yes. Ke dasha also good. Shukra dasha, Ma, Ra, and Ju go better, other periods go totally crazy.\n")
    if asc == 'Pi' and (set([("Mo 2H"),("Ma 5H")]) <= set(planets_houses)):
        print("2H Mo and 5H Ma, so Ma dasha goes very good, gives good result. \n")
    if asc == 'Pi' and phd.get('Ju') == 10:
        print("10H Ju, Ju period will go very good. \n")

maA = []
juA = []
saA = []
veA = []
meA = []
moA = []
suA = []
raA = []
keA = []

def asp():
    global maA
    global juA
    global saA
    global veA
    global meA
    global moA
    global suA
    global raA
    global keA
    for k,v in phd.items():
        if k == 'Ma':
            maA.extend((v+3,v+6,v+7))
        if k == 'Ju':
            juA.extend((v+4,v+6,v+8))
        if k == 'Sa':
            saA.extend((v+2,v+6,v+9))
        if k == 'Ve':
            veA.append((v+6))
        if k == 'Me':
            meA.append((v+6))
        if k == 'Mo':
            moA.append((v+6))
        if k == 'Su':
            suA.append((v+6))
        if k == 'Ra':
            raA.append((v+6))
        if k == 'Ke':
            keA.append((v+6))


allA = []

def correctasp():
    global allA
    for y in allA:
        y[:] = [int(x)-12 if int(x)>12 else x for x in y]
    return(allA)

def MaSa():
 #   for k,v in phd.items():
     global phd
     if (phd['Ma'] in saA) and (phd['Sa'] in maA):
        print("Ma and Sa asp each other\n")
     if not(set(saA).intersection(maA)):
         pass
     else:
         for x in (set(saA).intersection(maA)):
             print("Ma and Sa asp",str(x)+"H")
         print("\n")

fmoon = []

def fullmoon():
    global phd
    global fmoon
    if (phd['Mo'] in suA):
        fmoon.append("y")
        print("Born during full moon\n")


def exchangechecker():
    if (1,11) in exchangel:
        print("Exchange 1-11: 2nd best exchange for money after 9-11 exchange. 1-11: PL served with body, worship. \n")
    if (1,3) in exchangel and asc == 'Pi':
        print("S: Pi asc exchange 1-3? P. Very good. \n")
    if (2,5) in exchangel and asc == 'Li':
        print("Exchange 2-5, asc Li: S. How about 2-5 exchange, Sa Ma, for Lib asc? P. This a little bit less, trikona.. \n")
    if (2,8) in exchangel:
        print("Exchange 2-8: Not good, gives sometime trouble. \n")
    if (2,11) in exchangel and asc == 'Cap':
        print("Exchange 2-11, asc Cap: P. I saw 11-2 exchange, Sa and Ma, for Cap asc, very big money he made, big land here in Rishikesh and Haridwar. \n")
    if (3,5) in exchangel and asc == 'Ta':
        print("Exchange 3-5, asc Ta: Very big talkers, can talk very good way.\n ")
    if (5,6) in exchangel:
        print("Exchange 5-6: Generally gives trouble to stomach a lot. \n")
    if (5,7) in exchangel:
        print("Exchange 5-7: Very very good for getting high profile person for marriage.\n")
    if (5,11) in exchangel:
        print("Exchange 5-11: 3rd best exchange for money after 9-11 and 1-11. 5-11: PL you invented something that people still use, you still get profit \n")

    if (8,10) in exchangel and asc == 'Vi':
        print("Exchange 8-10, Vi asc: S: 10-8 exchange Vi asc? P. Tongue can be very sharp, they can say very bad things sometime, and by accident people can die. If they work with mine, property, land the can make very good money. Digging wells, roads can make very good money. S: Very good for 10H but not for 1H. P. Yes. S: Can make good money but.. P. Lose the money also. S: Maybe not honest. P. They can be misers. They can put all the money in the bank, not give to other people, because 2H is house of bank money, make money for the bank not for the family.\n")
    if (8,10) in exchangel:
        print("Exchange 8-10: Good in property but sometimes illness can come. S. What kind of illness? P. Woman area problem. S. Ups and downs in job? P. Yes, exchange is not good. Confusion in job, what to do? They have to concentrate mind in one work and sure they have success. They should not leave the job again and again. S. When you say good in property is it real estate? P. Real estate or property doesn’t belong to them and they can get commissions. S. Can it be other kind of business? P. Other kind of business also, commission business. They aspect the 4H, not their own property but they can sell.\n")
    if (6,8) in exchangel:
        print("S. Good for long life just like 8-12 exchange? P. No.\n6-8 exchange very good, very rich people, sometime they can get car with flag (government officers). Vipareeta yoga sometime more powerful than Kendra-Trikona exchange, I saw even 9-10 exchange, sometime not effective, but 6-12 or 6-8 exchange very strong. S: Even if say Ju and Ve? P. No problem, even stronger because they have totally opposite qualities. \n")
    if (8,12) in exchangel:
        print("Exchange 8-12: Very good for long life. S. Same for 8 and 6? P. No, 8 and 12. Very good in education. Good ambassador or in consulate, representatives of own country. Very intelligent. Photographic memory. S. Why? P. 5 from 8. It’s like and exchange between 5 and 8. S. Because 12H is 8 from 5? P. 8 from 5. And it is 8L sitting from the 8 in the 5H again. S. Why photographic? House of the eye? P. Yes. S. Intelligent because of same reason? P. Same reason. But only if this is exchange. All that I said is for exchange. S. Good education, good ambassador? P. Yes, all for exchange. They don’t die in other country, they die in own\n")
    if asc == 'Ge'and (set([("Sa 12H"),("Ve 8H")]) <= set(planets_houses)):
        print("Exchange 8-12, Ge asc: Very good.")

    if (9,11) in exchangel:
        print("Exchange 9-11 is best of profit. Best exchange for money: PL good, spiritual\n")
    if (9,11) in exchangel and asc == 'Le':
        print("Le asc exchange Ma and Me: make money from another country\n")
    if (9,12) in exchangel:
        print("Confirm") #S: If exchange 12 and 9? P. Very good spiritual man, but he will have guru from other country. S: For Ar asc? P. This is different thing, Ju there 9H they think they are the guru.


#S: 12 and 10 exchange? P. If they can go enlightenment field, if positive planets, they don’t want to do bad karma they want to be pure, nice people, good exchange. If benefic planets can be highly intellectual people. If malefic planets intelligent but mind can go hocus pocus, can do black magic and shamanic healing this kind of thing. S: Intelligent because 6 and 8 exchange from 5H? P. Ya (but not entirely convincing). S: Good for father? P. Good for father also, yes. S: But exchange between Kendra and dusthana? P. Good for father for work, property and health for father, not for life and health of father.
#S: My brother has Vi asc, 10 and 8 exchange. P. Very clever guy. S: Why so clever? P. 8H is silent knowledge, hidden knowledge. Very clever people. S: 10 and 8 exchange not good for health of father, but good for property? P. Agrees… S: Doesn’t it make connection between karma and 8H? P. Can sell out things for dead, can make lots of money. These people can sell out flowers for graveyard. S: What kind of karma does it bring? P. Nothing, they are helping. S: Make money of death. P. No, help them. When you kill animal after death your sell it. You didn’t kill them, killed by gods selling service for them. People near death can cure their pain, give massage to them, can cure their pain, main thing, if someone die near family nobody near them, if you go to help you are very near friend to them, this is 8 and 10 house combinations, like in our family, people come all over the world, burn their body in the ganga, they come to us and we help them do ceremonies to release the soul, go and never come back, clean the karma, very good work. The relatives don’t want to touch the body, you are like angel, very good work.
# S: 12 and 11 exchange, my sister in law has this for Li asc? P. She can make money to money, she can give rent and get money. But very strange people, very clever people, they know how to use other people.


def plhochecker():
    global cn
    if ("Ve 4H") in planets_houses and asc == 'Sa':
        print("Ve 4H, asc Sa: Not good, gives trouble from family, no happiness, 6L sitting 4H is not good. \n")
    if ("Ve 7H") in planets_houses and ("Ve" in (sorted(k for k,v in phd.items() if cn[v] == 1))):
        print("Ve alone 7H will not give very good results, divorce or woman will have affairs, partner will not be satisfied. \n")
    if ("Ve 7H") in planets_houses and asc == 'Ar':
        print("Ve 7H, asc Ar: If alone in 7H will not give very good results, divorce or woman will have affairs, partner will not be satisfied. \n")
    if ("Ju 1H") in planets_houses and asc == 'Ta' and (("Ju R") in retrolist):
        print("Ju R 1H Ta asc: S.In general how does it change if retro, goes the opposite? P. Totally changes the energy. So Ta Ju 1H? P. Then less negative results come (in general Ta asc Ju 1H not so good results, see below..)  S. But still not good. P. No, but less results.\n")
    if ("Ju 1H") in planets_houses and asc == 'Can':
        print("Ju 1H, Can asc: These people lie a lot. One moment they can be very angry other moment they can be very normal, one moment very high temper, they can kill all the world, after 10 min, normal (relaxed). And lie a lot, but sweet lying, people like their lying. Like I was in bus saw elephant, elephant came in bus. They are pathological lyers. They are not easy people, always things if I show other’s mistake they will become best. They have big difficulty to say about somebody else they are good guys, they never say. If they say about anyone that he is a good person, they think this is the best thing they did in their life; they never say. Not good for partnership... \nThey don’t even remember what they said yesterday. S. Bad memory? P. No, they talk too much. To hide one lie, you have to talk a lot. \n")
    if ("Ju 1H") in planets_houses and asc == 'Can' and (("Ju R") in retrolist):
        print("Ju 1H, Can asc: These people lie a lot.  S: If retrograde worse? P. Prateek agrees and laughs. These people make little things big things, because Ju is big planet. If they see stick on floor they say snake. They like to make sensations. S. They like in small things or also in important things, to exaggerate or fundamental things? P. Many things.  S. So you can trust them. P. I don´t trust them. \n")
    if ("Ju 1H") in planets_houses and asc == 'Pi' and (("Ju R") in retrolist):
        print("Ju R 1H Pi asc: S.In general how does it change if retro, goes the opposite? P. Totally changes the energy. S. Pi asc then less good? P. Better, then more powerful.\n")
    if ("Ju 1H") in planets_houses and asc == 'Sa' and (("Ju R") in retrolist):
        print("JuR 1H Sa asc: S.In general how does it change if retro, goes the opposite? P. Totally changes the energy. S. In Sa asc then very bad for health for example? S. Not good for health but good for lots of knowledge. But this will be nothing, they won´t be using this.\n")
    if ("Ju 1H") in planets_houses and asc == 'Ge':
        print("Ju 1H, Ge asc: starting life is ups and down, later age becomes better. They don’t think too much about to make house, these things, if coming they welcome it, if not they don’t care. S. They don´t care about materialistic things. P. They don´t care, if coming good, but not fighting for that. If god gives them good money to live and they live good life. They love their partners a lot, they want to go with them until they want to do, they don’t force it but want to go until the last day of their life.  \nGood for people who want to study about Ayurveda, also good combination for lawyers, judge, can get good name and fame in these subjects. Very sharp minded people. Very successful in debate, not this not that. \n")
    if ("Ju 1H") in planets_houses and asc == 'Li':
        print("Ju 1H, Li asc: Can be poet or singer. They don’t think too much about to make house, these things, if coming they welcome it, if not they don’t care. S. They don´t care about materialistic things. P. They don´t care, if coming good, but not fighting for that. If god gives them good money to live and they live good life. They love their partners a lot, they want to go with them until they want to do, they don’t force it but want to go until the last day of their life.  \nGood for people who want to study about Ayurveda, also good combination for lawyers, judge, can get good name and fame in these subjects. Very sharp minded people. Very successful in debate, not this not that \n")
    if ("Ju 1H") in planets_houses and asc == 'Cap':
        print("Ju 1H, Cap asc: They like a little to go to cinema, theatre and like to read lots of books. Most of the time bad results come. They talk a lot of gossip. And not good habits. Always jealous. They don’t lie they want to show people they are the best. 1H has ego, what I say it´s right . S. How is it for partnership? P. Very good. S. Brings a lot of partners? P. Not a lot of partners but good partner. Very good people.... \nFantastic, even if they do something they can say, no, no, he did it, give to him. S: Still something false in their personality? P. Of course. False is they don’t have lots of things to do. Cancer  people have lot of things to play with, like born with building. Cap building have to build their building, their playground, and then play. S. But they will manage to build it? P. [apparently agrees]. Very surprising things.  \nBut in Cap physical level not very good, but when they cross 40, 45 no disease they can get good life.\n")
    if ("Ju 1H") in planets_houses and asc == 'Aq':
        print("Ju 1H, Aq asc: They don’t think too much about to make house, these things, if coming they welcome it, if not they don’t care. S. They don´t care about materialistic things. P. They don´t care, if coming good, but not fighting for that. If god gives them good money to live and they live good life. They love their partners a lot, they want to go with them until they want to do, they don’t force it but want to go until the last day of their life.  \nGood for people who want to study about Ayurveda, also good combination for lawyers, judge, can get good name and fame in these subjects. Very sharp minded people. Very successful in debate, not this not that, because most of time Aq people like logic things, they want to learn by logic and have good logic mind. \n")
    if ("Ju 1H") in planets_houses and asc == 'Pi':
        print("Ju 1H, Pi asc: Very good habits, they make good institutions for helping, they can make big NGO institutions, for children, for older people, they think not only about little family, they see all world is my family. They think not only about their joy but also of other people, they have good luck, sometime they don’t get married, and sometime they get more than two marriages. S: One marriage possible? P. Possible but sometime they don’t think only for partner, they think for other people, wife can feel maybe he has other women, but they don´t, so this makes problem. If you have something very near you can´t see it, they feel like my wife is part of me, they don´t see it. \n")
    if ("Ju 1H") in planets_houses and (asc in('Ar','Le','Sa')):
        print("Ju 1H this asc: gives good result, they are open hearted people and behave like a king, always try to do good work for welfare they know how to deal with people, they love all people in neighbourhood, they are like relatives. Long life, they want to do good worship.  Even they don’t have good education they look like they have lots of  knowledge. P. Magha Nak problematic? P. Not good 1st and 2nd pada. This is good for religious people. S. Same for Ash nak? P. Magha nak more. P. Most of time can have good knowledge about language, teaching, lawyer, judge, writer, singing, good name, good fame.\n")
    if ("Ju 1H") in planets_houses and (asc in('Ar','Le','Sa','Ge','Pi')):
        print("Ju 1H this asc gives all the good results. If Ju not aspected by any negative planet, woman mostly, can become pregnant early age. But possible also that time period the boy 13 y/old had strong body, can have relationship with older woman she can have baby.\n")
    if ("Ju 1H") in planets_houses and (asc in('Ta','Vi','Cap','Aq','Sc')):
        print("Ju 1H this asc: First half of life will be not good for body.\n")
    if ("Ju 1H") in planets_houses and (asc in('Ar','Ge','Can','Vi','Cap')):
        print("Ju 1H this asc: People don’t loose most of time hair. Beard has less hair than moustache. Can be good players, sportsmen if Ma combines with Ju. They can mimic other people well, like acting. S. With Ma also? P. Alone. Witty, make lots of fun in life. Starting age, harder work but slowly slowly better. They like friendship very much. When they get good position they can also make good money. But these people don’t collect the money. They follow the tradition, sometime proud of family tradition. People sometime try to give them some negative energy but by their own mind/energy they can neutralize all negative energy. \n")
    if ("Ju 1H") in planets_houses and (asc in('Ta','Le','Li','Sc','Sa','Aq','Pi')):
        print("Ju 1H this asc: they can loose hair on head early age.\n")
    if ("Ju 1H") in planets_houses and asc == 'Sc':
        print("Ju 1H this asc: If Ju not aspected by any negative planet, woman mostly, can become pregnant early age. These people also have negative feelings, lots of anger, and they do sometime activities good people don’t like. S: If Ju retrograde 1H Sc asc? P. Different. \n")
    if ("Ju 1H") in planets_houses and (asc in('Ar','Le')):
        print("Ju 1H this asc: not too many children are born.\n")
    if ("Ju 1H") in planets_houses and (asc in('Ar','Le')) and (("Ju R") in retrolist):
        print("Ju R 1H this asc: S.In general how does it change if retro, goes the opposite? P. Totally changes the energy. S. So for Ar and Leo asc if retro (few children, see above..), then a lot of children or normal? P. Normal (amount of) children.\n")
    if ("Ju 1H") in planets_houses and (asc in('Ta','Ca','Vi','Li','Sc','Cap','Aq')):
        print("Ju 1H this asc: Doesn’t give good results, you have to suffer. S: Mixed results? P.  Not good. Very few result can be good, but most of the time not good results come. \n")
    if ("Ju 1H") in planets_houses:
        print("Ju 1H: Lots of vata in the body. Ju is not the planet that gives lots of money in the 1H, ok? Any sign. He gives knowledge, intellectual, vidya, Then other planets can use and then you can make money. Himself he makes person very elite, it won´t guarantee how you will use your education, what you studied. You have knowledge but how you use it depends on other planets also. I give you my knowledge, I´m Ju, but depends on you how you use it, I´m not responsible for how you use the knowledge. \nThey shouldn’t go police and wine, alcohol sector. \nS: Ju 1H not good for the house it sits in (1H)? P. They always have physical problems, beautiful personality but this beautiful life they can´t keep all the life, falling down. Rama horoscope, exalted Ju with Mo 1H, by Ju he left everything and went to jungle. Then Ju was working very nicely, this age opposite. They will say to the brother you go to jail, I stay home and enjoy the life. \n")
    if ("Ju 1H") in planets_houses and ("Ve 1H") in planets_houses and asc == 'Pi':
        print("Ju and Ve 1H, Pi asc: A very highly yogi, had Pi asc, Ju and Ve together 1H. Most of the time these people can be yogi.\n")
    if ("Ju 1H") in planets_houses and ("Me 1H") in planets_houses and asc == 'Pi':
        print("Ju 1H, Pi asc, Me 1H: Father die earlier then mother starts to live with different man, in any nakshatra. S. A friend has Ju, Me and Su, and father lives over 90 years. P. Su indicator of father sitting with Ju, different things. S. But not good relationship with father. \n")
    if ("Ju 1H") in planets_houses and asc == 'Sa' and ("Ma 8H") in planets_houses:
        print("Ju 1H this asc with Ma 8H: sometime they cannot have son (confusion if it’s e also daughter..)\n")
    if ("Ju 1H") in planets_houses and (asc in('Can','Sc')):
        print("Ju 1H Can or Sc asc: They like a lot to eat good food and sometimes they can cook also. Very good for doctor.\n")
    if ("Ju 1H") in planets_houses and asc == 'Pi':
        print("Ju 1H, Pi asc: They like Vedanta, poetry, they like very much Ve things. Very good for doctor.\n ONLY THIS NAK!: Ju UBha Nak 2nd pada brings problems, kills the body, disease in the body. Every 6 or 12 years problems come in life. When Ju comes back in transition. S. Only 1H? P. 1H. S: If Me there? P. It´s ok. But if Ve there, more problems. But if Ve, Me, Ju there, very good. Ju is planet not for giving lots of money, any sign. Gives the knowledge, intellectual, good vidya, lots of subject knowledge, if other planets good can use money. Himself makes person elite, but not sure how to . What´s the logic? P. Me kendra ruler in kendra not good. No sorry, Venus when goes it´s 8L exalted with Ju, killing the body. S. So Me is kendra adipathi, so it´s weak. P. Not making many troubles. S. So lowering down the troubles. P. Yes. \nONLY THIS NAK!: Ju 1H especially UBha Nak 3rd pada sometime they love very much women can have silent relationship with woman. S: For woman also? P. Mostly for men.\n")
    if ("Ju 1H") in planets_houses and (asc in('Ta','Li','Vi')):
        print("Ju 1H this asc: Most of the time bad results come. They talk a lot of gossip. And not good habits. Always jealous. They don’t get good money most of time, if alone, all of these if Ju alone. Suppose in Ta, Li or Cap Sa sitting with Ju these people can have billions, lots of money, beautiful wife and beautiful relationship, because Sa yogakarka, a kind of raja yoga, 9 and 10 together. S: Ju not disturbing Raja yoga? P. Starts to give good results and becomes himself positive there. \n")
    if ("Ju 1H") in planets_houses and (asc in('Ta','Vi')):
        print("Ju 1H Ta or Vi asc: they don’t get pleasure of materialistic life. They easily go scared when difficulties come in life. Easily they don’t feel comfortable. Very stubborn people, and they think what they say is only the right thing. They can tell people they are doing wrong, doing wrong but same mistake they do again and again. They never admit to their mistakes, most of time for Ta asc. They are never romantic people. They don’t like any kind of hobbies like party cinema, they just want to read books. S: So if they have Ve 7H big confusion? P. You are right, big confusion if Ve 7H, because they want to go to see lots of woman, so then, what to do now? If Ve strong in transition they go cinema with friends, if Ve is weak or sits in the horizon or combust will be only in home. They always like to eat good food, what to eat and what not to eat. Sometimes they can cook also. \n")
    if ("Ju 2H") in planets_houses and asc == 'Pi':
        print("2H Ju, Pi asc: Harsh voice\n")
    if ("Ju 2H") in planets_houses and asc == 'Ge':
        print("2H Ju, Ge asc: Sometimes wife can die age of 48-52, or goes very well. S: Osho had this? P. His wife died. The man you can see has company of motorcycles, Bajash, his wife also died, he is Ge asc, his wife died when he was 52. \n")
    if ("Ju 2H") in planets_houses and asc == 'Ge' and ("Ma 2H") in planets_houses:
        print("Ju 2H with Ma, Ge asc: If Ma also there, Ge asc, they all the time have trouble in the mouth, even Ju exalted there. Sometime they have very bad connection with old people in the family. \n")
    if ("Ju 2H") in planets_houses and (asc in('Pi','Can','Sc')):
        print("Ju 2H this asc: If Ju in Ar, Le or Sa they fight with father, mother, something they have totally different energy from them. -->Fire signs \n")
    if ("Ju 2H") in planets_houses and (asc in('Ar','Le','Sa','Cap')):
        print("Ju 2H in Ta, Vi, Cap, Aq sign: they can make some money also. -->Earth signs+Aq\n")
    if ("Ju 2H") in planets_houses and (asc in('Ar','Can','Li','Cap')):
        print("Ju 2H in Ta, Le, Sc, Aq sign: they all the time think about money. If they get money they think oh my god, how to keep this money, so they think a lot. Most of time they have to be true, not lie, then Ju stronger and more money can come. S. In this signs. P. Yeah. S: Also if retrograde? P. They have to control the voice,retro Ju people. S. In the sense of not shouting? P. Not shouting, not lying, not tell bad things to other people, good things they have to tell.  \n")
    if ("Ju 2H") in planets_houses and ("Su 2H") in planets_houses:
        print("If Ju 2H and Su 2H: Father and son cannot progress under same roof, father has to go to different house, mother in different apartment. One house, they never get progress. If son or father go far very much progress comes. \n")
    if ("Ju 2H") in planets_houses and (("Ju R") in retrolist):
        print("If Ju very bad 2H retrograde so family makes money very bad way, they don’t have good income, people get this money and after they suffer by that a lot. Suppose there is one child of the family, he gets some property from the parents, and when the money, the property comes to him he goes disturbed a lot in the life. S. So when Ju is in a bad house. P. In 2H, in a bad sign. S. My brother has Vi asc in 2H. P. So he will get property from the father, but after property, mind goes a bit crazy. S1. Yes, he doesn´t like it, he´s worried. But one of the guys (Yogesh) also had it, Vi asc, Sa 8H.. P. Yes, when his father fies he got some property, his father had big fighting, now he´s living in different house and brother in different house; before they loved a lot together. S. What do you mean by family makes money in a bad way?  S. Not sure about my dad, he´s probably in the middle. So what can my brother do? P. Suppose is he gets 100 rupees, 10 rupees he should donate.  Donation gives the purification of the money, mantra chanting purifies the tongue, bathing in the Ganga and using Ayurveda purifies the body, knowledge about Bhagavad Gita and spiritual books purifies the mind. \n")
    if ("Ju 2H") in planets_houses:
        print("Ju 2H: If people are professional judgement, like lawyer, advocate or something like that or guru or teacher who advises people or gives lecture for Vedanta, yoga, this kind of things, then they make good money, but other people most of time don’t make good money. People who work with voice give lecture, I’m sure they become successful get good money. S. So telling good things. P. Yes, if they becomes astrologers they tell more good things than bad things. But they have very sensitive body, not very strong body. \n")
    if ("Ju 4H") in planets_houses and ("Mo 4H") in planets_houses:
        print("Ju and Mo 4H, Ca asc: I saw Ju exalted with Mo 4H Can sign Gaja Keshari. She has house in Tomsk. But all the life, now 60 years old, she lived in rented houses. S. You said this combination doesn´t work for women. P. Not working, she´s living in rented house all her life. In reality you will see that exalted planets don’t give results as they wrote there.\n")
    if ("Ju 5H") in planets_houses and asc == 'Vi':
        print("Ju 5H, asc Vi: S. My friend has Ju fallen 5H, very smart guy. P. Very very good for wisdom, but then no children, Ju eats one thing.\n")
    if ("Ju 7H") in planets_houses and asc == 'Cap':
        print("Ju 7H, Cap asc: And when you have 7H exalted Ju it's very crazy, you should not trust them, Can Ju 7H is the worst of any place.\n")
    if ("Sa 1H") in planets_houses and asc == 'Ar':
        print("Sa 1H, Ar asc: Very good people.\n")
    if ("Sa 1H") in planets_houses and asc == 'Li':
        print("Sa 1H, Li asc: Full or pride, I´m this, I am that, you are nothing. And you don´t see much success, exalted Sa. How the books explain you cannot see. I \n")
    if ("Sa 4H") in planets_houses:
        print("Sa 4H: Sometime giving good results, can make big heart for people, think big way not only for self. If woman has, she will have very short breast, no milk, because vata, if man has this sometime fear will come very deeply, and they go many houses, many places. They always think where to go and real house comes after age of 40, 42, when they can settle in the life, till then lots of thought for placement. \n")
    if ("Mo 8H") in planets_houses and asc == 'Li':
        print("Mo 8H, Li asc: It’s 10L. 10H is house of akash/sky. So sky is underground. Akash means name and fame. So name and fame go down. But it’s exalted. They can get name and fame after death. With death it will open, then luck, name and fame can come. Or if they have spa with hot water, if they can make cold water, hot water coming from underground, thermal water, they can make lots of money. Country that has this Mo exalted in 8H can have lots of spring water. They can make lots of spas in the country.\n")
    if ("Su 12H") in planets_houses and asc == 'Can':
        print("Su 12H, asc Can: If you have 12H Su every day Jala Neti, the water should cross the nose.\n")
    if ("Ra 3H") in planets_houses and asc == 'Can':
        print("Ra 3H, asc Can: Ra especially Vi sign very very brave and get money many ways. \n")
    if ("Ra 8H") in planets_houses:
        print("Ra 8H: Sudden problems: like suddenly losing money\n")
    if ("Ke 5H") in planets_houses:
        print("Ke 5H: not good for work, during Ke period people can lose their job, Ke 8 from 10 is very very bad.\n")




#function to uncheck boxes when 'reset' happens.
def delretrocheckbox():
    mvar.set(0)
    mvar1.set(0)
    mvar2.set(0)
    mvar3.set(0)
    mvar4.set(0)


#12L neecha they don’t have good sexual relationship with woman, they always lose some energy there.
def lordchecker():
    global asc
    x = lord_in_houses_dict.items()
    print("Info based on Lords in houses:")
    if (1,1) in x:
        print("1L 1H: Can be interested in wrestling and sports. Can defeat death many times, will overcome any problems. Family member becomes an enemy to him because sitting 12th from 2H. Enemies are afraid from him, (die in front of him). If benefic 1L big forhead. If they practice hatha yoga they can go very deeply in this field, but not for Lib and Ar asc, because then they are 8L too. \n")
    if (1,2) in x:
        print("1L 2H: They like to eat a lot of food and they are very choosy about their food, they cannot eat anything. If Mo and Ve they like to drink more, if Sa they like fast more, Ju they like sweet food, Su they like hot food very much, if Ra there they like fermented, preserved food, wine, if Ke 2H they like (salt?) dried foods, Ma they like hot and dried foods, and nuts (hot energy). Also if 1L (with) malefic or 1L with Ra 2H they can see hidden things, voyeurism, or they can work for secret agency.\n")
    if (1,3) in x and asc == 'Le':
        print("1L 3H, Le asc: Leo asc and 1L 3H they die in the clinic, institution, because Su is false there. \n")
    if (1,3) in x:
        print("1L 3H: can be very strong with their own rules and can think their own rules are best and other’s rules are nothing, so they give preference to their own rules. If malefic detached from family and vice versa if benefic. If benefic they go to pilgrimages, religious traveling different places. If malefic there is operation with ear and throat and can die old age of hearing powers. If benefic they die peacefully (they don’t hear the walk of death) and vice versa if malefic they die very bad way. Because 3H is 8 from 8. \n")
    if (1,4) in x and (asc in('Can','Li','Ta')):
        print("1L 4H, asc Can/Li/Ta: These people want to live in nature near water, very sensitive people. Otherwise, make this if you want to live a peaceful life\n")
    if (1,4) in x and (asc in('Ar','Le','Sc','Cap','Aq')):
        print("1L 4H, malefic: if malefic there they can think an animal is their mother, or they can have a step mother.\n")
    if (1,4) in x and (asc in('Ge','Vi')):
        print("1L 4H, asc Ge/Vi: House will be very close to where children study, school or college. Otherwise, make this if you want to live a peaceful life\n")
    if (1,4) in x and asc == 'Le':
        print("1L 4H, asc Le: They will have government office near their house. Otherwise, make this if you want to live a peaceful life\n")
    if (1,4) in x and (asc in('Ar','Sc')):
        print("1L 4H, asc Sc/Ar: If Ma 1L a bakery or restaurant near their house. Otherwise, make this if you want to live a peaceful life. \n")
    if (1,4) in x and (asc in ('Pi','Sa')):
        print("1L 4H, asc Pi/Sa: If Ju, their house will be very close to education or religious center or temple. Otherwise, make this if you want to live a peaceful life\n")
    if (1,5) in x:
        print("1L 5H: They can have lots of children, also write about some problem for 1st child, or 1st child can go away from them. Parvati had 1L 5H. Her and Shiva’s 1st son Kartike went away, and Ganesha stayed. Very good scholar can achieve very high education. If 1L malefic 5H they can learn education not according to their caste, different than their family tradition. Not good for father relationship, strange, maybe as 8 to 10H. \n")
    if (1,6) in x and asc == 'Li':
        print("1L 6H, asc Li: Makes the person slow, sophisticated, nice. \n")
    if (1,6) in x:
        print("1L 6H: These people talk very loudly and they want to show they have more knowledge than they really posses. They don’t like charity too much, they want to be practical, they want to expend money for themselves and for friends and such, for fun. \n")
    if (1,7) in x:
        print("1L 7H: They have knees like peacock (sharp) they can be very good dance, music and art, they like to have a lot of fun in life, if knees not like that they can be very good business, increase the money. If malefic there they can have prostate or testicle problem. If sitting there with Ra (Ke), they think how they can have more women, but they suffer a lot from back and lower back problems, and they can have operation young age reproductive area. They should eat lots of bale. Reason why my grandfather planted a tree of bale here, he had this combination. \n")
    if (1,8) in x and asc  == 'Ar':
        print("1L 6H, asc Ar: Makes the person very active.\n")
    if (1,8) in x:
        print("1L 8H: They can do a lot of magic things, Prateek found they like it, have knowledge to do it, but are afraid to use it. Their tongue can cause them big trouble in their life, because they are angry people, sometime they are not formal people, if they leave their country they will be very happy, own country they can have habit for drugs and this kind of things. They should marry woman 15 years younger and if woman they should marry older man. This is house of family of wife. \n")
    if (1,9) in x:
        print("1L 9H: Good luck and can study about other languages also. If female, luck rises by female and if male planet luck by male. If Ma luck by brother, Mo luck by mother, Me by aunt, and so on.. Age for raising the luck, Ma 28, Sa 36, Me 32, Su 22, this is the age for rising the luck. Ra and Ke 42 and 46. False planet in house of luck gives false luck, outside appearance very lucky but inside nothing there. Exception, Sa fallen 9H very good luck otherwise they make trouble. S: Sa will not be 1L then. P. Suppose Leo asc and Su exalted there with false Sa, Sa will not give bad effects then. What planet you have 9H this color you should put forehead and this color should wear more. Leo asc they should wear more red colors. They have to live far more luck will rise. \n")
    if (1,10) in x and (asc in ('Sc','Ar')):
        print("1L 10H, asc Ar or Sc: very courageous people especially when Ma 1L 10H, very, very, good, not good for mother, but can be very good for themselves. Father can marry several times. Long life also. \n")
    if (1,10) in x and asc == 'Ar' and  ("Ra 10H") in planets_houses:
        print("1L 10H, asc Ar, Ra 10H: They can be very good politicians and diplomats. Ma with Ra 10H never gives negative effect.\n")
    if (1,10) in x and (asc in ('Pi','Sa')):
        print("1L 10H, asc Pi or Sa: Kills the father. \n")
    if (1,10) in x:
        print("1L 10H: Good karma and sukarma, they like to work if benefic, they like politics, they like name and fame, live different countries, very courageous people. \n")
    if (1,11) in x:
        print("1L 11H: Very good profit, many children, like to eat a lot of food, big personality, if Me or Ve they can have beautiful face but lots of physics problems like skin problems. S: Strange because 11H is profit from body. P. If Ve 1L also 8L. If they have skin problems they should worship Ganesha and use lots of henna. \n")
    if (1,12) in x:
        print("1L 12H: They go many, many places for traveling, they see many things, and they expend a lot of money without any reason. Woman can give them trouble and sometime they don’t get married. They kill their own bedroom life. S: Parashara says they would be careful about expending money. P. Because benefic, malefic also here. Benefic would expend goods ways. Malefic they mean Ma and Sa and Ra. \n")
    if (2,1) in x:
        print("2L 1H: Very good for developing personality and always learn something new, try to do the best, very good connectivity with uncle. They like family of wife also, and if benefic planet the family of wife benefits.  \n")
    if (2,2) in x:
        print("2L 2H: Rich people, valuable people, lots of value in society, childhood very strong, get everything from childhood, get good woman and can make good family. If malefic 2H problem teeth and eye, if Ju there they can have very good voice for talking. If Ma there they give orders. If Su 2H OH responsible people, can take pain of family own shoulders. Ra, Ke 2H they live far away from family or remain thin, can have back problems. \n")
    if (2,3) in x:
        print("2L 3H: The brothers and sisters become stronger, they speak other languages too, they like festivals a lot, enjoy festivals with family. Festival in the sense of entertainment. Can make money by hand work. \n")
    if (2,4) in x:
        print("2L 4H: Very good connectivity PL with mother and sometime mother can give a lot of property to children. He is the person who can connect with mother. They can have good name and fame. By talking they can make a lot of money. If 2L exalted 4H they can make a lot of money by agriculture and property. 2L with malefic 4H many animals but the animals die a lot. \n")
    if (2,5) in x:
        print("2L 5H: Intelligent person, good memory, sometime children go far from family, or children can divide property many parts. People can have knowledge about future life, can be good astrologers. \n")
    if (2,6) in x:
        print("2L 6H: False truth. They will want to say truth but it will be false, mistaken. They gossip a lot. Eye operation and sometime some mark on face somewhere. 6H is 5th from 2H so they want to be truthful but 6H it turns false. They follow the law by the letter and it doesn’t work. They can know lots of medicine but it confuses them. \n")
    if (2,7) in x:
        print("2L 7H: Very difficult relationship with wife, always doubt character of wife. They can make very good business, or sometime family business they can take. They make lots of oral sex. \n")
    if (2,8) in x:
        print("2L 8H: Bridges between own family and family of wife, if malefic destroys relationship and benefic otherwise. It can be good sometime for money but not good for family. Anal sex. They can have Vastu Dosha in the house. Makes problem for the family also. The energy of the family goes underground.\n")
    if (2,9) in x:
        print("2L 9H: Lots of holy trees in the house. Like to make their family like beautiful garden, but sometime they can lose a very beautiful member of family and feel very sad afterward. Very nice people good look good money they want to live perfect way. They can chant lots of mantras. If benefic Ve or Me they can sing music. 2H voice and 3H throat, benefic they can chant music very well. \n")
    if (2,10) in x:
        print("2L 10H: Very good people especially they provide for following generation, they want to leave good world for following generation, they can be good environmental researchers. 2L 10H father cares about children. They become very good in politics.\n")
    if (2,11) in x:
        print("2L 11H: Very good for money, for business, but they have stomach problems, gastric trouble, very clever mind, they do a lot for the family, good swimmer and good athlete. S: Why clever mind? P. 2H is house of computer, mathematics, so logic mind aspecting 5H. \n")
    if (2,12) in x:
        print("2L 12H: Expending money to other people, but getting a lot of money too. Can invest in different countries. Can give good job to different country people, but in bedroom they go silent, they expend their energies on other things and finally don’t have energy. \n")
    if (3,1) in x:
        print("3L 1H: Good character, good children and good brothers and sisters and healthy people. They listen to spiritual mantras and prayers and chant also good mantras. S: 3H also dushtana? P. Ya, because people will tell them if they have physical problems go to temple chant mantra.. \n")
    if (3,2) in x:
        print("3L 2H: Listen only family not other people but then blame their family for the problems. Their nature is to blame other people for their problems. They can follow the family tradition job-wise. Mother can marry twice or have two relationships.\n")
    if (3,3) in x and (asc in ('Pi','Le')):
        print("3L 3H, asc Pi or Le: Ve 3H own house attract too much in the music things\n")
    if (3,3) in x and (asc in ('Aq','Vi')):
        print("3L 3H: asc Aq or Vi: Ma 3H own house they can be very good in making things by hand, like land, or can keep weapons too in house.\n")
    if (3,3) in x and (asc in ('Cap','Li')):
        print("3L 3H, asc Cap or Li: Ju 3H own house lots of blessing,\n")
    if (3,3) in x and asc == 'Sa':
        print("3L 3H, asc Sa: Not good. Can do woodwork.")
    if (3,3) in x and (asc in ('Sc','Sa')):
        print("3L 3H, asc Sc or Sa: Can be very industrious. \n")
    if (3,3) in x and (asc in ('Ar','Can')):
        print("3L 3H, asc Ar or Can: Me 3H very good talker and writer, technical things. \n")
    if (3,3) in x:
        print("3L 3H: Brave people, if fallen or malefic aspect they can be very aggressive people and can murder but in 10 minutes they can relax. Many malefic planets 3H and 3L 3H mother can have lots of abortions and miscarriage. Young age throat and ear problems. Traveling a lot. Voice becomes very heavy. If many malefics 3H they want to put pressure on other people, to become stronger. 3H 3rd chakra. They like clean environments. \n")
    if (3,4) in x:
        print("3L 4H: Strong connectivity with own country, with mother, with mother land, they make happiness by themselves. Good mother and good pleasure by brothers and sisters and friends. 3L 3H and 3L 4H they like clean environments. \n")
    if (3,5) in x:
        print("3L 5H: Brothers and sisters behave like children toward this person. S: Children? P. Children behave like brothers and sisters, opposite comes. They have stomach problem. 1st pregnancy can be very quick sometime premature. 3H gives very quick results. S: Bhavat bhavam 3L 5H is very good for courage and hard work? P. Yes. Bhavat bhavam, 1L 1H, 2L 3H, 3L 5H, 4L 7H, 5L 9H, 6L 11H, is very good. S: 12L 11H P. This is not good…. \n")
    if (3,6) in x:
        print("3L 6H: Brother and sister can die very young age and they can become very big enemies to them. Hand and shoulder can break and problem with hearing (operation) young age. They should be careful of snake biting. S: Bad karma? P. Not necessarily, after the bite they can become very lucky.\n")
    if (3,7) in x:
        print("3L 7H: Make their own business, own work and wife comes from long distance. 3H is short time travel (go and come back quickly) but not necessarily short distance travel. Also they can like many women, are attracted to braveness and open mindedness of people. If woman 3L 7H she has very high expectations of partner and difficult to get married because 3H is house of desire, she wants man to be beautiful, courageous etc.\n")
    if (3,8) in x:
        print("3L 8H: Problem at death, hard death, sometime either alone or painful etc. They shouldn’t live old age in their children’s house, the children tell them bad things, asking when they will die. They cannot express their feelings in front of children. 3L 8H not so good pleasure and they can have not so long life sometime, if twins both will never survive. S: What kind of karma do twins have? P. Many karma together, long time partnership.\n")
    if (3,9) in x:
        print("3L 9H: Good luck hard work, positive way want to make karma, but people give them hard time cause barriers in their lives, but they cross the barriers. They often try (and should) put gold or silver on the hands. If Ve 3L sitting 9H it is very very good, gives also knowledge of different countries. If Ve, Me or Ju, 3L 9H they can learn Sanjivaniya, how to bring people back to life, especially with Ve. They can work in emergency rooms.\n")
    if (3,10) in x:
        print("3L 10H: Very karmic people, hard work to improve life, they don’t believe in lottery, believe in reality, stomach problem and children sometime become enemy to them.  Sometime they get help from wife, wife can become bit like male. Stomach problem with 6H from 5H. They can become very successful from hand work. If benefic creative and if malefic work with machines. \n")
    if (3,11) in x:
        print("3L 11H: can make lots of money working with the hand, can have lots of brothers and sisters. Lakshmi lives with them. Lucky people and very prosperous. \n")
    if (3,12) in x:
        print("3L 12H: Eye problems, sometime after 2 children woman makes operation not to have baby. 12H of bedroom, they want to have pleasure but not to have babies. \n")
    if (4,1) in x:
        print("4L 1H: They have special knowledge for taking poison out. Can cure people of snake bites. S: Why? P. 4H of animals. 10H from 4H can advise people if they have mind pollution, work with mind and body very good way, good healers, long life also for mother, but they can be own mother. They can be very good in yoga practice and go higher education. \n")
    if (4,2) in x:
        print("4L 2H: Good profit for money, good property, they get family property, family money mother side also, but sometime can have problem with prostate or urinary. They should not eat meat, body problems come.\n")
    if (4,3) in x:
        print("4L 3H: Lots of traveling, sometime they choose the work where they have to move here and there. Distribute letters (postman), messengers. Sometime they can die in disasters like in floods or fall in well, or water animals can give them trouble. Can be very good architects and house makers. Good mechanics too.\n")
    if (4,4) in x and (asc in ('Sc','Li')):
        print("4L 4H, asc Li or Sc: They can make good money different countries.\n")
    if (4,4) in x and (asc in ('Aq','Can','Ge','Pi')):
        print("4L 4H, asc Aq/Can/Ge/Pi: Very good to make money their own country. \n")
    if (4,4) in x and asc == 'Ar':
        print("4L 4H, asc Ar: S.Mo good to make money own country? P. Sometime not because 4H is not good placement. \n")
    if (4,4) in x and (asc in ('Vi','Sa')):
        print("4L 4H, asc Vi or Sa: They can make good money different countries. 4H is not good placement. S: Why is Ju not good here? P. Ju – Brahmins, big ego by ego they don’t understand other people, same with 5H, they think they know everything. Best remedy is to surrender. People have good heart and like celebrations a lot. S: Friend has Ju in Sag and doesn’t like to celebrate. P. Ju destroys quality of 4H. \n")
    if (4,4) in x:
        print("4L 4H: Good heart, helping people, social worker. Can make money by own effort. If they leave their own country they get more success. \n")
    if (4,5) in x:
        print("4L 5H: Very good for winning elections, can become very good ministers, if good combination with minister they can make money by politics, they can be very advisors. Also mother has good karmic connection with her grandchildren (his children). \n")
    if (4,6) in x:
        print("4L 6H: Thieves, sometime can destroy quality, but they can be very good as heart surgeons, can be big lawyer. By this work can make lots of property and money. But heart problems. Mother can have problem with digestive system. \n")
    if (4,7) in x:
        print("4L 7H: Good pleasure with woman. One time not divorced but can marry twice. They like very beautiful bedrooms, showers, they want beautiful house, if benefic there they can invest a lot of money in luxury houses. \n")
    if (4,8) in x:
        print("4L 8H: Mother suffers a lot and sometime mother father can be separated, mother can come from lower caste, simple family. Ragiv Gandhi, Sonia Gandhi was waitress from Italy. If Ve 4L 8H they can do stage show for dancing different countries, Su should also be 8H, they don’t feel shy, they just tell things. \n")
    if (4,9) in x:
        print("4L 9H: They can live very near to temple, can travel many religious countries, can meet many religious masters, lots of teachers can connect with you. They can give donation to religious people. If Ju then very good teacher. If Sa they make gardens. \n")
    if (4,10) in x:
        print("4L 10H: Big land, or even if they have their own land they like to make very good apartment, they like to eat very good food, and like to use perfume, good smell they like and like touching a lot. 4H is water and 10H is air, water goes down air goes stronger, air is touching. Good job, good work. If 4L is retrograde they can go far away from place of birth, malefic in particular, they like animals a lot. \n")
    if (4,11) in x:
        print("4L 11H: Lots of charity, many many learnings, good writing, problem for stomach, very good property, sometime living or traveling other country. Can have pleasure with mother and father. \n")
    if (4,12) in x:
        print("4L 12H: Restless person, senses not in control. Sometime they can make baby from different people like donation from sperm, or women can rent other women to have baby also. Sometime animals can be difficult for these people, they can fall from horses and break the legs, nowadays accidents with vehicles. \n")
    if (5,1) in x:
        print("5L 1H: Very good connectivity with people and with themselves also. They know about themselves what they need or not. Self knowledge. They live long lives. Self confident, but by some reason they don’t show self confidence young age but then they regain bit. S: Why? P. Some reason may come, perhaps they go far away from family, some reason comes. \n")
    if (5,2) in x:
        print("5L 2H: Very good for society, but they have power in the tongue, and their forehead is always hot, very good studies, very good business, very good management power and very good for money, they go far from family if 5L is malefic and make their new family far from old family. Sometime teeth problem because they speak a lot. \n")
    if (5,3) in x:
        print("5L 3H: Very good creative people, but they can have big problem to believe on other people, so selfish people, but very good for education, logical people, good physics and mathematics and they love their father a lot, good karma with father, because 8 from 10H sitting 6H from father. \n")
    if (5,4) in x:
        print("5L 4H: Very good connectivity with mother lots of prosperity, they like to make their house in nature, they expend money on buying books, reading is very good hobby for them. They don’t like traveling too much, enjoy staying in house all the time. They have specific time table they don’t like it broken. They bring happiness to children and children bring happiness to them.\n")
    if (5,5) in x:
        print("5L 5H: Very clever mind, deep thinking but sometime they are whimsical (they go by themselves, they don’t like to listen), very good digestive system but lots of gas, especially if malefic. If benefic own sign sometime one son one daughter, malefic many children it gives. \n")
    if (5,5) in x and asc == 'Le':
        print("5L 5H, asc Le: Spiritual teacher. \n")
    if (5,6) in x:
        print("5L 6H: Education about medical science, law, inspector and therapist for criminals, if malefic they can become themselves thieves. Young age they don’t have education but later age they want to learn many things. S: Why? P. They give effect later, suppose Ma is there, till 28 age no education, trouble. \n")
    if (5,7) in x:
        print("5L 7H: Wife very clever and person thinks all the time for the wife. They think about women, women can work for them, woman make their life (they go by advice of woman). Mind very good business and think a lot about sex, but they can be very good how to connect with body, make body stronger. S: Because of aspect to 1H? P. Yes. \n")
    if (5,8) in x:
        print("5L 8H: Very clever mind, very good learner quick mind, very good researcher, but sometime heavy things can fall on their head and can have a operation, a rock can fall on their head while in the water, son can die, and if malefic there they can kill their own son too. \n")
    if (5,9) in x:
        print("5L 9H: Religious minded, good luck and can learn many religious languages and brother and sister love them a lot. Can have very good connection with yoga and meditation and they can see grand children (long life). \n")
    if (5,10) in x:
        print("5L 10H: Very good name and fame, education, children also go very high level, good karma. They like eating good food, beautiful wife, wife can be rich, lots of property. \n")
    if (5,11) in x:
        print("5L 11H: Very very good connectivity with money and mind, and these people can have lots of writing and very good in communication also. If benefic big belly if malefic thin belly, benefic like to eat and vice versa.\n")
    if (5,12) in x:
        print("5L 12H: Expending money, bad habits, buy a lot. No children, but very spiritual people, connect easily with other country people, lots of knowledge about other countries and can go enlightened path. \n")
    if (6,1) in x:
        print("6L 1H: His own enemy, very intelligent people, they want to control all the diseases immediately, afraid to go to hospital, usually they are healthy but young age will be difficult. Sometime suffer a lot from hidden enemies. They want to do good things but it can turn bad sometime. Sometime bodily they can become very heavy and they like to do tattoos, earrings, strange hobbies. S: Why they become heavy? P. Self killer, tattoo too, punishment to themselves. S: Earrings not good? P. Men also do it, they shouldn’t. \n")
    if (6,2) in x:
        print("6L 2H: Sometime they get adopted or born different family or go different family, or mother father get married twice and sth is in the family. S: I have this combination, Vi asc, but it doesn’t apply to me. P. Where is your brother? S: Europe. P. Ya, family will not stay together, will go here and there. S: Sa is both 5L and 6L. P. Bit less, 5H also, but still family has some effects. Big depression comes sometimes on old family member. They have bitter tongue, if they don’t control they can become enemies with everybody, especially if it sits with Ra 2H, makes sometime trouble. Can have strange family history. Can immigrate from different country. Money-wise sometime they can become bankrupt (with Ra?). \n")
    if (6,3) in x:
        print("6L 3H: Sometime brother becomes enemy or he becomes enemy to the brother, many traveling higher study other country. Can be engine (speed) driver. \n")
    if (6,4) in x:
        print("6L 4H: Can cheat a lot, lie a lot, a horoscope example was discussed concerning bankruptcy. Big trouble can die in water. Can give heart problem, physical heart can also have trouble.  \n")
    if (6,5) in x:
        print("6L 5H: 6L 5H they can make abortion, miscarriage, child can be adopted. 6L 2H they can go other family, 6L 5H they can adopt another child. S: 6L 5H not good for mind? P. 6L 5H good for medical science, about law, with computers and mathematics it will not work out, chemistry and biology it will work. \n")
    if (6,6) in x:
        print("6L 6H: Brave person, kills enemies they are not stronger than him. He is a fighter for few people come, like guerilla fighter. Sometime they can become very high level officers in army, can be very good doctors in the army. S: 6L is not good indicator, shouldn’t be strong, say Ju sitting 6H for Lib asc? P. 6L 6H, which house it sits it will destroy the quality of this house. S: But say Ju sitting Pi 6H? P. He can be good lawyer, good, doctor, good judge. S: You said once 6L sitting 6H, person is own enemy. P. Even the 1H. S: 6L 6H own enemy? P. They take risk, don’t care about themselves. \n")
    if (6,7) in x:
        print("6L 7H: Wife can have problem gynecological area or may have syphilis, can lose sperm. If they want to kill somebody they don’t think too much who it is, they just do it, or sometime don’t control anger in their mind. They like massage touching a lot, because they can have skin problems and itching comes. \n")
    if (6,8) in x:
        print("6L 8H: Can be very big thieves or mafia king, or lots of drinking drugs and around them such people can come many times. They have to expend money also. Can have lots of research in their work, sometime pain in the leg a lot, eye sight problem also later age. S: Why? P. 4H young 7H middle age, 8H late age. \n")
    if (6,9) in x:
        print("6L 9H: Sure they go other religion, sometime change religion, attracted to other cultures, or not attached with religion. Can say, I don’t want to be this person but I respect what is good from other religions. Lots of traveling, gives good knowledge about body because 6H is house of disease, therapy knowledge. As they get older and older they get more and more money. Even if young age they don’t make good money with time they will go better for money. They can make money from traveling and different countries. They like nature too. They like very much women but don’t express their feelings, wait for women to express first. Can make money from guru also. \n")
    if (6,10) in x:
        print("6L 10H: Strong name and fame, sometime negative way, like Bin Laden. Sometime bad karma but they never realize they are doing bad karma, sometime they can make poisonous vegetables. \n")
    if (6,10) in x and asc == 'Vi' and ((8,10) in exchangel):
        print("6L 10H, asc Vi, 8-10 exchange: P. Two or three children? S: 2 daughters. P. Ya, only daughters. Fighting with brother future over property. \n")
    if (6,11) in x:
        print("6L 11H: Lots of money good career, beautiful wife, good critics writer, can compare things very good way. Always problem in the stomach. S: Why pretty wife? P. 12L from 7H is weak sitting 6 from 7H (6H?), that which takes from beauty. My beauty will increase if my 12L sits in the 6H. Beautiful wife not only body but also nature. \n")
    if (6,12) in x:
        print("6L 12H: They can die by sth that falls on them, most of the time they will have accident, good people travel a lot, can work in ambulance, go home to home for diseases, nurses who work other countries have this combination. They have many moles on back and hips. S: why? P. 6L eyes can see this only in the bedroom. **** They like gold a lot, because 11 from 8 income from (mine?) sitting 12H looking 7H of beauty. S: Why sth falls on them, vipareeta? P. This is house of traveling in the sky, problem not only in the earth, can change energy in earth but cannot change anything in the skies. \n")
    if (7,1) in x:
        print("7L 1H: More than two wives, healthy children, healthy wife, long relationship. Can be very good in management, intelligent people, know how to do business and satisfy other people. They like touching people, even when they talk they like touching people. Beautiful people and long life.\n")
    if (7,2) in x:
        print("7L 2H: lots of speaking, partner talks a lot, gives lots of trouble by talking, oral sex and sometime unnatural sex backward (8-6 relationship). They can be very good in collecting money, however partner family, not their own family uses this money. They can get diabetes. S: Why? Too much sex gives diabetes. 7H marrkesh in 2H marrkesh, gives effect especially kidney and pancreas. \n")
    if (7,3) in x:
        print("7L 3H: Can abuse little girls and can have relationship with younger sister, or they hide a lot, but they travel a lot always relationship with different kind of women, any cast, can have problem with ear and throat. S: Why? P. 7L marakesh gives problem to any place. S: You gave more positive indications for 7L 11H? P. Any planet sitting 11H increases something, maybe can give trouble to 5H. S: Still problem even though 7L sits 9th from 7H? P. Ya. If Mo sign is 9 to 5 relationship between partners, not good for marriage between partners, guru child relationship. Similarly here 9-5 relationship not good here.\n")
    if (7,4) in x:
        print("7L 4H: Good connectivity with family, love their family, can go traveling, find other country man, other city man. Very good heart but sometime behavior may not be easy, they want to be like mother or father, ask too many questions. They can have hotel, property with partner can work very nicely. Best job for them architect, vastu, real estate work, their hotels, they hate teaching, not good for them, can be impatient, but learning is good for them. Gives good connectivity with people. S: Why they don’t have patience? P. Too much pressure on heart they don’t have patience. They will have mole on face or breast, because 4H is heart chakra. They like to clean very much, they cut their pubic hair, everything they want to clean, 4H of home, they want to keep everything perfect. 7H house of activity, of action, 4H house of home, they do a lot of action in the home. They like very much animals dogs. Sometime they want to have sex with animals or sleep cuddle with animals, even pillow. They enjoy the sex. The partner will be famous with good name and fame. 4H 10th from 7H.\n")
    if (7,5) in x:
        print("7L 5H: not good connectivity with partner, divorce, they want to become child all the time but partner should be partner, stomach problems, bad habits can make life crazy. Should be careful of smoking, drugs and alcohol, but it will be good for partner who will get more property. Always some issues in life to solve. If they can do mind work very very good for them. If malefic sometime they want to kill themselves. 7L 5H 90% marriage is not successful. (Wife has ego because trikona stronger than Kendra. Opposite when 5L 7H. *** not recorded, check with Prateek).\n")
    if (7,6) in x:
        print("7L 6H: Disease for person, (disease for partner?) and sometime can steal jewelry of partner and sell out. Thinking about how to give trouble to other people and get out of trouble. Loose lots of money through divorce. Partner gets money through them. Can have big trouble especially sex in water. S: Sex in water is not good? P. Water kidneys are working both outside and inside not good. If they want to live long life they should plant lots of trees, best remedy for them. S: Why? P. 7H and 6H connectivity, PL they cut lots of trees, this lifetime they have to pay so planting trees, so they can have peaceful family life. Sometime they can have one leg shorter than the other.\n")
    if (7,7) in x:
        print("7L 7H: Beautiful wife, good name, good fame, good business, but too much sex problem for having less life. \n")
    if (7,8) in x:
        print("7L 8H: Death of partner, not good for relationship with in laws, mother in law may not like person. Not good for people who want to live in family of partner. Sometime partner can die very quickly. \n")
    if (7,9) in x:
        print("7L 9H: Good connectivity after marriage, a lot of energy for doing big project in life, energy for long travels with partner or sometime they can get partner while traveling. Partner may be spiritual and have many brothers or friends. If malefic there with 7L especially Ra, Ke not good to marry Muslim, all the luck finito. S: My 7L is 9H, should I be looking for girl with many siblings? P. Yes, or many friends.\n")
    if (7,10) in x:
        print("7L 10H: Partner can work with husband. Sometime very PL connectivity with partner’s father. Gives lots of traveling especially for work. Lots of ups and downs especially for partner with relationship with her father. She thinks she is her own father. Good karma and business, and lots of business and hotel management. Big projects. Good for them to make hotel management or property business (looking 4H also). \n")
    if (7,11) in x:
        print("7L 11H: Good for money after marriage, good business, life very much sweet and good children, can have many children, no children they can be good in writing also, their writing can be their children (5th from 7H). Very pretty partner, long life partner. 5 from 7H connectivity Trikona with Kendra. \n")
    if (7,12) in x:
        print("7L 12H: Good for getting marriage other country, expend money and business success in foreign countries. Like animals a lot, because 12H is 9 from 4H S: And 7H is 4 from 4H? P. Ya.. 7L 12H, sexual relationship with different country or different caste women. \n")
    if (8,1) in x:
        print("8L 1H: Not strong outside, inside yes (6 from 8H=physical problems?) Skin problems, lies a lot, gossip and lies about good people that do good job/good things, good intuition, sometimes sees future in dreams, earthquake, negative things, good to work with people that will die soon, they can work good way with them, lose hair, nail problems, skin-->effects are outside, unlike 6H which has deeper effects. Diseases are inside. But 8L gives outer effect. Death starts from outside. Disease starts to come from inside, uses life positively/ give out?\n")
    if (8,2) in x:
        print("8L 2H: Tongue and eyes disease. Get things in a bad state and make them better: like becoming president of India when it’s a chaos. They get damaged wife, children, etc and make them better. You can have good ability, you can make it very good, because it’s 7H from the sky, so it’s not going down, it’s going up. They can take the negative things and make them better, like institutions, companies, whatever. S. Also repairing computers for example? P. Yes. Also buying a land that people are fighting over, you can make good money. Don’t get good energy from family. They will see deaths in family. Many people can die in front of them, maybe friends. So they have a different attitude of lifeS. They can get money of the family of wife? P. Hmm, they can destroy money of family of wife. They can lose the money of the family of wife., eyes operation, financial problems, Don’t like too much discipline. I don’t give astrology education to them, because they don’t follow the family rules or these things. Don’t give secrets to them, they will blah blah to everybody. When they are old they will have had eye operation in the past. Cataracts, eyes operation.\n")
    if (8,3) in x and asc == 'Sa':
        print("8L 3H, Sa asc: Moon 3H in Aquarius, they travel a lot\n")
    if (8,3) in x and asc == 'Ar':
        print("8L 3H, Ar asc: Mars sure kills brother in Ge sign, because it’s enemy sign there. S. This person kills the brother? P. Yes, you are right also, sometimes in PL this person killed his brother. \n")
    if (8,3) in x and (asc == 'Can' or asc == 'Ge'):
        print("8L 3H, Saturn: Good technician\n")
    if (8,3) in x:
        print("8L 3H: Lots of traveling. Long life. If they are doctor, they can do lots of operations, save people by their therapy. Good therapists, good healing power. Normally books say lots of negative things, but my family found the good things from 8H. Younger brother can die before them. S. Brother or sister? P. Mostly brother. Or they don’t have brothers, mother already abortion. Good in physics and computers. Good knowledge of hardware. Servants will not respect them, thinking he doesn’t treat them well, he’s hard, he doesn’t give good money to us. Because this people tell bad things to the servants. If he’s the boss of an office they won’t like him... People remember them after death. \n")
    if (8,4) in x and asc == 'Can':
        print("8L 4H, Can asc: Gets property that doesn’t belong to him some aunt or somebody dies, and he gets the property. Like a kind of gift. So these people get by blessings, they will not win elections but get a position, no property but they get it. Things come from the sky. Sometimes they are flying in plane and get promoted in business class\n")
    if ((8,4) in x) and ((1,4) in x):
        print("8L 1H and 1L 4H: Very silent people, they don’t talk too much, talks simply but deep knowledge about everything. S. Why? P. 1L in 4H, 4H is higher education. And 8L is in 9H from his house, which is 5 from 5, also knowledge. High and deep knowledge. S. Positive and negative planets? P. Positive and negative knowledge. if malefic planet can use knowledge negatively, like how to make trick to get money from people, from the pocket. And positive, how can I serve people.\n")
    if (8,4) in x:
        print("8L 4H: Can make money with vastu. Good knowledge about directions. Good in army, or captain of ship. Sometimes lives in a house in land that used to be graveyard. They go totally crazy mind. Effects of souls, affects them emotion wise. Careful where they make house. Or lives near graveyard, burning ghat or their house is last house of the street. Mother can be good therapist or very good mother if 8L is retro (-)+(-)=(+). Mother can be very good and long life. Never will win at elections. Most time they are nominated but they lose. But they have friendship with very high people, can get assignments or good positions from other people, like friends or boss. Can learn old therapies.\n")
    if ((8,4) in x) and ((6,4) in x):
        print("8L 4H and 6L 4H: S. Pleasure from dancing. P. Yes, or mother can be a good dancer, or their family can have a good dancer, or they can have pleasure to look dancing, or if they go to dance club they get good energy, or good energy when going see hospitals where people die, they can get happiness there. S. Helping people? P. Helping, or distributing food, they get good energy. S. Why dancing? P: 8L and 6L are legs, and 4H is happiness.\n")
    if (8,5) in x:
        print("8L 5H: Long life. Thinks always about death. Can learn to anaesthesiate people. They can learn to hipnotize, bring out memories from other people. S. But it’s their own mind, not other people’s mind. P. Yes, but it’s knowledge of how to do it. S. To bring to the surface or to delete? P. PL regressions, this kind of things. Can learn to keep old things, like library, old books they can collect. Learn how to do learn old therapies, like jyotish, they can attract this. First baby can have physical problem. First child can have problem with souls, spirits or black magic. Can easily hide things. Good to keep secretsStomach can digest secret things. Can know past lives (own). Lots of energy especially if they are on empty stomach. After eating, feeling sleepy. Empty stomach they can’t work hard no problem. S. Also for 8L in 1H? P. Yes. S. Because I feel this. P. Yes, sometimes, very good work but after food they want to sleep. Also like that.\n")
    if (8,6) in x:
        print("8L 6H: After being born mother can lose her brother or problems start in her side of family. Always wins over enemies. Have properties, problems with enemies, goes to court and wins. Can become very ill in young age, but with age goes high it can be fixed. Careful about skiing or kind of things where the legs use, like football, skiing, where they use their legs a lot. Can be attacked by bullet or knife if Ge asc and Ra+Sa in 6H. Can be killed by enemies. Can die near hospital or court. S. If Sa by itself then no problem? P. Also little problem.S. How to judge 8L in 6H? Because it’s vipareeta. P. You should be careful, see if malefic or benefic. If planet is benefic, good doctor, lawyer, judge. He can kill people by the pen, you will be hanged. Power in the hand. Can be a good doctor but can do mistake and patient can die. Or can be a judge and not judge well, you get this problem. If with Ra, mostly with Ra. Mistakes come by Ra.If malefic, someone can kill him near this place, hospital. Then he can be victim. S. By court or disease. P. Yes\n")
    if (8,7) in x and asc == 'Li' and ("Ma 7H") in planets_houses:
        print("8L 7H, asc Li, Ma 7H: They can be good to clean the gold mines, they can get the gold from underground. They can clean the gold with the mud, with the sand. They also have power to get good things from nature or people, and the rest they can leave. Kind of sadhu. If you tell blah blah blah they don’t listen. If you tell the good things, they can receive. Very good people. Not only just for gold, also in daily life. They take the good things. S. But not good for relationship. P. No.\n")
    if (8,7) in x and asc == 'Ge' and ("Ra 7H") in planets_houses:
        print("8L 7H, asc Li, Ra 7H: if Ra with Sa in this house, they can have herpes or this kind of energy they can give to other people, so careful when you have sex with them\n")
    if (8,7) in x:
        print("8L 7H: Sometimes they can have two wives. Or 1st wife can die or get divorced, then he gets another wife. S. When you said two wives you meant at the same time? P. Affair with different woman. S. For women is same? P. Yes. Can have good business related to after death, selling coffin or graveyard. They can make lots o money. If exchange 7L and 8L, very good business for this. Ge asc or Can asc, for sure it can happen because Sa is god of death. Problem in genital area. If they have mole in testicles or woman area, many men or many women they can have. They can have sex with different woman, she gets pregnant and they don’t know. Man especially, not women. [is it related to the mole condition?] S. What? P. If 8L in 7H, this man can have sex with different women, sometimes and she can get pregnant, and this man goes other country, they can have baby but he doesn’t know. Can work in fermentation business, like alcohol, very good money. Oil, gas, good money. Things that come from underground. If exchange also sure very good. S. But I guess not vegetables that come from underground? P. Mines, coal business. S. So not like potatoes. P. Potatoes if you have Mercury, nature. Mercury is more green and nature, so it can work out for potatoes, carrots, this kind of things. If Jupiter there, mustard oil, oil business. Or deep knowledge business, selling knowledge in different countries. Venus selling sperm of animals, they can make or work in sperm bank. But root is same. If both partners have 8L in 7H, (-)+(-)=(+). They can have vey good relationship between them. Works kind of kuja dosha, not kuja doja, if 8L in 7H.\n")
    if (8,8) in x and (asc == 'Sc' or asc == 'Aq'):
        print("8l 8H, asc Sc or Aq: Long life. Can be big thieves, if Me, electronics. If good planet aspects, the tendency goes down. They can be good thieves for the talking. They steal by words, claim intellectual property, like take good pictures from internet, say they took them\n")
    if (8,8) in x and (asc == 'Pi' or asc == 'Li'):
        print("8L 8H, asc Pi or Li: One time Indra, the lord of the angels, in heaven, he had a beautiful garden. He started to burn. The leaves going finished. He said what happened? Because this is the heaven, even one planet goes bad he never dies. What happened? He ask to Jupiter, and he said oh it happened everywhere. Because Jupiter made the muhurta for this. Jupiter made the muhurta for this garden. Muhurta, the good time for starting something. He called Shukra, Venus. Venus said actually, you made this mistake, that the nadi was not good. Nadi was agni nadi when you started this. In a day we have 24 minutes is one muhurta. Total is 60 muhurta, from sunrise to sunrise. In the different muhurtas different nadis come. So this knowledge comes by Venus, the muhurta knowledge. So when you have 8L in 8H, and it is Venus, so this people can make very good muhurta. They can be very good astrologers. So for Libra or Piscis ascendant.\n")
    if (8,8) in x and (asc == 'Ge' or asc == 'Can'):
        print("8L 8H, asc Ge or Can: One time Indra, the lord of the angels, in heaven, he had a beautiful garden. He started to burn. The leaves going finished. He said what happened? Because this is the heaven, even one planet goes bad he never dies. What happened? He ask to Jupiter, and he said oh it happened everywhere. Because Jupiter made the muhurta for this. Jupiter made the muhurta for this garden. Muhurta, the good time for starting something. He called Shukra, Venus. Venus said actually, you made this mistake, that the nadi was not good. Nadi was agni nadi when you started this. In a day we have 24 minutes is one muhurta. Total is 60 muhurta, from sunrise to sunrise. In the different muhurtas different nadis come. So this knowledge comes by Venus, the muhurta knowledge. So when you have 8L in 8H, and it is Venus, so this people can make very good muhurta. They can be very good astrologers. S. And if you would have 8L in 8H but is Sa, for Ge asc? P. Then they can tell you when you are going to die. The ruler will be the same, but the way of talking will change. Venus tells positive things. Sa tells the negative things, and it is going to be true. Sa asp 2H, negative things come from the voice. \nLong life\n")
    if (8,8) in x and (asc == 'Ar' or asc == 'Vi') and ("Sa 2H") in planets_houses:
        print("8L 8H, asc Ar or Vi, Sa 2H: Mars 8L. They can have big operation for anus and hips area. They can have mark there. They can make tattoo in the lower back area that touches the hips area.\n")
    if (8,8) in x and ("Ve 2H") in planets_houses:
        print("8L 8H, Ve 2H: Ve asp from 2H. Good photographer or nude painter. Especially if 3L is Ve (Le asc)\n")
    if (8,8) in x and asc == 'Can':
        print("8L 8H, Can asc: Only Sa and Can asc they don’t give 8H results, they give normal results. People don’t die. Illness but don’t die. \n")
    if (8,8) in x and (asc == 'Le' or asc == 'Ta'):
        print("8L 8H, Ju: Can be big thieves. If Ju is lord, steals books. If good planet aspects, the tendecy goes down. They can be good thieves for the talking. They steal by words, claim intellectual property, like take good pictures from internet, say they took them\n")
    if (8,8) in x and (asc == 'Pi' or asc == 'Li'):
        print("8L 8H, Ve: Can be big thieves. If Ve is lord, steals jewellery. If good planet aspects, the tendecy goes down. They can be good thieves for the talking. They steal by words, claim intellectual property, like take good pictures from internet, say they took them\n")
    if (8,8) in x and (asc == 'Sa' or asc == 'Cap'):
        print("8L 8H, Sa or Cap asc: If Sun or Moon 8L in 8H? P. Both of them different, they don’t give negative results. They don’t effect by the 8H.\n")
    if (8,8) in x and (asc in('Ge','Can','Ta','Le')) and ("Ju 8H") in planets_houses and ("Sa 8H") in planets_houses:
        print("8L 8H, Ju 8H, Sa 8H: S. Ju and Sa together? P. Long life but ill body. Many times ill. Because they are big planets. So sometimes hormones can go very difficult. Because they are big planets they give the minute chemicals from the body. They give efffect in the minute effect of the body. So hormones go crazy. So they shold worship  Ju and Sa every day.Or vishu worship or yellow sapphire.\n")
    if (8,8) in x:
        print("8L 8H: Long life, mainly Sa, Me, Ve. Ju gives physical problems from time to time. Nude dancer, they can show their hips easily. \n")
    if (8,9) in x and (asc == 'Ar' or asc == 'Vi') and ("Ra 3H") in planets_houses and ("Sa 3H") in planets_houses:
        print("8L 9H, 8L is Ma, Sa and Ra 3H: Can lose hand in accident\n")
    if (8,9) in x:
        print("8L 9H: Family of wife is very good, get support or money from them. Good wife. Good in negative tantra, they can drink alcohol, left tantra. They can worship Kali, Tara, this kind of goddess. They can make black magic easily. Shamanic healer. They go hungry a lot. S. Especially for Ta asc? P. Yes. S. Because Ju fallen. P. They eat a lot of food. Skilled to meditate and call souls of dead people.Sometimes spirits roam around them. S. If someone dies what is the best thing that you can do for them? P. Best to go to Ganga and give prayers for them, give remedies, ceremony. Ganga is only the god in this Earth who can give the blessings. S. Does it matter if immediately after? P. Some time after, maybe 5 days after. S. What do you give to Ganga? P. Maybe take the Ganga water and give this soul. Take it from your hand. Or make a ceremony, make piradan, a kind of special seeds come like this and they make a pinda of spirit of this person and offer. Sometimes make the gold from this person, make a statue, make prana [not clear] in it and offer to Ganga. Spirit can go, this is the best. Meditate, live in graveyard easily, no fear. S. Good to live away from place of birth? P. Yes\n")
    if (8,10) in x:
        print("8L 10H: Good astrologer. Father dies early or not good relationship with father. Good intuition. They tell whay they feel, not shy. This is not good, I don’t like that. Good karma form PL, so this life they have good abilities to get good partner this life and they can have good life, good pleasure. Fear of death and slowly overcome it. S. They have good karma P. Yes, very good karma. PL. S. This lifetime? P. This lifetime also they can do good karma, because this is 11 from 10. Good children\n")
    if (8,11) in x:
        print("8L 11H: Stomach problems. Intelligent people, they can learn lots of things. Problems with mother. Mother can feel like they are enemy. Karma with mom PL. Beautiful people. S. Why? 8H is death, he is sitting 4 from his house. S. So happiness from... P. So they can give happiness to other people, they can tell good things to other people. Good mind to learn about old things or things from other country. S. Why other country? P. 5H is own country knowledge. 8L in 11H aspects 5H is other country knowledge. For example is they belong to Jewish country they will not learn Judaism, they will learn Hinduism. They can make lots of friends but few are good. Profit from dead, like getting inheritance. Marry with foreigners or older people is good. Family in law loves them\n")
    if (8,12) in x:
        print("8L 12H: Sometimes unnatural death. Not so long life. Sometimes they die in other country. S. Esp for Sa asc.\n")
    if (9,1) in x:
        print("9L 1H: Beautiful, good character, intelligent, people think he’s god person, gets abilities to learn about religion, good children, spends money in religious matters or traveling, more prosperous after marriage, peace in the face, always happy \n")
    if (9,2) in x and asc == 'Ar':
        print("9L 1H and asc Sc: If Mo 9L in 1H (false Mo): Lot of depression, past life didn’t give water to anybody, liver or kidney problem this life. Upaya: Give water to people on Mondays\n")
    if (9,2) in x and asc == 'Ar':
        print("9L 2H and Ar asc: They talk something but they mean something else (they don’t know how to communicate well). Ju and Ve say different things.\n")
    if (9,2) in x and asc == 'Sa':
        print("9L 2H and Sa asc: No property from family, but get high level property by themselves\n")
    if (9,2) in x and asc == 'Li' and ("Ke 2H") in planets_houses:
        print("9L 2H and Li asc and Ke 2H: Me and Ke 2h: they don’t speak a lot\n")
    if (9,2) in x:
        print("9L 2H: More happy from wife and children, especially son, strong sexual desire (Ve energy), rich, spiritual talker, good reading spiritual books (get knowledge from them), more famous than family, if brahmins they progress a lot/high level. \n")
    if (9,3) in x and asc == 'Cap':
        print("9L 3H and Cap asc: Lots of troubles from teachers (Me in the 3H), mainly spiritual teachers\n")
    if (9,3) in x and asc == 'Le':
        print("9L 3H and Le asc: Have friends with abilities to change the country, like reporters, writers, revolutionaries. In a better way (Ma in the 3H).\n")
    if (9,3) in x:
        print("9L 3H: Helping siblings, lots of spiritual traveling, likes to go to places with spiritual energy, good friends that support them, can leave job for spiritual purposes, past life death came from traveling. In in this life they go back to this place their luck goes 7 or 8 times more, but normally they don’t want to go there.\n")
    if (9,4) in x and asc == 'Ta':
        print("9L 4H and Ta asc: If they change the door of the house, bad luck comes. If their door is old, then good luck. Sa is old hings. They should use old bricks when making house, then blessings comes.\n")
    if (9,4) in x and ("Ra 4H") in planets_houses:
        print("9L 4H and Ra 4H: Nature things like earthquakes, or people, can destroy house. Donate to religious place or build temple, then house is ok.\n")
    if (9,4) in x:
        print("9L 4H: Past life karma with mom: sister, friend (depending on 3H and 11H), lots of property, they get property by luck, likes cars and material things a lot, parents get separated, ups and downs in health of parents, in the beginning luck is bad, then it goes better. Bath in sea, lake, Ganga is good for them. 4H is water.\n")
    if (9,5) in x:
        print("9L 5H: Good writer of spiritual books, scholar, likes guru, people like him, past karma with children: if benefic good connection with them and vice versa. If benefic: future life is good. If malefic, mixed results (but what you do in this life can change it), good children, can reach very high level, special people, good intuition, can know what will happen in future, most times people are good people, but consider if 9L is benefic or malefic, good for father\n")
    if (9,5) in x and (asc == 'Can' or asc == 'Ar'):
        print("9L 5H and Ju 5H: Maybe next life soul in different planet\n")
    if (9,5) in x and asc == 'Can' and ("Ra 5H") in planets_houses and ("Ma 5H") in planets_houses :
        print("9L 5H with Ma and Ra 5H: Spirituality is good, just problems with children, maybe abortions. Still Ra can lie.\n")
    if (9,6) in x and (asc == 'Li' or asc == 'Cap'):
        print("9L 6H Me: Lots of logic but misuse it (Me not good in 6H in general)\n")
    if (9,6) in x and (asc == 'Vi' or asc == 'Aq'):
        print("9L 6H Ve: Ve not good, can get ill from water disease\n")
    if (9,6) in x and asc == 'Cap' and ("Ra 6H") in planets_houses:
        print("9L 6H Cap asc Ra 6H: Me-Ra in gemini: power to catch silent things, like ghosts, shamanic healer\n")
    if (9,6) in x and (asc == 'Can' or asc == 'Ar'):
        print("9L 6H Ju: Ju good \n")
    if (9,6) in x and (asc == 'Pi' or asc == 'Le'):
        print("9L 6H Pi or Le asc: Open pharmacy, esp Ma 6H Le or Cap sign (not asc): Big winner. They want to prove they’re the best. Red face\n")
    if (9,6) in x and asc == 'Ta':
        print("9L 6 Ta asc: If Sa exalted 6H very good: if they can go in jail once very good luck. Or if in hospital once, then after very good health. Advice: eat food in jail cantine or do service in hospital in Sa period.\n")
    if (9,6) in x:
        print("9L 6H: If child born in same town where mom was born, very lucky child. I in dad’s not so lucky, good relation with uncle of mom side, good doctor, lawyer, catching thieves: very high, igf malefic, maybe thief that nobody can catch, can heal in a spiritual way, good for traveling abroad, but can lose wallet or something abroad\n")
    if (9,7) in x and asc == 'Sa':
        print("9L 7H Sa asc: Esp if Su is 9L: good wife but doesn’t care about her, wants to divorce. PL she gave positive things to them, this life they want to do it (Su asp 1H, more negativity, Su not good in 7H) \n")
    if (9,7) in x and asc == 'Can':
        print("9L 7H Can asc: Ju in Cap, pL negative karma between husband and wife. If Sa is good, good relationship between them and vice versa \n")
    if (9,7) in x and asc == 'Sc':
        print("9L 7H Sc asc: Mo 7H very good. Wife was mom in PL. This life wife also treats like mother or mom like wife. Problems between wife and mom. For women horoscope, mom could be sister \n")
    if (9,7) in x and asc == 'Sa':
        print("9L 7H Sa asc: For women Su, father has karma, was husband PL or wanted to be with her. \n")
    if (9,7) in x and (asc == 'Ar' or asc == 'Can'):
        print("9L 7H Ar or Can asc: Ju: spiritual. Depends on Sa.\n")
    if (9,7) in x and asc == 'Ta':
        print("9L 7H Ta asc: Sa 7H esp Ta asc wife is honest\n")
    if (9,7) in x:
        print("9L 7H: Good luck after marriage, lots of positive karma, past life lots of business, people are positive, they want to make holy symbol in body, like om tattoo. But it’s not good, you shold do holy symbol in karma, do good karma, wife has good heart and is beautiful. Profit from her\n")
    if (9,8) in x:
        print("9L 8H: PL bad death, if they remember their death, they can becoe very spiritual and dettached from life (esp in Ge), if travel go to old countries or cities, or live in old house, luck goes up, doesn’t want family/children if benefic planet and vice versa, not bad people, good people. They do their best in life. Sometimes weak, doesn’t take risk in life, PL fearsThey should meditate in greaveyard for more luck or in cremation places\n")
    if (9,9) in x and (asc == 'Aq' or asc == 'Vi'):
        print("9L 9H Aq or Vi asc: If Ve exalted or own sign, Ve dasha not very strong\n")
    if (9,9) in x and asc == 'Ar':
        print("9L 9H Ar asc: Beautiful, long life, good person\n")
    if (9,9) in x and asc == 'Ta':
        print("9L 9H Ta asc: good luck, after 36 ys very strong luck\n")
    if (9,9) in x:
        print("9L 9H: Very good luck, If any false planet, not necessarily 9L, the dasha very good: luck is wife of hard work, then they work hard with their exalted aspext in kali yuga. False planets they give good results because they want to prove they are the best, positive energy, happy, want to make others happy, PL: priest, rabbi, spiritual, good brothers and friends, beautiful\n")
    if (9,9) in x and (("Sa 9H") in planets_houses) and (("Ra 9H") in planets_houses) and (asc == 'Le' or asc == 'Pi'):
        print("9L 9H Le or Pi asc: Ma 9L, Sa/Ra in 9H, problems with mom and dad\n")
    if (9,10) in x and asc == 'Sa':
        print("9L 10H Sa asc: 9 in 10 especially very positive this asc, rich people. In Ge not so great because it’s dual sign and the 10H needs action, plus Ve and Ge are femenine. In the case of Sag asc, it’s ok because Vi is dual but 9L is Su, which is strong in the 10H\n")
    if (9,10) in x and asc == 'Ta':
        print("9L 10H Ta asc: good luck, after 36 ys very strong luck\n")
    if (9,10) in x and asc == 'Ar':
        print("9L 10H Ar asc: Beautiful, long life, good person\n")
    if (9,10) in x and asc == 'Ta':
        print("9L 10H Ta asc: good luck, after 36 ys very strong luck\n")
    if (9,10) in x and asc == 'Aq':
        print("9L 10H Aq asc: S: For aq asc? P: ok.\n")
    if (9,10) in x and (asc == 'Ta' or asc == 'Sc'):
        print("9L 10H Ta or Sc asc: Rich people\n")
    if (9,10) in x and asc == 'Ge':
        print("9L 10H Ge asc: Not so great because it’s dual sign and the 10H needs action, plus Ve and Ge are feminine. \n")
    if (9,10) in x:
        print("9L 10H: High position, king, name and fame, good abilities, good energy, PL worked with king\n")
    if (9,11) in x:
        print("9L 11H: Very good, always do work that can give them profit, special machine in mind to get profit, practical people, even make money from enemies, False or exalted same: profitable, can win lottery, no problems in money in life, good active children, connection with father. Father rich, real estate brings good money, not learn much in university but know a lot about everything, sometimes selfish people, 11 (wife of children)-3-7 lakshmi houses\n")
    if (9,12) in x and (asc == 'Vi' or asc == 'Aq'):
        print("9L 12H Vi or Aq asc: Ve 9L in 12H good luck in other country. If Ve 12H with natural malefic, spends money in bad ways like drugs. Sa or Ke. And vice versa, in good fun ways.\n")
    if (9,12) in x:
        print("9L 12H: Good luck in other country, do good karma, can leave things and go in enlightened path, If natural malefic kills problems that come in other countries and vice versa. Benefics will have to face some problems. PL: lots of debts, responsibilities from other people (like special guru). In this life, if stays in place of birth, feels pressure, luck goes down\n")
#Likes to honour guestsm eso if Ve 12H. If Ve with Ke, up. If Ve with Ma or Ju they leave everything and go for enlightened path in Ke period
    if (10,1) in x and asc == 'Ar':
        print("10L 1H asc Ar: S. Sa 1H in Ar? P. Very good. Aishwarya Rai, miss universe, had many planets fallen, ascendant also. Sachin Tendular, best cricket player, had 3 planets fallen.\n")
    if (10,1) in x and asc == 'Pi':
        print("10L 1H, asc Pi: S. Kendradipathi dosha? P. If Ju 1L then fine, \n")
    if (10,1) in x and (asc == 'Ge' or asc == 'Sa'):
        print("10L 1H, asc Ge or Sa: 7L and 10L in 1H then sometime problems can come, two fathers, sometime father can separate from mother, mother can go with different man, or physical problems for father. \n")
    if (10,1) in x:
        print("10L 1H: Can have two fathers, can be their own father, these people can be very good in physical work, revolutionary changes in life. Can bring lots of happiness to wife, business, lots of positive energy for relationship. People can have very strong connectivity with joy and happiness, enjoy their job and work, go high level work wise, very clever people. \n")
    if (10,1) in x and (asc == 'Can' or asc == 'Aq'):
        print("10L 1H, asc Can or Aq: If Ma 10L 1H sometime can give problem physical level, accident, but other positive effects remain. They should not drive fast, and they should be careful about the horses. \n")
    if (10,2) in x and asc == 'Li':
        print("10L 2H, asc Li: S: Mo fallen 2H? P. Mother side ancestor can come back in family, can have eyes like mother side, only problem can lose tradition of family, mainly money wise, can spend or lose what he got from family. S: Weakens 2H or 10H? P. Weakens the 10H, change the job, and sometime family stops their progress, mother can be too attached, doesn’t allow children to go here and there, and they can lose their energy.\n")
    if (10,2) in x:
        print("10L 2H: Very special people, can be traditional people, can follow all tradition of family, like to be with family, good karmic connection with father, sometime ancestor like great grandfather can come back in family and go very positively. Can have same eyes like father. \n")
    if (10,3) in x:
        print("10L 3H: Brave people, sometime PL father can be brother, or this lifetime father can be like good friend, but father can have disease. S: If benefic. P. Benefic. S: If malefic? P. No problem. They travel a lot and can go for short travels to other countries. Can work with hand a lot. If malefic like Sa can be thieves, tendency to steal. Can have many friends, many countries, like to do facebook. S: Because karma with friends? P. Yes. They can be very good drivers, like to do long driving. S: 3H short travels. P. Timing short, from city to city, still (overall?) distance will be the same.\n")
    if (10,4) in x:
        print("10L 4H: Kendradipathi dosha, father and mother can have problems physical problems, mainly for dual lagna. They work for happiness, if they feel bit problem, they always cry why they don’t have happiness, little things can make them happy, little things can make them unhappy. Very good for buying and selling property. If malefic, mainly Ma, can be very angry, because always connect karma with emotions, they work more with emotion, can create tension. Can have good energy for social work, can be high in social status, can have strong and positive karmic connection with mother, best combination for living very good house, 9L 4H they get property by luck, 10L 4H they work hard then get property. Sometime can have working and living place together, can live very near minister, or higher people living very near. Can have connectivity with nature, can work in nature and with animals. They work more with happiness.\n")
    if (10,5) in x and (asc == 'Cap' or asc == 'Le'):
        print("10L 5H, asc Cap or Le: Ve 10L they should have very good children. S: Especially Cap asc? P. Yes. Good children and good education and can work higher level. For Cap asc Ve is 10L and 5L, so it doesn’t go markesh.\n")
    if (10,5) in x and asc == 'Pi':
        print("10L 5H, asc Pi: Pi asc Ju 5H they may not have babies, PL they did something wrong with Brahmins, Brahmins cursed them, or they were very bad with priest PL. 10L sitting 8 from 10 and exalted. Ju 5H akaraka. \n")
    if (10,5) in x:
        print("10L 5H: Government job, good name, good fame, very honest if benefic. Their children go very high level. Can get education about the state, geography, and state government, and study history and politics also. Father always intelligent, but what father worked they will work different job. 10L 5H is good for 1H, 5H, 9H, 11H but not good for 10H. \n")
    if (10,6) in x and asc == 'Aq':
        print("10L 6H asc Aq: S: Ma fallen 6H? P. Very good condition, can succeed a lot in police and military, can also be good in technology, but not good for father, aspects 9H, gives not luxurious life for father.\n")

    if (10,6) in x:
        print("10L 6H: Very good lawyers, advocates, doctors, fight and get the luck, and father can be very popular. But sometime father and child may fight with each other. S: Good for work? P. For father work, not for child, but if working as lawyer, doctor, can support them. \n")
    if (10,7) in x and asc == 'Vi':
        print("10L 7H, asc Vi: Tells lots of jokes and funny stories. Bad partners. \n")
    if (10,7) in x and asc == 'Vi' and ("Ra 7H") in planets_houses:
        print("10L 7H, asc Vi, Ra 7H: If fallen planet there, with Ra, sometime wife can have relationship with father also. Or father can be abusive to women living in the home. \n")
    if (10,7) in x:
        print("10L 7H: Very good combination, wife can be more educated. People can be very good in business, management, can have very good energy working with higher people. Partner can be bit more open minded, and person can be bit more closed minded, then thought differences can come. 10L makes person stronger, but aspecting 1H doesn’t give good results when malefic. S: When benefic? P. Not big trouble. Malefic give big trouble. Malefic 7H can give good business, but aspecting 1H, can give health problems and personality will be blocked. Father and wife can do same business, very successful.\n")
    if (10,8) in x:
        print("10L 8H: Can have problem with work, can change work a lot, they can make a lot of money with business related to death or anesthesia. If malefic can murder very well, or by mistake can make accident, tongue can be very sharp, people can feel like they are dying. \n")
    if (10,9) in x and asc == 'Cap':
        print("10L 9H, asc Cap: If Ve is there 9H, Cap asc, sometime people can lose a lot of money woman area. They can fall in love with woman, and woman can check out on them. S: Strange, because 10 in 9 still strong Raj yoga. P. They get the pleasure from the woman, but lose money, they can buy presents for prostitutes, or say buy flat for their partner.\n")
    if (10,9) in x:
        print("10L 9H: Very good raj yoga, but they expend credit what they get from PL positively, this lifetime they expend all, 12 from 10, reason they have good luck. S: Not so good. P. Laughing, this is the condition. S: Same for 9-10 exchange? P. Of course, same thing. S: Deepak Chopra has this exchange. P. Good name, good fame, but afterward all in the ground… They like religious work, yoga practice, meditation, they can have very good intuition, father can have long life, good karma, can think clearly, but not good for mother. S: Why father thinks clearly, 12 from 10 P. 9H of luck, religion. 9H is also house of father. Sure they get good achievement of life, during the 10L period they live very good way\n")
    if (10,10) in x and ("Ra 10H") in planets_houses and (asc in('Can','Aq')):
        print("10L 10H, asc Can or Aq, Ra 10H: Very good politician, practical people, if someone is useful for them, they use them and afterward kick them away. \n")
    if (10,12) in x and asc == 'Le':
        print("10L 12H asc Le: S. Le asc? P. Very good for work, traveling sign, and traveling house, Ve becomes more like traveler, can surely work other country, very far.\n")

    if (10,12) in x:
        print("10L 12H: can work other country, travel other country, can have lots of energy for work, but when they want to rest they can’t, they have to work all their life, can’t retire, they are so connected with work they cannot take retirement, sometime death comes when they work, not in the hospital. They work, work, work, Usually 12H is not considered good house, people say they will not work, but opposite comes. Very good people, can invest money for pleasures, want to make everybody happy, try to be very positive, can travel a lot, can expend money on themselves and learn a lot from different things, can learn totally different things, because 8 from 5H so totally different education, death for 1st education. S: Expend themselves through work? P. It is like that, work all their life, sometime they can work other country, and come back. \n")
    if (10,10) in x and (("Sa 10H") in planets_houses) and (("Ma 10H") in planets_houses) and (asc in('Ar','Ta','Aq','Can')):
        print("10L 10H, Ma and Sa 10H: Very practical people, selfish, they don’t consider others.\n")
    if (10,10) in x:
        print("10L 10H: Brave person, good person, enjoys the life, see the clear world. If malefic can be very hard people, they cannot be easy, they work hard and get achievement, but heart chakra can be blocked. If benefic there, especially Ve, Mo or Su, this brings very positive energy, can do something for society, Ju there also very good social work. S: Kendradipathi? P. If also 1L it will not work, if also 7L and 4L it will work, but sometime father, mother can have physical problems. Good for Pi and Vi asc, but not good for Ge asc.\n")
    if (10,11) in x and (asc in('Can','Aq')):
        print("10L 11H, asc Can or Aq: Not good for stomach, especially if Ma 10L.")
    if (10,11) in x and (asc in('Can','Aq')) and ("Ra 11H") in planets_houses:
        print("10L 11H, asc Can or Aq, Ra 11H: Sometimes eater of baby, gives trouble to baby.")
    if (10,11) in x:
        print("10L 11H: Can make lots of money, very positive people, they have good heart, but sometime mother can have problems woman area, and father can have physical problems, eyes especially. They can make money from money (interest). Can do very positive things. Their work and their children’s work can be the same, because children business and father the same. They can think a lot. They like to make lots of money, but they care about family a lot, especially about children. Not good for stomach\n")
    if (11,1) in x and asc == 'Vi':
        print("11L 1H, asc Vi: Mo 1H, beautiful wife, like a lot their family, but like a lot also their in law family. Mo can give money from different kind of people, not only one kind of people.\n")
    if (11,1) in x and asc == 'Li':
        print("11L 1H, asc Li: Suppose Su is there, can have very strong self confidence. S: Even though fallen? P. Can be bully.\n")
    if (11,1) in x and (asc == 'Ar' or asc == 'Pi'):
        print("11L 1H, asc Ar or Pi: S. Sa 1H? P. Can have hotels, lots of karma, very good business. Connect a lot to in law family.\n")
    if (11,1) in x:
        print("11L 1H. Make a lot of profit from home, very hard working people, they can have very good partnership, can treat partner very well, can have very good partnership. Can be oldest sibling in family. Self made, work by self.\n")
    if (11,2) in x and (asc == 'Ta' or asc == 'Aq'):
        print("11L 2H, asc Ta or Aq: Very very good. Ju 2H can make a lot of money by talking and astrology. \n")
    if (11,2) in x and (asc == 'Ta' or asc == 'Aq') and ("Sa 2H") in planets_houses:
        print("11L 2H, asc Ta or Aq, Sa 2H: Ju and Sa there can make a lot of money by astrology, very good for intuition, and communication.  \n")
    if (11,2) in x and (asc == 'Ar' or asc == 'Pi'):
        print("11L 2H, asc Ar or Pi: Sa 2H very very good\n")
    if (11,2) in x and (asc == 'Ar' or asc == 'Pi') and ("Ju 2H") in planets_houses:
        print("11L 2H, asc Ar or Pi, Ju 2H: Ju and Sa there can make a lot of money by astrology, very good for intuition, and communication. \n")
    if (11,2) in x and ("Ra 2H") in planets_houses:
        print("11L 2H, Ra 2H: Not good for people who have connectivity with family, maybe grandfather or great grandfather can have injury in hospital, or army. \n")
    if (11,2) in x and (("Ra 2H") in planets_houses) and (("Ma 2H") in planets_houses):
        print("11L 2H, Ra and Ma 2H: Also Ma and Ra, old members can have accident. S: Good for money? P. Very good. S: Are they good for family, or family good for them? P. Family good for them.\n")
    if (11,2) in x and asc == 'Vi':
        print("11L 2H, asc Vi: Mo 2H gets lots of money by woman, women can be very favorable for them. \n")
    if (11,2) in x:
        print("11L 2H: Good for income.\n")
    if (11,3) in x and (asc == 'Ta' or asc == 'Aq'):
        print("11L 3H, asc Ta or Aq: If Ju there, can have good spiritual way, can make money by spiritual way also. \n")
    if (11,3) in x:
        print("11L 3H: These people, especially if Sa, can make a lot of money by traveling, younger siblings can help them, they like animals a lot, sometime can make money by driving, can work with export, import make good money. S: Why do they like animals? Animals is 8 and 12 from 4H, animals can scare them, they like to go near animals they want to open the fear, other planets not good, always afraid from animals, but Sa make the animal (quality?).\n")
    if (11,4) in x:
        print("11L 4H: Very very good for them 2nd hand car. 1st hand car can be problematic for them. Or if they buy land that has problems, for example if two people fight for land, they can bargain for it and get good price. They can have two mothers. Very clever, know how to make money with the people, they can work hard and make the money. But they search for happiness, enjoyment everywhere.\n")
    if (11,5) in x:
        print("11L 5H: Very very good, can use ability full way, what they studied very good education, can improve education different places, can be very very good in it. Can have good child useful for family. Very very good karma for people, can feel family member is their child, or PL family member was their child. But for money wise they can compromise everywhere, can be very tricky and clever for money wise. S: Why is 11L period not good, but many indications of 11L are good? P. Health wise not good.\n")
    if (11,6) in x:
        print("11L 6H: Very very good in medical sciences, can make lots of money by medical profession. Can heal people very good way, different kind of healings. Very good energy for becoming lawyer. S: Pretty partner? P. In a way you are right, 6 is 11H, sitting in 8 killing in the, of the 7H. S: I recall you said 6L 11H pretty partner? P. Also like that. Can have court case and lose lots of money there, or problem with insurance company, can lose lots of money. Remedy ceremony for 11L.\n")
    if (11,7) in x and ("Ra 7H") in planets_houses :
        print("11L 7H, Ra 7H: 1st child child can go little crazy, if Ra sits with 11L. S: Why 1st child? P. 3rd from 5H, also kind of markesh. \n")
    if (11,7) in x:
        print("11L 7H: wife can make more money than person, both can make money, can have good way of income. Very clever, can be very good in management, post office, or insurance company. Wife can have physical problems, especially gynecological problems.\n")
    if (11,8) in x:
        print("11L 8H: Archeologists. Very good money, gas, oil, or good income from dead people, or good fertilizer (S: Dead things? P. Ya, separate from body), they can count people, how many died or not, very good analysts, researchers, can have problem for getting wedding. S: Why problem for wedding? P. Not good for family of wife. S: But 11L is 4 from 8H. P. Yes, but 6 from 6, disease coming there.\n")
    if (11,9) in x:
        print("11L 9H: Very very good for money, 11 from 11 really really good, 4 times more luck than normal people. They can travel all around the world, make money all over the world, people like them, can be spiritual, and spirituality can also give money to them.\n")
    if (11,10) in x:
        print("11L 10H: Very happy people, most of time they invest money and make money, invest money and make money. They love their father a lot, and sometime can get income from the father. Very clever, can make lots of building, lots of energy, can have lots of property too. But sometime they can lose hair easily, and sometime they can have sky problem, like tension from flying. S: Karma for loosing hair? P. PL they laughed a lot at people who were not beautiful. They should not laugh at other people, this lifetime.\n")
    if (11,10) in x and (10,9) in x and (9,8) in x:
        print("11L 10H, 10L 9H, 9L 8H: If mala yoga starts in 11 to 8 is not very good. They can have strong energy and know when they will die. S. Strong energy or not good? P. People know when they will die, they can have intuition, they can do everything before. S. You said it’s not a good combination. P. Because they know their death. Even it’s very good, even it’s not good. Sometimes doctor can tell you have cancer, you are going to die this day.\n")
    if (11,11) in x:
        print("11L 11H: very good for money, for profit, making money not only one way, many ways of income, but they should work not only one place, they should go different places, can make very good money. Sometime their child can have.… their wife can bring lots of money. S: Good for children? P. Very good for children wife, can bring very beautiful wife, and money can come, maybe child will be alone, alone wife, she can have good job, bring good money for family.\n")
    if (11,12) in x:
        print("11L 12H: very very good, especially for people dealing with import and export, can make money from money, can give money to people and make money, (PayPal), can make money through other people, international transfer, commission. S: But this is 11L in dushthana. P. Not good for big brother, sister, and not fixed money, sometime can lose money a lot, if rate goes very down, sometime they can lose all the money.\n")
    if (12,1) in x and asc == 'Aq':
        print("12L 1H and Aq asc: Then positive, expend money for beauty, gym, this kind of things, because then it is pancha mahapurusha.\n" )
    if (12,1) in x:
        print("12L 1H Gives not good body, thin body, lots of coughing, bit crazy mind, not so easy mind, sometime depression, expends money for body maybe beauty, maybe medicine, or maybe making body stronger or in the gym.")
    if (12,2) in x and asc == 'Sa':
        print("12L 2H and Sa asc: Money will be spent very positive way, can buy house and land and make family other country or other place where usually their family members will not go there, or if Ma retrograde they make sure they come back own place where family lives, even they go traveling, they come back for sure. \n")
    if (12,2) in x and asc == 'Pi':
        print("12L 2H and Pi asc: Sa 2H false, can expend a lot of money eye operation, sometime young age, sometime age of 36, teeth, sometime beauty they have to expend a lot of money, sometime for ear. Sure they have good money, but sometime they can expend money for teeth. S: Aspecting 11H. P. Yes, gives good money, they can make very good money like Jewish people made money by lending, but if Ra aspecting also from 8H they lose money also, and sometime they can be murdered for money, when they can’t return the money.\n")
    if (12,2) in x:
        print("12L 2H: Sometime thieves can take paternal money, or their family members cannot stay united, big fighting in family, one go East, one go West, one go North, one go South, family dispersed, sure they will have big family members, if they 4 directions so big family. They like to talk about religion, spirituality, good positive things. Old age they have sometime eye operation. This is our tradition, not Parashari say one two things… They can talk about big big things, Oh I will go here, I will go there, bla, bla, bla, but reality sometime not very much there, reality is very less, still they have positive way of doing things, they don’t want to hurt anybody, they don’t want to kill anybody, they want to be good people, only sometime nature to talk higher way. \n")
    if (12,3) in x and asc == 'Aq':
        print("12L 3H and Aq asc: If Sa false 3H they go far from country, but they want to go but they don’t go, they have a feeling to go other country, but sometime they don’t go because family stops them, but they are lucky people, and they travel other countries a lot. They expend money for right purpose of the life. S: Exalted aspect to 9H. P. And 12H they see own sign. But if 1st pada of Asw so first sign, first Nak, first pada, so first child (sibling) can have big trouble, but if retrograde last child will have problem. All the rules you will not get in the books, very difficult because all the rishis they wrote the things, what people.. they knew the future astrology will be like that, so they didn’t show anything, just little things people say what to do with this knowledge. Selfish people sometime, they expend money only for self if sitting own sign 3H, or you can say self centered people. Not negatively selfish. They think if I’m not hungry I can give money to people. Tendency also, if you find person Western country especially, European, Russian country, they don’t give anything for other people, everything they want to take. \n")
    if (12,3) in x and asc == 'Can':
        print("12L 3H and Can asc: S: Still better house for Me Can asc. P. This is ok, this is ok, positive planet they do like that, they will tell, don’t lie, don’t do this thing, this is dangerous for you, but self they will do it. Don’t smoke, don’t drink alcohol, but at night, kchoo… 12L sitting exalted Me house of their hand, own energy, because exalted Me, benefic planet exalted, so of course they will give good things to other people, this is house of giving to other people, sure Me will force them, they will write very beautiful writings were people are happy, they will write very beautiful character in the movie, himself they never follow this, I have my one friend Dr Sharma, he tells everybody don’t eat this don’t eat that, but himself becomes like potato. \n")
    if (12,3) in x:
        print("12L 3H: Parashari says good talking expend money positive way, good worship, all kind of pleasure people can get it.\n ")
    if (12,4) in x and asc == 'Ar':
        print("12L 4H and Ar asc: Very positive if Ju not retrograde not with Ra, not with Ma very very good. If alone, and with Mo best people can expend money for other people, they make money and expend money. Bill Gates son has Ju and Mo 4H. S: What if Ma there? P. Then he will have fear he will not play with full enjoyment, will play with very less joy, then he will destroy 4H and Ju has power to destroy 4H. S: If Ju retrograde 4H Can sign then difficult, not giving good, difficult situation for people, they have very open heart chakra they cannot use it, they sure think they will sure always think I have to do something, but they will sit in the office and  work there, and they have to make big decision take out and do something service to people. \n")
    if (12,4) in x and asc == 'Le' and ("Ke 4H") in planets_houses:
        print("S: Trump, 12L Mo sitting 4H (with Ke)? P. Will disturb foreign policy of country, do strange rules, makes more limitations, this belongs to us, this belongs to us. S: No immigrants. P. Belongs to us, you should not come. S: 12L weak with Ke good? P. Good business man. Heartless person. He will have fighting with the sea, I’m sure sea South of China, sure some trouble will come from there. He is now Ju/Ju period, started exactly on the date, Ju very indicator, very nice in his horoscope. S: He has nice Me. P. Good business.\n")
    if (12,4) in x and asc == 'Ge':
        print("12L 4H and Ge asc: S: Ve 4H in Vi? P. Very good, but sometime they can take lots of loans from bank for house for car but difficult to give back, they don’t earn enough to give back. False house we say. S: I have this combination, Autumn I bought property, didn’t take loans. P. Can make good money by property. Not your house, not born for yourself. For selling it is good. S: Plan to sell. P. I’m sure it will be very good because Ve indicator for 4H and materialistic way, when it goes false sign, mythological (traditional?) way selling land and house is not good karma, land is like mother, selling your mother, so false planet sure you will do this karma, getting the money. Past it was not good business selling the lands, cows, it belongs to  your mother. We donate - if somebody needs it. Food is not for selling, it is giving for others who are hungry. We make big business for that. Food and land is big business, big money, clothes also, people who feel cold. Sat yuga when they created this things. Now Kali yuga all rules have changed. You can invest money in property, you can make good money. S: What kind of karma does it give? P. Next lifetime you will run after house, you will not have your own house. This land is not yours, born not for nothing, you bring karma with you, so not use tell mine mine mine, god give you this everything.\n")
    if (12,4) in x:
        print("12L 4H: Sometimes internal connection with mother broken, like the cord what is coming, reason I check navel, cord between mother and child. Most of the time navel is outside so child is giver to mother, if inside they can receive from mother. Navel very deep mother gives them a lot they are full of love, they are able to give things to other people. Only follow these rules if 12L 4H, then really check it, how is relationship between mother and child. \n")
    if (12,5) in x and asc == 'Sc':
        print("12L 5H: If planet exalted will expend money for the son, by going to doctor to get the son, or after born on education. \n")
    if (12,5) in x:
        print("12L 5H: If they can have other city other country for education very good for them. S: For children or for person themselves? P. For children.. for person also, for person more, and they can come easily influenced by other people, not own people, suppose I have this combination I will not listen to my family, my wife children, ear will go further, not to family, and they can make money by expending money, can take risk for money, big risk for the life... They expend money on spiritual travelings, because 9 from 9 expending money. If they can make orphanage very successful, where lots of children come and play, or something for children. S: Benefic? P. More positive child, if malefic more negative, if female, more girls will come there, but this work is good for them.\n")
    if (12,6) in x and asc == 'Sc':
        print("12L 5H and asc Sc: Ve sitting 6H Not good. S: For man? P. For man mainly not good.\n")
    if (12,6) in x:
        print("12L 6H: expend lots of money helping other people. Suppose they go by car, see someone fell on Earth, they take them in car and help them. But they are very angry people. Most of the time nice people can reach very high level. Talks about Roberto, this man has good energy to help people and do positive energy. Lots of people can become his enemies, lots of black magic. They will not be enough to disturb him but sure he will have lots of enemies. But very good for football, if malefic, suppose Ma there, if 12L 6H and 2L also sitting 8H, can make money by feet, if 12L and 2L sit 6 and 8, or 6 and 8 exchange can have very good football player. S: No strange death then? P. Can die on field, or strange death, or nobody knows how it happened. \n")
    if (12,7) in x and (asc == 'Sc' or asc == 'Ge'):
        print("12L 7H and asc Sc or Ge: Ve not good there, even Ve is very good 7H, why? It brings very quickly death of person. If man has 7H Ve every day he goes for sex, woman will go younger if they have every day sex, man it will go opposite, they grow older, 8H of death will go near death, expend the life, 7H we say lots of lust, woman no problem, very creative woman can go better. \n")
    if (12,7) in x and (7,2) in x and (2,12) in x: #code better
        print("12L 7H and 7L 2H and 2L 12H: we say she do naked dance on bar can make a lot of money. S: In India? P. Can do bar dancing, in Bombei every street has this. \n")
    if (12,7) in x:
        print("12L 7H: very choosy people, want this want that in woman, big expectations for woman, themselves when they get it very simple, they would like her eyes to be like fox. they expend a lot of money for wife, they buy her cream powder, they really care what woman wants, so woman should choose man who has 12L 7H. S: If malefic? P. This tendency will not go maybe they buy wine for wife everyday, but they will care about her. They want to give everything to wife, like house good things. But if malefic or false planet they can do illegal work, can hide taxes, can be problem. 12L 7H, export and import can make very good money, buying from other country selling own country can be very successful. Woman can be very good not as girlfriend or wife, but suppose want to go to Greece, need wife they will translate for you, but not have sex with you (like escort).\n")
    if (12,8) in x and asc == 'Vi':
        print("12L 8H: and asc Vi: Su exalted 8H, very good, can be famous after death. S: Aspect to 2H? P. 12L aspecting 2H, all family members want something from him, after death property can be distributed many ways. Nice people, not for killing, good will. \nP. Very good. S: But 12L is then very strong. P. No problem, he will have great income, no expenditures.\n ")
    if (12,8) in x and ("Ra 8H") in planets_houses:
        print("12L 8H with Ra: S.Leo asc 12L Mo with Ra 8H? P. 8H Ra with Mo not so good, sometime give trouble, but 12L 8H,  combination very good, nice people, they know their people, very good people most of time, not a fighter, they are good.\n")
    if (12,8) in x:
        print("12L 8H: very positive all positive things will get, good life, long life, and religious person, living good way in life, he is like king energy, can bring a lot of positivity everywhere, lots of friends, can get a lot of money by expending, comes back good way. Can buy a lot of property, lots of good things he can do but after his death his property will go not one hand, will be distributed many places, maybe 3, 4 kids.\n")
    if (12,9) in x and (asc == 'Cap' or asc == 'Ar'):
        print("12L 9H and asc Cap or Ar: Sometime can become big guru. Can have followers other country and they expend money for him, like Prem Baba, all money come from other country, nothing he is very clever guy, his is like Ju works very strongly there, especially Ju, Cap and Ar asc. If 9L influenced by 12L they can do very good money traveling business. They can make money by the throat, they can speak. S: If malefic? P. By the gun, threaten. Both are thieves actually, one gets money positive way, other negative. S: If guru gives wrong advice? P. Next life will have hearing problem. \n")
    if (12,9) in x and asc == 'Sa':
        print("12L 9H and Sa asc: Sometime PL if positive planet they expended money positive way, this lifetime their luck can come with positive planet, if malefic they expend money very negative way PL, especially 9H Ma go there Sag asc very very highly spiritual people, and many lifetime same work like priest, astrologer, come back. \n")
    if (12,9) in x and asc == 'Aq':
        print("12L 9H and Aq asc: Sa 9H most of time PL very highly business people, left their big family, they born are met this family again. If retrograde met same family again, suppose exalted Sa 9H, then they go again this family, can take part of money what they earn and go different country. \n")
    if (12,9) in x and asc == 'Le':
        print("12L 9H and Le asc: If 4th pada of Asw or 1st pada of Kri, very very bad. These people can be no luck and sometime when they swim swim swim at the end drown. Can work hard but last moment they lose the thing. Sometime can become big guru, like Ju, can have followers other country and they expend money for him\n")
    if (12,9) in x:
        print("12L 9H: They will not like teacher or guru, will always fight guru, will have many teachers, will always see some negativity. S: 12L 9H with regard PL? P. They are never born same country were they were born before, connectivity with other country people. S: Retrograde? P. Go back to their PL country, meet their relatives there but they come back, make very good friendship, but they continuously go to this country. Sometime PL if positive planet they expended money positive way, this lifetime their luck can come with positive planet, if malefic they expend money very negative way PL \n")
    if (12,10) in x and asc == 'Le':
        print("12L 10H, Le asc: If Leo asc, Mo there most of time other country people can give them traveling ticket and they can travel easily, or they can be good traveler other country and can make money by the people. If 12L Mo, sits exalted sign 10H, they expend all money traveling wise.\n ")
    if (12,10) in x and asc == 'Vi':
        print("12L 10H and Vi asc: Su 12H government pays them, can get high money from government, in the past they wrote in the tradition they will be employer of King and Queen. They rent out horses to King and Queen, they can be good ministers and commanders and King pay them.\n")
    if (12,10) in x and (8,10) in x:
        print("12L 10 and 8L in 10: Strange thing here if 12L and 8L both 10H they can be very high work CIA, KGB, can be very good officers, because they don’t tell secret to everybody. When they die they keep very big secret in their heart, next life they open them. Two missiles come from different (12H and 8H) and blast nothing there.\n" )
    if (12,10) in x and asc == 'Aq':
        print("12L 10H and Aq asc: By self will not take money from government, will be offered by government, but will not take. Will give own things, and also what money they give you will hide and put in the bank.\n")
    if (12,10) in x and asc == 'Ar':
        print("12L 10H and Ar asc: S: Ju fallen 10H? P. Most of time can make money by teaching. Teaching can come by other country. Sometime they can teach languages other country and government pays them, if Ju Srawan Nak, can be very good teachers, can be ambassadors, diplomats, government pays them other country. S: But will not be good for father? P. Cap Ju 10H absolutely not good for father.  \n")
    if (12,10) in x :
        print("12L 10H: They can have very nice ability.\n")
    if (12,11) in x and asc == 'Sc':
        print("12L 11H and Sc asc: S. Ve 11H in Vi? P. Very good people can get lots of money from wife side, wife can bring lots of money. S: Wife or husband? P. Wife or husband whatever. S: Exalted aspect to 11 from 7. P. Also 7L sitting in 11H, and Ve 12L 11H, 12 from 12 Ve very good there. S: They can make money by expending money? P. Yes. \n")
    if (12,11) in x:
        print("12L 11H: They always have trouble getting the profit, even they get profit they lose again, but if they can go other country they make good profit, own country they can lose the money. Eye problems and they have to be really careful about eyesight, or if they can go other country and find woman other country, children can go other country, not from own country, can bring good energy, also 12L 11H maybe sometime mother father other country or very different energies. 2nd from 10H, like Kitcheri rice and dahl together. They can go overseas. Sometime profit from people they are agent for insurance. Can make money from life insurance, can be good agent for that because 12H is future, or people who want to sell dreams, like sell dream house, sell vacation.\n")
    if (12,12) in x and asc == 'Li' and ("Sa 6H") in planets_houses:
        print("12L 12H and Li asc and Sa6H: Very successful beer, bar, alcohol factory. Owner of beer bar from Germany, Denmark he has combination Sa 6H, Me 12H he makes very very good wine all over the world. Usually wine is very bad business according to astrology giving bad energy to people, sure you will suffer for this, sure you will have problem for liver and kidney, Sa 6H and 12H you will suffer a lot, but good for money\n")
    if (12,12) in x and (6,6) in x:
        print("12L 12H and 6L 6H: Can be very good doctor Ayurveda if 12L 12H and 6L 6H this is aspecting, make very good asab, with fruit very good for digestion. Very positive. Suppose Ju Pi 12H and Me Vi 6H or opposite can be very good Vedya, ayurvedic doctor. \n")
    if (12,12) in x and asc == 'Le':
        print("12L 12H and Le asc: Mo 12H, so most of time lots of traveling comes, but people can have depression a lot if Ash Nak without depression, but depression a lot, can bring very spiritual mother but doesn’t connect with children, goes far away from them by spirituality. Mo will be 9H from the 4H, very good.\n")
    if (12,12) in x and asc == 'Ta':
        print("12L 12H and Ta asc: If Tau asc, Ma 12H same thing can happen with wife (not connecting to children, goes far away from thm by spirituality), wife can be very spiritual and go own path, separation comes or she is not interested in sex, become manglic, 6, 7 house ruler becomes own sign 12H, she becomes spiritual\n")
    if (12,12) in x:
        print("12L 12H IF aspected by benefic planet they expend money positive way, buy good car good things. Lots of anger people. Immediately they can go angry, without reason sometime, sometime they manipulate people easily. And if they can work with alcohol or wine very good money they can make.  \n")


def retrochecker():
    print("Info based on retrograde planets: ")
    if ("Ju R") in retrolist and ("Sa R") in retrolist:
        print("Ju R and Sa R: Old soul?")
    if asc == 'Le' and (phd.get('Ju') == 7) and  (('Ju R') in retrolist):
        print("If JuR 7H problem after marriage, and again marriage, or after marriage, can have good health. \n")
    if asc == 'Vi' and (phd.get('Ju') == 2) and  (('Ju R') in retrolist):
        print("S: Ju retrograde 2H? P. Same, problem, but if another retrograde there then no problem. \n")
    if asc == 'Cap' and  (('Ju R') in retrolist) and (phd.get('Ju') == 2):
        print("S: Ju 2H retrograde? P. In Aq we say Ju positive. \n")
    if (('Ju R') in retrolist) and (phd.get('Ju') in (1,7)):
        print("S: Why Ju 1H retrograde better than 7H? P. 1H of self. 7H not good, partner. S: In what way is Ju fallen retrograde 1H good for personality? P. For knowledge and for finding good partner. Retrograde fallen 1H very good. Fallen planet much better than stronger planet in kali yuga. S: Sometime you say 1H false planet. P. Even false personality they try to be best, they will not have ego.\n")
    if asc == 'Vi' and (('Ve R') in retrolist) and (phd.get('Ve') == 1) :
        print("Sometimes Vi asc Ve 1H retrograde also very good. Good for soft people. S: Person himself will be soft? P. Soft and will not take risk in life. Fallen planet much better than stronger planet in kali yuga. S: Sometime you say 1H false planet. P. Even false personality they try to be best, they will not have ego. \n")
    if asc == 'Pi' and (('Me R') in retrolist) and (phd.get('Me') == 1) :
        print("Sometimes Pi asc Me retrograde 1H can be very good. Also gives knowledge. Fallen planet much better than stronger planet in kali yuga. S: Sometime you say 1H false planet. P. Even false personality they try to be best, they will not have ego.\n")
    if asc == 'Can' and (('Ma R') in retrolist) and (phd.get('Ma') == 1) :
        print("If Ma retrograde in fallen sign 1H not good. Ma retrograde 1H fallen, hard people, but positive. \n")
    if asc == 'Ar' and (('Sa R') in retrolist) and (phd.get('Sa') == 1) :
        print("If Sa retrograde in fallen sign 1H not good. \n")


exalted = []
false = []
def planetsignchecker():
    global lord_planet
    print("Info based only on Planets and Signs:")
    if ('Su Ar') in pslist:
        exalted.append("Su")
        print("Sun is exalted")
    if ('Su Li') in pslist:
        false.append("Su")
        print("Sun is false")
    if ('Mo Ta') in pslist:
        exalted.append("Mo")
        print("Moon is exalted")
    if ('Mo Sc') in pslist:
        false.append("Mo")
        print("Moon is false")
    if ('Ju Cap') in pslist:
        false.append("Ju")
        print("Jupiter is false")
    if ('Ju Can') in pslist:
        exalted.append("Ju")
        print("Jupiter is exalted")
    if ('Sa Li') in pslist:
        exalted.append("Sa")
        print("Sa is exalted")
    if ('Sa Ar') in pslist:
        false.append("Sa")
        print("Sa is false")
    if ('Ma Cap') in pslist:
        exalted.append("Ma")
        print("Ma is exalted")
    if ('Ma Can') in pslist:
        false.append("Ma")
        print("Ma is false")
    if ('Me Vi') in pslist:
        exalted.append("Me")
        print("Me is exalted")
    if ('Me Pi') in pslist:
        false.append("Me")
        print("Me is false")
    if ('Ve Pi') in pslist:
        exalted.append("Ve")
        print("Ve is exalted")
    if ('Ve Vi') in pslist:
        false.append("Ve")
        print("Ve is false")
    if ('Ra Ge') in pslist:
        exalted.append("Ra")
        print("Ra is exalted")
    if ('Ra Sa') in pslist:
        false.append("Ra")
        print("Ra is false")
    if ('Ke Sa') in pslist:
        exalted.append("Ke")
        print("Ke is exalted")
    if ('Ke Ge') in pslist:
        false.append("Ke")
        print("Ke is false")
    if lord_planet.get(8) in exalted:
        print("8L exalted: Extra knowledge of things you can’t get from books, born with it?\n")
    if lord_planet.get(8) in false:
        print("8L false: Can have knowledge but it’s false\n")

#def redirector(inputStr):
#    txt.insert(INSERT, inputStr)



class StdoutStub:
    def __init__(self, txt):
        self.txt = txt
    def write(self, inputStr):
        self.txt.insert(INSERT, inputStr)
    def flush(self):
        pass


#sys.stdout = StdoutStub(txt)

"""
def redirector(inputStr=""):
    import sys
    root = Toplevel()
    txt = ScrolledText(master, bg="#C2DFFF", width = 97, height= 25, font = "Arial 11")
    sys.stdout = StdoutStub("txt")
    txt.grid(column = 0, row = 14, columnspan=3)

#sys.stdout.write = redirector #whenever sys.stdout.write is called, redirector is called.
"""

def ok():
    global asc
    global rot
    global phd
    global lord_in_houses
    global allA
    global cn
    makesigns()
    makepslist()
    asc = getasc()
    addHL()
    rot = find_rotator()
    asc_rotator()
#    print("Planets in signs:")
#    print(pslist)
    print("Planets in houses:")
    print(planetshouses())
    RKcheck()
    txt.insert(END, '\n')
    phd = dict(zip(planets, houselist))
    cn = Counter(phd.values())
    asp()
    allA = [maA,juA,saA,veA,meA,moA,suA,raA,keA]
    correctasp()
    MaSa()
    fullmoon()
    f(lord_base_dict)
    f(lord_base_dict2)
    lordinhouses()
    txt.insert(END, '\n')
    exchange(lord_in_houses_dict)
    findlordisplanet()
    ascinfo()
    periodinfo()
    printexchange()
    exchangechecker()
    txt.insert(END, '\n')
    addR()
    print(retrolist)
    retrochecker()
    txt.insert(END, '\n')
    planetsignchecker()
    txt.insert(END, '\n')
    plhochecker()
    txt.insert(END, '\n')
    lordchecker()
    txt.insert(END, '\n')
    #redirector("Thanks for using the app")
    sys.stdout = StdoutStub(txt)
    #textbox.configure(state="disabled")
    master.quit()

# Resert all lists necessary to start calculations again
def reset():
    global txt
    txt.delete(1.0,END)
    global signs
    global pslist
    global houselist
    global planets_houses
    global asclist
    global exchangel
    global lord_in_houses_dict
    global lord_in_houses_dict2
    global lhlist
    global lordlist
    global lordlist2
    global nhouselist
    global nhouselist2
    global templords
    global planet_houselist_dict
    global lord_base_dict
    global lord_base_dict2
    global retrolist
    global RaKeCheck
    global lord_planet
    global exalted
    global false
    global phd
    global allA
    global maA
    global juA
    global saA
    global veA
    global meA
    global moA
    global suA
    global raA
    global keA
    signs = []
    pslist = []
    houselist = []
    planets_houses = []
    asclist = []
    exchangel = []
    lord_in_houses_dict = {}
    lord_in_houses_dict2 = {}
    lhlist = {}
    lordlist = []
    lordlist2 = []
    nhouselist = []
    nhouselist2 = []
    planet_houselist_dict = {}
    templords = []
    lord_base_dict = dict(zip(lord_base_list,lords))
    lord_base_dict2 = dict(zip(lord_base_list2,lords2))
    retrolist = []
    delretrocheckbox()
    RaKeCheck= []
    lord_planet = {}
    exalted = []
    false = []
    allA = []
    maA = []
    juA= []
    saA = []
    veA = []
    meA = []
    moA = []
    suA = []
    raA = []
    keA = []
    phd = {}


def cancel():
    print("The user clicked 'Cancel")
    master.destroy()


retrolist = ["Ra R", "Ke R"]

# make retrolist
def addR():
    global retrolist
    if mvar.get() == 1:
        retrolist.append("Ma R")
    if mvar1.get() == 1:
        retrolist.append("Ve R")
    if mvar2.get() == 1:
        retrolist.append("Me R")
    if mvar3.get() == 1:
        retrolist.append("Ju R")
    if mvar4.get() == 1:
        retrolist.append("Sa R")
    return retrolist




#Label
label1 = Label(text="  Welcome to Astrology App",bg="#C2DFFF",font=("Times New Roman",18))
label1.grid(column=0,row=0)

label2 = Label(text="Ma: ",bg="#C2DFFF")
label2.grid(column=0,row=2)

label3 = Label(text="Ve: ",bg="#fcffce")
label3.grid(column=0,row=3)
label4 = Label(text="Me: ",bg="#C2DFFF")
label4.grid(column=0,row=4)
label5 = Label(text="Mo: ",bg="#fcffce")
label5.grid(column=0,row=5)
label6 = Label(text="Su: ",bg="#C2DFFF")
label6.grid(column=0,row=6)
label7 = Label(text="Ju: ",bg="#fcffce")
label7.grid(column=0,row=7)
label8 = Label(text="Sa: ",bg="#C2DFFF")
label8.grid(column=0,row=8)
label9 = Label(text="Ra: ",bg="#fcffce")
label9.grid(column=0,row=9)
label10 = Label(text="Ke: ",bg="#C2DFFF")
label10.grid(column=0,row=10)
labelasc = Label(text="Select ascendant:",bg="#fcffce")
labelasc.grid(column=0,row=1)
labelretro = Label(text="If R check box:",bg="#fcffce")
labelretro.grid(column=1,row=1)

txt = ScrolledText(master, bg="#C2DFFF", width = 97, height= 25, font = "Arial 11")
txt.grid(column = 0, row = 14, columnspan=3)

#sys.stdout = StdoutStub(txt)


button = Button(master, text="OK", default ='active',command=ok).grid(column=2,row=11)
button = Button(master, text="Reset", default ='active',command=reset).grid(column=2,row=12)
button = Button(master, text ="Cancel",command = cancel).grid(column=0,row=11)

#C1 = Checkbutton(master, state = ACTIVE, variable = mvar,command =addRM)
C1 = Checkbutton(master, state = ACTIVE, variable = mvar)
C1.grid(column = 1, row=2)
#C2 = Checkbutton(master, state = ACTIVE, variable = mvar1,command =addRV)
C2 = Checkbutton(master, state = ACTIVE, variable = mvar1)
C2.grid(column = 1, row=3)
#C3 = Checkbutton(master, state = ACTIVE, variable = mvar2,command =addRME)
C3 = Checkbutton(master, state = ACTIVE, variable = mvar2)
C3.grid(column = 1, row=4)
#C4 = Checkbutton(master, state = ACTIVE, variable = mvar3,command =addRJ)
C4 = Checkbutton(master, state = ACTIVE, variable = mvar3)
C4.grid(column = 1, row=7)
#C5 = Checkbutton(master, state = ACTIVE, variable = mvar4)
C5 = Checkbutton(master, state = ACTIVE, variable = mvar4)
C5.grid(column = 1, row=8)


master.mainloop()
