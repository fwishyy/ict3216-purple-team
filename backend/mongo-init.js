db = db.getSiblingDB('admin');
db.auth(process.env.MONGO_INITDB_ROOT_USERNAME, process.env.MONGO_INITDB_ROOT_PASSWORD);

db = db.getSiblingDB('bank');
db.createUser({
    user: 'apiuser',
    pwd: '9FK6FXHK3Vm9jQniH7y6',
    roles: [
        {
            role: "readWrite",
            db: "bank"
        }
    ]
})

db.createCollection('users');
db.accounts.createIndex({ "email": 1 }, { unique: true });
db.accounts.insertMany(
    [
        {
            "name": "Alice Carpenter",
            "email": "alice.carpenter@example.com",
            "password": "zP8m!kVt92#x",
            "balance": 2483.75
        },
        {
            "name": "Brian Torres",
            "email": "brian.torres@example.com",
            "password": "R9&uTbE12^wx",
            "balance": 1589.20
        },
        {
            "name": "Charlotte Nguyen",
            "email": "charlotte.nguyen@example.com",
            "password": "Y!2nmqZx$3Pk",
            "balance": 764.00
        },
        {
            "name": "Daniel Murphy",
            "email": "daniel.murphy@example.com",
            "password": "mL#71Xte!cKd",
            "balance": 5327.40
        },
        {
            "name": "Ella Simmons",
            "email": "ella.simmons@example.com",
            "password": "n@Vr2QxP8&j3",
            "balance": 298.10
        },
        {
            "name": "Frankie Patel",
            "email": "frankie.patel@example.com",
            "password": "W!3ezXpT#91m",
            "balance": 913.67
        },
        {
            "name": "Grace Holloway",
            "email": "grace.holloway@example.com",
            "password": "tF7&plvK$z0x",
            "balance": 1904.55
        },
        {
            "name": "Henry Wallace",
            "email": "henry.wallace@example.com",
            "password": "Kz8#u1Qm!vTp",
            "balance": 610.30
        },
        {
            "name": "Isla Benson",
            "email": "isla.benson@example.com",
            "password": "qM!49Vut*oXj",
            "balance": 4729.85
        },
        {
            "name": "Jackie Rhodes",
            "email": "jackie.rhodes@example.com",
            "password": "X2$yNbV!73kp",
            "balance": 329.90
        }
    ]
);
db.createCollection('cards');
db.cards.createIndex
db.cards.insertMany([
    {
        "card": "4539 1488 0343 6467",
        "cvv": "923",
        "expiry": "09/26"
    },
    {
        "card": "5500 0000 0000 0004",
        "cvv": "378",
        "expiry": "11/27"
    },
    {
        "card": "4716 1234 5678 9010",
        "cvv": "145",
        "expiry": "04/25"
    },
    {
        "card": "6011 1111 1111 1117",
        "cvv": "612",
        "expiry": "12/28"
    },
    {
        "card": "4000 0566 5566 5556",
        "cvv": "298",
        "expiry": "07/24"
    },
    {
        "card": "5105 1051 0510 5100",
        "cvv": "837",
        "expiry": "10/26"
    },
    {
        "card": "4111 1111 1111 1111",
        "cvv": "492",
        "expiry": "03/30"
    },
    {
        "card": "6011 6020 1234 5678",
        "cvv": "301",
        "expiry": "06/25"
    },
    {
        "card": "4007 1234 5678 9010",
        "cvv": "584",
        "expiry": "08/29"
    },
    {
        "card": "5555 5555 5555 4444",
        "cvv": "729",
        "expiry": "01/27"
    }
]);