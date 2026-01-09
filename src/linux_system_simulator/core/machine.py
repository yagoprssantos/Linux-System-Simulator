class Machine:
    """
    Classe que representa uma máquina.

    Atributos:
    - machine_type (str): Tipo de máquina.
    - description (str): Descrição da máquina.

    Métodos:
    - Nenhum    
    """

    def __init__(self, machine_type, description):
        """
        Construtor da classe Machine.

        Parâmetros:
        - machine_type (str): Tipo de máquina.
        - description (str): Descrição da máquina.
        """

        self.machine_type = machine_type
        self.description = description