import glob


def main():
    senarai_fail = glob.glob("../DFP40203_MK10_Selasa/*.txt")
    for nama_fail in senarai_fail:
        print(nama_fail)


if __name__ == '__main__':
    main()
