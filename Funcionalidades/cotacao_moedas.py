def cotacao_moedas():
    """
    Site da API -> https://docs.awesomeapi.com.br/api-de-moedas
    """
    import requests
    from Visual.interface_simples import interface_simples

    interface_simples('Cotação de moedas')

    while True:
        try:
            moeda = str(input('Digite o código da moeda desejada: ')).upper()

            link = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
            requisicao = requests.get(link)
            dic_requisicao = requisicao.json()
            cotacao = dic_requisicao[f'{moeda}BRL']['bid']
        except:
            print('Código da moeda inválido')
        else:
            break

    print(f'R${cotacao}')



if __name__ == '__main__':
    cotacao_moedas()
