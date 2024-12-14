from Animal import Animal

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, bisa, ukuran):
        super().__init__(nama, makanan, hidup, berkembang_biak),
        self.warna = warna
        self.bisa = bisa
        self.ukuran = ukuran

    def info_ular(self):
        super().info_Animal()
        print("Warna \t\t\t :", self.warna,
              "\nBisa \t\t\t :", self.bisa,
              "\nUkuran \t\t\t :", self.ukuran)
        
ular_cobra = ular("cobra", "tikus", "darat", "bertelur", "hitam", "berbisa", "1,5_meter")
ular_cobra.info_ular()
ular_python = ular("python", "kelinci_domba_burung", "darat", "bertelur", "coklat_kekuningan", "tidak_berbisa", "4_sampai_7_meter")
ular_python.info_ular()



