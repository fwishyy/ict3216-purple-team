db = db.getSiblingDB('admin');
db.auth(process.env.MONGO_INITDB_ROOT_USERNAME, process.env.MONGO_INITDB_ROOT_PASSWORD);

db = db.getSiblingDB('bank');
db.createUser({
    user: 'bankuser',
    pwd: 'bankpassword',
    roles: [
        {
            role: "readWrite",
            db: "bank"
        }
    ]
})

db.createCollection('users');
db.users.createIndex({ "email": 1 }, { unique: true });
db.users.insertMany([
    {
        "name": "John Doe",
        "email": "john@mail.com",
        "password": "password",
        "balanace": 1000
    },
    {
        "name": "Alice",
        "email": "alice@mail.com",
        "password": "password",
        "balance": 2000
    }
])