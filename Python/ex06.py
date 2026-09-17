media = input("Digite a média: ")
media = float(media)

arredondar = lambda media: round(media, 2)
media_arredondada = arredondar(media)
print(f"A média arredondada é: {media_arredondada}")