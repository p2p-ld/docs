```{index} RDF
```
# RDF and Friends

RDF is one of the elephants in the room when it comes to triplet graphs and linked data. Its history is complex and torrid, known as hopelessly and aggressively complex or a divine calling, depending on your disposition.

**p2p-ld does not necessarily seek to be an RDF-based p2p protocol,** though strategizing for interoperability with RDF and RDF-derivative formats would be nice.

One of the primary challenges to using RDF-like formats is the conflation of URLs and URIs as the primary identifiers for schema and objects. This idea (roughly) maps onto the "neat" characterization of linked data where everything should have ideally one canonical representation, and there should be a handful of "correct" general-purpose schema capable of modeling the world. 

We depart from that vision, instead favoring radical vernacularism {cite}`saundersSurveillanceGraphs2023`. URIs are extremely general, and include decentralized identifiers like {index}`multiaddrs <IPFS; Multiaddr>`

## RDF And Friends

```{important}
Return here re: RDF canonicalization and IPFS https://github.com/multiformats/multicodec/pull/261
```

```{index} JSON-LD
```
### JSON-LD




## Challenges

### Ordered Data

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

### Tabular Data

As an overbrief summary, converting data from tables to RDF needs a schema mapping:

- Columns to Properties
- 
- Column names in source table to symbolic names used within the conversion schema
- datatype (for representation in concrete RDF syntax)
- 


