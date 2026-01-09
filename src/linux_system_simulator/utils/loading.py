import sys, time

def LoadingAnimation(repeat_times=0):
    """
    Função meramente ilustrativa com o intuito de mostrar que o programa está carregando.
    Existe excepcionalmente para que o código fique visualmente mais agradável.
    """
    
    for _ in range(repeat_times):
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(1)

        sys.stdout.write("\b\b\b   \b\b\b")  
        sys.stdout.flush()
        time.sleep(0.5)

    sys.stdout.write("...\n")
