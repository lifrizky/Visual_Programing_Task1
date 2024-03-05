class Myclass:
    def __init__(self, nama="", kelas="", prodi="", fakultas="", tempat_tinggal="", asal=""):
        self.bio1 = nama
        self.bio2 = kelas
        self.bio3 = prodi
        self.bio4 = fakultas
        self.bio5 = tempat_tinggal
        self.bio6 = asal

while True:
    print("")
    print("Selamat Datang di Program Sederhana Biodata")
    print("===============================================")
    input_user = input("Masukkan Data Anda (Nama, Kelas, Prodi, Fakultas, Tempat tinggal, Asal) :")
    strings = input_user.split(", ")
    print("===============================================")
    user1 = Myclass(*strings)
    print("")
    print("Biodoata User")
    print("===============================================")
    print("Nama             :", user1.bio1)
    print("Kelas            :", user1.bio2)
    print("Prodi            :", user1.bio3)
    print("Fakultas         :", user1.bio4)
    print("Tempat Tinggal   :", user1.bio5)
    print("Asal             :", user1.bio6)
    print("===============================================")
    ulangi = input("Apakah ingin mengulang proses input biodata? (ya/tidak)").lower()
    if ulangi != 'ya':
        break