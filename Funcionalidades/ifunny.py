def ifunny():
    """
    Site da API -> https://imgflip.com/api
    """
    import requests
    import webbrowser as wb
    from random import choice, shuffle
    from Visual.interface_simples import interface_simples

    interface_simples('Ifunny Base')

    link = 'https://api.imgflip.com/get_memes'
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    memes = requisicao_dic['data']['memes']
    shuffle(memes)
    meme_aleatorio = choice(memes)['url']

    # print(meme_aleatorio)

    wb.open(meme_aleatorio)


if __name__ == '__main__':
    ifunny()
