liczba_elementow = int(input("podaj liczbe elementow:"))
suma_wszystkich_kilogramow = 0
waga_paczki = 0
ilosc_paczek = 1
suma_pstych_kilogramow = 0
paczka_z_najwieksza_liczba_pustych_kg = 1
najwiecej_pustych_kilogramów = 0
for liczba_elementow in range(liczba_elementow):
        waga_elementu = float(input("podaj wage elementu :"))
        suma_wszystkich_kilogramow += waga_elementu
        if waga_elementu < 0 or waga_elementu > 10:
                import sys
                sys.exit(0)
        if waga_elementu + waga_paczki < 20 :
                waga_paczki += waga_elementu
        else:
                suma_pstych_kilogramow += (20 - waga_paczki)
                puste_kilogramy_w_tej_paczce = 20 - waga_paczki
                if puste_kilogramy_w_tej_paczce > najwiecej_pustych_kilogramów :
                        paczka_z_najwieksza_liczba_pustych_kg = ilosc_paczek
                        najwiecej_pustych_kilogramów = puste_kilogramy_w_tej_paczce
                waga_paczki = waga_elementu
                ilosc_paczek += 1
puste_kilogramy_w_ostatniej_paczce = 20 - waga_paczki
suma_pstych_kilogramow += (20 - waga_paczki)
if puste_kilogramy_w_ostatniej_paczce > najwiecej_pustych_kilogramów :
        paczka_z_najwieksza_liczba_pustych_kg = ilosc_paczek
        najwiecej_pustych_kilogramów = puste_kilogramy_w_ostatniej_paczce
print(f" Suma wszystkich kilogramow wyslanych to: {suma_wszystkich_kilogramow}")
print(f" ilosc paczek to : {ilosc_paczek}")
print(f" waga pustych kilogramow w paczce to: {suma_pstych_kilogramow}")
print(f"Najmnie kilogramow bylo wyslane w paczce: {paczka_z_najwieksza_liczba_pustych_kg} bylo to: {najwiecej_pustych_kilogramów}")
