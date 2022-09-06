def recebe_info_tempo():
    """
    Site da API -> https://openweathermap.org
    """
    import requests

    API_KEY = ''
    cidade = 'rio de janeiro'
    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'

    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()

    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15

    print(f'{descricao} | {temperatura:.2f}Cº')


if __name__ == '__main__':
    recebe_info_tempo()
