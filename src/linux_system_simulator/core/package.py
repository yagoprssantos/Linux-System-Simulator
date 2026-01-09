from linux_system_simulator.utils.loading import LoadingAnimation
from linux_system_simulator.core.repository import Repository


class Package(Repository):
    """
    Classe que representa um pacote de software instalável.

    Atributos:
    - reponame (str): Nome do repositório de onde o pacote foi baixado.
    - packname (str): Nome do pacote de software.
    - version (str): Versão do pacote de software.
    - installed (bool): Indica se o pacote está instalado ou não.

    Métodos:
    - install(): Instala o pacote de software.
    - uninstall(): Desinstala o pacote de software.
    """

    def __init__(self, reponame, address, packname, version):
        """
        Construtor da classe Package.

        Parâmetros:
        - reponame (str): Nome do repositório de onde o pacote foi baixado.
        - packname (str): Nome do pacote de software.
        - version (str): Versão do pacote de software.
        """

        super().__init__(reponame, address)
        self.reponame = reponame
        self.packname = packname
        self.version = version
        self.installed = False


    def install(self):
        """
        Instala o pacote de software.

        Parâmetros:
        - Nenhum.
        """

        if not self.installed:
            print(f"Instalando {self.packname} (Versão: {self.version}) do repositório {self.reponame}", end='')
            LoadingAnimation(1)
            self.installed = True
            print(f"Pacote {self.packname} (Versão: {self.version}) do repositório {self.reponame} instalado.\n")
        else:
            print(f"Pacote {self.packname} (Versão: {self.version}) do repositório {self.reponame} já está instalado.\n")


    def uninstall(self):
        """
        Desinstala o pacote de software

        Parâmetros:
        - Nenhum.
        """

        if self.installed:
            print(f"Desinstalando {self.packname} (Versão: {self.version}) do repositório {self.reponame}", end='')
            LoadingAnimation(1)

            self.installed = False
            print(f"Pacote {self.packname} (Versão: {self.version}) do repositório {self.reponame} desinstalado.")
        else:
            print(f"Pacote {self.packname} (Versão: {self.version}) do repositório {self.reponame} não está instalado.")
