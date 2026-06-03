# importar o módulo pgzrun para rodar o jogo
import pgzrun

# primeiro bloco
quad = Actor('quadrado.png')
quad.pos = 400, 10

# segundo bloco
quad2 = Actor('kaka.jpg')
quad2.pos = 300, 10

# base
base = Actor('base.png')
base.pos = 400, 510

# largura e altura da janela
WIDTH = 800
HEIGHT = 600

# desenhar na tela
def draw():
    screen.clear()
    quad.draw()
    quad2.draw()
    base.draw()

# atualizar posições
def update():
    # bloco 1
    if not quad.colliderect(base):
        quad.top += 10

    # bloco 2
    if not quad2.colliderect(base):
        quad2.top += 10

# executar o jogo
pgzrun.go()
