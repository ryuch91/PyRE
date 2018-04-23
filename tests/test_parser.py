import pronto


def test_print_ont():
    ont = pronto.Ontology('https://protege.stanford.edu/ontologies/pizza/pizza.owl')
    print(ont.json)


if __name__ == "__main__":
    print("hello")
    test_print_ont()
