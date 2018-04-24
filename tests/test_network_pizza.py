# -*- coding: utf-8 -*-
from reteUL.common import Has, Rule, WME
from reteUL.network import Network
from rdflib import Graph


def init_network():
    net = Network()
    c0 = Has('$x', 'http://www.co-ode.org/ontologies/pizza/pizza.owl#hasTopping', '$y')
    c1 = Has('$y', 'http://www.w3.org/2000/01/rdf-schema#subClassOf', 'http://www.co-ode.org/ontologies/pizza/pizza.owl#VegetableTopping')
    net.add_production(Rule(c0, c1))
    return net


def add_wmes():
    net = init_network()
    g = Graph()
    g.load('./pizza.owl')
    for s,p,o in g:
        wme = WME(s,p,o)
        net.add_wme(wme)


def test_init_network(benchmark):
    benchmark(init_network)


def test_add_wmes(benchmark):
    benchmark(add_wmes)
