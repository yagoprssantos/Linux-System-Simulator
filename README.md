# Simulador do Sistema Operacional Linux

![Banner](banner.png)

---

## Tabela de Conteúdos

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Instalação](#instalação)
3. [Como Usar](#como-usar)
4. [Funcionalidades](#funcionalidades)
5. [Estrutura do Projeto](#estrutura-do-projeto)

## Sobre o Projeto

O Simulador do Sistema Operacional Linux é uma ferramenta educacional que oferece um ambiente Linux simplificado para aprendizado prático. Permite aos usuários explorar e interagir com componentes de hardware, software e rede de forma segura e controlada. Ideal para estudantes, desenvolvedores e entusiastas que desejam compreender o funcionamento básico de um sistema Linux sem riscos ao ambiente real.

## Instalação

Certifique-se de ter Python 3.6 ou superior instalado: [python.org/downloads](https://www.python.org/downloads)

Clone o repositório e acesse a pasta do projeto:

```bash
git clone https://github.com/yagoprssantos/Linux-System-Simulator.git
cd Linux-System-Simulator
```

## Como Usar

Execute o simulador a partir da raiz do projeto:

```bash
python run.py
```

O menu principal será exibido, permitindo o acesso rápido às funções de simulação de hardware, gerenciamento de software, configuração de aplicativos e visualização de informações do sistema.

## Funcionalidades

- **Simulação de Hardware**: Experimente as funcionalidades de uma máquina virtual com componentes como CPU, memória e armazenamento.

- **Componentes de Software**: Interaja com um sistema operacional semelhante ao Linux, incluindo kernel e arquitetura de software.

- **Gerenciamento de Pacotes**: Simule um sistema de repositório de software com a capacidade de instalar e desinstalar pacotes.

- **Interface Amigável**: Utilize uma interface intuitiva baseada em menus que torna o sistema acessível a usuários de todos os níveis.

## Estrutura do Projeto

```

Linux-System-Simulator/
├── src/
│   └── linux_system_simulator/
│       ├── core/    # Lógica principal: simulação do sistema, kernel, hardware, pacotes e repositórios
│       ├── ui/      # Interface do usuário: menus e navegação
│       └── utils/   # Utilitários: animações, limpeza de console, listagens
├── run.py           # Executa o simulador
├── setup.py         # Instalação e dependências
├── .gitignore       # Exclusões do Git
└── README.md        # Documentação do projeto

```

### Módulos Principais

- **core/**: Contém toda a lógica de negócio e simulação do sistema
  - **linux_os.py**: Sistema operacional Linux simulado com funções de gerenciamento
  - **kernel.py**: API do kernel Linux e suas funcionalidades
  - **hardware.py**: Simulação de componentes de hardware (CPU, memória, armazenamento)
  - **app_interface.py**: Gerenciamento e interface de aplicativos
  - **package.py** e **repository.py**: Sistema de pacotes e repositórios

- **ui/**: Interface do usuário e menus
  - **menus.py**: Menus interativos para navegação

- **utils/**: Utilitários gerais
  - **loading.py**: Animações de carregamento
  - **refresh.py**: Funções de limpeza de console
  - **list.py**: Funções de listagem de informações
  - **list.py**: Funções de listagem de informações
  - **list.py**: Funções de listagem de informações
