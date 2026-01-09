from linux_system_simulator.utils.refresh import Refresh
from linux_system_simulator.core.hardware import Hardware
from linux_system_simulator.core.server import Server
from linux_system_simulator.core.architecture import SoftwareArchitecture


class List:
    """
    Classe que representa a lista de informações do sistema.
    Existe excepcionalmente para que o código não fique muito extenso, ou seja, esta função é apenas para organizar o código.

    Atributos:
    - refresh: objeto da classe Refresh responsável por atualizar a tela da interface
    - hardware: objeto da classe Hardware representando o hardware do sistema
    - server: objeto da classe Server representando o servidor do sistema
    - architecture: objeto da classe SoftwareArchitecture representando a arquitetura de software do sistema
    - installed_apps: lista de objetos da classe Package representando os aplicativos instalados no sistema

    Métodos:
    - HardwareInfo: mostra informações sobre o hardware do sistema
    - ServerInfo: mostra informações sobre o servidor do sistema
    - ArchitectureInfo: mostra informações sobre a arquitetura de software do sistema
    - InstalledApps: mostra os aplicativos instalados no sistema
    """

    def __init__(self):
        """
        Construtor da classe List.

        Parâmetros:
        - Nenhum.

        """

        self.refresh = Refresh()

    def HardwareInfo(self, hardware):
        """
        Mostra informações sobre o hardware do sistema.

        Parâmetros:
        - hardware (Hardware): objeto da classe Hardware representando o hardware do sistema
        """

        self.refresh.Fresh()
        self.hardware = hardware

        print("Informações da Máquina:")
        print(f"Tipo: {self.hardware.machine_type}")
        print(f"Descrição: {self.hardware.description}")
        print(f"CPU: {self.hardware.cpu}")
        print(f"Memória: {self.hardware.memory}")
        print(f"Armazenamento: {self.hardware.storage}")
        if input("\nPressione Enter para voltar ao menu...") == '':
            return

    def ServerInfo(self, server):
        """
        Mostra informações sobre o servidor do sistema.

        Parâmetros:
        - server (Server): objeto da classe Server representando o servidor do sistema
        """

        self.refresh.Fresh()
        self.server = server

        print("Informações do servidor:")
        print(f"Tipo: {self.server.server_type}")
        print(f"Endereço IP: {self.server.ip_address}")
        print("Máquinas conectadas:")
        for machine in self.server.machines:
            print(f"- {machine.machine_type}: {machine.description}")
        if input("\nPressione Enter para voltar ao menu...") == '':
            return


    def ArchitectureInfo(self, architecture):
        """
        Mostra informações sobre a arquitetura de software do sistema.

        Parâmetros:
        - architecture (SoftwareArchitecture): objeto da classe SoftwareArchitecture representando a arquitetura de software do sistema
        """

        self.refresh.Fresh()
        self.architecture = architecture

        print("Informações da Arquitetura de Software:")
        print(f"Tipo: {self.architecture.software_type}")
        print(f"Descrição: {self.architecture.description}")
        print("Componentes:")
        for component in self.architecture.components:
            print(f"- {component}")
        print("Integrações:")
        for integration in self.architecture.integrations:
            print(f"- {integration}")
        if input("\nPressione Enter para voltar ao menu...") == '':
            return


    def InstalledApps(self, installed_apps):
        """
        Mostra os aplicativos instalados no sistema.

        Parâmetros:
        - installed_apps (list): lista de objetos da classe Package representando os aplicativos instalados no sistema
        """

        self.refresh.Fresh()
        self.installed_apps = installed_apps


        for index, app in enumerate(self.installed_apps):
            print(f"{index + 1}. {app.name} (Versão: {app.version}, {'Em execução' if app.running else 'Parado'})")
