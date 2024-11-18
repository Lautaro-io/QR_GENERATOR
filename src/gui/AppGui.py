from tkinter import PhotoImage

import customtkinter as ctk
import qrcode
from PIL import Image,ImageTk
import io

from qrcode.console_scripts import commas

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.center_window()
        self.main()


    def main(self):
        self.grid_columnconfigure(1,weight=1)
        title = ctk.CTkLabel(self,text="Generador de QR" ,font=("Roboto", 25,"bold"))
        title.grid(row =0 , column = 1 ,pady =20 )
        self.entry = ctk.CTkEntry(self,placeholder_text="Ingrese una URL o texto" , width= 250)
        self.entry.grid(row = 1, column = 1 ,pady = 20)
        btn = ctk.CTkButton(self, text="Submit" , width=250, command = self.generate_qr,fg_color="white", text_color="black" , hover_color="gray")
        btn.grid(row = 2 ,column = 1 )





    def center_window(self):
        ancho = 400
        alto = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (ancho // 2)
        y = (screen_height // 2) - (alto // 2)

        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def clean_label(self):
        #self.qr_label.configure(text=" " , image =None)
        self.qrFrame.destroy()
        self.cleanBtn.destroy()
        self.qr_label.destroy()
        self.main()

    def generate_qr(self ):
        data = self.entry.get()
        self.qrFrame = ctk.CTkFrame(self,fg_color="transparent")
        self.qrFrame.grid(row = 3 , column =1 )
        self.qr_label = ctk.CTkLabel(self.qrFrame, text = "" ,width=300,height=300  )
        self.qr_label.grid(row = 0, column = 0 ,pady = 0)
        #self.qr_label.configure(text= "")
        if data  != "":
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=1,
            )
            qr.add_data(data)
            qr.make(fit=True)

            img =  qr.make_image(fill= "black", back_color = "white")
            img_tk = ImageTk.PhotoImage(img)
            self.qr_label.configure(image=img_tk)
            #self.qr_label.image = img_tk
            self.cleanBtn = ctk.CTkButton(self,text = "Limpiar QR. ",width = 250, command=self.clean_label)
            self.cleanBtn.grid(row =4 , column =1 )
        else:
            self.qr_label.configure(text = "Ingrese un texto correcto. ")




