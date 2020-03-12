#Main.py Violent Thomas PYCharm 2019.3.2 09/03/2020

import sys
import os
import datetime

#CE SCRIPT DOIT ETRE EXECUTE EN TANT QUE ROOT

#lit le fichier /etc/dnsmasq.d/02-pihole-dhcp.conf et cherche la ligne avec la chaine "[::]"
#si cette ligne est trouvé, remplace "[::]" par "[fe80::]" et redemarre pihole (redémarre dnsmasq)
#sinon, ne fait rien

#active le mode débug, si cette propriété est active, le programme ecrit plus d'information dans le fichier log et la console python
#si false, écrira uniquement les érreurs
DEBUG_MODE = False

#FILE_PATH = "/etc/dnsmasq.d/02-pihole-dhcp.conf"
FILE_PATH = "D:\\violentt.SNIRW\\Divers\\Projets random\\DNSFixPiHole\\02-pihole-dhcp.conf"
LOG_PATH = "D:\\violentt.SNIRW\\Divers\\Projets random\\DNSFixPiHole\\log.txt"

#écrit et affiche les messages de debug sur la console et dans un fichier texte
#affiche les messages uniquement si c'est un message d'érreur ou que la variable DEBUG_MODE est sur TRUE
#log: file, object fichier ouvert en écriture
#msg: string, contenu du message, sera précedé de la date et heure courrante du système
#error_level: integer, niveau du message: 0=information, 1=erreur
def logg(log, msg, error_level):
    if (DEBUG_MODE or error_level == 1):
        print(datetime.datetime.now(), " - ", msg)
        try:
            log.write(str(datetime.datetime.now()))
            log.write(" - ")
            log.write(msg)
            log.write("\n")
        except:
            print("Error on writing log: ", sys.exc_info()[0], "\n", sys.exc_info()[1], "\n", sys.exc_info()[2])


def main():

    try:
        #ouvre le fichier en mode lecture avec "updating" (écriture)
        log = open(LOG_PATH, mode="a")

        logg(log, "", 0)
        logg(log, "Starting", 0)

        f = open(FILE_PATH, mode="r")


        #lit le fichier
        text = f.read()

        #ferme le fichier pour le réouvrir en mode écriture
        f.close()
        f = open(FILE_PATH, mode="w")

        #remplace la ligne qui nous intéresses
        text2 = text.replace("[::]", "[fe80::]")

        #vérifie si le fichier à changé
        if (text != text2):
            logg(log, "found [::], replacing with [fe80::] and writing file", 0)
            #écrit dans le fichier
            f.write(text2)

            logg(log, "send system call to restart PiHole", 0)
            #envoie une commande au système
            os.system("pihole restartDNS");

        logg(log, "end of script, clossing files", 0)
        #ferme le fichier
        f.close()
        log.close()
    except:
        logg(log,"Error:" + str(sys.exc_info()[0]) + "\n" + str(sys.exc_info()[1]) + "\n" + str(sys.exc_info()[2]), 1)




if __name__=="__main__":
    main()
