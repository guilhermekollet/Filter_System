#Filter System Tool Image
from PIL import Image

#Aplication Simple, open the img em save em .ico to GUI
img = Image.open(r"E:\Usuários\GuiSk\GitHub\Filter_System\img\IconePNG.png") #directory
img.save("iconGUI.ico") #the name and .format
print("Img converted!")
