#!/usr/bin/env python3
"""
Linux System Simulator - Ponto de entrada principal

Este script executa o simulador de sistema Linux.
Execute-o diretamente com: python run.py
"""

import sys
from pathlib import Path

# Adicionar o diretório src ao path
src_path = Path(__file__).parent / 'src'
sys.path.insert(0, str(src_path))

from main import Output

if __name__ == "__main__":
    Output().Run()
