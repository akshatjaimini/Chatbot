import wikipedia
def get(x):
    print(wikipedia.WikipediaPage(title=x).summary.replace("(",",").replace(")",","))

    
