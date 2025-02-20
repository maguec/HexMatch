# Sample Queries

## Find the location of Consumer 45

```sql
GRAPH HexMatch 
MATCH(c:Consumer{id: 45})-[l:HAS_CONSUMER]->(h:Hex)
RETURN c.id AS Consumer,c.searching AS Searching, h.id AS Location 
```
## Show me the Count of Producers and consumers by Hex in SQL

```sql
SELECT
    h.id,
    COUNT(hp.id) AS provider_count,
    COUNT(hc.id) AS consumer_count
  FROM
    Hex AS h
    LEFT JOIN HasProvider AS hp ON h.id = hp.to_id
    LEFT JOIN HasConsumer AS hc ON h.id = hc.to_id
  GROUP BY
    h.id;
```

## Show me the Count of Producers and consumers by Hex in GCQL

```sql
GRAPH HexMatch
MATCH (h:Hex)
OPTIONAL MATCH (h)<-[:HAS_PROVIDER]-(p:Provider)
OPTIONAL MATCH (h)<-[:HAS_CONSUMER]-(c:Consumer)
RETURN h.id AS hex_id, count(DISTINCT p) AS provider_count, count(DISTINCT c) AS consumer_count
ORDER by hex_id
```

## Find me all available Providers closest to Consumer 45

```sql
GRAPH HexMatch
MATCH(c:Consumer{id: 45})-[l:HAS_CONSUMER]->(h:Hex)-[a:HAS_ADJACENT]->{1,5}(ph:Hex)<-[:HAS_PROVIDER]-(p:Provider{available: 1})
return c.id as Consumer, ARRAY_LENGTH(a) as Distance, p.id as Provider
ORDER BY Distance  LIMIT 3
```

## Find Providers closest with a rating >=4 

```sql
GRAPH HexMatch
MATCH ANY SHORTEST (c:Consumer{id: 12})-[l:HAS_CONSUMER]->(h:Hex)-[a:HAS_ADJACENT]->{1,5}(ph:Hex)<-[:HAS_PROVIDER]-(p:Provider{available: 1})
WHERE p.rating >= 4
return c.id as Consumer, ARRAY_LENGTH(a) as Distance, p.id as Provider
ORDER BY Distance
```

## Get the max distance for the shortest path

```sql
 GRAPH HexMatch
 MATCH ANY SHORTEST (c:Consumer{id: 12})-[l:HAS_CONSUMER]->(h:Hex)-[a:HAS_ADJACENT]->{1,5}(ph:Hex)<-[:HAS_PROVIDER ]-(p:Provider{available: 1})
 LET total_distance = SUM(a.radius) * 2
 RETURN h.id AS start_hex, ARRAY_LENGTH(a) as hops, total_distance, p.Id, p.Rating, ph.id as end_hex
```
## Move a Provider to a new Hex

```sql
DELETE from HasProvider where id = 19 AND to_id = 12;
INSERT INTO HasProvider (id, to_id) VALUES(19, 1);
```

## Find the hex with the most Consumers

```sql
GRAPH HexMatch
MATCH (c:Consumer)-[:HAS_CONSUMER]->(h:Hex)
RETURN COUNT(h) as per_hex, h.id as hex_id
ORDER by per_hex DESC LIMIT 5
```

## Find the hex with then most available Providers

```sql
GRAPH HexMatch
MATCH (p:Provider{available: 1})-[:HAS_PROVIDER]->(h:Hex)
RETURN COUNT(h) as per_hex, h.id as hex_id
ORDER by per_hex DESC LIMIT 5
```
