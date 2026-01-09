from linux_system_simulator.utils.loading import LoadingAnimation


class Repository:
    """
    Classe que armazena informações e funções de repositórios

    Atributos:
    - reponame (str): Nome do repositório.
    - address (str): Endereço do repositório.
    - repo_pack_list (list): Lista de pacotes do repositório.

    Métodos:
    - DownloadRepo(): Baixa todos os pacotes do repositório.
    - ListPackages(): Lista todos os pacotes do repositório.
    - InstallPackage(): Instala um pacote do repositório.
    - UninstallPackage(): Desinstala um pacote do repositório.
    """

    def __init__(self, reponame, address):
        """
        Construtor da classe Repository.

        Parâmetros:
        - reponame (str): Nome do repositório.
        - address (str): Endereço do repositório.
        """

        self.reponame = reponame
        self.address = address
        self.repo_pack_list = []


    def DownloadRepo(self):
        """
        Faz o download do repositório.

        Parâmetros:
        - Nenhum.
        """

        print(f"Endereço: {self.address}\nBaixando pacotes do repositório {self.reponame}", end='')
        LoadingAnimation(1)
        print("\n")
        # Faz loop para baixar todos os pacotes do repositório
        for package in self.repo_pack_list:
            package.install()
        print(f"Pacotes do repositório {self.reponame} baixados.\n")


    def ListPackages(self):
        """
        Lista todos os pacotes do repositório.

        Parâmetros:
        - Nenhum.
        """

        print(f"\nPacotes no repositório {self.reponame}:")
        for package in self.repo_pack_list:
            print(f"- {package.packname} // Versão: {package.version} // Instalado: {package.installed}")


    def InstallPackage(self, package_name):
        """
        Instala um pacote pelo nome, se existir no repositório

        Parâmetros:
        - package_name (str): Nome do pacote a ser instalado.
        """

        package = next((p for p in self.repo_pack_list if p.packname == package_name), None)
        if package:
            package.install()
        else:
            print(f"Pacote '{package_name}' não encontrado no repositório {self.reponame}.")


    def UninstallPackage(self, package_name):
        """
        Desinstala um pacote pelo nome, se existir e estiver instalado

        Parâmetros:
        - package_name (str): Nome do pacote a ser desinstalado.
        """

        package = next((p for p in self.repo_pack_list if p.packname == package_name), None)
        if package:
            package.uninstall()
        else:
            print(f"Pacote '{package_name}' não encontrado no repositório {self.reponame}.")
