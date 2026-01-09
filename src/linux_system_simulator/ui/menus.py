import os

from linux_system_simulator.core.app_interface import ApplicationInterface
from linux_system_simulator.core.linux_os import LinuxOperatingSystem
from linux_system_simulator.core.machine import Machine
from linux_system_simulator.utils.list import List
from linux_system_simulator.utils.refresh import Refresh
from linux_system_simulator.core.server import Server
from linux_system_simulator.core.repository import Repository

"""
Este arquivo existe excepcionalmente para organizar o código.
"""

class MainMenu:
    """
    Classe que representa o menu principal do sistema.

    Atributos:
    - Nenhum.

    Métodos:
    - DisplayMenu: mostra o menu principal do sistema
    """

    def __init__(self):
        """
        Construtor da classe MainMenu.

        Parâmetros:
        - Nenhum.
        """

        self.refresh = Refresh()


    def DisplayMenu(self):
        """
        Mostra o menu principal do sistema.

        Parâmetros:
        - Nenhum.
        """

        self.refresh.Fresh()
        print("\nMenu Principal:")
        print("1. Analisar Hardware")
        print("2. Aplicativos")
        print("3. Repositórios")
        print("4. Informações")
        print("5. Sair do Linux")
        return int(input("Escolha uma opção: "))


class HardwareMenu:
    """
    Classe que representa o menu de hardware do sistema.

    Atributos:
    - hardware: objeto da classe Hardware representando o hardware do sistema
    - app_interface: objeto da classe ApplicationInterface representando a interface de aplicativos do sistema

    Métodos:
    - DisplayMenu: mostra o menu de hardware do sistema
    """

    def __init__(self, hardware, app_interface):
        """
        Construtor da classe HardwareMenu.

        Parâmetros:
        - hardware (Hardware): objeto da classe Hardware representando o hardware do sistema
        - app_interface (ApplicationInterface): objeto da classe ApplicationInterface representando a interface de aplicativos do sistema
        """

        self.refresh = Refresh()
        self.hardware = hardware
        self.app_interface = app_interface


    def DisplayMenu(self):
        """
        Mostra o menu de hardware do sistema.

        Parâmetros:
        - Nenhum.
        """

        while True:
            self.refresh.Fresh()
            print("\nMenu de Hardware:")
            print("1. Verificar a Saúde")
            print("2. Monitorar uso da CPU")
            print("3. Gerenciar Memória")
            print("4. Voltar para menu principal")
            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                self.hardware.CheckHealth()
                input("\nPressione Enter para continuar...")
            elif choice == 2:
                self.hardware.MonitorCPU(self.app_interface.running_apps)
                input("\nPressione Enter para continuar...")
            elif choice == 3:
                MemoryMenu(self.hardware, self.app_interface).DisplayMenu()
            elif choice == 4:
                break
            else:
                print("Opção inválida. Tente novamente.")


class MemoryMenu:
    """
    Classe que representa o menu de gerenciamento de memória do sistema.

    Atributos:
    - hardware: objeto da classe Hardware representando o hardware do sistema
    - app_interface: objeto da classe ApplicationInterface representando a interface de aplicativos do sistema

    Métodos:
    - DisplayMenu: mostra o menu de gerenciamento de memória do sistema
    """

    def __init__(self, hardware, app_interface):
        """
        Construtor da classe MemoryMenu.

        Parâmetros:
        - hardware (Hardware): objeto da classe Hardware representando o hardware do sistema
        - app_interface (ApplicationInterface): objeto da classe ApplicationInterface representando a interface de aplicativos do sistema
        """

        self.refresh = Refresh()
        self.list = List()
        self.hardware = hardware
        self.app_interface = app_interface


    def DisplayMenu(self):
        """
        Mostra o menu de gerenciamento de memória do sistema.

        Parâmetros:
        - Nenhum.
        """

        while True:
            self.refresh.Fresh()
            print("\nMenu de Gerenciamento de Memória:")
            print("1. Mostrar memórias alocadas")
            print("2. Liberar memória")
            print("3. Voltar ao menu de hardware")
            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                self.hardware.ShowMemoryAllocations()
                input("\nPressione Enter para continuar...")

            elif choice == 2:
                self.refresh.Fresh()
                if self.app_interface.installed_apps:
                    self.list.InstalledApps(self.app_interface.installed_apps)
                    index = int(input("\nDigite o índice do aplicativo para liberar memória: ")) - 1
                    self.app_interface.StopApplication(index)
                    input("Memória liberada.\nPressione Enter para voltar ao menu...")
                else:
                    print("Nenhum aplicativo instalado. ")
                    input("\nPressione Enter para voltar ao menu...")

            elif choice == 3:
                break
            else:
                print("Opção inválida. Tente novamente.")


