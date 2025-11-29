# app.py – Sistema simples para manutenção

import datetime  # Import necessário para data/hora

class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    # Correção: Tratamento para divisão por zero
    def dividir(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero não é permitida."
        return a / b


# Feature completada: Gera relatório textual com data/hora, nome da operação e salva em arquivo .txt
def gerar_relatorio(operacao, resultado):
    """
    Gera um relatório textual sobre uma operação matemática, incluindo data/hora,
    nome da operação e salva em arquivo lucas.txt.
    """
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    relatorio = f"[{agora}] Resultado da operação '{operacao}': {resultado}\n"
    
    # Salva no arquivo lucas.txt (modo append para não sobrescrever)
    with open("lucas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(relatorio)
    
    return relatorio.strip()  # Retorna o relatório sem a quebra de linha extra


# Função principal
def main():
    calc = Calculadora()
    print("Calculadora Básica")

    a = 10
    b = 0  # Usado para demonstrar tratamento de erro

    print("\n--- Operações ---")
    print("Soma:", calc.somar(a, b))
    print("Subtração:", calc.subtrair(a, b))
    print("Multiplicação:", calc.multiplicar(a, b))

    # Divisão agora tratada corretamente
    print("Divisão:", calc.dividir(a, b))

    # Gerar e salvar relatório para cada operação
    print("\nGerando relatórios...")
    print(gerar_relatorio("soma", calc.somar(a, b)))
    print(gerar_relatorio("subtração", calc.subtrair(a, b)))
    print(gerar_relatorio("multiplicação", calc.multiplicar(a, b)))
    print(gerar_relatorio("divisão", calc.dividir(a, b)))


if __name__ == "__main__":
    main()
