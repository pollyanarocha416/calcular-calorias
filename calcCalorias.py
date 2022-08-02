
calorias = {
    "arroz": 400,
    "pao": 300,
    "salada": 100,
    "molho picante": 100,

}
refeição = ["arroz", "pao", "salada", "molho picante"]

total = 0
for item in refeição:
    total+=calorias[item]
print("Total de calorias na refeição: " + str(total))    