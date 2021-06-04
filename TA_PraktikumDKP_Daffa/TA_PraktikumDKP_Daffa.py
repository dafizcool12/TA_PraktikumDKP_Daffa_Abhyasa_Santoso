from tkinter import * 
from tkinter import ttk
from tkinter import messagebox 
from convention import Convention

conv = Convention()

def convert():
    try:
        int_temp = float(num_box.get())
        if int_temp == "":
            messagebox.showerror("Error","Anda belum mengisi nilai yang ingin dikonversikan")
            return
        if radio3.get()== 0:
            messagebox.showerror("Error","BELUM MEMILIH JENIS KONVERSI")
            return
        elif radio3.get() == 1:
            if radio1.get() == 0:
                messagebox.showerror("Error","BELUM MEMILIH JENIS SATUAN YANG AKAN DIKONVERSIKAN")
            elif radio1.get() == 1:
                if radio2.get() == 0:
                    messagebox.showerror("Error","BELUM MEMILIH JENIS SATUAN YANG AKAN DIKONVERSIKAN")
                elif radio2.get() == 1:
                    result = float((int_temp * 0.03937))
                    conv.setUnit("Inci")
                elif radio2.get() == 2:
                    result = float((int_temp * 0.00328))
                    conv.setUnit("Kaki")
                elif radio2.get() == 3:
                    result = float((int_temp * 0.00109))
                    conv.setUnit("Yard")
                elif radio2.get() == 4:
                    result = float(int_temp * 0.000000621)
                    conv.setUnit("Mil")
            elif radio1.get() == 2:
                if radio2.get() == 0:
                    messagebox.showerror("Error","BELUM MEMILIH JENIS SATUAN YANG AKAN DIKONVERSIKAN")
                elif radio2.get() == 1:
                    result = float((int_temp * 0.3937))
                    conv.setUnit("Inci")
                elif radio2.get() == 2:
                    result = float((int_temp * 0.0328))
                    conv.setUnit("Kaki")
                elif radio2.get() == 3:
                    result = float((int_temp * 0.0109))
                    conv.setUnit("Yard")
                elif radio2.get() == 4:
                    result = float(int_temp * 0.00000621)
                    conv.setUnit("Mil")
            elif radio1.get() == 3:
                if radio2.get() == 0:
                    messagebox.showerror("Error","BELUM MEMILIH JENIS SATUAN YANG AKAN DIKONVERSIKAN")
                elif radio2.get() == 1:
                    result = float((int_temp * 39.37))
                    conv.setUnit("Inci")
                elif radio2.get() == 2:
                    result = float((int_temp * 3.28))
                    conv.setUnit("Kaki")
                elif radio2.get() == 3:
                    result = float((int_temp * 1.09))
                    conv.setUnit("Yard")
                elif radio2.get() == 4:
                    result = float(int_temp * 0.000621)
                    conv.setUnit("Mil")
            elif radio1.get() == 4:
                if radio2.get() == 0:
                    messagebox.showerror("Error","BELUM MEMILIH JENIS SATUAN YANG AKAN DIKONVERSIKAN")
                elif radio2.get() == 1:
                    result = float((int_temp * 39370))
                    conv.setUnit("Inci")
                elif radio2.get() == 2:
                    result = float((int_temp * 3280))
                    conv.setUnit("Kaki")
                elif radio2.get() == 3:
                    result = float((int_temp * 1090))
                    conv.setUnit("Yard")
                elif radio2.get() == 4:
                    result = float(int_temp * 0.621)
                    conv.setUnit("Mil")
        elif radio3.get() == 2:
            if radio1.get() == 0:
                messagebox.showerror("Error","BELUM MEMILIH JENIS SATUAN YANG AKAN DIKONVERSIKAN")
            elif radio1.get() == 1:
                if radio2.get() == 0:
                    messagebox.showerror("Error","BELUM MEMILIH JENIS SATUAN YANG AKAN DIKONVERSIKAN")
                elif radio2.get() == 1:
                    result = float((int_temp * 25.4))
                    conv.setUnit("Millimeter")
                elif radio2.get() == 2:
                    result = float((int_temp * 2.54))
                    conv.setUnit("Centimeter")
                elif radio2.get() == 3:
                    result = float((int_temp * 0.0254))
                    conv.setUnit("Meter")
                elif radio2.get() == 4:
                    result = float(int_temp * 0.0000254)
                    conv.setUnit("Kilometer")
            elif radio1.get() == 2:
                if radio2.get() == 0:
                    messagebox.showerror("Error","BELUM MEMILIH JENIS SATUAN YANG AKAN DIKONVERSIKAN")
                elif radio2.get() == 1:
                    result = float((int_temp * 304.8))
                    conv.setUnit("Millimeter")
                elif radio2.get() == 2:
                    result = float((int_temp * 30.48))
                    conv.setUnit("Centimeter")
                elif radio2.get() == 3:
                    result = float((int_temp * 0.3048))
                    conv.setUnit("Meter")
                elif radio2.get() == 4:
                    result = float(int_temp * 0.0003048)
                    conv.setUnit("Kilometer")
            elif radio1.get() == 3:
                if radio2.get() == 0:
                    messagebox.showerror("Error","BELUM MEMILIH JENIS SATUAN YANG AKAN DIKONVERSIKAN")
                elif radio2.get() == 1:
                    result = float((int_temp * 914.4))
                    conv.setUnit("Millimeter")
                elif radio2.get() == 2:
                    result = float((int_temp * 91.44))
                    conv.setUnit("Centimeter")
                elif radio2.get() == 3:
                    result = float((int_temp * 0.9144))
                    conv.setUnit("Meter")
                elif radio2.get() == 4:
                    result = float(int_temp * 0.0009144)
                    conv.setUnit("Kilometer")
            elif radio1.get() == 4:
                if radio2.get() == 0:
                    messagebox.showerror("Error","BELUM MEMILIH JENIS SATUAN YANG AKAN DIKONVERSIKAN")
                elif radio2.get() == 1:
                    result = float((int_temp * 1609340))
                    conv.setUnit("Millimeter")
                elif radio2.get() == 2:
                    result = float((int_temp * 160934))
                    conv.setUnit("Centimeter")
                elif radio2.get() == 3:
                    result = float((int_temp * 1609.34))
                    conv.setUnit("Meter")
                elif radio2.get() == 4:
                    result = float(int_temp * 1.60934)
                    conv.setUnit("Kilometer")
                   

        pesan = "Nilai", "Panjang", "setelah", "dikonversikan", "adalah", result, conv.getUnit()
        messagebox.showinfo("Hasil", pesan)
        
    except:
        messagebox.showerror("Error", "Masukan Tidak Valid, Coba Lagi")


