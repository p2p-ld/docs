```{index} RDF
```
# RDF and Friends

RDF is one of the elephants in the room when it comes to triplet graphs and linked data. Its history is complex and torrid, known as hopelessly and aggressively complex or a divine calling, depending on your disposition.

**p2p-ld does not necessarily seek to be an RDF-based p2p protocol,** though strategizing for interoperability with RDF and RDF-derivative formats would be nice.

One of the primary challenges to using RDF-like formats is the conflation of URLs and URIs as the primary identifiers for schema and objects. This idea (roughly) maps onto the "neat" characterization of linked data where everything should have ideally one canonical representation, and there should be a handful of "correct" general-purpose schema capable of modeling the world. 

We depart from that vision, instead favoring radical vernacularism {cite}`saundersSurveillanceGraphs2023`. URIs are extremely general, and include decentralized identifiers like {index}`multiaddrs <IPFS; Multiaddr>`

## RDF And Friends

RDF has a lot of formats and 

```{index} JSON-LD
```
### JSON-LD




## Challenges

### Tabular and Array Data

```{important}
See https://www.cs.ox.ac.uk/isg/challenges/sem-tab/
```

The edges from a node in a graph are unordered, which makes array and tabular data difficult to work with in RDF!

This has been approached in a few ways:

**RDF** uses a [godforsaken `rdf:first` `rdf:rest` linked list syntax](https://www.w3.org/TR/rdf12-schema/#ch_collectionvocab)

eg. one would express `MyList` which contains the `Friends` `["Arnold", "Bob", "Carly"]` in (longhand) turtle as

```turtle
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix : <https://example.com> .

:MyList :Friends :list1 . 

:list1
	rdf:first :Amy ;
	rdf:rest :list2 .

:list2
	rdf:first :Bob ;
	rdf:rest :list3 .

:list3
	rdf:first :Carly ;
	rdf:rest rdf:nil .
```

And thankfully turtle has a shorthand, which isn't so bad:

```turtle
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix : <https://example.com> .

:MyList
	:Friends (
		:Amy
		:Bob
		:Carly
	).
```

Both of these correspond to the triplet graph:

```{mermaid}
flowchart LR
	MyList
	list1
	list2
	list3
	nil
	Amy
	Bob
	Carly
	
	MyList -->|Friends| list1
	list1 -->|rest| list2
	list2 -->|rest| list3
	list3 -->|rest| nil
	list1 -->|first| Amy
	list2 -->|first| Bob
	list3 -->|first| Carly
```

Which is not great.

**{index}`JSON-LD`** uses a `@list` keyword:

```jsonld
{
  "@context": {"foaf": "http://xmlns.com/foaf/0.1/"},
  "@id": "http://example.org/people#joebob",
  "foaf:nick": {
    "@list": [ "joe", "bob", "jaybee" ]
  },
}
``` 

which can be expanded recursively to [mimic arrays](https://www.w3.org/TR/json-ld11/#example-84-coordinates-expressed-in-json-ld)

`````{tab-set}
````{tab-item} JSON-LD
```jsonld
{
  "@context": {
    "@vocab": "https://purl.org/geojson/vocab#",
    "coordinates": {"@container": "@list"}
  },
  "geometry": {
    "coordinates": [
        [
            [-10.0, -10.0],
            [10.0, -10.0],
            [10.0, 10.0],
            [-10.0, -10.0]
        ]
    ]
  }
}
```
````
````{tab-item} Turtle
```turtle
@prefix geojson: <https://purl.org/geojson/vocab#>.

[
  a geojson:Feature ;
  geojson:bbox (-10 -10 10 10) ;
  geojson:geometry [
    a geojson:Polygon ;
    geojson:coordinates (
      (
        (-10 -10)
        (10 -10)
        (10 10)
        (-10 -10)
      )
    )
  ]
] .
```
````
`````

### Naming

- All names have to be global. Relative names must resolve to a global name via contexts/prefixes. The alternative is blank nodes, which are treated as equivalent in eg. graph merges. Probably here enters pattern matching or whatever those things are called.
- Blank nodes and skolemization https://www.w3.org/TR/rdf11-mt/#skolemization-informative


## References

- [RDF 1.1 Primer](https://www.w3.org/TR/rdf11-primer/)
- W3C Recommendation on generating RDF from tabular data: {cite}`tandyGeneratingRDFTabular2015`
- {index}`JSON Schema` in RDF: {cite}`charpenayJSONSchemaRDF2023`
- [Turtle](https://www.w3.org/TR/rdf12-turtle/)
- [N-ary relations in RDF](https://www.w3.org/TR/swbp-n-aryRelations/)
- [RDF 1.1 Semantics](https://www.w3.org/TR/rdf11-mt/)

### Libraries

- [jsonld.js](https://github.com/digitalbazaar/jsonld.js)
- [rdf-canonize-native](https://github.com/digitalbazaar/rdf-canonize-native)
- [biolink-model](https://github.com/biolink/biolink-model) for a nice example of generating multiple schema formats from a .yaml file.
- [linkml](https://linkml.io/) - modeling language for linked data {cite}`moxonLinkedDataModeling2021`
	- Multidimensional arrays in linkml https://linkml.io/linkml/howtos/multidimensional-arrays.html
- [oaklib](https://incatools.github.io/ontology-access-kit/index.html) - python package for managing ontologies
- [rdflib](https://github.com/RDFLib/rdflib) - maybe the canonical python rdf library

### See Also

- [HYDRA vocabulary](https://www.hydra-cg.com/spec/latest/core/) - Linked Data plus REST
- [CORAL](https://github.com/jmchandonia/CORAL)