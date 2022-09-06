def viajar():
    from datetime import datetime
    from geopy.geocoders import Nominatim
    from geopy import distance
    from Visual.interface_simples import interface_simples

    interface_simples('Uber Helicóptero')

    geolocator = Nominatim(user_agent="cebola")
    hora = datetime.now().hour
    partida = str(input("Digite o local de partida: "))
    partida_coord = geolocator.geocode(partida)
    destino = str(input("Digite o local de destino: "))
    destino_coord = geolocator.geocode(destino)
    distancia = float(distance.distance((partida_coord.latitude, partida_coord.longitude),
                                        (destino_coord.latitude, destino_coord.longitude)).km)
    print("A distância da viagem é de: " + str(round(distancia, 2)) + "km")

    if distancia <= 3:
        preco_km = 4
    elif distancia <= 5:
        preco_km = 3.5
    elif distancia <= 7:
        preco_km = 3
    elif distancia <= 10:
        preco_km = 2.5
    else:
        preco_km = 2

    if hora == 17 or hora == 19:

        print("Preços um pouco mais altos que o normal, valor total: R$" + str(round((distancia * preco_km) * 1.2, 2)))

    elif hora == 18:

        print("Preços mais altos que o normal, valor total: R$" + str(round((distancia * preco_km) * 1.5, 2)))

    else:

        print("Valor total: R$" + str(round(distancia * 4, 2)))


if __name__ == '__main__':
    viajar()
