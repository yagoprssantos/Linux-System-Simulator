class Server:
    """
    Classe que fornece serviços a outras máquinas na rede
    
    Atributos:
    - server_type (str): Tipo do servidor.
    - ip_address (str): Endereço IP do servidor.
    - machines (list): Lista de máquinas conectadas ao servidor.

    Métodos:
    - InitializeServer(): Inicializa o servidor.
    - ShutdownServer(): Desliga o servidor.
    """
    
    def __init__(self, server_type, ip_address):
        """
        Construtor da classe Server.

        Parâmetros:
        - server_type (str): Tipo do servidor.
        - ip_address (str): Endereço IP do servidor.
        """
        
        self.server_type = server_type
        self.ip_address = ip_address
        self.machines = []

    def InitializeServer(self):
        """
        Inicializa o servidor
        
        Parâmetros:
        - Nenhum.
        """

        print(f"Servidor {self.server_type} no endereço {self.ip_address} inicializado.")
        

    def ShutdownServer(self):
        """
        Desliga o servidor.
        
        Parâmetros:
        - Nenhum.
        """

        print(f"Servidor {self.server_type} no endereço {self.ip_address} desligado.")
        

    def AddMachine(self, machine):
        """
        Adiciona uma máquina ao servidor
        
        Parâmetros:
        - machine (Machine): Máquina a ser adicionada ao servidor.
        """

        self.machines.append(machine)
        print(f"Máquina adicionada ao servidor no endereço {self.ip_address}.")
        
