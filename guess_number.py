def guess_number():
    secret_number = 9
    guess = 0
    guess_limit = 3

    while guess < guess_limit:
        user = int(input("Maukkan angka > "))
        if user == secret_number:
            print ("selamat, anda berhasil menemukan angkanya")
            break
        else:
            print ("salah!")
            guess +=1
    else:
        print(f"anda tidak menemukan angkanya, angka rahasianya adalah {secret_number}")