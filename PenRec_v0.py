from tkinter import *
from tkinter import ttk
import pyautogui
from fpdf import FPDF
import os
import time
from PIL import Image
from datetime import datetime
import threading

root = Tk()
root.title("PenRec v0")
frm = ttk.Frame(root, padding=10)
frm.grid()
global f
f = True
global w
w = 15

def inc_up():
	global w
	w = w + 1
	print("Interval Increased to " + str(w))
def inc_dn():
	global w
	w = w - 1
	print("Interval Decreased to " + str(w))

def start(): 
    print("start")
    global f
    a = 0
    oldScrot = 0
    while f == True:
      scrot = pyautogui.screenshot()
      if scrot != oldScrot:
                print("*")
                a = a + 1
                temp = "tmp/scrot" + str(a) + ".jpg"
                scrot.save(temp)		
                scrot = oldScrot
      time.sleep(w)

def stop():
  print("stop")
  global f
  f = False
  
  pdf = FPDF()
  pdf.set_auto_page_break(0)

  imagelist = [i for i in os.listdir('tmp') if i.endswith('jpg')]
  print(imagelist)
  
  for image in sorted(imagelist):
    pdf.add_page()
    pdf.image('tmp/' + image, w=190)
    images = "tmp/" + image
    os.remove(images)
  dt = datetime.now()
  pdf.output("Transcript" + str(dt) + ".pdf", "F")
  print("Output Success.")

def press_start():
	t1 = threading.Thread(target=start)
	t1.start()

def press_stop():
	t2 = threading.Thread(target=stop)
	t2.start()

if __name__ == "__main__":
	start_btn = ttk.Button(frm,text="Start",command=press_start).grid(column=0, row=0)
	stop_btn = ttk.Button(frm,text="Stop",command=press_stop).grid(column=0, row=1)
	inc_up = ttk.Button(frm,text="+1s", command=inc_up).grid(column=1, row=0)
	inc_dn = ttk.Button(frm,text="-1s", command=inc_dn).grid(column=1, row=1)
	root.mainloop()
