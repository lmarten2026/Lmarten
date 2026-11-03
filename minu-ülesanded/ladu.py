import csv

def loe_read(failinimi, kodeering="utf-8"):
    with open(failinimi, encoding=kodeering) as f:
        next(f, none)
        for rida in f:
            yield rida.rstrip("\n")

toodete_arv = 0
toode_rida = []
vanad_mm = {}
otsas_toode = { }

def lisa_toode(nimekiri, toode):
    nimekiri[toode[0]] = {
        'nimetus': toode[1],
        'hind_km_ta': toode[2],
        'laoseis': toode[3],
        'km_maar': toode[4]
    }
    
def kontrolli_eks_toode(nimekiri, toode):
    #kas maks?
    if nimekiri.get("max_t")["hind"] < toode[2]:
      #  lisa_toode()
    #kas min?
for rida in loe_read("tooted.csv"):
    ['inventari_nr;nimetus;hind_km_ta;laoseis;km_maar']
    ['INV-101894;Veebikaamera Lite;60.19;240;22']

    toode_rida = rida.split(";")
    toodete_arv += 1
    vanad_mm[toode_rida[4]] = vanad_mm.get(toode_rida[4], 0) + 1
    
    toode_kogus_int =(toode_rida[3]) #castime? int muutuja
    if toote_kogus_int > 0:
        lisa_toode(otsas_toode, toode_rida)
    

