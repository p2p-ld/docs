# Data Structures

Triplet graphs similar to linked data fragments with envelopes. decoupling content addressing from versioning

- Merkel DAGs
- Envelopes
- Versioning
- Typed objects with formatting

## Containers

- Packets of LD-triplets that contain
	- Hash of triplets
	- Encryption Info (if applicable)
	- Permissions scope
	- Signature
- Anything that can be directly referenced without local qualifier is a container. 
	- Triplets within a container can be referenced with the [query syntax](querying.html#Location)
- Containers also behave like "feeds" 
	- Eg. one might put their blog posts in `@user:blog` or 
- The account identifier is the top-level container.
- Ordering: 
	- Every triple within a scope is ordered by default by the time it is declared
	- A container can declare its ordering (see [vocabulary](vocabulary.html#Container))
- Naming: 
	- Each container intended to be directly referenced SHOULD contain a `name` so it can be referenced w.r.t its parent: `@<ACCOUNT>:<name>`
	- Each container can also be indicated numerically
- Identity: Each container is uniquely identified by the hash of its contents and the hash of the account identifier. 
- Format: A container can specify one or several ways it can be displayed 
- Capabilities: A container can specify different capabilities that another account can take (eg. "Like", "Upvote", "Reply")
	- Capabilities should also contain a permissions scope, if none is present, the global scope is assumed.



## Triplets

- Triplet format
	- Objects require a shortname that can be hierarchically indexed from 
- Types/Schema
- Including intrinsic notion of nesting
	- every object can have blank/positionally indexed children
	- every triple can have blank/positionally indexed "qualifiers" like RDF-star or wikidata's qualifiers.

## Schema


## Codecs

See IPLD Codecs and Linked Data Platform spec

Means of interacting with binary data. 

Describes

- Format
-  

## Versioning

- A given container has an identity hash from its first packing
- A given triple can be contained by


