# SQLite

```{index} Database Engine; RDBMS
```
```{index} RDBMS; SQLite
```

We want something like sqlite, but for {index}`Graph Database`s! 

Most of the existing triple stores and graph databases are very heavyweight services that would be impractical for packaging in a portable daemon in the same way that sqlite works. Maybe we can learn from how sqlite works and do something similar for graph databases?

Questions:

- How come these things can be faster than idk like a .json file
- How are they different architecturally than a traditional SQL server

## File Structure

- Main file
- Rollback Journal - stores additional information to restore in case of a crash. Store a copy of the original DB, write changes directly into DB file. COMMIT occurs when rollback is deleted
- Write-ahead Log - if in [WAL mode](https://www.sqlite.org/wal.html), append updates to WAL file. COMMIT occurs when writing to WAL file (not to main DB). Multiple transactions can be batched.

### Pages

Pages are the basic unit of an sqlite file.

Numeracy:

- Each page can be a power of 2 between 512 and 65536
- All pages are the same size
- Max `2^32 - 2` pages in a single DB. 


#### Types

Each page has a single type:


> - The lock-byte page
> - A freelist page
> 	- A freelist trunk page
> 	- A freelist leaf page 
> - A b-tree page
> 	- A table b-tree interior page
> 	- A table b-tree leaf page
> 	- An index b-tree interior page
> 	- An index b-tree leaf page 
> - A payload overflow page
> - A pointer map page 

##### Lock-byte

(artifact of windows 95 compatibility)

##### Freelist

Linked list of "trunks and leaves" to keep track of unused pages:
- Trunk pages:
	- Series of 4-byte integers that take up full page
	- First integer is the page number of the next trunk (zero if it's the last page)
	- Second integer is number of leaf pointers that follow
- Leaf pages:
	- contain nothing!

##### {index}`B-tree`

([B-tree wiki page](https://en.wikipedia.org/wiki/B-tree))

Two types of b-trees: table and index

- **Table B-Trees**: 
	- One table b-tree in the db file for each `rowid` table in the database schema
	- 64-bit signed integer key that refers to the `rowid` it implements
	- Store all data in leaves (interior pages just point to leaves)
	- 
- **Index B-Trees**: 
	- One index b-tree for each index in the schema
	- Arbitrary keys
	- Store no data.

Two types of b-tree pages:
- **Interior**
- **Leaf**

```{todo}
Describe freeblocks
```

#### Payload Overflow

> Define the "payload" of a cell to be the arbitrary length section of the cell. 
> - For an index b-tree, the key is always arbitrary in length and hence the payload is the key. 
> - There are no arbitrary length elements in the cells of interior table b-tree pages and so those cells have no payload. 
> - Table b-tree leaf pages contain arbitrary length content and so for cells on those pages the payload is the content.

When a payload is bigger than some threshold[^overflowthreshold], store it on a linked list of payload overload pages. The first four bytes of each overflow page are a 4-byte big-endian integer indicating the page number of the next page in the chain, or zero for the final page.

[^overflowthreshold]: > The overflow thresholds are designed to give a minimum fanout of 4 for index b-trees and to make sure enough of the payload is on the b-tree page that the record header can usually be accessed without consulting an overflow page. In hindsight, the designer of the SQLite b-tree logic realized that these thresholds could have been made much simpler. However, the computations cannot be changed without resulting in an incompatible file format. And the current computations work well, even if they are a little complex.

#### Pointer Maps

Backlinks from child to parent nodes in index trees to assist with vacuuming :)

Each pointermap page provides backlinks for the pages immediately following it.

Each 5-byte ptrmap entry consists of:

- 1 byte of page type information:
	- `0`: A b-tree root page
	- `0`: Freelist page
	- `prior page` or `first page`: payload overflow page
	- `parent page`: non-root b-tree page
- 4 byte big-endian page number


### Header

(Add header info here as the rest of the spec makes it relevant)

https://www.sqlite.org/fileformat.html#the_database_header

Useful properties
- Magic header string makes it easy to identify sqlite files
- File change counter & schema cookie - 4-byte integer that increments whenever the db file is unlocked. useful for cache invalidation
- `version-valid-for-number` - stores the version of the software that most recently modified it, and the change counter at that modification. Useful for detecting if certain behaviors like updating the in-header db size are behaving correctly by knowing what version made a given change.

## Schema

### Records

### Tables

### Indices

## I/O

```{todo}
**How does writing and querying an sqlite file actually work???**
```

All reads from and writes to the main database file happen at a page boundary.

All writes are an integer number of pages in size.

Most reads are also an integer number of pages in size, except opening the database which reads the header (first 100 bytes).




## See also

- [Graph Databases](graphdb)

## References

- [SQLite File Format](https://www.sqlite.org/fileformat.html)
- [SQLite Quirks](https://www.sqlite.org/quirks.html) - useful for understanding some design decisions
- [Customization and Porting](https://www.sqlite.org/custombuild.html)
- [SQLite Architecture](https://www.sqlite.org/arch.html)