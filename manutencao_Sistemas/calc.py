# app.py – Sistema simples para manutenção
import math  # Adicionado para suportar a raiz quadrada

class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    # BUG proposital: divisão por zero não tratada
    def dividir(self, a, b):
        return a / b

    # Nova função adicionada
    def raiz_quadrada(self, a):
        # Retorna a raiz quadrada ou None se o número for negativo
        if a < 0:
            return None
        return math.sqrt(a)


# Feature inacabada (para aluno completar)
def gerar_relatorio(operacao, resultado):
    """
    Gera um relatório textual sobre uma operação matemática.
    TODO: adicionar data/hora, nome da operação e salvar em arquivo .txt
    """
    return f"Resultado da operação {operacao}: {resultado}"


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

    # Testando a nova função de raiz quadrada
    print("Raiz Quadrada de a:", calc.raiz_quadrada(a))

    # Aqui vai causar erro — parte da atividade dos alunos
    try:
        print("Divisão:", calc.dividir(a, b))
    except Exception as e:
        print("Erro na divisão:", e)

    # Gerar relatório
    print("\nGerando relatório...")
    print(gerar_relatorio("soma", calc.somar(a, b)))


if __name__ == "__main__":
    main()