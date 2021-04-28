import pymongo

# Setup connection to mongodb
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Select database and collection to use
db = client.store_inventory
produce = db.produce

produce.insert_many(
    [
        {
            "type": "apples",
            "cost": .23,
            "stock": 333
        },
         {
            "type": "banana",
            "cost": .53,
            "stock": 111
        },
         {
            "type": "grapges",
            "cost": .22,
            "stock": 222
        },
         {
            "type": "strawberry",
            "cost": .44,
            "stock": 444
        },
         {
            "type": "mango",
            "cost": .55,
            "stock": 555
        },
         {
            "type": "watermelon",
            "cost": .66,
            "stock": 666
        },
         {
            "type": "dragonfruit",
            "cost": .77,
            "stock": 777
        }
    ]
)

print("Data Uploaded!")
