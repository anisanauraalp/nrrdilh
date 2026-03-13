import random

print("=== Game Tebak Angka ===")
print("Saya sudah memilih angka antara 1 sampai 100.")
print("Coba tebak angkanya!")

angka_rahasia = random.randint(1, 100)
percobaan = 0

while True:
    tebakan = int(input("Masukkan tebakanmu: "))
    percobaan += 1

    if tebakan < angka_rahasia:
        print("Terlalu kecil! Coba lagi.")
    elif tebakan > angka_rahasia:
        print("Terlalu besar! Coba lagi.")
    else:
        print(f"Selamat! Kamu menebak dengan benar dalam {percobaan} percobaan.")
        break
    