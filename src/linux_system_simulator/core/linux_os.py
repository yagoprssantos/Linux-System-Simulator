import random

from linux_system_simulator.utils.loading import LoadingAnimation
from linux_system_simulator.core.kernel import LinuxKernel
from linux_system_simulator.core.architecture import SoftwareArchitecture
from linux_system_simulator.core.package import Package
from linux_system_simulator.core.hardware import Hardware


class LinuxOperatingSystem:
    """
    Classe que representa o sistema operacional Linux.

    Atributos:
    - version (str): versão do sistema operacional Linux
    - kernel (LinuxKernel): objeto da classe LinuxKernel representando o Kernel do Linux
    - architecture (SoftwareArchitecture): objeto da classe SoftwareArchitecture representando a arquitetura de software do sistema
    - hardware (Hardware): objeto da classe Hardware representando o hardware do sistema
    - repositories (list): lista de objetos da classe Repository representando os repositórios de pacotes do sistema

    Métodos:
    - DefaultRepo: define um repositório padrão para o sistema
    - InstallDistro: instala uma distribuição Linux
    - StartSystem: inicia o sistema operacional Linux
    - ShutdownSystem: desliga o sistema operacional Linux
    """

    def __init__(self, version, kernel, architecture, hardware):
        """
        Construtor da classe LinuxOperatingSystem.

        Parâmetros:
        - version (str): versão do sistema operacional Linux
        - kernel (LinuxKernel): objeto da classe LinuxKernel representando o Kernel do Linux
        - architecture (SoftwareArchitecture): objeto da classe SoftwareArchitecture representando a arquitetura de software do sistema
        - hardware (Hardware): objeto da classe Hardware representando o hardware do sistema
        """

        self.version = version
        self.kernel = kernel
        self.architecture = architecture
        self.hardware = hardware
        self.repositories = []


    def DefaultRepo(self):
        """
        Define um repositório padrão para o sistema.

        Parâmetros:
        - Nenhum.
        """

        from linux_system_simulator.core.repository import Repository
        repo_data = [
        ("Debian Repository 1", "http://debian-repo1.com"),
        ("Debian Repository 2", "http://debian-repo2.com"),
        ("Debian Repository 3", "http://debian-repo3.com")
        ]
        for i in range(len(repo_data)):
            repo_name, repo_url = repo_data[i]
            repo = Repository(repo_name, repo_url)
            for _ in range(3):
                pack_name = f"Package-{random.randint(1, 100)}"
                pack_version = round(random.uniform(1.0, 12.0), 1)
                repo.repo_pack_list.append(Package(repo_name, repo_url, pack_name, pack_version))
            self.repositories.append(repo)


    def InstallDistro(self, name, defaultRepo=None):
        """
        Instala uma distribuição Linux.

        Parâmetros:
        - name (str): nome da distribuição
        - defaultRepo (list): lista de objetos da classe Repository representando os repositórios de pacotes padrão da distribuição
        """

        print(f"Instalando distribuição {name}", end='')
        LoadingAnimation(1)
        print()

        if defaultRepo is None:
            defaultRepo = self.repositories

        for repository in defaultRepo:
            repository.DownloadRepo()


    def StartSystem(self):
        """
        Inicia o sistema operacional Linux, simbolizando o boot do sistema.

        Parâmetros:
        - Nenhum.
        """

        print("Ligando o Sistema Linux", end='')
        LoadingAnimation(1)
        self.kernel.InitializeKernel()
        print("Sistema Linux ligado.")


    def ShutdownSystem(self):
        """
        Desliga o sistema operacional Linux, simbolizando o shutdown do sistema.

        Parâmetros:
        - Nenhum.
        """

        print("Desligando o Sistema Linux", end='')
        LoadingAnimation(1)
        self.kernel.ShutdownKernel()
        print("Sistema Linux desligado.")
