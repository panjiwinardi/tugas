# =======================================
#         Program Utama
# =======================================

from hitung_nilai import hitung_nilai_akhir
from input_util import input_nilai

def main():
    print("=== Sistem Pengelolaan Nilai Siswa ===")

    nama = input("Nama Siswa: ")
    tugas = input_nilai("Nilai Tugas: ")
    uts = input_nilai("Nilai UTS  : ")
    uas = input_nilai("Nilai UAS  : ")

    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

    print("\n=== HASIL NILAI ===")
    print("Nama         :", nama)
    print("Nilai Akhir  :", nilai_akhir)

if __name__ == "__main__":
    main()