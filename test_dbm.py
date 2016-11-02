import dbm

# una manera sencilla de almcenaar datos es utilizar DBM como unix


articulo =  [
              
              ['1','Gradias','Gilberto','31/03/1967'],
              ['2','Gradias','Alexa','21/03/2002'],
              ['3','Santacruz','Dora','07/04/1975']
            ]


def createDB(data, dbName):
    try:
        db = dbm.open(dbName, 'c')
        for datum in data:
            db[datum[0]] = ','.join(datum)
    finally:
        db.close()
        print(dbName, 'created')


def readDB(dbName):
    try:
        db = dbm.open(dbName,'r')
        print('Reading ',dbName)
        return [ db[datum]for  datum in db]
    finally:
        db.close()


def main():
    print ('crando archivo de datos:')
    createDB(articulo,'articuloDB')
    print('los articulos que se almacenaron son:')
    print(readDB('articuloDB'))


if __name__ == "__main__": main()