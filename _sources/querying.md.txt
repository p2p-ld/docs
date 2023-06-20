# Querying

How do we find peers that have subgraphs that are responsive to what we want?

- Query results should then become their own containers, with the component triplets of the query being hashed at the root level, so then the query-er can cache the query results (in case anyone else makes the same query) while also rehosting the original containers returned from the query.

## Syntax
 
(qlocation)=
### Location

How to refer to a given [container](Containers), eg.

```
@user:containerName:childName
```

or numerically

```
@user:containerName:{0}
```



### Version

How to refer to a specific version of a container

References without version qualification indicate the most recent version at the time of containerizing the links.

## Query Fragments

Using blank subgraphs to specify queries like {index}`Linked Data; Fragments` and {index}`SPARQL <Linked Data; SPARQL>`