class AppMenu:
    """
    Classe que representa o menu de aplicativos do sistema.

    Atributos:
    - app_interface: objeto da classe ApplicationInterface representando a interface de aplicativos do sistema

    Métodos:
    - DisplayMenu: mostra o menu de aplicativos do sistema
    """

    def __init__(self, app_interface):
        """
        Construtor da classe AppMenu.

        Parâmetros:
        - app_interface (ApplicationInterface): objeto da classe ApplicationInterface representando a interface de aplicativos do sistema
        """

        self.refresh = Refresh()
        self.list = List()
        self.app_interface = app_interface

    def DisplayMenu(self):
        """
        Mostra o menu de aplicativos do sistema.

        Parâmetros:
        - Nenhum.
        """

        while True:
            self.refresh.Fresh()
            print("\nMenu de Aplicativos:")
            print("1. Listar aplicativos instalados")
            print("2. Configurar aplicativos")
            print("3. Voltar para menu principal")
            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                self.refresh.Fresh()
                if self.app_interface.installed_apps:
                    self.list.InstalledApps(self.app_interface.installed_apps)
                    input("\nPressione Enter para voltar ao menu...")
                else:
                    print("Nenhum aplicativo instalado.")
                    input("\nPressione Enter para voltar ao menu...")

            elif choice == 2:
                ConfigAppMenu(self.app_interface).DisplayMenu()

            elif choice == 3:
                break

            else:
                print("Opção inválida. Tente novamente.")


