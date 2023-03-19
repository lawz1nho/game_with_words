# Importar módulos

from palavras import palavras
import random

# Seleciona a palavra
def selecionar_palavra():
    palavra = random.choice(palavras)
    return palavra.upper()

# Iniciar o jogo
def jogar(palavra):
    # Definir algumas variáveis
    palavra_a_completar = "_" * len(palavra)
    adivinhou = False
    letras_utilizadas = []
    palavras_utilizadas = []
    tentativas = 6

# Boas vindas ao jogador
    print("Vamos jogar!")
    print(exibir_forca(tentativas))
    print("Esta é a palavra: %s" % palavra_a_completar)

    # Enquanto o usuário não adivinhar e ainda houver tentativas
    while not adivinhou and tentativas > 0:
        tentativa = input("Digite uma palavra ou letrar para continuar: ").upper()

        print(tentativa)
    
        # Tentativa de Letra única
        # Verificar se a tentativa é uma única letra
        if len(tentativa) == 1 and tentativa.isalpha():
            # Verificar se a letra já foi utilizada
            if tentativa in letras_utilizadas:
                print("Você já utilizou esta letra antes: %s" % tentativa)
            # Verificar se a tentativa não está na palavra
            elif tentativa not in palavra:
                print("A letra %s não está na palavra" % tentativa)
                tentativas -= 1
                letras_utilizadas.append(tentativa)
            else:
                print("Você acertou! A letra %s está na palavra" % tentativa)
                letras_utilizadas.append(tentativa)
                # Transformar a palavra em uma lista
                palavra_lista = list(palavra_a_completar)
                
                print(palavra_a_completar)

                # Verifica onde pode substituir o underline baseado na letra que foi passada
                indices = [i for i, letra in enumerate(palavra) if letra == tentativa]
                for indice in indices:
                    palavra_lista[indice] = tentativa

                palavra_a_completar= "".join(palavra_lista)

                print(palavra_a_completar)

                if "_" not in palavra_a_completar:
                    adivinhou = True
        # TENTATIVA DE PALAVRA COMPLETA
        elif len(tentativa) == len(palavra) and tentativa.isalpha():

            # Palavra já utilizada
            if tentativa in palavras_utilizadas:
                print("Você já utilizou esta palavra %s" % tentativa)
            # Palavra está errada
            elif tentativa != palavra:
                print("A palavra %s esta incorreta" % tentativa)
                tentativas -= 1
                palavras_utilizadas.append(tentativa)
            # Acertou a palavra
            else:
                adivinhou = True
                palavra_a_completar = palavra


        # Tentativa inválida
        else:
            print("Tentativa inválida, tente novamente!")

        # Exibir o status do jogo
        print(exibir_forca(tentativas))
        print(palavra_a_completar)


    # Finaliza o jogo se o usuário adivinhou a palavra ou acabaram as tentatvias
    if adivinhou:
        print("Parabéns! Você acertou a palavra")
    else:
        print("Acabaram as tentativas, a palavra era: %s" % palavra)



# Status do jogo
def exibir_forca(tentativas):
    estagios = [  # Fim de jogo
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
              # Falta 1 tentativa
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
              # Faltam 2 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
              # Faltam 3 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,
              # Faltam 4 tentativas
              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
              # Faltam 5 tentativas
              """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
              # Estado inicial
              """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
    ]
    return estagios[tentativas]

# Iniciação do jogo e continuar jogando
def iniciar():
    palavra = selecionar_palavra()
    jogar(palavra)

    # Quanndo acaba o jogo, verifica se o usuário quer continuar jogando
    while input("Jogar novamente? (S/N)").upper() == "S":
        palavra = selecionar_palavra()
        jogar(palavra)

iniciar()
