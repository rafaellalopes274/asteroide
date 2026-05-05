import pygame
import random

pygame.init()

largura =600
altura =400
tamanho_tela=(largura,altura)
tela=pygame.display.set_mode(tamanho_tela)

relogio=pygame. time.Clock()

img_fundo=pygame.image.load("assets/fundo.jpg")
img_fundo=pygame.transform.scale(img_fundo,tamanho_tela)

img_player=pygame.image.load("assets/nave1.png")

player={
    "x":300,
    "y":250,
    "velocidade":5,
    "imagem":pygame.transform.scale(img_player,(50,50))
    
}

img_asteroides=pygame.image.load("assets/asteroides.png")
img_asteroides=pygame.transform.scale(img_asteroides,(50,50))
inimigos=[]
for i in range(3):({
    inimigos.append
        "x":random.randint(0,largura -50),
        "y":random.randint(-300,0),
        "vel":6
        "imagem":img_asteroides
    })


executando_jogo=True
while executando_jogo:
    relogio.tick(60)
    for evento in pygame .event.get():
        if evento.type == pygame.QUIT:
            executando_jogo= False
            
    tela.blit(img_fundo(0,0))
    teclas=pygame.key.get_pressed()
    
    if teclas[pygame.K_LEFT]:
        player["x"]-= player["velocidade"]
    if teclas[pygame.K_RIGHT]:
        player["x"]+= player["velocidade"]
        
    for inimigos in inimigos:
        inimigos["y"]+= inimigos["vel"]
        
        if inimigos["y"] > altura:
            inimigos["y"]=0
            inimigos["x"]=random.randint(0,largura-50)
        tela.blit(inimigos["imagem"],(inimigos["x"]),(inimigos["y"]))
        
    
    tela.blit(player["imagem"],(player["x"],player["y"]))
    
    pygame.display.update()
    
pygame.quit()
