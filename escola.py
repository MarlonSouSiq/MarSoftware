idade=int(input("Entre com a sua idade: "))
# if idade <16:
#     status="VOCÊ NÃO PODE VOTAR"
# if idade == 16 or idade ==17 or idade >= 60:
#     status="SEU VOLTO É OPCIONAL"
# if idade>=18 or idade<60:
#     status="SEU VOTO É OBRIGATORIO"

# print(f"{status}")

if idade < 16:
    status="VOCÊ NÃO PODE VOTAR"
elif idade ==16 or idade ==17 or idade >=60:
    status="SEU VOTO É OPICIONAL"
else:
    status="SEU VOTO É OBRIGATÓRIO"
print(f"{status}")




