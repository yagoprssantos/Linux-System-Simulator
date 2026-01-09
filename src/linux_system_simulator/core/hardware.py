import random

from linux_system_simulator.utils.loading import LoadingAnimation
from linux_system_simulator.core.kernel import LinuxKernelAPI
from linux_system_simulator.core.machine import Machine
from linux_system_simulator.utils.refresh import Refresh


class Hardware(Machine):
    """
    Classe que representa os componentes de hardware de uma máquina.

    Atributos:
    - machine_type (str): tipo da máquina (físico ou virtual)
    - description (str): descrição da máquina
    - cpu (str): modelo da CPU
    - memory (str): quantidade de memória RAM
    - storage (str): capacidade de armazenamento em disco
    - cpu_usage (int): uso atual da CPU em porcentagem
    - memory_allocations (dict): dicionário com os aplicativos e seus endereços de memória alocados

    Métodos:
    - CheckHealth: verifica o estado de saúde dos componentes de hardware
    - MonitorCPU: monitora o uso da CPU
    - ShowMemoryAllocations: mostra as memórias alocadas e seus endereços
    - AllocateMemory: aloca memória para um aplicativo
    - ReleaseMemory: libera memória de um aplicativo

    """

    def __init__(self, machine_type, description, cpu, memory, storage):
        """
        Construtor da classe Hardware.

        Parâmetros:
        - machine_type (str): tipo da máquina (físico ou virtual)
        - description (str): descrição da máquina
        - cpu (str): modelo da CPU
        - memory (str): quantidade de memória RAM
        - storage (str): capacidade de armazenamento em disco
        """

        super().__init__(machine_type, description)
        self.refresh = Refresh()
        self.kernel = LinuxKernelAPI()
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.cpu_usage = random.randint(28, 36)
        self.memory_allocations = {}


    def CheckHealth(self):
        """
        Verifica o estado de saúde dos componentes de hardware.

        Parâmetros:
        - Nenhum.
        """

        self.refresh.Fresh()
        print("Verificando integridade dos componentes de hardware", end='')
        LoadingAnimation(1)
        self.kernel.InteractWithKernel()
        health_list = ["Péssimo", "Ruim", "Ok", "Bom", "Ótimo"]
        print(f"Saúde do hardware: {random.choice(health_list)}!")


    def MonitorCPU(self, running_apps):
        """
        Monitora o uso da CPU.

        Parâmetros:
        - running_apps (list): lista de objetos App em execução
        """

        self.refresh.Fresh()
        print("Monitorando o uso da CPU", end='')
        LoadingAnimation(1)
        self.kernel.InteractWithKernel()
        if len(running_apps) == 0:
            self.cpu_usage = random.randint(28, 36)
        else:
            self.cpu_usage = min(50 + 10 * (len(running_apps) - 1), 100)  # CPU aumenta com base no número de aplicativos em execução.
        print(f"Uso da CPU: {self.cpu_usage}%")


    def ShowMemoryAllocations(self):
        """
        Mostra as memórias alocadas e seus endereços.

        Parâmetros:
        - Nenhum.
        """

        self.refresh.Fresh()
        print("Memórias alocadas:")
        for app_name, memory_address in self.memory_allocations.items():
            print(f"- '{app_name}': {memory_address}")


    def AllocateMemory(self, app_name):
        """
        Aloca memória para um aplicativo.

        Parâmetros:
        - app_name (str): nome do aplicativo
        """

        if app_name not in self.memory_allocations:
            memory_address = "0x" + ''.join(random.choice('0123456789ABCDEF') for _ in range(8))
            self.memory_allocations[app_name] = memory_address
            print(f"Memória alocada para '{app_name}' no endereço {memory_address}")
        else:
            print(f"'{app_name}' já possui alocação de memória")


    def ReleaseMemory(self, app_name):
        """
        Libera memória de um aplicativo.

        Parâmetros:
        - app_name (str): nome do aplicativo
        """

        if app_name in self.memory_allocations:
            del self.memory_allocations[app_name]
            print(f"Memória liberada de '{app_name}'")
        else:
            print(f"Não há alocação de memória para '{app_name}'")
