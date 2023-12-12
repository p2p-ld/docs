# Roadmap

What things do we build and in what order?

## Phase 1: Format Sandbox

```{admonition} Goals
- Experimenting with needs for format translation
- Encoding of triple graphs + hashed binary files
```

In this phase we are using {index}`NWB` as a naturalistic development case of a complex format with an idiosyncratic implementation (ie. written in its own schema language, with its own I/O API, etc.)

See [nwb-linkml](https://github.com/p2p-ld/nwb-linkml)


## Phase 2: Simple Transfer

```{admonition} Goals
- Simplest possible peer model: self-sharing between devices owned by peer
- Share, query, and download data
```

A `peer` has a public `identity` that is represented by one or multiple `machines` that host the `graphs` associated with that identity. Each graph has some collection of `triples` which are identified relative to the IRI of the parent graph. A triple can refer to a `binary` file that is not stored in the graph itself by its hash, encoding, and other metadata needed to use the file. The (semantic) metadata that describes that `binary` file can point to it without needing to encode arrays/etc. in RDF-like graphs.

```{mermaid}

---
config:
  er:
    layoutDirection: LR
---
erDiagram
	PEER {
		string private_key
	}
	PEER ||--|{ IDENTITY : knownAs
	IDENTITY {
		string private_key
		string public_key
		string preferredName
	}
	IDENTITY ||--|{ GRAPH : hasFeed
	IDENTITY }o--o{ IDENTITY : peerList
	IDENTITY }|--|{ MACHINE : represents
	MACHINE {
		graph mirrorRules
	}
	MACHINE }|--o{ GRAPH: stores

	GRAPH {
		IRI id
		string name
		capability read
		capability write
	}
	GRAPH }|--|{ TRIPLE : contains
	TRIPLE {
		IRI relative_id
		string subject
		string predicate
		string object
	}
	TRIPLE ||--o{ BINARY : indicates
	BINARY {
		string encoding
		string hash
		graph metadata

	}
```

The MVP for simple transfer is to have a single peer be able to transfer subgraphs and binary files between multiple machines keyed to their public identity.



## Phase 3: Schema Manipulation

```{admonition} Goals
- Make custom schema
- Declare and resolve sameness relations
- Dataset versioning
```

## Phase 4: Peer Federation

```{admonition} Goals
- Ontology for determining access
- Pinning and mirroring
```


## Phase 5: External Resources


```{admonition} Goals
- Treat external resources as peers
- HTTP, S3 mirroring
```

## Phase 6: Discoverability

```{admonition} Goals
- Use external sources of identity to connect to peer
- Bootstrap servers
```