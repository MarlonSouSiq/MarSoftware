import tkinter as ctk
import random

# Configuração da janela
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Pedra, Papel e Tesoura")
app.geometry("500x200")

# Função do jogo
def jogar(escolha_jogador):
    opcoes = ["Pedra", "Papel", "Tesoura"]
    escolha_pc = random.choice(opcoes)

    # Determinar resultado
    if escolha_jogador == escolha_pc:
        resultado = "Empate!"
    elif (escolha_jogador == "Pedra" and escolha_pc == "Tesoura") or \
         (escolha_jogador == "Papel" and escolha_pc == "Pedra") or \
         (escolha_jogador == "Tesoura" and escolha_pc == "Papel"):
        resultado = "Você venceu!"
    else:
        resultado = "Computador venceu!"

    # Atualizar texto na tela
    label_resultado.configure(
        text=f"Você: {escolha_jogador}\nComputador: {escolha_pc}\n\n{resultado}"
    )

# Título
titulo = ctk.CTkLabel(app, text="Pedra, Papel e Tesoura", font=("Arial", 28))
titulo.pack(pady=30) # 30 pix abaixo e acim

# Botões
frame_botoes = ctk.CTkFrame(app)
frame_botoes.pack(pady=10)

btn_pedra = ctk.CTkButton(frame_botoes, text="Pedra", width=120,
                          command=lambda: jogar("Pedra"))
btn_pedra.grid(row=0, column=0, padx=10)

btn_papel = ctk.CTkButton(frame_botoes, text="Papel", width=120,
                          command=lambda: jogar("Papel"))
btn_papel.grid(row=0, column=1, padx=10)

btn_tesoura = ctk.CTkButton(frame_botoes, text="Tesoura", width=120,
                            command=lambda: jogar("Tesoura"))
btn_tesoura.grid(row=0, column=2, padx=10)

# Área do resultado
label_resultado = ctk.CTkLabel(app, text="", font=("Arial", 22))
label_resultado.pack(pady=30)

app.mainloop()