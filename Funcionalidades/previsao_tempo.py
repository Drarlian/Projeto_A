def recebe_info_tempo():
    """
    Site da API -> https://openweathermap.org
    Documentação da API -> https://openweathermap.org/current#multi
    """
    import requests
    from Visual.interface_simples import interface_simples

    interface_simples('Previsão do tempo')

    API_KEY = "122bf90ee3f151a0eade016bef838296"

    while True:
        try:
            ip = requests.get('https://api.ipify.org').text
            cidade = requests.get('http://ip-api.com/json/' + ip).json()['city']

            link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'

            requisicao = requests.get(link)
            requisicao_dic = requisicao.json()

            descricao = requisicao_dic['weather'][0]['description']
            temperatura = requisicao_dic['main']['temp'] - 273.15
        except:
            print('A cidade informada, não existe no banco de dados.')
        else:
            break

    print(f'{descricao.capitalize()} | {temperatura:.0f}Cº')


if __name__ == '__main__':
    recebe_info_tempo()
