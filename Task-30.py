список_гласные = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
список_согласные = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]

гласные = 0
согласные = 0

word = input()

for i in word.lower():
    if i in список_согласные:
        согласные +=1
    if i in список_гласные:
        гласные+=1

print(f"Количество гласных {гласные}")
print(f"Количество согласных {согласные}")