import customtkinter as ctk

#configuração da aparencia
ctk.set_appearance_mode('dark')


# Criação ds funções de funcionalidadess
def validar_login():
    usuario=campo_usuario.get()  # get pega o resultado dentro do campo usuario
    senha=campo_senha.get()     # get pega o resultado dentro do campo senha

    if usuario=="Marlon" and senha=='1234':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
    else: 
        resultado_login.configure(text='Login com erro!', text_color='red')  
                                  



# criação da janela principal
app=ctk.CTk()
app.title("Sistema de Login")
app.geometry('300x300')

#criação dos campos
#label
label_usuario=ctk.CTkLabel(app,text='Usuário', font=("Arial", 26))
label_usuario.pack(pady=10)   # espaçamento de 10 pixels para cima a paa baixo
#entry
campo_usuario =ctk.CTkEntry(app, placeholder_text='Digite o seu usuário')
campo_usuario.pack(pady=10)

label_senha=ctk.CTkLabel(app,text='Senha', font=("Arial", 26))
label_senha.pack(pady=10)   # espaçamento de 10 pixels para cima a paa baixo
#entry
campo_senha =ctk.CTkEntry(app, placeholder_text='Digite a sua senha')
campo_senha.pack(pady=10)

#Button
botao_login=ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)

#campo feedback de login
resultado_login=ctk.CTkLabel(app,text='') # texto invisivel, no if muda para um texto
resultado_login.pack(pady=10)


app.mainloop()