Data Model and Query Model
==========

## Relational model
- Proposed in 1970 
- express data as a row
- long term used
- full join support

## NoSQL
- Document database is a part of NoSQL
* pros:
    * scalability
    * flexible compared to relational schema 
* --> So why still RDB exists?
- cons:
  - few join supports

- RDB is not good at storing one-to-many relationship.
- It stores in the following non-intuitive manners:
    * 1. make table
    * 2. have info as json
    * ..
- Necessary information is not in-place.
- It is a case where NoSQL supresses RDB.

Note: However, document databse is **not suitable for  many-to-many relationship**, as document database doesn’t support join fully.


## RDB vs NoSQL

NoSQL is good because
* flexible schema
* data locality (better performance)
* close data structure to programming languages

RDB is good because of full join support.


### Schema flexibility
Document database is actually not schema-less.
-> it is **schema-on-read** (has schema when reading; cf: schema-on-write … RDB)

Schema-on-read is good when data structure dependes on outer system

### data structure
NoSQL stores data in the form of BSON
* so that frequent-seen document require less disk access
* update which doesn’t change document size is fast

### Query language
SQL is a major language:
declarative query language (hide how-to-extract, describe what-to-extract0
