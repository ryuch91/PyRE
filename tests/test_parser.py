from rdflib import Graph


def test_print_ont():
    # ont = pronto.Ontology('https://protege.stanford.edu/ontologies/pizza/pizza.owl')
    # print(ont.json)
    # result = g.parse('https://protege.stanford.edu/ontologies/pizza/pizza.owl', format="application/rdf+xml")
    g = Graph()
    g.load('./wine.rdf')
    # g.parse(location='./wine.rdf', format='nt')
    for s,p,o in g.triples((None, None, None)):
        print (s,p,o)


if __name__ == "__main__":
    test_print_ont()
