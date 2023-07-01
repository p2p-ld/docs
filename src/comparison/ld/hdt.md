```{index} Linked Data; HDT
```
(hdt)=
# HDT

Like [Linked Data Fragments](ld_fragments), [HDT](https://www.rdfhdt.org/) is a transport and query format for linked data triples.

It is a compressed format that preserves headers to enable query and browsing without decompression. 

## Format

It has [three components](https://www.rdfhdt.org/technical-specification/):

{attribution="https://www.rdfhdt.org/technical-specification/"}
> - **Header:** The Header holds metadata describing an HDT semantic dataset using plain RDF. It acts as an entry point for the consumer, who can have an initial idea of key properties of the content even before retrieving the whole dataset.
> - **Dictionary:** The Dictionary is a catalog comprising all the different terms used in the dataset, such as URIs, literals and blank nodes. A unique identifier (ID) is assigned to each term, enabling triples to be represented as tuples of three IDs, which reference their respective subject/predicate/object term from the dictionary. This is a first step toward compression, since it avoids long terms to be repeated again and again. Moreover, similar strings are now stored together inside the dictionary, fact that can be exploited to improve compression even more.
> - **Triples:** As stated before, the RDF triples can now be seen as tuples of three IDs. Therefore, the Triples section models the graph of relationships among the dataset terms. By understanding the typical properties of RDF graphs, we can come up with more efficient ways of representing this information, both to reduce the overall size, but also to provide efficient search/traversal operations.

### Header

A header contains

- At least one resource of type `hdt:Dataset`, which has
    - Publication metadata - Where and when the dataset was published
    - Statistical metadata - Number of triples, number of terms, etc.
    - Format metadata - Encoding of dataset, which must have
        - `hdt:dictionary` 
        - `hdt:triples`
    - Additional metadata - uh idk anything?
    

````{dropdown} HDT Header Example
```turtle
@prefix void: <http://rdfs.org/ns/void#>.
@prefix dc: <http://purl.org/dc/terms/>.
@prefix foaf: <http://xmlns.com/foaf/0.1/>.
@prefix hdt: <http://purl.org/HDT/hdt#>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
@prefix swp: <http://www.w3.org/2004/03/trix/swp-2/>.

<http://example.org/ex/DBpediaEN> 
  a hdt:Dataset ;
  a void:Dataset ;
  hdt:publicationInformation :publication ;
  hdt:statisticalInformation :statistics ;
  hdt:formatInformation      :format ;
  hdt:additionalInformation  :additional ; 
  void:triples "431440396" ;
  void:properties "57986" ;
  void:distinctSubjects "24791728" ;
  void:distinctObjects "108927201" .

:publication   dc:issued "2012-11-23T23:17:50+0000" ;
  dc:license <http://www.gnu.org/copyleft/fdl.html> ;
  dc:publisher [  a foaf:Organization ;
    foaf:homepage <http://www.dbpedia.org>] ;
  dc:source <http://downloads.dbpedia.org/3.8/en> ;
  dc:title "DBpediaEN" ;
  void:sparqlEndpoint <http://www.dbpedia.org/sparql> .

:statistics    hdt:originalSize "110630364018" ;
  hdt:hdtSize "3082795954" .

:format    hdt:dictionary :dictionary ;
  hdt:triplesBitmap :triples .

:dictionary    dc:format hdt:dictionaryFour ;
  hdt:dictionaryNamespaces [hdt:namespace [hdt:prefixLabel "dbpedia" ;
    hdt:prefixURI "http://dbpedia.org/resource/"]] ;
  hdt:dictionarynumSharedSubjectObject "22762644" ;
  hdt:dictionarysizeStrings "1026354060" ;
  hdt:dictionaryBlockSize "8" .

:triples   dc:format hdt:triplesBitmap ;
  hdt:triplesOrder "SPO" ;
  hdt:triplesnumTriples "431440396" .

:additional    swp:signature "AZ8QWE..." ;
  swp:signatureMethod "DSA" .
```
````

### Dictionary

The dictionary replaces all terms in the dataset with short, unique IDs to make the dataset more compressible. Oddly, rather than being a simple lookup table, it splits the dictionary into four sections: a "shared" section that includes subjects and objects, and predicates are separated. Terms are lexicographically ordered and [front coded](https://en.wikipedia.org/wiki/Incremental_encoding) to additionally aid compression. 

Separating encoding information into a header dictionary is a straightforwardly good idea, and an argument for distributing linked data in 'packetized' forms rather than as a bunch of raw triples, as we do here. 

### Triples

Triples are encoded as a tree, where each subject forms a root, with each predicate as children, and likewise for objects. Since the dictionary is ordered such that the subjects are the lowest IDs, it is possible to use an implicit representation of each subject (ie. subjects are not encoded). The predicate and object layers are each encoded with two parallel bit streams: Each predicate or object entry has one `Sp` entry for its dictionary ID, and one `Bp` "bitsequence" entry which is `1` if the entry is the first child of its parent and `0` otherwise.

## Querying

The dictionary being uncompressed allows for the dataset to be indexed at a vocabulary level - it is possible to eg. 'find all datasets that use this set of terms,' as well as slightly more refined queries like 'find datasets that use this term as both subject and object.'

Lookup is fast for subject-based queries, but predicate and object queries are slower because of the bitmap triple encoding. 






## Lessons

First, there are good strategies here for practical compression and serialization of RDF triples! 

The most interesting thing for p2p-ld here is the header: we are also interested in making it possible to do restricted queries and indexing over containers of triples without needing to necessarily query, download, or unpack the entire dataset. The primary focus here is compression, which has add-on benefits like faster query performance because the dataset can be held in memory. We would instead like to focus on exposing hashed tree fragments that can encapsulate query logic - eg. a given RDF resource that might indicate the metadata for a type of experiment would be hashed as a tree, and queries can discover it by querying for the root or any of its child hashes. So we will take the ideas re: using the dictionary encoding without necessarily adopting HDT wholesale.

The bitmap encoding is also interesting, as according to their tests it outperforms other similar compression schemes and I/O times. We will keep this in mind as a potential serialization format for raw triple data. 

The idea of including publication data in the header seems obvious, but according to the authors later work that is not necessarily the case in RDF world {cite}`polleresMoreDecentralizedVision2020`. Since p2p-ld is built explicitly around making identity and origin a more central component of linked data, we will further investigate using the {index}`VOID vocabulary <Ontology; VOID>` - https://www.w3.org/TR/void/




## References

- [HDT Homepage](https://www.rdfhdt.org/)
- Original Paper: {cite}`fernandezBinaryRDFRepresentation2013`
- Later contextualization: {cite}`polleresMoreDecentralizedVision2020`