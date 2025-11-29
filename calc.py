import datetime

# app.py – Sistema simples para manutenção

class Calculadora:
    # 1. MELHORIA: Uso de @staticmethod, pois os métodos não dependem do estado da instância (self)
    @staticmethod
    def somar(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtrair(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiplicar(a: float, b: float) -> float:
        return a * b

    # 2. MELHORIA: Tratamento de Erro de Divisão (Robustez)
    @staticmethod
    def dividir(a: float, b: float) -> float:
        if b == 0:
            # Lança a exceção específica, permitindo que o chamador trate a condição de forma limpa.
            raise ZeroDivisionError("Erro: Não é possível dividir por zero.")
        return a / b


# 3. MELHORIA: Função gerar_relatorio completa
def gerar_relatorio(operacao: str, expressao: str, resultado: float | str, nome_arquivo="relatorio_calculadora.txt"):
    """
    Gera um relatório textual sobre uma operação matemática e o salva em arquivo .txt.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    conteudo = (
        f"--- Relatório de Operação ---\n"
        f"Data/Hora: {timestamp}\n"
        f"Operação: {operacao}\n"
        f"Expressão: {expressao}\n"
        f"Resultado: {resultado}\n"
        f"-----------------------------\n\n"
    )

    try:
        # Abre o arquivo em modo 'a' (append/anexar) para não sobrescrever operações anteriores
        with open(nome_arquivo, "a") as f:
            f.write(conteudo)
        return f"Relatório salvo em '{nome_arquivo}'."
    except Exception as e:
        return f"Erro ao salvar o relatório: {e}"


# Função principal
def main():
    # A instância 'calc' ainda é usada, mas agora chama métodos estáticos
    # Uma instância não é estritamente necessária após a refatoração.
    # No entanto, vamos mantê-la para mostrar a sintaxe de chamada.
    calc = Calculadora() 
    print("Calculadora Básica Refatorada")

    a = 10
    b = 0  # Mantido propositalmente para testar o tratamento de erro

    print("\n--- Operações ---")
    
    # Soma
    soma_res = calc.somar(a, b)
    print("Soma:", soma_res)
    gerar_relatorio("Soma", f"{a} + {b}", soma_res)
    
    # Subtração
    sub_res = calc.subtrair(a, b)
    print("Subtração:", sub_res)
    gerar_relatorio("Subtração", f"{a} - {b}", sub_res)
    
    # Multiplicação
    mult_res = calc.multiplicar(a, b)
    print("Multiplicação:", mult_res)
    gerar_relatorio("Multiplicação", f"{a} * {b}", mult_res)

    # Divisão (Testando o Erro Tratado)
    print("\nTestando Divisão por Zero...")
    try:
        div_res = calc.dividir(a, b)
        print("Divisão:", div_res)
        gerar_relatorio("Divisão", f"{a} / {b}", div_res)
    except ZeroDivisionError as e:
        erro_msg = str(e) # Captura a mensagem de erro específica
        print(erro_msg)
        # Salva a mensagem de erro no relatório
        print(gerar_relatorio("Divisão", f"{a} / {b}", erro_msg))


if __name__ == "__main__":
    main()