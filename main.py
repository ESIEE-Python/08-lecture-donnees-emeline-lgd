"""
08-lecture doonnées
"""
#### Imports et définition des variables globales


FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename,mode= 'r', encoding='utf8') as f:
        l = f.readlines()
        t=[]
        for i in range (len(l)):
            li=[int(x) for x in l[i][:-1].split(";")]
            t.append(li)
    return t

def get_list_k(data, k):
    """
    fonction qui retourne le k-ième element
    """
    return data[k]

def get_first(l):
    """
    retournne le premier element
    """
    return l[0]

def get_last(l):
    """
    retournne le dernier element
    """
    return l[-1]

def get_max(l):
    """
    retournne le max element d'une liste
    """
    return int(max(l))

def get_min(l):
    """
    retournne le min element d'une liste
    """
    return int(min(l))

def get_sum(l):
    """
    retournne la somme des elements d'une liste
    """
    return int(sum(l))


#### Fonction principale


def main():
    """
    fonction principale qui test les fonctions secondaires
    """
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
