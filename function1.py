# Belajar module

def say_hello(nama):
    print(f"Halo {nama}")

def total(*list_angka):
    hasil = 0
    for data in list_angka:
        hasil = hasil + data
    return hasil