def comida():
    import json
    import random

    from geopy.geocoders import Nominatim
    from geopy import distance

    geolocator = Nominatim(user_agent="cebola")
    while True:
        try:
            entrega = str(input("Digite o local para a entrega: "))
            entrega_coord = (geolocator.geocode(entrega).latitude, geolocator.geocode(entrega).longitude)
            break
        except:
            print("Endereço inválido")
    print("Procurando os restaurantes próximos a você...")
    with open('restaurante.json', encoding="utf8") as file:
        restaurantes = json.load(file)
        restaurantes_perto = []
        for x in restaurantes:
            r = geolocator.geocode(x['address'])
            distancia = float(distance.distance(entrega_coord, (r.latitude, r.longitude)).km)
            if distancia <= 25:
                restaurantes_perto.append(x['name'].upper())
        if len(restaurantes_perto) == 0:
            print("Nenhum restaurante disponível na sua região")
        else:
            print("Restaurantes próximos: " + ', '.join(restaurantes_perto))
            while True:
                escolha = str(input("Escolha um restaurante: "))
                if escolha.upper() in restaurantes_perto:
                    break
                else:
                    print("Restaurante inválido, tente novamente")
            conta = random.randint(10, 200)
            print("Sua conta deu R$" + str(conta))
            print("Pagamento na entrega! Obrigado por usar iFode!")


if __name__ == '__main__':
    comida()
