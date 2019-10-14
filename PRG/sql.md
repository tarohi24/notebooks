SQL
===========

## TIPS

### Count for multiple attributes

```sql
SELECT COUNT(*) AS key, admindept FROM room GROUP BY admindept
```


### Coping only schema (no data)

```sql
CREATE TABLE TAB1_COPY AS SELECT * FROM TAB1 WHERE 1<>1
```
