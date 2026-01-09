# Simulador do Sistema Operacional Linux

![Banner](banner.png)

---

## Tabela de Conteúdos

- [Descrição](#descrição)
- [Instalação](#instalação)
- [Uso](#uso)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuindo](#contribuindo)

## Descrição

O Simulador do Sistema Operacional Linux é uma ferramenta educacional abrangente que simula um ambiente Linux simplificado. Ele fornece aos usuários uma experiência prática em trabalhar com componentes de hardware, software e rede em um ambiente simulado e controlado.

Se você é um aspirante a administrador de sistemas, desenvolvedor ou simplesmente curioso sobre como o Linux funciona, este simulador oferece uma maneira segura de explorar e experimentar vários aspectos de um sistema Linux.

## Instalação

Para instalar o simulador, você precisa ter o Python 3.6 ou superior instalado em seu sistema. Você pode baixar o Python no site oficial: <https://www.python.org/downloads/>

Depois de ter o Python instalado, você pode baixar o código-fonte do simulador do repositório do GitHub:

```bash
git clone https://github.com/yagoprssantos/Linux-System-Simulator.git
cd Linux-System-Simulator
```

## Uso

Para executar o simulador, execute o seguinte comando na raiz do projeto:

```bash
python run.py
```

Isso iniciará o simulador e exibirá o menu principal. A partir do menu principal, você pode escolher visualizar informações sobre o hardware, o servidor, a arquitetura de software ou os aplicativos instalados. Você também pode configurar os aplicativos instalados, instalando, desinstalando, iniciando, parando ou gerenciando permissões para eles.

## Funcionalidades

- **Simulação de Hardware**: Experimente as funcionalidades de uma máquina virtual com componentes como CPU, memória e armazenamento.

- **Componentes de Software**: Interaja com um sistema operacional semelhante ao Linux, incluindo kernel e arquitetura de software.

- **Gerenciamento de Pacotes**: Simule um sistema de repositório de software com a capacidade de instalar e desinstalar pacotes.

- **Interface Amigável**: Utilize uma interface intuitiva baseada em menus que torna o sistema acessível a usuários de todos os níveis.

## Estrutura do Projeto

```
Linux-System-Simulator/
├── src/
│   ├── linux_system_simulator/
│   │   ├── core/              # Componentes principais do sistema
│   │   │   ├── __init__.py
│   │   │   ├── application.py    # Classe Application
│   │   │   ├── app_interface.py  # Interface de aplicativos
│   │   │   ├── architecture.py   # Arquitetura de software
│   │   │   ├── hardware.py       # Componentes de hardware
│   │   │   ├── kernel.py         # Kernel Linux
│   │   │   ├── linux_os.py       # Sistema operacional
│   │   │   ├── machine.py        # Classe Machine
│   │   │   ├── package.py        # Pacotes de software
│   │   │   ├── repository.py     # Repositórios
│   │   │   └── server.py         # Servidor
│   │   ├── ui/                # Interface do usuário
│   │   │   ├── __init__.py
│   │   │   └── menus.py          # Menus interativos
│   │   ├── utils/             # Utilitários
│   │   │   ├── __init__.py
│   │   │   ├── loading.py        # Animações de carregamento
│   │   │   ├── refresh.py        # Limpeza de console
│   │   │   └── list.py           # Listagens de informações
│   │   └── __init__.py
│   └── main.py               # Classe principal Output
├── run.py                    # Ponto de entrada do programa
├── setup.py                  # Configuração de instalação
├── .gitignore               # Arquivos ignorados pelo git
└── README.md                # Este arquivo
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

## Contribuindo

Se você deseja contribuir para o projeto, faça um fork do repositório e crie uma solicitação de pull. Certifique-se de seguir as convenções de codificação usadas no projeto e escrever testes para qualquer nova funcionalidade.

---

**Aproveite sua jornada de simulação do Linux!**
