#LEIAME ODAVAIMA HINNA


from elering_hinnad import tanased_hinnad

# Küsi Eleringist tänased hinnad
hinnad = tanased_hinnad()

# Leia odavaim ja kalleim ajahetk
odavaim_aeg = min(hinnad, key=hinnad.get)
kalleim_aeg = max(hinnad, key=hinnad.get)

odavaim_hind = hinnad[odavaim_aeg]
kalleim_hind = hinnad[kalleim_aeg]

# Loo TXT-fail odavaima hinnaga
with open("odavaim_hind.txt", "w", encoding="utf-8") as fail:
    fail.write("ODAVAIM ELEKTRIHIND\n")
    fail.write(f"Aeg: {odavaim_aeg:%d.%m.%Y %H:%M}\n")
    fail.write(f"Hind: {odavaim_hind:.2f} EUR/MWh\n")

# Loo TXT-fail kalleima hinnaga
with open("kalleim_hind.txt", "w", encoding="utf-8") as fail:
    fail.write("KALLEIM ELEKTRIHIND\n")
    fail.write(f"Aeg: {kalleim_aeg:%d.%m.%Y %H:%M}\n")
    fail.write(f"Hind: {kalleim_hind:.2f} EUR/MWh\n")

print("TXT-failid on edukalt loodud!")
print("Odavaim hind:", odavaim_hind, "EUR/MWh")
print("Kalleim hind:", kalleim_hind, "EUR/MWh")
