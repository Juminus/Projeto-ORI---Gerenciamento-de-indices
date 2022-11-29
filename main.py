url = 'Arquivos/ref.txt'
#url = input("URL: ")

numArq = []

dicio_palavra = {}

count_link = 1

with open(url, "r") as f:  

    
    for link in f: 
        link = link.replace("\n", "")
        arq = open(link, 'r')

        for linha in arq:
            for palavra in linha.split():
                palavra = palavra.replace("\n", "")
                palavra = palavra.replace(".", "")
                palavra = palavra.replace(",", "")
                palavra = palavra.replace("!", "")
                palavra = palavra.replace("?", "")
                
                if palavra in dicio_palavra.keys():
                    dicio_palavra[palavra] = {
                        "quaisArq": numArq.__add__(count_link),
                        "qtd": dicio_palavra[palavra]["qtd"]+1
                    }
                else:
                    dicio_palavra[palavra] = {
                        "quaisArq": numArq.append(count_link),
                        "qtd": 1
                    }

        count_link+=1            

    print(dicio_palavra)
