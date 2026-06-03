class Jogador:
    def __init__(self, nome: str, clube: str, posicao: str):
        self.nome = nome
        self.clube = clube
        self.posicao = posicao

    def __str__(self):
        return f"{self.nome} - {self.clube} ({self.posicao})"


class Selecao:
    def __init__(self, nome: str, jogadores: list[Jogador]):
        self.nome = nome
        self.jogadores = jogadores

    def __str__(self):
        lista = ""

        for jogador in self.jogadores:
            lista += str(jogador) + "\n"

        return f"""
Seleção: {self.nome}

Jogadores:
{lista}
"""

j1 = Jogador("Alisson Becker", "Liverpool FC", "Goleiro")
j2 = Jogador("Ederson Moraes", "Fenerbahçe SK", "Goleiro")
j3 = Jogador("Hugo Souza", "Corinthians", "Goleiro")

j4 = Jogador("Matheus Bidu", "Corinthians", "Lateral")
j5 = Jogador("Wesley França", "Roma", "Lateral")
j6 = Jogador("Matheuzinho", "Corinthians", "Lateral")
j7 = Jogador("Douglas Santos", "Zenit", "Lateral")

j8 = Jogador("Bremer", "Juventus", "Zagueiro")
j9 = Jogador("Gabriel Magalhães", "Arsenal", "Zagueiro")
j10 = Jogador("Roger Ibañez", "Al-Ahli", "Zagueiro")
j11 = Jogador("Gustavo Henrique Vernes", "Corinthians", "Zagueiro")
j12 = Jogador("Marquinhos", "Paris Saint-Germain", "Zagueiro")

j13 = Jogador("Bruno Guimarães", "Newcastle United", "Meio-campo")
j14 = Jogador("Casemiro", "Manchester United", "Meio-campo")
j15 = Jogador("Danilo Barbosa", "Botafogo", "Meio-campo")
j16 = Jogador("Fabinho", "Al-Ittihad", "Meio-campo")
j17 = Jogador("Rodrigo Garro", "Corinthians", "Meio-campo")
j18 = Jogador("Kaká", "Milan", "Meio-campo")
j19 = Jogador("Joshua Kimmich", "FC Bayern München", "Meio-campo")

j20 = Jogador("Yuri Alberto", "Corinthians", "Atacante")
j21 = Jogador("Endrick", "Olympique Lyonnais", "Atacante")
j22 = Jogador("Gabriel Martinelli", "Arsenal FC", "Atacante")
j23 = Jogador("Igor Thiago", "Brentford FC", "Atacante")
j24 = Jogador("Luiz Henrique", "FC Zenit Saint Petersburg", "Atacante")
j25 = Jogador("Matheus Cunha", "Manchester United FC", "Atacante")
j26 = Jogador("Neymar", "Santos FC", "Atacante")
j27 = Jogador("Raphinha", "FC Barcelona", "Atacante")
j28 = Jogador("Rayan Vitor", "AFC Bournemouth", "Atacante")
j29 = Jogador("Vinícius Júnior", "Real Madrid CF", "Atacante")
j30 = Jogador("Flavio Caça Rato", "Santa Cruz Futebol Clube", "Atacante")
j31 = Jogador("Ángel Romero", "Corinthians", "Atacantes")
j32 = Jogador("Lamine Yamal", "FC Barcelona", "Atacante")
j33 = Jogador("Pelé","Santos FC", "Atacante")


brasil = Selecao(
    "Brasil",
    [j1, j2, j3,"", j4, j5, j6, j7,"", j8, j9, j10, j11, j12,"", j13, j14, j15, j16, j17, j18, j19,"", j20, j21, j22, j23, j24, j25, j26, j27, j28, j29, j30, j31, j32, j33]
)

print(brasil)
