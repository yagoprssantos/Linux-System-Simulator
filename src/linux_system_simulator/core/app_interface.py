from linux_system_simulator.utils.loading import LoadingAnimation
from linux_system_simulator.utils.refresh import Refresh
from linux_system_simulator.core.application import Application
from linux_system_simulator.core.hardware import Hardware


class ApplicationInterface:
    """
    Classe que representa a interface de aplicativos do sistema.

    Atributos:
    - refresh: objeto da classe Refresh responsável por atualizar a tela da interface
    - installed_apps: lista de objetos da classe Application representando os aplicativos instalados
    - running_apps: lista de strings com os nomes dos aplicativos em execução
    - hardware: objeto da classe Hardware representando o hardware do sistema

    Métodos:
    - AddApplication: adiciona um novo aplicativo à lista de aplicativos instalados
    - RemoveApplication: remove um aplicativo da lista de aplicativos instalados
    - StartApplication: inicia a execução de um aplicativo
    - StopApplication: para a execução de um aplicativo
    - ManagePermissions: gerencia as permissões de um aplicativo
    """

    def __init__(self, hardware):
        """
        Construtor da classe ApplicationInterface.

        Parâmetros:
        - hardware (Hardware): objeto da classe Hardware representando o hardware do sistema
        """

        self.refresh = Refresh()
        self.installed_apps = []
        self.running_apps = []
        self.hardware = hardware


    def AddApplication(self, app_name, app_version):
        """
        Adiciona um novo aplicativo à lista de aplicativos instalados.

        Parâmetros:
        - app_name: string com o nome do aplicativo
        - app_version: string com a versão do aplicativo
        """

        new_app = Application(app_name, app_version)
        self.installed_apps.append(new_app)
        print(f"O aplicativo '{app_name}' foi instalado com sucesso!\n")


    def RemoveApplication(self, app_index):
        """
        Remove um aplicativo da lista de aplicativos instalados.

        Parâmetros:
        - app_index: índice do aplicativo na lista de aplicativos instalados
        """

        app_name = self.installed_apps[app_index].name
        app_version = self.installed_apps[app_index].version
        app = next((app for app in self.installed_apps if app.name == app_name), None)
        if app is None:
            print(f"O aplicativo '{app_name}' não foi encontrado.")
        elif app.running == True:
            print(f"O aplicativo '{app_name}' está em execução.\nPare a execução do aplicativo para poder removê-lo.")
            return
        else:
            print(f"Removendo o aplicativo '{app_name}' (Versão: {app_version})", end='')
            LoadingAnimation(1)
            self.installed_apps.remove(app)
            print(f"\nAplicativo '{app_name}' removido com sucesso!")


    def StartApplication(self, app_index):
        """
        Inicia a execução de um aplicativo.

        Parâmetros:
        - app_index: índice do aplicativo na lista de aplicativos instalados
        """

        app_name = self.installed_apps[app_index].name
        app_version = self.installed_apps[app_index].version
        app = next((app for app in self.installed_apps if app.name == app_name), None)
        if app is None:
            print(f"O aplicativo '{app_name}' não foi encontrado.")
        elif app.permissions["Execução"] == False:
            print(f"O aplicativo '{app_name}' não possui permissão de execução.")
            return
        if app.running == True:
            print(f"O aplicativo '{app_name}' já está em execução.")
        else:
            print(f"Iniciando o aplicativo '{app_name}' (Versão: {app_version})", end='')
            LoadingAnimation(1)
            self.hardware.AllocateMemory(app_name)
            app.running = True
            self.running_apps.append(app_name)
            print(f"\nAplicativo '{app_name}' iniciado com sucesso!")


    def StopApplication(self, app_index):
        """
        Para a execução de um aplicativo.

        Parâmetros:
        - app_index: índice do aplicativo na lista de aplicativos instalados
        """

        app_name = self.installed_apps[app_index].name
        app_version = self.installed_apps[app_index].version
        app = next((app for app in self.installed_apps if app.name == app_name), None)
        if app is None:
            print(f"O aplicativo '{app_name}' não foi encontrado.")
        elif app.running == False:
            print(f"O aplicativo '{app_name}' não está em execução.")
        else:
            print(f"Parando o aplicativo '{app_name}' (Versão: {app_version})", end='')
            LoadingAnimation(1)
            self.hardware.ReleaseMemory(app_name)
            app.running = False
            self.running_apps.remove(app_name)
            print(f"\nAplicativo '{app_name}' parado com sucesso!")


    def ManagePermissions(self, app_index):
        """
        Gerencia as permissões de um aplicativo.

        Parâmetros:
        - app_index: índice do aplicativo na lista de aplicativos instalados
        """

        app = self.installed_apps[app_index]
        permissions = ["Leitura", "Escrita", "Execução"]

        while True:
            self.refresh.Fresh()
            print(f"Permissões para o aplicativo '{app.name}':")
            for permission in permissions:
                print(f"- {permission}: {'Ativa' if app.permissions[permission] else 'Desativada'}")

            print("\nOpções:")
            print("1. Ativar/Desativar permissão de Leitura")
            print("2. Ativar/Desativar permissão de Escrita")
            print("3. Ativar/Desativar permissão de Execução")
            print("4. Voltar ao menu de aplicativos")

            option = input("Escolha uma opção: ")

            if option.isdigit():
                option = int(option)
                if 1 <= option <= len(permissions):
                    permission = permissions[option - 1]
                    app.permissions[permission] = not app.permissions[permission]
                    print(f"Permissão '{permission}' trocada.")
                elif option == 4:
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            else:
                print("Opção inválida. Tente novamente.")