According to the [Tabular Data to RDF](https://www.w3.org/TR/csv2rdf/) recommendation, one would convert the following table (encoded as `csv`):

```{csv-table}
countryCode,latitude,longitude,name
AD,42.5,1.6,Andorra
AE,23.4,53.8,"United Arab Emirates"
AF,33.9,67.7,Afghanistan
```

Into one of two "minimal" or "standard" formats of RDF:

`````{tab-set}
````{tab-item} Minimal mode
```turtle
@base <http://example.org/countries.csv> .

:8228a149-8efe-448d-b15f-8abf92e7bd17
  <#countryCode> "AD" ;
  <#latitude> "42.5" ;
  <#longitude> "1.6" ;
  <#name> "Andorra" .

:ec59dcfc-872a-4144-822b-9ad5e2c6149c
  <#countryCode> "AE" ;
  <#latitude> "23.4" ;
  <#longitude> "53.8" ;
  <#name> "United Arab Emirates" .

:e8f2e8e9-3d02-4bf5-b4f1-4794ba5b52c9
  <#countryCode> "AF" ;
  <#latitude> "33.9" ;
  <#longitude> "67.7" ;
  <#name> "Afghanistan" .
```
````
````{tab-item} Standard mode
```turtle
@base <http://example.org/countries.csv> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:d4f8e548-9601-4e41-aadb-09a8bce32625 a csvw:TableGroup ;
  csvw:table [ a csvw:Table ;
    csvw:url <http://example.org/countries.csv> ;
    csvw:row [ a csvw:Row ;
      csvw:rownum "1"^^xsd:integer ;
      csvw:url <#row=2> ;
      csvw:describes :8228a149-8efe-448d-b15f-8abf92e7bd17
    ], [ a csvw:Row ;
      csvw:rownum "2"^^xsd:integer ;
      csvw:url <#row=3> ;
      csvw:describes :ec59dcfc-872a-4144-822b-9ad5e2c6149c
    ], [ a csvw:Row ;
      csvw:rownum "3"^^xsd:integer ;
      csvw:url <#row=4> ;
      csvw:describes :e8f2e8e9-3d02-4bf5-b4f1-4794ba5b52c9
    ]
  ] .

:8228a149-8efe-448d-b15f-8abf92e7bd17
  <#countryCode> "AD" ;
  <#latitude> "42.5" ;
  <#longitude> "1.6" ;
  <#name> "Andorra" .

:ec59dcfc-872a-4144-822b-9ad5e2c6149c
  <#countryCode> "AE" ;
  <#latitude> "23.4" ;
  <#longitude> "53.8" ;
  <#name> "United Arab Emirates" .

:e8f2e8e9-3d02-4bf5-b4f1-4794ba5b52c9
  <#countryCode> "AF" ;
  <#latitude> "33.9" ;
  <#longitude> "67.7" ;
  <#name> "Afghanistan" .
```
````
`````

The recommendation also covers more complex situations. These make use of a JSON schema that handles mapping between the CSV data and RDF.

By default, each row of a table describes a single RDF resource, and each column has a single property (so each cell is a triple). 

For example this table of concerts:

```{csv-table}
Name, Start Date, Location Name, Location Address, Ticket Url
B.B. King,2014-04-12T19:30,"Lupo’s Heartbreak Hotel","79 Washington St., Providence, RI",https://www.etix.com/ticket/1771656
B.B. King,2014-04-13T20:00,"Lynn Auditorium","Lynn, MA, 01901",http://frontgatetickets.com/venue.php?id=11766
```

Needs to be mapped to 3 separate resources with 7 properties. The values are not transformed, just grouped in different places under different resources. Notice how in the standard mode the `csvw:describes`{l=turtle} entry can have three objects. The turtle is surprisingly humane.

The JSON schema describes five concrete triples that carry the data from the CSV, and five `virtual` triples that give the resources types and link them together. Abstractions over table iterators take the form of `"#event-{_row}"` to create a resource `<#event-1>`, `<#event-2>`, etc. for each row.

`````{tab-set}
````{tab-item} Minimal mode
```turtle
@base <http://example.org/events-listing.csv> .
@prefix schema: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<#event-1> a schema:MusicEvent ;
  schema:name "B.B. King" ;
  schema:startDate "2014-04-12T19:30:00"^^xsd:dateTime ;
  schema:location <#place-1> ;
  schema:offers <#offer-1> .

<#place-1> a schema:Place ;
  schema:name "Lupo’s Heartbreak Hotel" ;
  schema:address "79 Washington St., Providence, RI" .

<#offer-1> a schema:Offer ;
  schema:url "https://www.etix.com/ticket/1771656"^^xsd:anyURI .

<#event-2> a schema:MusicEvent ;
  schema:name "B.B. King" ;
  schema:startDate "2014-04-13T20:00:00"^^xsd:dateTime ;
  schema:location <#place-2> ;
  schema:offers <#offer-2> .

<#place-2> a schema:Place ;
  schema:name "Lynn Auditorium" ;
  schema:address "Lynn, MA, 01901" .

<#offer-2> a schema:Offer ;
  schema:url "http://frontgatetickets.com/venue.php?id=11766"^^xsd:anyURI .
```
````
````{tab-item} Standard mode
```turtle
@base <http://example.org/events-listing.csv> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix schema: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:95cc7970-ce99-44b0-900c-e2c2c028bbd3 a csvw:TableGroup ;
  csvw:table [ a csvw:Table ;
    csvw:url <http://example.org/events-listing.csv> ;
    csvw:row [ a csvw:Row ;
      csvw:rownum 1 ;
      csvw:url <#row=2> ;
      csvw:describes <#event-1>, <#place-1>, <#offer-1>
    ], [ a csvw:Row ;
      csvw:rownum 2 ;
      csvw:url <#row=3> ;
      csvw:describes <#event-2>, <#place-2>, <#offer-2>
    ]
  ] .

<#event-1> a schema:MusicEvent ;
  schema:name "B.B. King" ;
  schema:startDate "2014-04-12T19:30:00"^^xsd:dateTime ;
  schema:location <#place-1> ;
  schema:offers <#offer-1> .

<#place-1> a schema:Place ;
  schema:name "Lupo’s Heartbreak Hotel" ;
  schema:address "79 Washington St., Providence, RI" .

<#offer-1> a schema:Offer ;
  schema:url "https://www.etix.com/ticket/1771656"^^xsd:anyURI .

<#event-2> a schema:MusicEvent ;
  schema:name "B.B. King" ;
  schema:startDate "2014-04-13T20:00:00"^^xsd:dateTime ;
  schema:location <#place-2> ;
  schema:offers <#offer-2> .

<#place-2> a schema:Place ;
  schema:name "Lynn Auditorium" ;
  schema:address "Lynn, MA, 01901" .

<#offer-2> a schema:Offer ;
  schema:url "http://frontgatetickets.com/venue.php?id=11766"^^xsd:anyURI .
```
````
````{tab-item} JSON Schema
```json
{
  "@context": ["http://www.w3.org/ns/csvw", {"@language": "en"}],
  "url": "events-listing.csv",
  "dialect": {"trim": true},
  "tableSchema": {
    "columns": [{
      "name": "name",
      "titles": "Name",
      "aboutUrl": "#event-{_row}",
      "propertyUrl": "schema:name"
    }, {
      "name": "start_date",
      "titles": "Start Date",
      "datatype": {
        "base": "datetime",
        "format": "yyyy-MM-ddTHH:mm"
      },
      "aboutUrl": "#event-{_row}",
      "propertyUrl": "schema:startDate"
    }, {
      "name": "location_name",
      "titles": "Location Name",
      "aboutUrl": "#place-{_row}",
      "propertyUrl": "schema:name"
    }, {
      "name": "location_address",
      "titles": "Location Address",
      "aboutUrl": "#place-{_row}",
      "propertyUrl": "schema:address"
    }, {
      "name": "ticket_url",
      "titles": "Ticket Url",
      "datatype": "anyURI",
      "aboutUrl": "#offer-{_row}",
      "propertyUrl": "schema:url"
    }, {
      "name": "type_event",
      "virtual": true,
      "aboutUrl": "#event-{_row}",
      "propertyUrl": "rdf:type",
      "valueUrl": "schema:MusicEvent"
    }, {
      "name": "type_place",
      "virtual": true,
      "aboutUrl": "#place-{_row}",
      "propertyUrl": "rdf:type",
      "valueUrl": "schema:Place"
    }, {
      "name": "type_offer",
      "virtual": true,
      "aboutUrl": "#offer-{_row}",
      "propertyUrl": "rdf:type",
      "valueUrl": "schema:Offer"
    }, {
      "name": "location",
      "virtual": true,
      "aboutUrl": "#event-{_row}",
      "propertyUrl": "schema:location",
      "valueUrl": "#place-{_row}"
    }, {
      "name": "offers",
      "virtual": true,
      "aboutUrl": "#event-{_row}",
      "propertyUrl": "schema:offers",
      "valueUrl": "#offer-{_row}"
    }]
  }
}
```
````
`````

One could imagine how this might generalize into multidimensional array data, but that immediately becomes pretty ridiculous - a better strategy in all cases that I can think of would be to just provide metadata about the array like the encoding, the sizes, types, etc. of their axes and indices and then link to the array.

I'll just leave this example of encoding the pixels in one RGB video frame as a joke.

```turtle
@prefix vid: <http://example.com/GodforsakenVideoSchema> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

:myVideo a vid:VideoGroup ;
  vid:video [ a vid:Video ;
    vid:url <http://example.com/myVideo.mp4> ;
    vid:frame [ a vid:Frame ;
      vid:framenum 1 ;
      vid:url <#frame=1> ;
      vid:describes <#frame-1> ;
    ], [ a vid:Frame ;
      vid:framenum 2 ;
      vid:url <#frame=2> ;
      vid:describes <#frame-2> ;
    ]
  ] .

<#frame-1> a vid:VideoFrame ;
  vid:timestamp "2023-06-29T12:00:00"^^xsd:dateTime ;
  vid:bitDepth 8 ;
  vid:width 1920 ;
  vid:height 1080 ;
  vid:channels <#red-1>, <#green-1>, <#blue-1> ;

<#red-1> a vid:VideoChannel ;
  :pixel-1 a vid:pixelValue ;
    rdf:first 0 ;
    rdf:rest :pixel-2 .

  :pixel-2 a vid:pixelValue ;
    rdf:first 46 ;
    rdf:rest :pixel-3 .

  # ...

  :pixel-2073600 a vid:pixelValue ;
    rdf:first 57 ;
    rdf:rest rdf:nil .
```

### Naming

- All names have to be global. Relative names must resolve to a global name via contexts/prefixes. The alternative is blank nodes, which are treated as equivalent in eg. graph merges. Probably here enters pattern matching or whatever those things are called.
- Blank nodes and skolemization https://www.w3.org/TR/rdf11-mt/#skolemization-informative


## References

- [RDF 1.1 Primer](https://www.w3.org/TR/rdf11-primer/)
- W3C Recommendation on generating RDF from tabular data: {cite}`tandyGeneratingRDFTabular2015`
  - Tabular data model: https://www.w3.org/TR/2015/REC-tabular-data-model-20151217/#parsing
  - Metadata model: https://www.w3.org/TR/2015/REC-tabular-metadata-20151217/
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
- [csv2rdf](https://github.com/Swirrl/csv2rdf/)

### See Also

- [HYDRA vocabulary](https://www.hydra-cg.com/spec/latest/core/) - Linked Data plus REST
- [CORAL](https://github.com/jmchandonia/CORAL)
- [SEMTAB](https://www.cs.ox.ac.uk/isg/challenges/sem-tab/) - competition for mapping tabular data to RDF
- [SciSPARQL](https://www.ceur-ws.org/Vol-1272/paper_22.pdf) - an extension of SPARQL to include arrays.

### Example Datasets

- [RDF Data Dumps](https://www.w3.org/wiki/DataSetRDFDumps)
- [bio2rdf](https://download.bio2rdf.org)