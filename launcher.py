#|==============================================================|#
# Made by IntSPstudio
# Mafith
# ID: 980004001
#
# Twitter: @IntSPstudio
#|==============================================================|#

#LIBRARIES
from tkinter import Tk, Frame, Button, LEFT, BOTH, Entry, StringVar, Label, N, S, W, E, Text, FLAT, END
import calcproc
#SETTINGS
#MAIN
root = Tk()
rootWidth =854 #X
rootHeight =480 #Y
rootSize = str(rootWidth) +"x"+ str(rootHeight)
root.geometry(rootSize)
root.title("Mafith")
#FRAMES
frame1Width = int(rootWidth /5)
frame1Height = rootHeight
frame1Color = "#181818"
frame2Width = rootWidth - frame1Width
frame2Height = rootHeight
frame2Color = "#202020"
frameInputBoxColor ="white"
#LABELS
titleLabelColor ="#0080ff"
#CONTENT
contentTextComFont ="arial"
contentTextColor ="white"
#BUTTONS
buttonBackground ="black"
#INPUT
fileNameMainText = StringVar()
fileNameSecText = StringVar()
contentModeText = StringVar()
#FUNCTION REQUEST
def buttonControl(buttonId):
  #IMPORT
  result = calcproc.rawUserFunctionRequest(fileNameMainInput.get(), fileNameSecInput.get(), contentModeInput.get(), buttonId)
  #EXPORT
  contentTextAdder(result)
def contentTextAdder(rawUserInput):
  contentBox.insert("1.0",calcproc.returnCurrentDateTime(1) +"| "+ rawUserInput +"\n")
#START
if __name__ == "__main__":
  #FRAMES
  f1 = Frame(root, width = frame1Width, height = frame1Height, bg = frame1Color, relief="flat") #1
  f1.pack(fill=BOTH, expand=0, side=LEFT)
  f2 = Frame(root, width = frame2Width, height = frame2Height, bg = frame2Color, relief="flat") #2
  f2.pack(fill=BOTH, expand=1, side=LEFT)
  #LABELS
  fileNameMainLabel = Label(f1, font=(contentTextComFont, 16), text= calcproc.lT61149, fg = titleLabelColor,bg = frame1Color) #1
  fileNameMainLabel.grid(row=1, column=0)
  fileNameSecLabel = Label(f1, font=(contentTextComFont, 16), text= calcproc.lT62150, fg = titleLabelColor,bg = frame1Color) #2
  fileNameSecLabel.grid(row=2, column=0)
  contentModeInputLabel = Label(f1, font=(contentTextComFont, 16), text= calcproc.lT135126, fg = titleLabelColor,bg = frame1Color) #3
  contentModeInputLabel.grid(row=3, column=0)
  buttonAreaALabel = Label(f1, font=(contentTextComFont, 11), text= calcproc.lT23150, fg = titleLabelColor,bg = frame1Color) #4
  buttonAreaALabel.grid(row=4, columnspan=2, sticky=W)
  #INPUT
  fileNameMainInput = Entry(f1, font=(contentTextComFont, 16), textvariable= fileNameMainText, bd=0, insertwidth=1, bg= frameInputBoxColor, justify="left") #1
  fileNameMainInput.grid(row=1, column=1)
  fileNameSecInput = Entry(f1, font=(contentTextComFont, 16), textvariable= fileNameSecText, bd=0, insertwidth=1, bg= frameInputBoxColor, justify="left") #2
  fileNameSecInput.grid(row=2, column=1)
  contentModeInput = Entry(f1, font=(contentTextComFont, 16), textvariable= contentModeText, bd=0, insertwidth=1, bg= frameInputBoxColor, justify="left") #3
  contentModeInput.grid(row=3, column=1)
  #CONTENT
  contentBox = Text(f2, font=(contentTextComFont, 10),bd=0,bg=frame2Color, fg = contentTextColor) #1
  contentBox.pack(fill=BOTH, expand=1)
  #BUTTONS
  b219587 = Button(f1, text= calcproc.lB220730, command = lambda: buttonControl(calcproc.lBi24656), relief=FLAT, bg= buttonBackground, fg= contentTextColor) #1
  b219587.grid(row=5, columnspan=2, sticky=W)
  b25862 = Button(f1, text= calcproc.lB2201022, command = lambda: buttonControl(calcproc.lBi24950), relief=FLAT, bg= buttonBackground, fg= contentTextColor) #2
  b25862.grid(row=6, columnspan=2, sticky=W)
  b25969 = Button(f1, text= calcproc.lB2201116, command = lambda: buttonControl(calcproc.lBi241050), relief=FLAT, bg= buttonBackground, fg= contentTextColor) #3
  b25969.grid(row=7, columnspan=2, sticky=W)
  b35570 = Button(f1, text= calcproc.lB320662, command = lambda: buttonControl(calcproc.lBi34642), relief=FLAT, bg= buttonBackground, fg= contentTextColor) #4
  b35570.grid(row=8, columnspan=2, sticky=W)
  #COM
  root.mainloop()
