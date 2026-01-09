from linux_system_simulator.utils.loading import LoadingAnimation
from linux_system_simulator.ui.menus import MainMenu, HardwareMenu, AppMenu, RepositoryMenu, InfoMenu
from linux_system_simulator.utils.list import List
from linux_system_simulator.utils.refresh import Refresh
from linux_system_simulator.core.hardware import Hardware
from linux_system_simulator.core.architecture import SoftwareArchitecture
from linux_system_simulator.core.server import Server
from linux_system_simulator.core.app_interface import ApplicationInterface
from linux_system_simulator.core.kernel import LinuxKernel, LinuxKernelAPI
from linux_system_simulator.core.linux_os import LinuxOperatingSystem
from linux_system_simulator.core.machine import Machine


"""
Este código representa um simulador interativo de um ambiente do sistema operacional Linux.
Ele oferece funcionalidades simuladas relacionadas a hardware, aplicativos, repositórios,
servidores e informações gerais do sistema, permitindo que o usuário explore e interaja
com diferentes aspectos desse sistema operacional fictício.

No início do código, é possível perceber que todas as variáveis e objetos são inicializados
e instanciados. Isso é feito para que o usuário possa interagir com o sistema operacional
de forma mais dinâmica, sem a necessidade de criar e instanciar objetos a cada interação.
Caso deseja alterar algo, altere os valores das variáveis e objetos nessas instâncias.

Neste projeto, você pode encontrar:

- Análise de Hardware: É possível visualizar informações de hardware, como tipo, modelo,
processador, memória RAM e armazenamento.

- Simulação de Aplicativos:  instalação e remoção de aplicativos em um sistema
operacional, além de funcionalidades como iniciar e encerrar aplicativos, e visualizar
informações de aplicativos.

- Gerenciamento de Pacotes: Simulação de um sistema de repositório de software com a capacidade
de instalar e remover pacotes de software individualmente.

- Servidores: Experimente um servidor web com a capacidade de adicionar e remover máquinas
virtuais, além de visualizar informações de máquinas virtuais.

- Informações do Sistema: Acesse informações gerais do sistema operacional, como versão do
kernel, arquitetura de software e informações de hardware, que podem ser úteis para
desenvolvedores e usuários.

Curiosidades do projeto:
- Este projeto utiliza conceitos de programação orientada a objetos para modelar o ambiente simulado
do sistema operacional Linux, como classes, objetos, herança, polimorfismo e encapsulamento.
- As funcionalidades são simuladas e não realizam operações reais do sistema, proporcionando uma
experiência de usuário fictícia, ou seja, não é possível instalar aplicativos reais ou acessar]
repositórios reais. Então não se preocupe, você não irá quebrar nada!

Agradeço por ler até aqui e explorar este simulador interativo de sistema operacional!

Para acessar o código fonte deste projeto, visite o repositório no GitHub:
[https://github.com/yagoprssantos/Linux-System-Simulator]

"""

class Output:
    def __init__(self):
        self.refresh = Refresh()
        self.lists = List()

        self.hardware = Hardware("Físico", "Samsung", "Intel i7", "16GB", "1TB SSD")
        self.architecture = SoftwareArchitecture("Monolítica", "Arquitetura de software monolítica")
        self.server = Server("Web Server", "192.168.1.1")
        self.app_interface = ApplicationInterface(self.hardware)
        self.kernel = LinuxKernel("5.10.0-8-amd64")

        self.linuxOS = LinuxOperatingSystem("Debian 12", self.kernel, self.architecture, self.hardware)
        self.machine = Machine("Virtual", "VMWare Virtual Machine")
        self.kernel_api = LinuxKernelAPI()

    def Run(self):

        self.refresh.Fresh()

        self.linuxOS.DefaultRepo()
        defaultRepo =  [self.linuxOS.repositories[0], self.linuxOS.repositories[1]]
        self.linuxOS.InstallDistro("Debian", defaultRepo)

        self.linuxOS.StartSystem()

        self.kernel_api.InteractWithKernel()

        self.architecture.DefineComponents()
        self.architecture.DefineIntegrations()

        self.server.InitializeServer()
        self.server.AddMachine(self.machine)


        while True:
            choice = MainMenu().DisplayMenu()
            if choice == 1:
                HardwareMenu(self.hardware, self.app_interface).DisplayMenu()
            elif choice == 2:
                AppMenu(self.app_interface).DisplayMenu()
            elif choice == 3:
                RepositoryMenu(self.linuxOS).DisplayMenu()
            elif choice == 4:
                if InfoMenu(self.hardware, self.server, self.architecture).DisplayMenu():
                    continue
            elif choice == 5:
                self.refresh.Fresh()
                self.linuxOS.ShutdownSystem()
                break


if __name__ == "__main__":
    Output().Run()
