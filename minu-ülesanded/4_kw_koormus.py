
from elering_hinnad import tanased_hinnad
from datetime import timedelta

# Küsi tänased elektrihinnad
hinnad = tanased_hinnad()

# Sorteeri hinnad aja järgi
ajad = sorted(hinnad.keys())

# Leia odavaim järjestikune 4 tunni periood
intervallide_arv = 16  # 16 x 15 min = 4 tundi

parim_algus = None
parim_keskmine_hind = float("inf")
parim_kogukulu = None

for i in range(len(ajad) - intervallide_arv + 1):
    periood = ajad[i:i + intervallide_arv]

    # Kontrolli, et kõik intervallid oleksid järjestikused
    jarjestikused = all(
        periood[j + 1] - periood[j] == timedelta(minutes=15)
        for j in range(len(periood) - 1)
    )

    if not jarjestikused:
        continue

    # Iga intervalli hind EUR/MWh -> EUR/kWh
    # 1 kW masin kasutab 15 minutiga 0.25 kWh
    kogukulu = sum(hinnad[a] / 1000 * 0.25 for a in periood)

    if kogukulu < parim_keskmine_hind:
        parim_algus = periood[0]
        parim_keskmine_hind = kogukulu
        parim_kogukulu = kogukulu

if parim_algus is not None:
    parim_lopp = parim_algus + timedelta(hours=4)

    with open("soodsaim_4_tundi.txt", "w", encoding="utf-8") as fail:
        fail.write("SOODSAIM 4 TUNNI PERIOOD\n")
        fail.write(f"Algus: {parim_algus:%d.%m.%Y %H:%M}\n")
        fail.write(f"Lopp:  {parim_lopp:%d.%m.%Y %H:%M}\n")
        fail.write("Masina võimsus: 1 kW\n")
        fail.write(f"Elektrikulu: 4 kWh\n")
        fail.write(
            f"Börsielektri maksumus: {parim_kogukulu:.4f} EUR\n"
        )

    print("Leidsin soodsaima 4 tunni perioodi!")
    print("Algus:", parim_algus)
    print("Lõpp:", parim_lopp)
    print(f"Börsielektri maksumus: {parim_kogukulu:.4f} EUR")
else:
    print("Sobivat 4 tunni perioodi ei leitud.")
