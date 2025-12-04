# =======================================
#   Modul Validasi & Input Nilai Siswa
# =======================================

def input_nilai(pesan):
    while True:
        try:
            nilai = float(input(pesan))
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Nilai harus antara 0–100!")
        except ValueError:
            print("Input harus berupa angka!")
