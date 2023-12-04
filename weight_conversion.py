def weight_conversion():
    berat = int(input("masukkan berat anda > "))
    satuan = input("dalam satuan apa berat yang anda masukkan? (K untuk KG, L untuk LBS)> ")

    if satuan.lower()== 'l':
        print (f"berat anda dikonversi menjadi kilogram adalah {round(berat * 0.4535)} kg ")
    elif satuan.lower() == 'k':
        print(f"berat anda dikonversi menjadi pons adalah {round(berat * 2.20462)} lbs")