# Querying

How do we find peers that have subgraphs that are responsive to what we want?

## Syntax

(qlocation)=
### Location

How to refer to a given [container](data_structures.html#Containers), eg.

```
@user:containerName:childName
```

or numerically

```
@user:containerName:{0}
```


Children 

### Version

How to refer to a specific version of a container

References without version qualification indicate the most recent version at the time of containerizing the links.

## Query Fragments

Using blank subgraphs to specify queries