import shutil

def write_file(nome_file=0, xt=0):
    file = open(nome_file, 'a')
    file.write('segunda linha')
    file.close()
    
def update_file(nome_file=0, txt=0):
    file = open(nome_file, 'a')
    file.write(txt)
    file.close()
    
def read_file(txt=0):
    file = open(txt, 'r')
    texto = file.read()
    print(texto)
    file.close()
    
    
def copy_file(file):
    shutil.copy(file, '~/Documentos/cursos/python/')    #copia arquivo para outra pasta, basta passar o nome do arquivo que deseja copiar e o respectivo caminho para o local de armazenamento do novo arquivo
    
def move_file(file):
    shutil.move(file, '~Documentos/cursos/python/')     #move o arquivo para outra pasta, basta passar o nome do arquivo que deseja mover e o respectivo caminho para o local de armazenamento do novo arquivo
    
    
def media(arq=0):
    arquivo = open(arq, 'r')
    alunos = arquivo.read()
    alunos = alunos.split('\n')
    print(alunos)
    lista_media = []
    for x in alunos:
        lista_notas = x.split(',')
        alunos = lista_notas[0]
        lista_notas.pop(0)
        print(alunos)
        media = lambda notas: sum([float(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({alunos: media(lista_notas)})
    return lista_media
    
if __name__ == '__main__':
    list_media = media('teste.txt')
    print(list_media)
    