Encoding
=============

## Application change

### change of application
- evolvavility: how easy it is changed (detail in Chapter1)
- server side: rolling upgrade (not stop the service)
- client side: not frequently

It is common to have old/new source codes at the same time.
- **backword compatibility**: load old file to new file
- **forward compatibility**: load new file from old code (difficult)


## Data encoding format
Encoding is to convert data in memory structure into byte sequence (self-consistent).

Language-specific encoding format has some problems: for language developers, compatibility has less importance.

Language-agnostic text-based encoding such as JSON, XML, Binary variants and CSV are
- not distinguishable number from string
- don't support binary characters
- CSV does not have schemas

Thus, language-agnostic binary encoding is necessary. e.g. messagepack (one of the JSON binary encoding format)

### Thirft
- Created by facebook
- doesn't field names, but has field tag
- thirft compact protocol: field type and tag are expresssed in  a byte

### Protocol Buffer
- almost same as thirft

### Compatibility
Backword compatibility is not supported. If we want to support, define default values for each field (though it's not a perfect solution). Forward compatibility is supported (just to ignore new fields is fine).

### Bit length
- Forward compatibility is not guaranteed if bit lenghts change (e.g. 32 bits -> 64 bits).

#### Avro
* not having data type neither field type
* UTF-8 concat
* variable-length encoding
* when decoding. schema should match
    * because data itself has no 
