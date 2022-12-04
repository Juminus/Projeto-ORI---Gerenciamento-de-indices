def main():
    url = input("Caminho do arquivo conjuntos: ")
    descon = input("Caminho do arquivo desconsideradas: ")     #Recebe os caminhos dos arquivos
    consu = input("Caminho do arquivo consulta: ")          

    dic = geraDicDosArq(url, descon) #Gera um dicionário com as informações sobra as palavras contidas nos textos
    consulta(dic, consu, url) #Busca nos textos as palavras contidas no arquivo consulta 



def geraDicDosArq(url, descon):
    with open(url, "r") as f:  #Abre o arquivo dos conjuntos
        lista_arq = [] #Declara uma lista
        count_arq = 0 #Declara um contador
        for link in f:  #Para cada caminho contido em conjuntos
            palavras = {} #Declara ou esvazia o conteúdo do dicionário
            link = link.replace('\n', '') #Tira o '\n' do final de cada linha
            arquivos = open(link, 'r') #Abre o arquivo do caminho (a.txt, b.txt, c.txt, etc...)

            for linhas in arquivos.readlines(): #Para cada linha contida no arquivo
                for word in linhas.split(): #Para cada palavra contida no arquivo
                    word = tratar_texto(word, descon) #Remove as pontuações e retira as palavras desconsideradas

                    if word != '': #Se a palavra for diferente de ''(vazio)
                        if word in palavras.keys(): #Se a palavra já estiver no dicionário
                            palavras[word] += 1 #Incrementa um na quantidade de aparições
                        else: 
                            palavras[word] = 1 #Se não estiver no dicionário, é a primeira aparição dela
            
            lista_arq.append(palavras.copy()) #Ao final de cada arquivo, adiciona o dicionário em um vetor da lista
            count_arq+=1 #Incrementa um na 'posição' do arquivo aberto
    return geraIndice(lista_arq)



def tratar_texto(word, descon):
    word = word.replace('\n', '')
    word = word.replace('.', '')
    word = word.replace(',', '')    #Substitui cada pontuação e '\n' por ''(vazio)
    word = word.replace('!', '')
    word = word.replace('?', '')

    with open(descon, 'r') as desc: #Abre o arquivo com as palavras que devem ser desconsideradas
        for i in desc.readlines(): #Para cada palavra no arquivo
            i = i.replace('\n', '') #Remove o '\n'
            if word == i: #Se a palavra desconsiderada for igual a palavra 
                return '' #Substitui por ''(vazio)
        return word



def geraIndice(lista_arq):
    dicFinal = {} #Declara um dicionário
    count_arq = 1 #Declara um contador da posição do arquivo
    for arq in lista_arq: #Para cada palavra na lista com as palavras dos arquivos
        for elemento, valor in arq.items(): #Para cada palavra e quantidade de aparições
            if elemento in dicFinal.keys(): #Se a palavra já estiver no dicionário
                dicFinal[elemento] = dicFinal[elemento] + f' {count_arq},{valor}' #Adiciona na string qual arquivo ela apareceu e quantas vezes
            else:
                dicFinal[elemento] = f'{count_arq},{valor}' #Se  não estiver no dicionário, adiciona em qual arquivo e quantas vezes ela apareceu primeiro
        count_arq+=1 #Incrementa a posição do arquivo

    with open('Saidas/indice.txt', 'w') as indice: #Cria o arquivo índice
        for elemento, valor in sorted(dicFinal.items()): #Ordena e adiciona as palavras, em qual arquivo e quantas vezes apareceu
            indice.write(f'{elemento}: {valor}\n')

    return dicFinal

def consulta(dic, consu, url):
    list = [] #Declara uma lista
    count_cons = 0 #Declara um contador para a quantidade de palavras a serem consultadas
    with open(consu, 'r') as consult: #Abre o arquivo de consulta
        for linhas in consult.readlines(): #Para cada linha no arquivo de consulta
            for palavras in linhas.split(): #Para cada palavra a ser consultada
                count_cons += 1 #Incrementa um na quantidade de palavras a serem consultadas
                if palavras in dic.keys(): #Se a palavra a ser consultada estiver no dicionário
                    for arq in dic[palavras].split(): #Para cada arquivo que a palavra apareceu
                        list.append(arq[0]) #Adiciona o arquivo na lista
                        
    list_unicos = set(list) #Declara uma lista sem repetir os arquivos
    list_f = [] #Declara uma lista vazia
    for elemento in list_unicos: #Para cada arquivo com as palavras consultada 
        if list.count(elemento) == count_cons: #Compara a quantidade de palavras encontradas, se for igual a quantidade de palavras no arquivo consultado
            list_f.append(elemento) #Adiciona o arquivo na lista
    links = [] #Declara uma lista
    with open(url, 'r') as f: #Abre o arquivo com os caminhos de cada texto
        count_link = 1 #Declara um contador da posição do arquivo aberto
        for link in f: #Para cada caminho
            if str(count_link) in list_f: #Se a posição do contador, estiver na lista com o resultado da consulta
                links.append(link) #Salva o endereço do arquivo na lista
            count_link += 1 #Incrementa a posição do arquivo aberto
        
    with open('Saidas/resposta.txt', 'w') as resposta: #Cria um arquivo resposta
        resposta.write(f'{len(links)} \n') #Escreve a quantidade de arquivos que possuem a consulta
        for elemento in links:
            resposta.write(elemento) #Escreve o caminho dos arquivos



main() #Chama a main