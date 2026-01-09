from linux_system_simulator.utils.loading import LoadingAnimation


class LinuxKernel:
    """
    Classe que representa o Kernel do Linux responsável pelo gerenciamento de hardware, recursos do sistema e interação com dispositivos.

    Atributos:
    - version (str): versão do Kernel do Linux
    - devices (list): lista de dispositivos gerenciados pelo Kernel do Linux

    Métodos:
    - InitializeKernel: inicializa o Kernel do Linux
    - ShutdownKernel: desliga o Kernel do Linux
    """

    def __init__(self, version):
        """
        Construtor da classe LinuxKernel.

        Parâmetros:
        - version (str): versão do Kernel do Linux
        """

        self.version = version
        self.devices = [
            "CPU1", "CPU2", "CPU3", "CPU4",
            "RAM1",
            "SSD1",
            "PlacaDeRedeEthernet", "AdaptadorWiFi",
            "Teclado", "Mouse",
            "PlacaDeVideo", "Monitor",
            "PlacaDeSom", "DispositivoDeAudio",
            "Touchpad",
            "SistemaDeArquivos",
            "Temporizadores", "RelogioDoSistema",
            "DispositivoDeCriptografia", "DispositivoDeSeguranca", "DispositivoDeVirtualizacao",
            "FonteDeEnergia"
        ]


    def InitializeKernel(self):
        """
        Inicializa o Kernel do Linux.

        Parâmetros:
        - Nenhum.
        """

        print("Inicializando o Kernel Linux", end='')
        LoadingAnimation(1)
        print(f"Kernel Linux {self.version} inicializado com sucesso.")


    def ShutdownKernel(self):
        """
        Desliga o Kernel do Linux.

        Parâmetros:
        - Nenhum.
        """

        print("Desligando o Kernel Linux", end='')
        LoadingAnimation(1)
        print(f"Kernel Linux {self.version} desligado.")



class LinuxKernelAPI:
    """
    Classe que fornece uma interface estável para os programas interagirem com o Kernel do Linux.

    Atributos:
    - Nenhum.

    Métodos:
    - InteractWithKernel: interage com o Kernel do Linux
    """

    def InteractWithKernel(self):
        """
        Interage com o Kernel do Linux, simbolizando a interação de um programa com o Kernel do Linux.
        """

        print("Interagindo com o Kernel do Linux", end='')
        LoadingAnimation(1)
