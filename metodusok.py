


# ------- Szükséges: pip install opencv-python -------
import cv2 as cv
import os







# ------- Mondatok és képek beolvasása -------
def fajlBeolvasas(n):
	fajl = open("szintek.txt","r",encoding="UTF-8")
	mondatok = fajl.readlines()
	return print(f"\n\t{mondatok[n]}"), Kepek(n)






# ------- A játék szíve, ő futtat mindent -------
def Motor():
	os.system("")

	igek = ["megy", "eszik", "felvesz", "hasznal", "ad", "vizsgal"]
	fonevek = ["epulet", "kut", "kastely", "penz", "vartemplom", "kamra", "ajto", "kulcs", "ajto", "faajto", "etel"]


	n = 0
	fajlBeolvasas(n)	# Mondat és kép betöltése

	print(f"\t(Figyelem! A 3. helyszínváltás után minden alkalommal csökkeni fog az életpont!)")


	eletEro = 5
	helyszin = 2
	szamlalo = 0

	penz = 0
	kulcs = 0

	ig = 3


	while eletEro != 0:
		bekert = str(input("\n>> "))
		szavak = bekert.split()

		# 3. helyszínváltás után csökkenő életerő
		if szamlalo > 2:
			eletEro -= 1


		# Evés után 3 körig nem megy le életerő
		if eletEro == 9:
			if ig != 0:
				ig -= 1	
				eletEro += 1



		n = None

		if szavak[0] == igek[0] and szavak[1] == fonevek[0] and helyszin == 2:	# megy epulet
			n, helyszin = 2, 3



		elif szavak[0] == igek[0] and szavak[1] == fonevek[1]:	# megy kut
			n, helyszin = 3, 4
		elif szavak[0] == igek[0] and szavak[1] in (fonevek[0], fonevek[2]) and helyszin == 3: # megy epulet / kastely
			n, helyszin = 5, 6



		elif szavak[0] == igek[2] and szavak[1] == fonevek[3]:	#felvesz penz
			n, helyszin = 4, 5
			if penz == 0:
				penz += 1
		elif szavak[0] == igek[0] and szavak[1] in (fonevek[0], fonevek[2]) and helyszin == 4: # megy epulet / kastely
			n = 5



		elif szavak[0] == igek[0] and szavak[1] in (fonevek[0], fonevek[2]) and helyszin == 5: # megy epulet / kastely
			n, helyszin = 5, 6



		elif szavak[0] == igek[0] and szavak[1] == fonevek[4]:	# megy vartemplom
			n, helyszin = 6, 7
		elif szavak[0] == igek[0] and szavak[1] == fonevek[5] and helyszin == 6:	# megy kamra
			n = 9
		elif szavak[0] == igek[0] and szavak[1] == fonevek[6] and helyszin == 6:	# megy ajto
			n = 14



		elif szavak[0] in (igek[3], igek[4]) and szavak[1] == fonevek[3]:	# hasznal penz / ad penz
			if penz == 1:
				n, helyszin = 7, 8
				penz = 0
			else:
				print(f"Nincs nálad pénz!")
		elif szavak[0] == igek[0] and szavak[1] == fonevek[5] and helyszin == 7:	# megy kamra
			n = 9
		elif szavak[0] == igek[0] and szavak[1] == fonevek[6] and helyszin == 7:	# megy ajto
			n = 13



		elif szavak[0] == igek[2] and szavak[1] == fonevek[7]:	# felvesz kulcs
			n, helyszin = 8, 9
			kulcs = 1
		elif szavak[0] == igek[0] and szavak[1] == fonevek[5] and helyszin == 8:	# megy kamra
			n = 9
		elif szavak[0] == igek[0] and szavak[1] == fonevek[6] and helyszin == 8:	# megy ajto
			n = 13



		elif szavak[0] == igek[0] and szavak[1] == fonevek[5] and helyszin == 9:	# megy kamra
			n, helyszin = 9, 10
		elif szavak[0] == igek[0] and szavak[1] == fonevek[6] and helyszin == 9:	# megy ajto
			n = 13



		elif szavak[0] == igek[0] and szavak[1] == fonevek[9] and helyszin == 10:	# megy faajto
			n, helyszin = 10, 11
		elif szavak[0] == igek[1] and szavak[1] == fonevek[10] and helyszin == 10:	# eszik etel
			n, helyszin = 12, 11
			eletEro = 10
		elif szavak[0] == igek[0] and szavak[1] == fonevek[6] and helyszin == 10:	# megy ajto
			n = 13



		elif szavak[0] == igek[3] and szavak[1] == fonevek[7] and helyszin == 11:	# hasznal kulcs
			if kulcs == 1:
				n, helyszin = 11, 12
				kulcs = 0
			else:
				print("Nincs nálad kulcs")



		elif szavak[0] == igek[1] and szavak[1] == fonevek[10]:	# eszik etel
			n, helyszin = 12, 13
			eletEro = 10
		elif szavak[0] == igek[0] and szavak[1] == fonevek[9] and helyszin == 12:	# megy faajto
			n = 10
		elif szavak[0] == igek[0] and szavak[1] == fonevek[6] and helyszin == 12:	# megy ajto
			n = 13



		elif szavak[0] == igek[0] and szavak[1] == fonevek[6] and helyszin == 13:	# megy ajto
			n, helyszin = 13, 14



		elif szavak[0] == igek[3] and szavak[1] == fonevek[7] and helyszin == 14:	# hasznal kulcs
			if kulcs == 1:
				n = 14
				kulcs = 0
			else:
				print("Nincs nálad kulcs!")
		elif szavak[0] == igek[5] and szavak[1] == fonevek[6] and helyszin == 14:	# vizsgal ajto
			n = 14
			if kulcs == 1:
				n = 14
				kulcs = 0
			else:
				print("Nincs nálad kulcs!")

		# A játék végtelenítés szempontjából lett ez a sor beleírva
		elif szavak[0] == igek[0] and szavak[1] in (fonevek[0], fonevek[2]) and helyszin == 14: # megy epulet / kastely
			n, helyszin = 5, 6
		





		if n == None:
			print("Hiba, próbáld újra!")
		else:
			szamlalo += 1
			fajlBeolvasas(n-1)
			print(f"\t\033[32mPénz: \033[37m{penz}, \033[0;36mÉleterő: \033[37m{eletEro}, \033[33mKulcs: \033[37m{kulcs}") 

				
	print("\n\t"'\033[31m'+"Vége, elfogyott az életerőd, meghaltál!"+ '\033[37m'+"")	







# ------- Képek megjelenítése -------
def Kepek(n):

	kepLista = ["01_var.jpg", "02_kastely.png", "03_kut.jpg", "04_erme.png", "05_lepcso.jpg", "06_keregeto.png", "07_szerzetes.jpg", "08_kulcs.jpg", "09_kamra.jpeg", "10_ajto.png", "11_portal.png", "12_eleteros.png", "10_ajto.png", "14_nem.png"]

	utolsoPerJel = 0
	for letter in reversed(__file__):
		utolsoPerJel += 1
		if letter == '\\':
			break

	
	utvonal = __file__[:-utolsoPerJel] + "\\kepek\\" + kepLista[n]

	felirat = "Nyomj Entert"

	cv.namedWindow('Idoregesz', cv.WINDOW_NORMAL)
	image = cv.putText(cv.imread(f'{utvonal}'), felirat, (1700, 1700), cv.FONT_HERSHEY_SIMPLEX, 6, (0, 0, 255), 20, cv.LINE_AA)
	cv.imshow('Idoregesz', image)
	cv.moveWindow('Idoregesz', 401, 154)
	cv.waitKey(0)
	cv.destroyAllWindows()


	
































