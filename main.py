import keyboard
import time
import random
import tkinter 
import threading
from math import ceil

class App : 
    def __init__(self, root):
        self.window = root
        self.window.title("Anti-AFK Externe")
        self.window.geometry("480x360")
        self.window.minsize(480, 360)
        self.window.iconbitmap("asset/stop.ico")
        self.window.protocol("WM_DELETE_WINDOW", self.close)

        self.data = 0
        self.status = False
        #comps
        self.container = tkinter.Frame(self.window)
        self.txt = tkinter.Label(self.window, text="Indiquez le délai maximum avant d'être expulsé pour inactivité en minutes")
        self.box = tkinter.Entry(self.container, )
        self.btn = tkinter.Button(self.container, text="Sauvgarder", command=self.isInt)
        self.information = tkinter.Label(self.window, text="")
        self.startBtn = tkinter.Button(self.window, text="START", command=self.toggleFnc, bg="#00BB1E", padx=40)
        self.phase = tkinter.Label(self.window, text="PHASE : mise en place", pady=10)
        
        self.box.grid(row=0, column=0, padx=10, pady=10)
        self.btn.grid(row=0, column=1, padx=10, pady=10)

        self.txt.pack()
        self.information.pack()
        self.container.pack()

    def isInt(self):
        res = self.box.get()
        try :
            value = int(res)    
            self.data = value
            self.information["text"] = f"le délais maximun est de {value} min"
            self.startBtn.pack()
        except : 
            self.information["text"] = f"Veuillez indiquer un délai en minutes, car {res} n'est pas valable"
            self.startBtn.pack_forget()

    def toggleFnc(self) : 
        if not self.status:         
            self.status = True 
            self.thread = threading.Thread(target=self.antiAfk)
            self.thread.start()
            self.startBtn["text"] = "STOP"
            self.startBtn.configure(bg="#FF0000")
        else : 
            self.status = False 
            self.startBtn["text"] = "START"
            self.startBtn.configure(bg="#00BB1E")

    def antiAfk(self): 
        #start
        setup  = 0
        
        while self.status == True:
                
            if setup == 0 : 
                self.phase["text"] = "PHASE : mise en place"
                self.phase.pack()

            if setup <= 10 :
                keyboard.press('space')
                time.sleep(1)
                keyboard.release('space')
                setup += 1
            else :
                    
                cd = ((random.randint(ceil(self.data/2), ((self.data)-1)))*60)
                print(cd)
                while cd > 0 :
                    if self.status == False : 
                        break
                    self.phase["text"] = f"MODE AFK Activé, il reste {cd} secondes avant le prochain saut"
                    time.sleep(1)
                    cd -= 1

                keyboard.press('space')
                time.sleep(0.1)
                keyboard.release('space')
  
        
        setup = 0 
        self.phase.pack_forget()
    
    def close(self):
        self.status = False
        self.window.destroy()



      

if __name__ == "__main__":
    root = tkinter.Tk()
    app = App(root=root)
    root.mainloop()
