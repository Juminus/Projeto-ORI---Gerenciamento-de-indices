def main():
    url = 'Arquivos/conjuntos.txt'
    #url = input("URL: ")
    geraListaDosArq(url)



def geraListaDosArq(url):
    with open(url, "r") as f:  
        lista_arq = []
        count_arq = 0

        for link in f:
            palavras = {}
            link = link.replace('\n', '')
            arquivos = open(link, 'r')
            
            for linhas in arquivos.readlines():
                for word in linhas.split():
                    word = tratar_texto(word)

                    if word != '':
                        if word in palavras.keys():
                            palavras[word] += 1
                        else:
                            palavras[word] = 1
            
            lista_arq.append(palavras.copy())         
            count_arq+=1
    geraIndice(lista_arq)



def tratar_texto(word):
    word = word.replace('\n', '')
    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.replace('!', '')
    word = word.replace('?', '')

    with open('Arquivos/desconsideradas.txt', 'r') as desc:
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



def consulta():
    with open('Arquivos/consulta.txt', 'r') as consult:
        for linha in consult.readlines():
            for palavra in linha.split():
                palavra = tratar_texto(palavra)


consulta()