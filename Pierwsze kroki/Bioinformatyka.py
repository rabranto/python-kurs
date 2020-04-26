"""
Wyobraź sobie, że jesteś bioinformatykiem i otrzymujesz kod genetyczny do analizy.
Kod DNA składa się z 4 zasad azotowych: adeniny(A), cytozyny(D), guaniny(G), tyminy(T).
Idealny kod DNA wygląda następująco: TGCACGATCATGTCTACTATCCTCTCTATGGTGGGGTT.
Zdarza się, jednak, że kod zawiera małe jak i duże litery. Kolejny problem to maszyny
sekwencjonujące nie są wolne od błędów. W zależności od maszyny błędy sekwencjonowania
mogą zostać zamienione na znak – czy literę N.
Skopiuj kod genetyczny do swojego skryptu i zapisz jako DNA = ACTG...
Policz ile razy występuje w kodzie każda zasada azotowa – adenina,cytozyna, guanina, tymina.
Policz wystąpienia sekwencji GAGA i zamień je na AGAG
Policz ile razy w kodzie pojawiła się sekwencja CTGAAA
W sekwencji CTGAAA czasem mutuje ostania litera A, wówczas jakość ostatniej litery może być wątplia.
Ile sekwencji znajdziesz, jeśli weźmiesz pod uwagę wątpliwą, ostatnią adeninę?
Oczyść DNA z wszystkich błędów. Na podstawie czystej nici utwórz odpowiadającą jej nić RNA
(nić RNA w miejscu tyminy będzie mieć uracyl (U))
"""
print("*" * 20)
print("Zadanie 3 - Wyobraź sobie, że jesteś Bioinformatykiem")
print("*" * 20)
DNA = "ACTGTGCTGACTCCCGGTGCTGCCGCTGCCATAGCTAAAGCCCGGGTCCTGGTAGGCAGGCGGGAAGCAG\
GGTGGGGGTCCCGGGTACTGGTAGGGGTAGCCCTGACCCAGAGGCGGGGGGGCAGCCGGGTGGGGCAGCG\
GGGCCAGCGTGTCCTGAA-CGAAGTCCCACTGGAGCCACTGTTGAGGTTCAGGGTGGCGAGATCTGGCGG\
NNNAGGGTAGGTGAGGGCCGCGGAGGGGCCTCCGGCGTTCCCCTCCCCCCCGCCCTGAAACCCGAAGCCC\
CCACTCACTGCTGCAGAGATCCCCTGAAAACGTAGTAGCACTGCTCgagacAGGTGATCTGTTGACCTGA\
AACCGCAGGAAGCCGTGCTTCAGCAAGCTGCTGGCGTACTTCCGGGCCT---GCCGCTCCTTGAAGCCCT\
CCACGTGTGTGTACAGCCAGTCCACCACGTCCGCCCCTGGCCGGCACCAGCGGTCAGCCCGCAGCCTCGA\
GGCAAGCAGCCCTGCCNNTGGCACTATCCGC-CGCGGGGACGGCCACTCACCGATGACGGCATNNGCGAT\
GGTGATCTTGAGCCACATGCGGTCGCGGATCTCCAGTCCCGAG---GGCAGCTGCATGACCCGGACGACG\
GCGCTCATGTCACtcaccgtcagcggcgcctcttccagCCAGCTCTGCAAAGCACAGACAGCCCCGCTTC\
GCCCCAGCATCTGAAAGCGGGGGACTCggcAcgCTGCACCCCCAGGGGAGCCTCTGGGCAGAGCCTGCGC\
CAGGGCGCAAGCTGGACGGTGCGTGACAGCAGGGCCCCGGCCCACTGCAGGATGCACCCCCGTGAGGCTG\
GGGCGTGAGCAGGGGGGTTGGACAtttAGTCTCCCACTTCTACAGACACTTTTCATCAGGATCCTAGGCA\
CAAACTGGGCTGAAACCCCACCCTGCAGACCAGGAAGTAATGAGAACAGGGCAGGCCCCTTCCCCTCNNC\
GCATGCC-CACCCGAGAGCGCAGGCTGTTAGTCGTGTTAATGGCAGGAAGCAGAATGGAGACCTGGCCCC\
TGCCTCTGAA-CCGTGGGTGCTCaactggctaGCCCTACGTACATCCCCTGTTCcggCCAACACACAGAC\
ATGAGCAGGATGGGCTGCACAAGGTGGGCACGGGTGCCTGTGCACACGTCTGTGCAGGGAGTTGGGGACA\
GGCAACACACACGTGTCACAGCCCCATGACGGggcaattgcGCCATGCTGGCTGAATGGCAGAGACGCCC\
CTCCAAGCCTCGGTTTCTGCTGGGGCCCTCAGGAGCTGCCACTTACGTGGAGCACCAGGCACGGAGCTGG\
TTAGTGAGGAGGAGCTGGTGCGCGTGACGGCGCTGGAGCAGGGACTCGTACCGTAGCGGGGCAGGGCNNN\
TGTCAGTGCCGCCGTGTGGtcagcggcgatCGGCG-GGTCGATGGGCCGCACCGGGTCAGCTGGGTGNAG\
ACACGTGGCGATGACAGGCGGACAGATGGACAGGGTGGGAGGGCAGGGTGCAGGGCACAGAGGAGAGAGG\
CCTTCAGGCTAGGTAGGCGCCCCCTCCCCATCCCGccccGTGTGCCCCGAGGGCCACTCACCCCGTGGGA\
CGGTGAAGTAGCTTCG-GGCGTTGGGTCCAGCACTTGGCCACAGTGAGGCTGNAAATGGCTGCAGGAACG\
GTGGTCCCCCCGCAAGGCCCCCATGGTCCCACCTCCCTGCCTGGCCCCTCCCGCTCCAGCGCCNCCAGCC"
DNA = DNA.upper()
DNA = DNA.replace(" ", "")
print("Poniżej znajduje się kod DNA")
print(DNA)
print("Zawartość poszczególnych zasad azotowych w kodzie genetycznym wynosi: ")
adenina = DNA.count("A")
cytozyna = DNA.count("C")
guanina = DNA.count("G")
tymina = DNA.count("T")
print("adenina: {}, cytozyna: {}, guanina: {}, tymina: {}".format(adenina,cytozyna,guanina,tymina))

GAGA = DNA.count("GAGA")
print("Ilość wystąpień sekwencji GAGA: ",GAGA)
DNA = DNA.replace("GAGA", "AGAG")

CTGAAA = DNA.count("CTGAAA")
print("Ilość wystąpień sekwencji CTGAAA: ", CTGAAA)
"""
gdy jakość sekwencji nie pozwala dokładnie odczytać rodzaju zasady azotowej wstawiany jest znak „-”
Natomiast, gdy laser sczytujący ześlizgnie się, wstawiane są litery „N”,
jednocześnie ostatnia wartość zasady jest ponownie odczytywana bez ubytku zasady w tym miejscu.
"""
DNA = DNA.replace("-","")
DNA = DNA.replace("N","")
RNA = DNA.replace("T","U")
print("Oczyszczono DNA ze wszystkich błędów.\nNa podstawie czystej nici utworzono RNA")
print(RNA)
