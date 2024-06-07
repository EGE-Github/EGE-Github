import pgzrun

# Pencerenin Çizimi
hucre = Actor("sınır")
hucre1 = Actor('zemin')
hucre2 = Actor("çatlak")
hucre3 = Actor("kemikler")
ekran_g = 9  # Ekranın enindeki hücre sayısı
ekran_y = 10  # Ekranın boyundaki hücre sayısı
WIDTH = hucre.width * ekran_g
HEIGHT = hucre.height * ekran_y
print('Width:', WIDTH)
print('Height:', HEIGHT)
TITLE = "Zindanlar"  # Oyunun Adı
FPS = 60  # Saniyedeki Kare Sayısı

# Harita
haritam = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 1, 2, 1, 3, 1, 1, 0], 
    [0, 1, 1, 1, 2, 1, 1, 1, 0], 
    [0, 1, 3, 2, 1, 1, 3, 1, 0], 
    [0, 1, 1, 1, 1, 3, 1, 1, 0], 
    [0, 1, 1, 3, 1, 1, 2, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1]
]

karakter = Actor("karakter")
karakter.top = hucre.height
karakter.left = hucre.width
karakter.health = 100
karakter.attack = 5

def harita_cizim():
    for i in range(len(haritam)):
        for j in range(len(haritam[0])):
            if haritam[i][j] == 0:
                hucre.left = hucre.width * j
                hucre.top = hucre.height * i
                hucre.draw()
            elif haritam[i][j] == 1:
                hucre1.left = hucre.width * j
                hucre1.top = hucre.height * i
                hucre1.draw()
            elif haritam[i][j] == 2:
                hucre2.left = hucre.width * j
                hucre2.top = hucre.height * i
                hucre2.draw()
            elif haritam[i][j] == 3:
                hucre3.left = hucre.width * j
                hucre3.top = hucre.height * i
                hucre3.draw()

def draw():
    screen.fill("#2f3542")
    harita_cizim()
    karakter.draw()
    screen.draw.text('Sağlık: ' + str(karakter.health), (10, 450), color='white', fontsize=20)
    screen.draw.text('Hücum: ' + str(karakter.attack), (350, 450), color='white', fontsize=20)
def on_key_down(key):
    if (key == keys.RIGHT or key == keys.D) and karakter.x + hucre.width < WIDTH:
        karakter.x += hucre.width
        karakter.image = 'karakter'
    elif (key == keys.LEFT or key == keys.A) and karakter.x - hucre.width >= 0:
        karakter.x -= hucre.width
        karakter.image = 'sol'
    elif (key == keys.DOWN or key == keys.S) and karakter.y + hucre.height < 450:
        karakter.y += hucre.height
    elif (key == keys.UP or key == keys.W) and karakter.y - hucre.height >= 0:
        karakter.y -= hucre.height
pgzrun.go()