# Django Trade point server

### Run project in docker container

```
/cd src
docker compose up
```

### Get Trade point list

> GET: http://127.0.0.1:3333/api/market/v1/list?phone=+78001234567

```json
{
    "success": true,
    "code": 0,
    "message": "OK",
    "results": [
        {
            "id": 3,
            "title": "Trade market 3"
        },
        {
            "id": 2,
            "title": "Trade market 2"
        },
        {
            "id": 1,
            "title": "Trade market 1"
        }
    ],
    "count": 3,
    "page": 1,
    "last_page": 1
}
```

### Exception

```json
{
    "success": false,
    "code": 4,
    "message": "Торговая точка не найден!"
}
```

### Perform a store visit


> POST: http://127.0.0.1:3333/api/market/v1/visit/1

```json
{
    "success": true,
    "code": 0,
    "message": "ОК",
    "results": {
        "pk": 2,
        "date": "2022-05-13T17:36:12.208087Z"
    }
}
```

### Exception

```json
{
    "success": false,
    "code": 3,
    "message": "неверные данные",
    "debug": [
        "TradePoint matching query does not exist."
    ]
}
```
