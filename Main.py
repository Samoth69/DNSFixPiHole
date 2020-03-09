#Main.py Violent Thomas PYCharm 2019.3.2 09/03/2020

#lit le fichier /etc/dnsmasq.d/02-pihole-dhcp.conf et cherche la ligne avec la chaine "[::]"
#si cette ligne est trouvé, remplace "[::]" par "[fe80::]" et redemarre pihole (redémarre dnsmasq)
#sinon, ne fait rien

#FILE_PATH = "/etc/dnsmasq.d/02-pihole-dhcp.conf"
FILE_PATH = "02-pihole-dhcp.conf"

def main():
    #ouvre le fichier en mode lecture avec "updating" (écriture)
    f = open(FILE_PATH, mode="r")

    #lit le fichier
    text = f.read()

    #ferme le fichier pour le réouvrir en mode écriture
    f.close()
    f = open(FILE_PATH, mode="w")

    #remplace la ligne qui nous intéresses
    text = text.replace("[::]", "[fe80::]")

    #écrit dans le fichier
    f.write(text)

    #ferme le fichier
    f.close()




if __name__=="__main__":
    main()