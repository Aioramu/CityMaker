# Запуск
### для запуска используйте docker-compose:
``` docker-compose up ```
Eсли вы не добавили себя в группу пользователей docker -добавьте в начале sudo.

# Доступные url и методы:
## Список городов
### http://localhost/list/
##### method: GET
response Data:
**"code":200**
data:
```
[
    {
        "Cities": {
            "id": 2,
            "name": "London",
            "lon": -0.1276474,
            "lat": 51.5073219
        }
    },
    {
        "Cities": {
            "id": 3,
            "name": "Moscow",
            "lon": 37.6174943,
            "lat": 55.7504461
        }
    },
]
```

## Добавить город
### http://localhost/add/
##### method: POST
request Data:
```
{
    "name":"Manchester"
}
```
response Data:
**"code":200**

## Ближайший город к точке
### http://localhost/find/
##### method: POST
request Data:
```
{
    "lat":51,
    "lon":100
}
```
response Data:
**"code":200**
data:
```
[
    {
        "name": "Ulan-ude",
        "difference": 7.988131921812806
    },
    {
        "name": "Krakow",
        "difference": 81.35830732036676
    }
]
```
## Удалить город
### http://localhost/delete/
##### method: DELETE
request Data:
```
{
    "id":1
}
```
response Data:
**"code":200**
data:
```
[
    {
        "Cities": {
            "id": 2,
            "name": "London",
            "lon": -0.1276474,
            "lat": 51.5073219
        }
    },
    {
        "Cities": {
            "id": 3,
            "name": "Moscow",
            "lon": 37.6174943,
            "lat": 55.7504461
        }
    },
]
```
