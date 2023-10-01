print("Sisteme Kaydolma \n")

sistem_güvenlik_kodu = "2434"

ka = input("Kullanıcı adı: ")
p1 = input("Parola Giriş: ")
p2 = input("Yeniden Parola Giriş: ")

if p1 == p2:
    print("Parola Doğru")
    p = p1
    
else:
    print("Yanlış Parola")
    print("Otomatik parola atandı. Parolanız ==> 159753")
    p = "159753"
    
e_posta = input("E posta: ")
güvenlik_kodu = input("Güvenlik kodu: ")

if güvenlik_kodu == sistem_güvenlik_kodu:
    print("Sisteme giriş yapınız")
else:
    print("Güvenlik kodu yanlış \n\n")



print("Sisteme Giriş")


kullanıcı_adı = input("Kullanıcı adı: ")
parola = input("Parola: ")

if (kullanıcı_adı == ka) and (parola == p):
    print("Hoşgeldiniz.")
    
elif (kullanıcı_adı != ka) and (parola == p):
    print("Kullanıcı adını yanlış girdiniz.")
    
elif (parola != p) and (kullanıcı_adı == ka):
    print("Parolayı yanlış girdiniz.")
    
else:
    print("Hatalı giriş.")