root = Tk()  
root.geometry("600x400")
root.title("Metrik ke Imperial Konverter")

#creating label  
lb_nilai = Label(root, text = "Masukkan Nilai \t:")
lb_nilai.pack()
lb_nilai.place(x = 30,y = 5)
lb_satuan = Label(root, text = "Tentukan konversi yang diinginkan \t:")
lb_satuan.pack()
lb_satuan.place(x = 30, y= 30)

#create input  
num_box = Entry(root)
num_box.pack()
num_box.place(x = 160, y = 5)

#create radio 1
radio1 = IntVar()

R1 = Radiobutton(root, text="Millimeter", variable=radio1, value=1)
R1.pack()
R1.place(x=35, y=50) 
R2 = Radiobutton(root, text="Centimeter", variable=radio1, value=2) 
R2.pack()
R2.place(x=35, y=70)
R3 = Radiobutton(root, text="Meter", variable=radio1, value=3) 
R3.pack()
R3.place(x=35, y=90)
R4 = Radiobutton(root, text="Kilometer", variable=radio1, value=4) 
R4.pack()
R4.place(x=35, y=110)

#create radio 2
radio2 = IntVar()

R5 = Radiobutton(root, text="Inci", variable=radio2, value=1)
R5.pack()
R5.place(x=135, y=50) 
R6 = Radiobutton(root, text="Kaki", variable=radio2, value=2) 
R6.pack()
R6.place(x=135, y=70)
R7 = Radiobutton(root, text="Yard", variable=radio2, value=3) 
R7.pack()
R7.place(x=135, y=90)
R8 = Radiobutton(root, text="Mil", variable=radio2, value=4) 
R8.pack()
R8.place(x=135, y=110)

#create radio 3
radio3 = IntVar()

R9 = Radiobutton(root, text="Metrik ke Imperial", variable=radio3, value=1)
R9.pack()
R9.place(x=235, y=70) 
R9 = Radiobutton(root, text="Imperial ke Metrik", variable=radio3, value=2)
R9.pack()
R9.place(x=235, y=90) 

#create button
btn1 = Button(root, command = convert, text="UBAH").place(x=120,y=150)

root.mainloop()