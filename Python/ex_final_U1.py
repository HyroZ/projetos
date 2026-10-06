def get_grades():
    """Permite ao usuário inserir notas e as armazena em uma lista."""
    grades = []
    while True:
        try:
            num_grades = int(input("Quantas notas você deseja inserir? "))
            if num_grades <= 0:
                print("Por favor, insira um número positivo de notas.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

    for i in range(num_grades):
        while True:
            try:
                grade = float(input(f"Digite a nota {i+1} (0-10): "))
                if 0 <= grade <= 10:
                    grades.append(grade)
                    break
                else:
                    print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número para a nota.")
    return grades

def calculate_average(grades):
    """Calcula a média de uma lista de notas."""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def get_student_status(average):
    """Determina a situação do aluno (Aprovado/Reprovado) com base na média."""
    if average >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def display_report(grades, average, status):
    """Exibe o relatório final com as notas, média e situação do aluno."""
    print("\n--- Relatório Final ---")
    print("Notas inseridas:")
    for i, grade in enumerate(grades):
        print(f"  Nota {i+1}: {grade:.2f}")
    print(f"Média das notas: {average:.2f}")
    print(f"Situação do aluno: {status}")

def main():
    """Função principal que orquestra o sistema de gestão de notas."""
    print("Bem-vindo ao Sistema de Gestão de Notas!")
    grades_list = get_grades()

    if not grades_list:
        print("Nenhuma nota foi inserida. Encerrando o programa.")
        return

    average_grade = calculate_average(grades_list)
    student_status = get_student_status(average_grade)
    display_report(grades_list, average_grade, student_status)

if __name__ == "__main__":
    main()