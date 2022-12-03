def main():
    url = 'Arquivos/conjuntos.txt'
    #url = input("Caminho do arquivo conjuntos: ")
    consu = 'Arquivos/consulta.txt'
    #consu = input("Caminho do arquivo consulta: ")
    descon = 'Arquivos/desconsideradas.txt'
    #descon = input("Caminho do arquivo desconsideradas: ")
    dic = geraListaDosArq(url, descon)
    consulta(dic, consu, url)



def geraListaDosArq(url, descon):
    with open(url, "r") as f:  
        lista_arq = []
        count_arq = 0
        for link in f:
            palavras = {}
            link = link.replace('\n', '')
            arquivos = open(link, 'r')
            for linhas in arquivos.readlines():
                linhas = tratar_texto(linhas, descon)
                for word in linhas.split():

                    if word != '':
                        if word in palavras.keys():
                            palavras[word] += 1
                        else:
                            palavras[word] = 1
            
            lista_arq.append(palavras.copy())         
            count_arq+=1
    return geraIndice(lista_arq)



def tratar_texto(word, descon):
    word = word.replace('\n', '')
    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.replace('!', '')
    word = word.replace('?', '')

    with open(descon, 'r') as desc:
        execoes = desc.readlines()
        for i in execoes:
            i = i.replace('\n', '')
            if word == i:
                return ''
        return word



def geraIndice(lista_arq):
    dicFinal = {}
    count = 1
    for arq in lista_arq:
        for elemento, valor in arq.items():
            if elemento in dicFinal.keys():
                dicFinal[elemento] = dicFinal[elemento] + f' {count},{valor}'
            else:
                dicFinal[elemento] = f'{count},{valor}'
        count+=1

    with open('Saidas/indice.txt', 'w') as indice:
        for elemento, valor in sorted(dicFinal.items()):
            indice.write(f'{elemento}: {valor}\n')

    return dicFinal

def consulta(dic, consu, url):
    list = []
    count_cons = 0
    with open(consu, 'r') as consult:
        for linhas in consult.readlines():
            for palavras in linhas.split():
                count_cons += 1
                if palavras in dic.keys():
                    test = dic[palavras].split()
                    for letra in test:
                        list.append(letra[0])
    list_unicos = set(list)
    list_f = []
    for elemento in list_unicos:
        if list.count(elemento) == count_cons:
            list_f.append(elemento)
    links = []
    with open(url, 'r') as f:
        count_link = 1
        for link in f:
            if str(count_link) in list_f:
                links.append(link)
            count_link += 1
        
    with open('Saidas/resposta.txt', 'w') as resposta:
        resposta.write(f'{len(links)} \n')
        for elemento in links:
            resposta.write(elemento)

main()