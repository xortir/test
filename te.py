# -*- coding: utf-8 -*-

from Tkinter import *

# Vytvoříme samotné okno.
vypocet = Tk()

f_frame = Frame(vypocet)
f_frame.pack()
f_data = Frame(f_frame)
f_data.pack(side = LEFT)
f_text = Frame(f_frame)
f_text.pack(side = RIGHT)
f_frame1 = Frame(f_data)
f_frame1.pack()
f_frame2 = Frame(f_data)
f_frame2.pack()
f_frame3 = Frame(f_data)
f_frame3.pack()

f_lidi = Frame(f_frame1)
f_lidi.pack(side = LEFT)
l_lidi = Label(f_lidi, text = "Obyvatel")
l_lidi.pack()   
mb_lidi = Entry(f_lidi, width = 4)
mb_lidi.pack()

f_domy = Frame(f_frame1)
f_domy.pack(side = LEFT)
l_domy = Label(f_domy, text = "Domů")
l_domy.pack()   
mb_domy = Entry(f_domy, width = 4)
mb_domy.pack()

f_vojaku = Frame(f_frame1)
f_vojaku.pack(side = LEFT)
l_vojaku = Label(f_vojaku, text = "Vojáků")
l_vojaku.pack()   
mb_vojaku = Entry(f_vojaku, width = 4)
mb_vojaku.pack()

f_sypka = Frame(f_frame2)
f_sypka.pack(side = LEFT)
l_sypka = Label(f_sypka, text = "Kolo,kdy je sypka")
l_sypka.pack()   
mb_sypka = Entry(f_sypka, width = 4, text = "0")
mb_sypka.pack()

f_zold = Frame(f_frame2)
f_zold.pack(side = LEFT)
l_zold = Label(f_zold, text = "Žold")
l_zold.pack()   
mb_zold = Entry(f_zold, width = 4)
mb_zold.pack()

f_kola = Frame(f_frame2)
f_kola.pack(side = LEFT)
l_kola = Label(f_kola, text = "Kol")
l_kola.pack()   
mb_kola = Entry(f_kola, width = 4)
mb_kola.pack()

f_pocasi_zlato = Frame(f_frame3)
f_pocasi_zlato.pack(side = LEFT)
l_pocasi_zlato = Label(f_pocasi_zlato, text = "Počasí na zlato")
l_pocasi_zlato.pack()   
mb_pocasi_zlato = Entry(f_pocasi_zlato, width = 4)
mb_pocasi_zlato.pack()

f_pocasi_domy = Frame(f_frame3)
f_pocasi_domy.pack(side = LEFT)
l_pocasi_domy = Label(f_pocasi_domy, text = "Počasí na domy")
l_pocasi_domy.pack()   
mb_pocasi_domy = Entry(f_pocasi_domy, width = 4)
mb_pocasi_domy.pack()

f_bonus = Frame(f_frame3)
f_bonus.pack(side = LEFT)
l_bonus = Label(f_bonus, text = "Bonus země")
l_bonus.pack()   
mb_bonus = Entry(f_bonus, width = 4)
mb_bonus.pack()

t = Text(f_text, height = 20, width = 47)
t.pack(side = RIGHT)
t.insert(END, "Kolo\t Obyvatel\t Dostav domů/za\t Příjem země\n")


mb_sypka.insert(END, "0")
mb_zold.insert(END, "0")
mb_pocasi_zlato.insert(END, "100")
mb_pocasi_domy.insert(END, "100")
mb_bonus.insert(END, "0")

ob_start = 0
domy_start = 0
vojaku = 0
stoji_sypka = 0
zold = 0
pocet_kol = 0
pocasi_zlato = 0
pocasi_domy = 0
bonus = 0

	

def obyvatel(kolo):
	global ob_start
	global stoji_sypka
	prirustek = 1
	if (kolo-1 >= stoji_sypka):
		prirustek += 2
	ob = ob_start
	while (ob/10 > 0):
		prirustek += 0.5
		ob -= 10
	ob = int(ob_start + prirustek)
	ob_start = ob
	return ob

def domy():
	global ob_start
	global domy_start
	global vojaku
	celkem = ob_start + vojaku
	if (domy_start >= celkem):
		return 0,0
	else:
		kup = celkem - domy_start
		mas = domy_start
		plat = 0
		for i in range(kup):
			plat += int(((mas + 1.)*(mas + 1.)/81 + 60)*(pocasi_domy/100))
			mas += 1
		domy_start = mas
		return kup, plat
			
def zisk():
	global ob_start
	global pocasi_zlato
	global zold
	zlato = int(ob_start * 5 * pocasi_zlato * bonus) - zold
	return zlato
	
def vypocitej():
	t.delete(1.0, END)
	t.insert(END, "Kolo\t Obyvatel\t Dostav domů/za\t Příjem země\n")
	global ob_start, domy_start 
	ob_start = int(mb_lidi.get()) 
	domy_start = int(mb_domy.get())
	global vojaku 
	vojaku = int(mb_vojaku.get())
	global stoji_sypka 
	stoji_sypka = int(mb_sypka.get())
	global zold 
	zold = int(mb_zold.get())
	global pocet_kol 
	pocet_kol = int(mb_kola.get())
	global pocasi_zlato 
	pocasi_zlato = 1 + int(mb_pocasi_zlato.get())/100.
	global pocasi_domy 
	pocasi_domy = int(mb_pocasi_domy.get())
	global bonus 
	bonus = 1 + int(mb_bonus.get())/100.	
	for i in range(pocet_kol+1):
		if i == 0:
			prijem = zisk()	
			t.insert(END, str(i) + "\t    " + str(ob_start) + "\t       " + "0" + "/" + "0" + "\t              " + str(prijem) + "\n")
		else:
			lidi = obyvatel(i)
			domu, cena_domu = domy()
			prijem = zisk()
			t.insert(END, str(i) + "\t    " + str(lidi) + "\t       " + str(domu) + "/" + str(cena_domu) + "\t              " + str(prijem) + "\n")






bQuit = Button(vypocet, text="Konec", command = vypocet.quit)
bQuit.pack()

bt_vypocti = Button(f_data, text = "Vypočti", command = vypocitej)
bt_vypocti.pack()
"""
def obyvatel()

def domy()

def zisk()

def



for i in int(mb_kola.get())
"""
# Spustíme smyčku událostí.
vypocet.mainloop()
