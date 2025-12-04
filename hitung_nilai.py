# =======================================
#     Modul Perhitungan Nilai Siswa
# =======================================

def hitung_nilai_akhir(tugas, uts, uas):
    """Menghitung nilai akhir berdasarkan bobot:
       tugas 30%, UTS 30%, UAS 40%"""
    return (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
