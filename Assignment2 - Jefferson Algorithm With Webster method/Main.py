from Party import Party
from Country import Country

#Government election simulation for 2022 if Jefferson's algorithm was used using Webster's method
if __name__ == '__main__':
    Likud = Party("Likud",1115336)
    YeshHatid = Party("YeshHatid",847435)
    ZionootDatit = Party("ZionootDatit",516470)
    MahaneMamlahti = Party("MahaneMamlahti",432482)
    Shas = Party("Shas",392964)
    YaadootHatora = Party("YaadootHatora",280194)
    IsraelBeitenoo = Party("IsraelBeitenoo",213687)
    ReshimaHaravit = Party("ReshimaHaravit",194047)
    HadashTahal = Party("HadashTahal",178735)
    Havoda = Party("Havoda",175992)
    
    country = Country()
    country.AddParty(Likud)
    country.AddParty(YeshHatid)
    country.AddParty(ZionootDatit)
    country.AddParty(MahaneMamlahti)
    country.AddParty(Shas)
    country.AddParty(YaadootHatora)
    country.AddParty(IsraelBeitenoo)
    country.AddParty(ReshimaHaravit)
    country.AddParty(HadashTahal)
    country.AddParty(Havoda)

    country.Jefferson_Algorithm()
    country.PrintReasults()