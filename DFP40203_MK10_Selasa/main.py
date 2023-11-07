import glob
import os


def rename_file(nama_lama, nama_baru):
    lokasi_fail = f"../DFP40203_MK10_Selasa/{nama_lama}.txt"
    destinasi_fail = f"../DFP40203_MK10_Selasa/{nama_baru}.txt"
    os.rename(lokasi_fail, destinasi_fail)


def main():
    senarai_fail = glob.glob("../DFP40203_MK10_Selasa/*.txt")
    for nama_fail in senarai_fail:
        print(nama_fail)

    nama_lama = input("masukkan nama lama : ")
    nama_baru = input("masukkan nama baru : ")
    rename_file(nama_lama, nama_baru)

    senarai_fail = glob.glob("../DFP40203_MK10_Selasa/*.txt")
    for nama_fail in senarai_fail:
        print(nama_fail)


if __name__ == '__main__':
    main()