class ConfigAppMenu:
    """
    Classe que representa o menu de configuração de aplicativos do sistema.

    Atributos:
    - app_interface: objeto da classe ApplicationInterface representando a interface de aplicativos do sistema

    Métodos:
    - DisplayMenu: mostra o menu de configuração de aplicativos do sistema
    """

    def __init__(self, app_interface):
        """
        Construtor da classe ConfigAppMenu.

        Parâmetros:
        - app_interface (ApplicationInterface): objeto da classe ApplicationInterface representando a interface de aplicativos do sistema
        """

        self.refresh = Refresh()
        self.list = List()
        self.app_interface = app_interface

    def DisplayMenu(self):
        """
        Mostra o menu de configuração de aplicativos do sistema.

        Parâmetros:
        - Nenhum.
        """

        while True:
            self.refresh.Fresh()
            print("\nConfigurações de Aplicativos:")
            print("1. Instalar aplicativos")
            print("2. Desinstalar aplicativo")
            print("3. Iniciar aplicativo")
            print("4. Parar aplicativo")
            print("5. Permissões do aplicativo")
            print("6. Voltar para menu de aplicativos")
            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                self.refresh.Fresh()
                while True:
                    app_name = str(input("\nDigite o nome do aplicativo a ser instalado: "))
                    app_version = round(float(input("Digite a versão do aplicativo (float): ")), 1)
                    self.app_interface.AddApplication(app_name, app_version)
                    if input("Deseja adicionar outro aplicativo? (S/N) ").upper() in ["N", "NÃO", "NAO", ""]:
                        break

            elif choice == 2:
                self.refresh.Fresh()
                if self.app_interface.installed_apps:
                    self.list.InstalledApps(self.app_interface.installed_apps)
                    index = int(input("\nDigite o índice do aplicativo a ser desinstalado: ")) - 1
                    self.app_interface.RemoveApplication(index)
                    input("\nPressione Enter para voltar ao menu...")
                else:
                    print("Nenhum aplicativo instalado.")
                    input("\nPressione Enter para voltar ao menu...")

            elif choice == 3:
                self.refresh.Fresh()
                if self.app_interface.installed_apps:
                    self.list.InstalledApps(self.app_interface.installed_apps)
                    index = int(input("\nDigite o índice do aplicativo a ser iniciado: ")) - 1
                    self.app_interface.StartApplication(index)
                    input("\nPressione Enter para voltar ao menu...")
                else:
                    print("Nenhum aplicativo instalado.")
                    input("\nPressione Enter para voltar ao menu...")

            elif choice == 4:
                self.refresh.Fresh()
                if self.app_interface.installed_apps:
                    self.list.InstalledApps(self.app_interface.installed_apps)
                    index = int(input("\nDigite o índice do aplicativo a ser parado: ")) - 1
                    self.app_interface.StopApplication(index)
                    input("\nPressione Enter para voltar ao menu...")
                else:
                    print("Nenhum aplicativo instalado.")
                    input("\nPressione Enter para voltar ao menu...")

            elif choice == 5:
                self.refresh.Fresh()
                if self.app_interface.installed_apps:
                    self.list.InstalledApps(self.app_interface.installed_apps)
                    index = int(input("\nDigite o índice do aplicativo para gerenciar permissões: ")) - 1
                    self.app_interface.ManagePermissions(index)
                else:
                    print("Nenhum aplicativo instalado.")
                    input("\nPressione Enter para voltar ao menu...")

            elif choice == 6:
                break

            else:
                print("Opção inválida. Tente novamente.")

class RepositoryMenu:
    """
    Classe que representa o menu de repositórios do sistema.

    Atributos:
    - linuxOS: objeto da classe LinuxOperatingSystem representando o sistema operacional Linux

    Métodos:
    - DisplayMenu: mostra o menu de repositórios do sistema
    """

    def __init__(self, linuxOS):
        """
        Construtor da classe RepositoryMenu.

        Parâmetros:
        - linuxOS (LinuxOperatingSystem): objeto da classe LinuxOperatingSystem representando o sistema operacional Linux
        """

        self.refresh = Refresh()
        self.repositories = linuxOS.repositories


    def DisplayMenu(self):
        """
        Mostra o menu de repositórios do sistema.

        Parâmetros:
        - Nenhum.
        """

        while True:
            self.refresh.Fresh()
            print("\nMenu de Repositórios:")
            print("1. Listar todos os repositórios e seus pacotes")
            print("2. Configurar pacotes")
            print("3. Voltar para menu principal")
            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                self.refresh.Fresh()
                for reponame in self.repositories:
                    reponame.ListPackages()
                input("Pressione Enter para voltar ao menu...")
            elif choice == 2:
                self.refresh.Fresh()
                print("\nMenu de Repositórios:")
                for i, repo in enumerate(self.repositories, start=1):
                    print(f"{i}. {repo.reponame}")
                print(f"{i+1}. Voltar para menu principal")
                while True:
                    choice = int(input("Escolha uma opção: "))

                    if choice == i+1:
                        break
                    elif choice in range(1, i+1):
                        repository = self.repositories[choice-1]
                        PackageMenu(repository).DisplayMenu()
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
            elif choice == 3:
                break
            else:
                print("Opção inválida. Tente novamente.")

