import wave
import tkinter

audio = wave.open("test4.wav", "rb")

vzorkovacia_frekvencia = audio.getframerate()
print("Vzorkovacia frekvencia: {} Hz".format(vzorkovacia_frekvencia))

pocet_vzoriek = audio.getnframes()
print("Počet vzoriek: {}".format(pocet_vzoriek))

cas_zvuku = pocet_vzoriek/vzorkovacia_frekvencia
print("Dĺžka audia: {} sekúnd".format(cas_zvuku))

kanaly = audio.getnchannels()
print("Počet kanálov: {}".format(kanaly))

bajty = audio.getsampwidth()
print("Počet bajtov na vzorku: {} bajtov".format(bajty))
print("Počet bitov na vzorku: {} bitov".format(bajty*8))

kompresia = audio.getcompname()
print("Typ kompresie: {}".format(kompresia))

vzorky_byte = audio.readframes(pocet_vzoriek)

# ________________________________________________________________

signaly = list()
for i in range(int(len(vzorky_byte)/bajty)):
    signaly.append(int.from_bytes(vzorky_byte[:bajty],
                                  byteorder="little",
                                  signed=True))
    vzorky_byte = vzorky_byte[bajty:]

# ________________________________________________________________

canvas = tkinter.Canvas(height=800, width=800, background="black")
canvas.pack()

canvas.create_line(0, 400, 800, 400, fill="red")

posunutie_x = 800/pocet_vzoriek
velkost_y = 400/(2**(bajty*8)/2)

x = 0
for signal in signaly:
    canvas.create_line(x, 400, x, 400+signal*velkost_y,
                       fill="dark blue")
    x += posunutie_x

canvas.update()
