# Codecs

Interfaces to file formats

We want to support three kinds of interaction with files:

- **References** - treat files like abstract binary with some metadata indicating file type and a hash tree for the file
- **Introspection** - Export some metadata from the file that indicates components of the file along with byte ranges. We want to be able to know what is inside the file without downloading it, but we keep the file separate as an out of protocol entity.
- **Ingestion** - Export the metadata and the data contained within the file to triples. We also store some translation between the original binary file and the resulting triple through translation schema that allows us to update our triples if the files change and otherwise keep a strong link to the source, but otherwise enable forking/querying/etc. as if the data does not have an underlying file.

This is a challenging design balance, where we don't want clients to need to implement a large number of codecs for different files - so they can fall back to the reference strategy as needed - but we also want people to be able to interact and import their files without needing to abandon longstanding practices or other infrastructure they might already have for using/creating them.

```{toctree}
hdf5
```

- Files
	- json
	- csv
	- mat