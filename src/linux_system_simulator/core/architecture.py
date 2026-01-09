
from linux_system_simulator.utils.loading import LoadingAnimation

class SoftwareArchitecture:
    """
    Classe que representa a estrutura e integrações dos componentes de software da arquitetura de software do sistema.

    Atributos:
    - software_type (str): tipo da arquitetura de software (monolítica ou microsserviços)
    - description (str): descrição da arquitetura de software
    - components (list): lista de componentes de software
    - integrations (list): lista de integrações de software

    Métodos:
    - DefineComponents: define os componentes de software
    - DefineIntegrations: define as integrações de software
    """

    def __init__(self, software_type, description):
        """
        Construtor da classe SoftwareArchitecture.

        Parâmetros:
        - software_type (str): tipo da arquitetura de software (monolítica ou microsserviços)
        - description (str): descrição da arquitetura de software
        """

        self.software_type = software_type
        self.description = description
        self.components = []
        self.integrations = []


    def DefineComponents(self):
        """
        Define componentes fictícios de software.

        Parâmetros:
        - Nenhum.
        """

        print("Definindo componentes de software", end='')
        LoadingAnimation(1)
        self.components.append("Módulo de Autenticação")
        self.components.append("Serviço de Banco de Dados")
        self.components.append("Biblioteca de Criptografia")
        print("Componentes definidos")


    def DefineIntegrations(self):
        """
        Define integrações fictícias de software.

        Parâmetros:
        - Nenhum.
        """

        print("Definindo integrações de software", end='')
        LoadingAnimation(1)
        self.integrations.append("API REST para Comunicação entre Módulos")
        self.integrations.append("Barramento de Serviço para Integração de Aplicações")
        self.integrations.append("Middleware de Mensageria para Troca de Mensagens")
        print("Integrações definidas")
