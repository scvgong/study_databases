# NoSQL
* 빅 데이터를 빠르고 효율적인 처리를 위한 목적(SQL 일부 기능 포기)
* offical : https://www.mongodb.com/docs/manual/query-api/

### Excel VS SQL VS NoSQL
| Excel | RDBMS | NoSQL |
| --- | --- | --- |
| Excel | Database | Database |
| Sheet | Table | Collection |
| Column+Row | Tuple+Row | Document |
| Column | Column | Field |
| Link(?) | Table Join | Embedded Documents |
| 없음 | Primary Key | Primary Key(Default_id) |

### Syntex
```
db.posts.insertOne({
  title: "Post Title 1",
  body: "Body of post.",
  category: "News",
  likes: 1,
  tags: ["news", "events"],
  date: Date()
})
```

### Beginner
| 분류 | 설명 | 비고 |
| --- | --- | --- |
| CRUD Syntax | [INSERT](https://www.w3schools.com/mongodb/mongodb_mongosh_insert.php) , [DELETE](https://www.w3schools.com/mongodb/mongodb_mongosh_delete.php) , [FIND](https://www.w3schools.com/mongodb/mongodb_mongosh_find.php) , [UPDATE](https://www.w3schools.com/mongodb/mongodb_mongosh_update.php) |  |

### Intermediate
* [youtube-연산자를 활용한 검색](https://youtu.be/6ceKUg25zGs)

| 분류 | 설명 | 비고 |
| --- | --- | --- |
| Operators | [Query](https://www.w3schools.com/mongodb/mongodb_query_operators.php), [Update](https://www.w3schools.com/mongodb/mongodb_update_operators.php) |  |
| Database | [Create](https://www.w3schools.com/mongodb/mongodb_mongosh_create_database.php) |  |
| Collection | [Create](https://www.w3schools.com/mongodb/mongodb_mongosh_create_collection.php) |  |

### Advanced
| 분류 | 설명 | 비고 |
| --- | --- | --- |
| Aggregation | [Aggregation](https://www.w3schools.com/mongodb/mongodb_aggregations_intro.php) |  |
| Indexing & Search | [Indexing & Search](https://www.w3schools.com/mongodb/mongodb_indexing_search.php) |  |
| Schema Validation | [Schema Validation](https://www.w3schools.com/mongodb/mongodb_schema_validation.php) |  |

### mongodb functions
- insertOne() : db.fruits.insertOne({...})
- deletemany() : db.posts.deleteMany({})
- find() : db.fruits.find({});
- projection : db.posts.find({},{_id:1,title:1,category:1,likes:1});

예시
- { acknowledged: true, insertedId: ObjectId("657bf123bd5e41a4bcb0e7df") }
- db.fruits_colors.insertMany([{"fruits_id" : ObjectId("657bf123bd5e41a4bcb0e7df"),"color": "보라"},{"fruits_id" : ObjectId("657bf123bd5e41a4bcb0e7df"),"color":"연보라색"},{"fruits_id" : ObjectId("657bf123bd5e41a4bcb0e7df"),"color":"초록색"}]);
- { acknowledged: true,insertedIds: { '0': ObjectId("657bf475bd5e41a4bcb0e7e0"), '1': ObjectId("657bf475bd5e41a4bcb0e7e1"), '2': ObjectId("657bf475bd5e41a4bcb0e7e2")} }

# SQL
* Structured Query Language, 구조화 질의어
* 관계형 데이터베이스 관리 시스템(RDBMS) 데이터를 관리 위해 특수 목적 프로그래밍 언어

### Beginner
| 분류 | 설명 | 비고 |
| --- | --- | --- |
| CRUD Syntax | [INSERT INTO](https://www.w3schools.com/sql/sql_insert.asp) , [DELETE](https://www.w3schools.com/sql/sql_delete.asp) , [SELECT](https://www.w3schools.com/sql/sql_select.asp) , [UPDATE](https://www.w3schools.com/sql/sql_update.asp) |  |
| more SELECT | [WHERE](https://www.w3schools.com/sql/sql_where.asp) ~ [ORDER BY](https://www.w3schools.com/sql/sql_orderby.asp) , [LIKE](https://www.w3schools.com/sql/sql_like.asp) ~ [Aliases](https://www.w3schools.com/sql/sql_alias.asp) | [NULL Values](https://www.w3schools.com/sql/sql_null_values.asp) |

### Intermediate
| 분류 | 설명 | 비고 |
| --- | --- | --- |
| more SELECT | [GROUP BY](https://www.w3schools.com/sql/sql_groupby.asp) , [HAVING](https://www.w3schools.com/sql/sql_having.asp) , [count_avg_sum](https://www.w3schools.com/sql/sql_count_avg_sum.asp) , [min_max](https://www.w3schools.com/sql/sql_min_max.asp) , [CASE Expression](https://www.w3schools.com/sql/sql_case.asp) |  |
| Operators | [Operators](https://www.w3schools.com/sql/sql_operators.asp) |  |
| Joins | [Joins](https://www.w3schools.com/sql/sql_join.asp) ~ [UNION](https://www.w3schools.com/sql/sql_union.asp) |  |

### Advanced
| 분류 | 설명 | 비고 |
| --- | --- | --- |
| INSERT INTO SELECT | [Syntax](https://www.w3schools.com/sql/sql_insert_into_select.asp) |  |
| Functions | [MySQL Functions](https://www.w3schools.com/sql/sql_ref_mysql.asp) |  |
| 재귀질의 |  |  |
