# Sketchpad


## System Components

Strictly schematic and keeping track of different pieces. Not indicative of code structure and definitely not final

```{mermaid}
graph
	subgraph data
		direction TB
		Schema
		Triples
		Translation
		Codec
	end

	Schema -->|Models| Triples
	Codec <-->|Read/Write| Triples
	External[External Data] --> Codec
	External --> Translation
	Translation <-->|Maps Between| Schema

	subgraph peer
		direction TB
		Identity
		Instance
		Beacon
	end

	Identity -->|Has Many| Instance
	Beacon -->|Indicates| Identity
	Triples -->|Stored By| Instance


	subgraph social
		Federation
		Permissions
		Sharding
	end

	Schema -->|Defines| Federation

```

## Rough Roadmap

Enough to get us to SfN for now...

```{mermaid}
gantt
	dateFormat YYYY-MM

	section Data Modeling and Transfer
	Write Container Draft Spec :active, container, 2023-06, 2M
	Experiment with basic Networking components :networking, 2023-07, 2M
	Translate NWB Schema : trans, after container, 1M
	Codec for hdf5 :codec1, after container, 1M
	Webseeds with HTTP/S3: webseed, after trans, 1M

```

## Data

### Triple Data Model

```{mermaid}
erDiagram
	TRIPLE {
		id subject
		id predicate
		id object
	}

	CONTAINER {
		str content_hash
		str container_hash
		str version_hash
		str name
		id  creator
		int timestamp
		array capabilities
	}


	CONTAINER ||--|{ TRIPLE : hashes

```

- `content_hash` - hash of contained triple graph, after resolution
- `container_hash` - original hash of `content_hash` and metadata of container when first created
- `version_hash` - the version of this particular instance of the container, excluding `container_hash` - should be equal to container_hash when first instantiating.

Example

```{mermaid}
graph TB
	Root

	Root --> D1Root

	subgraph Dataset1
		direction TB
		D1Root
		D1Meta
		D1Name
		D1Date
		D1Etc

		D1Root --> D1Meta
		D1Meta --> D1Name
		D1Meta --> D1Date
		D1Meta --> D1Etc
	end

	Root --> Imported
	subgraph Vocabs
		Imported[Imported Schema]
		Term1

		Imported --> Term1

	end
```

Types of references and means of identifying
- Absolute (hash of a container): Containers are the only uniquely identifiable thing in the network. Everything else has to be done relative to them. 
- Relative (resolve against the containing context)
- Container: `. -> pred -> obj` - links that describe the container.
- External: How to refer to some external but otherwise identifiable thing? eg. How do I identify that I am making a translation layer for `numpy` when they aren't involved with p2p-ld at all? I should be able to use a variety of tactics - eg. I should be able to say `pypi:numpy` and then in turn identify `pypi` by URI. If someone else declares it by saying `url:numpy` and referring to their homepage, for example, then later we can declare those things as equal 

Resolving Cycles
- The identity is the root node of the graph, so do a breath-first

Resolving names
How do we go from an external hash to another object? Our peer should be able to hydrate every content hash into an `author:hash` pair so that our downloading peer knows who to ask about shit. Or if we are the owner of that thing they know they can ask us for an additional container. 








## Scrap

Just a stub to check if mermaid works

```{mermaid}
erDiagram
	IDENTITY {
		string hash
	}
	INSTANCE {
		string ip
		string client
	}
	BEACON {
		string uri
	}
	IDENTITY ||--o{ INSTANCE : runs
	BEACON }o--|{ INSTANCE : links
	BEACON }o--|| IDENTITY : represents

```

## Graph Data Model

- Triplets
- Containers
- Codecs


## Random notes

- re: {index}`Backlinks` - https://lists.w3.org/Archives/Public/public-rdf-comments/2012Jul/0007.html
