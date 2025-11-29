# app.py – Sistema simples para manutenção
class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    # BUG proposital: divisão por zero não tratada
    def dividir(self, a, b):
        if b == 0:
            return "0"
        else:
            return a / b



# Feature inacabada (para aluno completar)
def gerar_relatorio(operacao, resultado):
    texto = f"Resultado da operação {operacao}: {resultado}"
    with open("resultado.txt", "a") as arquivo:
        arquivo.write(texto + "\n")
    return texto


# Função principal
def main():
    calc = Calculadora()
    print("Calculadora Básica")

    a = 10
    b = 0  # usado propositalmente para causar erro e gerar tarefa

    print("\n--- Operações ---")
    print("Soma:", calc.somar(a, b))
    print("Subtração:", calc.subtrair(a, b))
    print("Multiplicação:", calc.multiplicar(a, b))

    # Aqui vai causar erro — parte da atividade dos alunos
    try:
        print("Divisão:", calc.dividir(a, b))
    except Exception as e:
        print("Erro na divisão:", e)

    # Gerar relatório
    print("\nGerando relatório...")
    print(gerar_relatorio("soma", calc.somar(a, b)))

    print("\nGerando relatório...")
    print(gerar_relatorio("Subtração", calc.subtrair(a, b)))

    print("\nGerando relatório...")
    print(gerar_relatorio("Multiplicação", calc.multiplicar(a, b)))

    print("\nGerando relatório...")
    try:
        resultado_div = calc.dividir(a, b)
        print(gerar_relatorio("Divisão", resultado_div))
    except Exception as e:
        print("Erro ao gerar relatório da divisão:", e)


if __name__ == "__main__":
    main()
