class person:
    def __init__(self, nama, umur, gender):
        self.nama = nama 
        self.umur = umur
        self.gender = gender

    def berjalan(self):
        print(f'{self.nama} sedang berjalan')

    def mgomong(self):
        if self.gender == 'pria':
            print (f'{self.nama} tidak bercerita karena dia {self.gender}')
        else:
            print(f'{self.gender} senang bercerita karena dia {self.gender}')
        
class supir(person):
    def __init__(self, nama, umur, gender):
        super().__init__(nama, umur, gender)
        self.sim = sim
    def berkendara(self):
        print(f'{self.nama} sedang berkendara dengan sim {self.sim}')

class mahasiswa(person):
    def __init__(self, nama, umur, gender):
        super().__init__(nama, umur, gender)
        self.nim = nim
    def belajar(self):
        print(f'{self.nama} sedang belajar')

sri = mahasiswa('sri', 17, 'wanita')
sri.belajar()

budi = person('budi', 20, 'pria')
budi.ngomong()

agus = supir('agus', 20, 'berkendara', 'A')
agus.ngomong()
print(agus.sim)
agus.berkendara()

