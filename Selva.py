import random
import time

VIDA_MAXIMA = 100
ENERGIA_MAXIMA = 100
PONTUACAO_VITORIA = 50

itens = {
    'agua': {'descricao': 'Água potável', 'vida': 0, 'energia': 10},
    'comida': {'descricao': 'Comida', 'vida': 5, 'energia': 10},
    'corda': {'descricao': 'Corda útil para escalar', 'vida': 0, 'energia': 0},
}

class JogoSelva:
    def __init__(self):
        self.vida = VIDA_MAXIMA
        self.energia = ENERGIA_MAXIMA
        self.pontos = 0
        self.mochila = []
        self.encontrou_saida = False

    def mostrar_status(self):
        print("\n--- Status Atual ---")
        print(f"Vida: {self.vida}/{VIDA_MAXIMA}")
        print(f"Energia: {self.energia}/{ENERGIA_MAXIMA}")
        print(f"Pontos: {self.pontos}")
        print(f"Mochila: {self.mochila}")

    def buscar_comida(self):
        print("\nVocê está buscando comida...")
        if random.choice([True, False]):
            self.mochila.append('comida')
            self.vida = min(self.vida + itens['comida']['vida'], VIDA_MAXIMA)
            self.energia = min(self.energia + itens['comida']['energia'], ENERGIA_MAXIMA)
            self.pontos += 10
            print("Você encontrou comida!")
        else:
            print("Você não conseguiu encontrar comida.")
        self.energia -= 10

    def buscar_agua(self):
        print("\nVocê está buscando água...")
        if random.choice([True, False]):
            self.mochila.append('agua')
            self.energia = min(self.energia + itens['agua']['energia'], ENERGIA_MAXIMA)
            self.pontos += 5
            print("Você encontrou água potável!")
        else:
            print("Você não conseguiu encontrar água.")
        self.energia -= 10

    def buscar_corda(self):
        print("\nVocê está buscando uma corda...")
        if random.choice([True, False]):
            self.mochila.append('corda')
            print("Você encontrou uma corda!")
        else:
            print("Você não conseguiu encontrar uma corda.")
        self.energia -= 10

    def montar_abrigos(self):
        print("\nVocê está montando um abrigo...")
        if 'corda' in self.mochila:
            self.pontos += 20
            print("Você montou um abrigo seguro!")
        else:
            print("Você precisa de uma corda para montar um abrigo.")
        self.energia -= 15

    def enfrentar_perigo(self):
        print("\nVocê encontrou um animal selvagem!")
        acao = input("Você quer (f)ugir ou (e)nfretar? ").lower()
        if acao == 'f':
            if random.choice([True, False]):
                print("Você conseguiu fugir com segurança!")
                self.pontos += 5
            else:
                print("O animal te atacou! Você perdeu 20 de vida.")
                self.vida -= 20
        elif acao == 'e':
            if random.choice([True, False]):
                print("Você assustou o animal e ele fugiu!")
                self.pontos += 10
            else:
                print("O animal te atacou! Você perdeu 20 de vida.")
                self.vida -= 20

    def verificar_resgate(self):
        if self.pontos >= PONTUACAO_VITORIA:
            print("\nParabéns! Você foi encontrado por uma equipe de resgate! Você sobreviveu!")
            self.encontrou_saida = True
        else:
            print("Pontos insuficientes! Colete mais pontos para ser resgatado...")

    def salvar_status(self):
        try:
            with open("status_final.txt", "w", encoding="utf-8") as file:
                file.write("=== STATUS FINAL DO JOGADOR ===\n")
                file.write(f"Vida: {self.vida}/{VIDA_MAXIMA}\n")
                file.write(f"Energia: {self.energia}/{ENERGIA_MAXIMA}\n")
                file.write(f"Pontos: {self.pontos}\n")
                file.write(f"Mochila: {self.mochila}\n")
            print("\nSeu status final foi salvo com sucesso no arquivo 'status_final.txt'.")
        except Exception as e:
            print(f"\nOcorreu um erro ao salvar o arquivo: {e}")

    def comer(self):
        if 'comida' in self.mochila:
         self.mochila.remove('comida')
         vida_ganha = itens['comida']['vida']
         energia_ganha = itens['comida']['energia']
         self.vida = min(self.vida + vida_ganha, VIDA_MAXIMA)
         self.energia = min(self.energia + energia_ganha, ENERGIA_MAXIMA)
         self.pontos += 5
         print(f"\nVocê comeu comida e recuperou {vida_ganha} de vida e {energia_ganha} de energia.")
        else:
         print("\nVocê não tem comida na mochila para comer.")

    def beber(self):
        if 'agua' in self.mochila:
         self.mochila.remove('agua')
         energia_ganha = itens['agua']['energia']
         self.energia = min(self.energia + energia_ganha, ENERGIA_MAXIMA)
         self.pontos += 3
         print(f"\nVocê bebeu água e recuperou {energia_ganha} de energia.")
        else:
         print("\nVocê não tem água na mochila para beber.")


    

def iniciar_jogo_selva():
    jogo = JogoSelva()
    jogo.jogar()

iniciar_jogo_selva()
