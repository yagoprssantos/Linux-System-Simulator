class Application:
    """
    Classe que representa uma aplicação.

    Atributos:
    - name (str): nome da aplicação.
    - version (str): versão da aplicação.
    - memory_address (None ou int): endereço de memória da aplicação.
    - running (bool): indica se a aplicação está em execução ou não.
    - permissions (dict): dicionário com as permissões da aplicação.

    Métodos:
    - Nenhum.
    """

    def __init__(self, name, version):
        """
        Construtor da classe Application.

        Parâmetros:
        - name (str): nome da aplicação.
        - version (str): versão da aplicação.
        """
        
        self.name = name
        self.version = version
        self.memory_address = None
        self.running = False
        self.permissions = {
            "Leitura": 1,
            "Escrita": 1,
            "Execução": 1            }

