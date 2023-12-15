### mongodb functions
- insertOne() : db.fruits.insertOne({...})
- deletemany() : db.posts.deleteMany({})
- find() : db.fruits.find({});
- projection : db.posts.find({},{_id:1,title:1,category:1,likes:1});

- { acknowledged: true, insertedId: ObjectId("657bf123bd5e41a4bcb0e7df") }

- db.fruits_colors.insertMany([{"fruits_id" : ObjectId("657bf123bd5e41a4bcb0e7df"),"color": "보라"},{"fruits_id" : ObjectId("657bf123bd5e41a4bcb0e7df"),"color":"연보라색"},{"fruits_id" : ObjectId("657bf123bd5e41a4bcb0e7df"),"color":"초록색"}]);

- { acknowledged: true,insertedIds: { '0': ObjectId("657bf475bd5e41a4bcb0e7e0"), '1': ObjectId("657bf475bd5e41a4bcb0e7e1"), '2': ObjectId("657bf475bd5e41a4bcb0e7e2")} }

- 