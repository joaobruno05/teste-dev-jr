class Comodo:
    def __init__(self, nome, janelas, portas):
        self.nome = nome
        self.janelas = janelas
        self.portas = portas

    def retornar_se_janelas_par(self):
        if self.janelas % 2 == 0:
            return True


class Casa:
    def __init__(self, endereco, cor, metragem, comodos):
        self.endereco = endereco
        self.cor = cor
        self.metragem = metragem
        self.comodos = comodos


class Mensagem:
    def exibir_mensagem_para_usuario():
        casas = [casa_1, casa_2, casa_3]
        lista_mensagens = set()

        for index in range(len(casas)):
            for comodo in casas[index].comodos:
                if comodo.retornar_se_janelas_par():
                    endereco = casas[index].endereco
                    metragem = casas[index].metragem
                    comodos = casas[index].comodos

                    resposta_1 = f"{endereco} - {metragem}m2 - "
                    resposta_2 = f"{len(comodos)} comodos"
                    resposta_final = resposta_1 + resposta_2

                    lista_mensagens.add(resposta_final)

        return lista_mensagens


# Instancia casa 1
cozinha_1 = Comodo("cozinha", 1, 1)
sala_1 = Comodo("sala", 1, 1)
quarto_1 = Comodo("quarto", 3, 2)
banheiro_1 = Comodo("banheiro", 1, 1)
garagem_1 = Comodo("garagem", 1, 1)

casa_1 = Casa(
    "Rua Naturalista Feijó 280",
    "verde",
    96,
    [cozinha_1, sala_1, quarto_1, banheiro_1, garagem_1],
)

# Instancia casa 2
cozinha_2 = Comodo("cozinha", 1, 1)
sala_2 = Comodo("sala", 3, 1)
quarto_2 = Comodo("quarto", 2, 1)

casa_2 = Casa(
    "Avenida Sargento Hermínio 1200",
    "preta",
    45,
    [cozinha_2, sala_2, quarto_2],
)

# Instancia casa 3
cozinha_3 = Comodo("cozinha", 1, 1)
sala_3 = Comodo("sala", 4, 1)
quarto_3 = Comodo("quarto", 2, 1)
banheiro_3 = Comodo("banheiro", 1, 1)

casa_3 = Casa(
    "Rua Afrânio Peixoto 288",
    "branca",
    70,
    [cozinha_3, sala_3, quarto_3, banheiro_3],
)

print(Mensagem.exibir_mensagem_para_usuario())
