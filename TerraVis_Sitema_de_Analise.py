# TerraVis - Global Solution - Space Connect
# Disciplina: Differentiated Problem Solving

def calcular_ndvi(mes):
    """
    Modelagem Polinomial: f(x) = -0.015(x - 5.5)^2 + 0.8
    Representa o ciclo de vigor da planta.
    """
    resultado = -0.015 * (mes - 5.5) ** 2 + 0.8
    return resultado


def calcular_risco_queimada(temp):
    """
    Modelagem Exponencial: g(t) = 2.718^(0.15 * (t - 25))
    Representa o crescimento acelerado do risco com a temperatura.
    (Usando 2.718 como aproximação de 'e' para evitar imports)
    """
    expoente = 0.15 * (temp - 25)
    resultado = 2.718 ** expoente
    return resultado


def exibir_menu():
    print("\n" + "=" * 40)
    print("      TERRAVIS - SISTEMA DE ANÁLISE")
    print("=" * 40)
    print("1. Analisar Vigor da Lavoura (NDVI)")
    print("2. Analisar Risco de Queimada")
    print("3. Simulação de Safra Completa")
    print("4. Sair")
    print("=" * 40)


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mes = float(input("Digite o mês da análise (1 para Jan, 12 para Dez): "))
            if 1 <= mes <= 12:
                valor = calcular_ndvi(mes)
                print(f"\n[RESULTADO] O índice NDVI estimado para o mês {mes} é: {valor:.2f}")
                if valor > 0.6:
                    print("Status: Vigor Vegetativo Alto (Pico de Safra)")
                elif valor > 0.4:
                    print("Status: Vigor Vegetativo Médio")
                else:
                    print("Status: Vigor Vegetativo Baixo")
            else:
                print("Erro: O mês deve estar entre 1 e 12.")

        elif opcao == "2":
            temp = float(input("Digite a temperatura atual (°C): "))
            risco = calcular_risco_queimada(temp)

            if risco > 20: risco = 20  # Limite visual para a escala
            porcentagem = (risco / 20) * 100

            print(f"\n[RESULTADO] O fator de risco calculado é: {risco:.2f}")
            print(f"Probabilidade de Incêndio: {porcentagem:.1f}%")

            if porcentagem > 70:
                print("ALERTA: Risco Crítico de Queimada!")
            elif porcentagem > 30:
                print("Aviso: Risco Moderado.")
            else:
                print("Seguro: Risco Baixo.")

        elif opcao == "3":
            print("\n--- Simulação de Safra (12 Meses) ---")
            for m in range(1,13):
                v = calcular_ndvi(m)
                print(f"Mês {m}: NDVI = {v:.2f}")
            print("-------------------------------------")

        elif opcao == "4":
            print("Encerrando o sistema TerraVis. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()