import os, platform


class Refresh:
    """
    Classe que faz uma limpa no terminal

    Atributos:
    - Nenhum.

    Métodos:
    - Fresh(): Limpa o terminal.
    """

    def Fresh(self):
        """
        Faz uma limpa no terminal.

        Parâmetros:
        - Nenhum.
        """
        
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        print("!! Isto é apenas uma simulação !!\n")

