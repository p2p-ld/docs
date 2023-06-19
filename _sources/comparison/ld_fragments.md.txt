```{index} Linked Data; Fragments
```
# Linked Data Fragments

[Containers](Containers) are one example of:


> However, we envision that different kinds of ldf partitionings will emerge, and that these might even vary dynamically depending on server load. Perhaps a semantic way to express the data, metadata, and hypermedia controls of each fragment will be necessary. -{cite}`verborghWebScaleQueryingLinked2014`

## Summary

[Linked data fragments](https://linkeddatafragments.org/publications/) are designed to "fill in the middle" between entirely serverside ({index}`SPARQL`) or clientside (downloading a triple store) usage of linked data triples. SPARQL queries are notorious for being resource intensive, as queries can become much more complex than typical relational algebra and the server needs to resolve a potentially enormous number of resources. Placing all the logic on the server, rather than the client, is an architectural decision that has a complex history, but descends from the idea that the web should work by having "agents" that work on the web on our behalf[^semwebagents]. 

Linked data fragments (LDFs) split the difference by placing more of the work on clients, with the server providing {index}`pre-computed sets of triples <pair: Graph; Partitioning>` for a given selector. "Selector" is a purposefully general concept, but the LDF authors focus primarily on [Triple Pattern Fragments](https://linkeddatafragments.org/specification/triple-pattern-fragments/) that are composed of:

- A **Triple Pattern**, a `?subject ?predicate ?object` that defines the contents of the fragment
- **Metadata**, specifically a `triples` predicate indicating the estimated total number of triples in the fragment since large fragments need to be paginated, and
- **Hypermedia Controls** that can be used to retrieve other related fragments. For example, a triple pattern corresponding to `s:people` `p:named` `o:tom` would have links to retrieve all the related combinations including each field being unspecified, eg. any triplet whose subject is a `person`, predicate is `named` and so on.

The hosting server then partitions all of the triples in a given dataset into all the possible combinations of subjects, predicates, and objects. 

## Overlap

p2p-ld follows Linked Data Fragments in that it emphasizes clientside logic rather than query logic on the network. Executing distributed queries with as much logic as SPARQL can embed adds substantial complexity to the protocol and would potentially import a lot of the problems with SPARQL like heightened resource requirements and potential for abuse for denial of service.

LDF is a strategy for (pre-)partitioning a dataset of triples into cacheable chunks, rather than having the server query over the entire graph at once. It also emphasizes querying as iteration: do many small queries in sequence rather than one large query and waiting for the entire result.


## Differences

- Primarily, containers are more generic than LDFs. Where LDFs create a deterministic partitioning of a set of triples (all combinations, including wildcards, of each subject, predicate, and object in the dataset), p2p-ld partitions based on meaning and use. They are not mutually exclusive, though - one could also make containers that correspond to the expected LDF format.

- re: {index}`Linked Data Platform`, p2p-ld also concerns "leaf" nodes with binary data accessed via codec, rather than represented as triplets. The results of queries are thus not necessarily imagined to be single factual assertions, but datasets, images, documents, posts, etc. -> So the container concept is less rigidly defined than an LDF host with a completely partitioned triplet graph.

Additionally, by being an explicitly *social* system, p2p-ld is unconcerned with arbitrary query execution on anonymous data systems - the expectation is that individual peers and {index}`peer federations <Peer Federations>` manage their resources and the norms around their use. Accordingly, they would manage a set of containers (or, the partition of its graph) that 


```{admonition} To be very clear!
:class: attention

p2p-ld does not attempt to replace or improve SPARQL. There are a number of philosophical and practical differences in the design of the greater semantic web, and particularly its instantiation as bigass corporate knowledge graphs. We will do what we can to integrate with RDF and RDF-like technologies, but p2p-ld is *not* a distributed SPARQL endpoint.
```



[^semwebagents]: See the history of the early to middle semantic web, discussed in {cite}`saundersSurveillanceGraphs2023`


## References

- Homepage: https://linkeddatafragments.org/
- Papers:
	- Original conference paper: {cite}`verborghWebScaleQueryingLinked2014`
	- {cite}`verborghTriplePatternFragments2016` 
- Specification: [Triple Pattern Fragments](https://linkeddatafragments.org/specification/triple-pattern-fragments/)