from Animal import Animal

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, ukuran):
        super().__init__(nama, makanan, hidup, berkembang_biak),
        self.warna = warna
        self.ukuran = ukuran

    def info_ikan(self):
        super().info_Animal()
        print("Warna \t\t\t :", self.warna,
              "\nUkuran \t\t :", self.ukuran)
        
Ikan_dori = Ikan("Dori", "Plankton", "Air", "Bertelur", "Biru_Hitam", "8_cm")
Ikan_dori.info_ikan()
print("=========================================")
Ikan_cupang = Ikan("Cupang", "Cacing_sutera", "Air", "Bertelur", "Warna_warni", "5_cm")
Ikan_cupang.info_ikan()
