import random

welcome_message = "WELCOME TO CUPY GAMES!"
cupy_position = random.randint(1, 4)

print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama_user = input("masukkan nama kamu: ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4

goa = goa_kosong.copy()
goa[cupy_position - 1] = "|0_0|"

goa_kosong = ' '.join(goa_kosong)
goa = ' '.join(goa)

print(f'''
Halo {nama_user} Coba perhatikan goa dibawah ini {goa_kosong}
''')

pilihan_user = int(input("menurut kamu di goa nomer berapa cupy [1 / 2 / 3 / 4]: "))

confirm_answear = input(f"apakah kamu yakin dengan jawabannya adalah {pilihan_user}? [y/n]: ")

if confirm_answear == "n":
    print("program dihentikan")
    exit()
elif confirm_answear == "y":
    if pilihan_user == cupy_position:
        print(f"{goa} \n Selamat {nama_user} kamu menang")
    else:
        print(f"{goa} \n Maaf {nama_user} kamu kalah")
else:
    print("silahkan ulang programnya")
    exit()
