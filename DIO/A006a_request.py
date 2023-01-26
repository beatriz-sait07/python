import requests

def dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/22041001/json/')
    print(response.status_code)
    print(response.text) #imprime o texto da pagina
    print(type(response.json())) #retorna jum dicionario com os dados do cep
    dados_cep1 = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep1
    
def dados_pokemon(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    dados_pokemon1 = response.json()
    return dados_pokemon1

def response(url): #leitura de pagina *inspecionar*
    resp = requests.get(url)
    return resp.text
    
if __name__ == '__main__':
    #dados_cep('22041001')
    #dados_pokemon_main = dados_pokemon('pikachu')
    #print(dados_pokemon_main['sprites']['front_shiny'])
    rep = response('https://globallabs.academy/')
    print(rep)