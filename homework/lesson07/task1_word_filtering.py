slowa = ["jabłko", "banan", "kiwi", "gruszka", "truskawka"]

# dlugie_slowa = [slowa[i] for i in range(len(slowa)) if len(slowa[i]) > 5]
slowa_przefiltrowane = [slowo for slowo in slowa if len(slowo) > 5]
print(slowa_przefiltrowane)