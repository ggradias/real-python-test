import random

plantilla =" AN {noun1} {noun2} {noun3}"


Nouns = ['fossil','horse','aardvark','judge','chef','mango','extrovert','gorilla']

Verbs = ['kicks','jingles','bounces','slurps','meows','explodes','curdles']

Adjectives = ['furry','balding','incredulous','fragrant','exuberant','glistening']

Prepositions =['against','after','into','beneath','upon','for','in','like','over','within']

Advervs =['curiosly','extragantly','tantalizingly','furiously','sensuously']


def poem(texto):
    sujetos = []
    verbos   = []
    adjetivos = []
    preposiciones = []
    adverbios   =[]
    for i in range (0,3):
        sujetos.append(random.choice(Nouns))
        verbos.append(random.choice(Verbs))
        adjetivos.append(random.choice(Adjectives))
        preposiciones.append(random.choice(Prepositions))
        adverbios.append(random.choice(Advervs))

    print (texto)

    print(adverbios)
    print (texto.format(noun1==sujetos[0], noun2==sujetos[1], noun3==sujetos[2])
                
poem(plantilla)
