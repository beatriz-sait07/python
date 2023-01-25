from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual)#deste jeito ele imprimira AA/MM/DD
    print(data_atual.strftime('%d/%m/%Y'))  #strftime configura para o modelo de sua preferencia
    print(data_atual.strftime('%A %B %Y'))
    
def trabalhando_com_time():
    horario = time(hour=16, minute=54, second=23)
    print(horario)
    
    
def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual.strftime('%d:%m:%y @d/'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    dias = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo', 'Domingo') #tupla de traducao
    print(dias[data_atual.weekday()])
    data_criada = datetime(2018, 8, 15, 17, 45, 20)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2023'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    diminuindo_data = data_convertida - timedelta(days=365, hours=6, minutes=32)
    print(diminuindo_data)
    
if __name__ == '__main__':
    #trabalhando_com_date()                                   
    #trabalhando_com_time()
    trabalhando_com_datetime()