import schedule
import time
import requests
from client_twitter import api
import random


url = 'https://api.hgbrasil.com/weather?woeid=455975&format=json'


def DrinkWater():
    frases = ['vai beber água vai! quem avisa amigo é viu 💦🚰',
              'ja bebeu agua? não? pois vaitimbora beber agua então abestado! 💦🚰',
              'Beba água, ja bastam as pedras no caminho, não queira ter nos ✨ rins ✨ ',
              'Você não é um cacto, beba água! 💦🚰',]
    text = random.choice(frases)
    print(text)
    try:
        api.update_status(status=text)
    except Exception as e:
        print(e)
        pass

def SayGoodFriday():
    frases_friday = ['"Sexta-feira. Dia de espalhar gentilezas. Dia de falar, sentir, fazer e sorrir. De beber, flertar, olhar e gargalhar. Dia meu. Dia nosso." - Livia Araújo',
                     '"Todo dia é dia de ser Feliz,\nMas hoje você tem um motivo a mais....\nÉ sexta-feira. Feliz sexta-feira!!!" - Rosangela Zorio',
                     '"O ânimo misteriosamente põe fim na canseira quando enfim chega a sexta-feira". - Leandro Cesaroni',
                     '"Sexta-feira! Um dos dias que muitos de nós gostamos, pois é como estar na véspera de uma recompensa." - Edu Lazaro',
                     '"Tenho paixão pelo Sábado, mas meu grande amor é a sexta-feira. - Freitas Branco"']
    text = random.choice(frases_friday)
    print(text)
    try:
        api.update_status(status=text)
    except Exception as e:
        print(e)
        pass


def sayGoodMorning():
    text = 'Bom dia seus lindos! 🌞\nsó os educados respondem. 😊'
    print(text)
    try:
        api.update_status(status=text)
    except Exception as e:
        print(e)
        pass


def sayGoodNight():
    text = 'Boa noite negada! 🌚 \nsó os educados respondem. 😊'
    print(text)
    try:
        api.update_status(status=text)
    except Exception as e:
        print(e)
        pass


def saytimeParnaiba():
    response = requests.get(url)
    city = response.json()['results']['city'].replace(',',' -')
    data = response.json()['results']['date']
    velocidade_vento = response.json()['results']['wind_speedy']
    nascer_sol = response.json()['results']['sunrise']
    por_sol = response.json()['results']['sunset']
    graus = response.json()['results']['temp']
    horario = response.json()['results']['time']
    descricao = response.json()['results']['description']
    
    # text = f'Clima em {city} em {data}\n🕐 Ultima consulta: {horario}\n🌡️ Temperatura: {graus}°C com {descricao}\n🌬️ Velocidade do vento: {velocidade_vento}.\n🌅 Nascer do Sol: {nascer_sol}\n🌇 Por do Sol: {por_sol}'
    text = f'Clima em {city} em {data}\n🕐 Ultima consulta: {horario}\n🌡️ T️emperatura: {graus}°C , {descricao}\n🌬️ Velocidade do vento: {velocidade_vento}.\n🌅 Nascer do Sol: {nascer_sol}\n🌇 Por do Sol: {por_sol}'
    print(text)
    try:
        api.update_status(status=text)
    except Exception as e:
        print(e)
        pass


schedule.every().friday.at("09:00").do(SayGoodFriday)
schedule.every().day.at("08:00").do(sayGoodMorning)
schedule.every().day.at("22:00").do(sayGoodNight)
schedule.every(2).hours.at(":12").do(DrinkWater)
schedule.every().hour.at(":40").do(saytimeParnaiba)

while True:
    schedule.run_pending()
    print('agendando...')
    time.sleep(1)