class PackageMenu:
    """
    Classe que representa o menu de pacotes do sistema.

    Atributos:
    - reponame: objeto da classe Repository representando um repositório

    Métodos:
    - DisplayMenu: mostra o menu de pacotes do sistema
    """

    def __init__(self, reponame):
        """
        Construtor da classe PackageMenu.

        Parâmetros:
        - reponame (Repository): objeto da classe Repository representando um repositório
        """

        self.refresh = Refresh()
        self.reponame = reponame

    def DisplayMenu(self):
        """
        Mostra o menu de pacotes do sistema.

        Parâmetros:
        - Nenhum.
        """

        while True:
            self.refresh.Fresh()
            print(f"\nMenu de Pacotes do repositório '{self.reponame.reponame}':")
            print("1. Listar todos os pacotes")
            print("2. Instalar pacotes")
            print("3. Desinstalar pacotes")
            print("4. Voltar para menu de repositórios")
            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                self.refresh.Fresh()
                self.reponame.ListPackages()
                input("Pressione Enter para voltar ao menu...")
                pass
            elif choice == 2:
                while True:
                    self.refresh.Fresh()
                    i = 0
                    print("Pacotes disponíveis:")
                    for package in self.reponame.repo_pack_list:
                        print(f"{i+1}. {package.packname} // Versão: {package.version} // Instalado: {package.installed}")
                        i += 1
                    print(f"{i+1}. Voltar para menu de pacotes\n")
                    choice = int(input("Escolha uma opção: "))
                    print("\n")
                    if choice == i+1:
                        break
                    elif choice in range(1, i+1):
                        self.reponame.InstallPackage(self.reponame.repo_pack_list[choice-1].packname)
                        input("\nPressione Enter para voltar ao menu...")
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
            elif choice == 3:
                self.refresh.Fresh()
                while True:
                    i = 0
                    print("Pacotes disponíveis:")
                    for package in self.reponame.repo_pack_list:
                        print(f"{i+1}. {package.packname} // Versão: {package.version} // Instalado: {package.installed}")
                        i += 1
                    print(f"{i+1}. Voltar para menu de pacotes\n")
                    choice = int(input("Escolha uma opção: "))
                    print("\n")

                    if choice == i+1:
                        break
                    elif choice in range(1, i+1):
                        self.reponame.UninstallPackage(self.reponame.repo_pack_list[choice-1].packname)
                        input("\nPressione Enter para voltar ao menu...")
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
            elif choice == 4:
                return
            else:
                print("Opção inválida. Tente novamente.")


class InfoMenu:
    """
    Classe que representa o menu de informações do sistema.

    Atributos:
    - hardware: objeto da classe Hardware representando o hardware do sistema
    - server: objeto da classe Server representando o servidor do sistema
    - architecture: objeto da classe SoftwareArchitecture representando a arquitetura de software do sistema

    Métodos:
    - DisplayMenu: mostra o menu de informações do sistema
    """

    def __init__(self, hardware, server, architecture):
        """
        Construtor da classe InfoMenu.

        Parâmetros:
        - hardware (Hardware): objeto da classe Hardware representando o hardware do sistema
        - server (Server): objeto da classe Server representando o servidor do sistema
        - architecture (SoftwareArchitecture): objeto da classe SoftwareArchitecture representando a arquitetura de software do sistema
        """

        self.refresh = Refresh()
        self.list = List()
        self.hardware = hardware
        self.server = server
        self.architecture = architecture

    def DisplayMenu(self):
        """
        Mostra o menu de informações do sistema.

        Parâmetros:
        - Nenhum.
        """

        while True:
            self.refresh.Fresh()
            print("\nMenu de Informações:")
            print("1. Máquina")
            print("2. Servidor")
            print("3. Arquitetura de Software")
            print("4. Voltar para menu principal")

            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                self.list.HardwareInfo(self.hardware)
            elif choice == 2:
                self.list.ServerInfo(self.server)
            elif choice == 3:
                self.list.ArchitectureInfo(self.architecture)
            elif choice == 4:
                break
            else:
                print("Opção inválida. Tente novamente.")
