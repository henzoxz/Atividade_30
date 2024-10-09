# crie uma função que calcule a media de 3 notas em seguida verifique se ele está aprovado ou reprovado para notas acima de 7.

def calcula_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media
    
def verificar_resultados(media):
    if media >= 7:
        return 'O Aluno foi Aprovado'
    else:
        return 'O Aluno foi Reprovado'

nota1 = float(input("Digite a 1ª Nota: "))
nota2 = float(input("Digite a 2ª Nota: "))
nota3 = float(input("Digite a 3ª Nota: "))

resultado_media = calcula_media(nota1, nota2, nota3)
print(f"A Média do Aluno é : {resultado_media}")

resultado_final = verificar_resultados(resultado_media)
print(resultado_final)