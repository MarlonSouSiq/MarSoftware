import tkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Resultado")

label = ctk.CTkLabel(app, text="Jogador 1 venceu!", font=("Arial", 24))
label.pack(expand=True, fill="both")

app.mainloop()
