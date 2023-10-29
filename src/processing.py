from operator import itemgetter


def dict_on_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Сортировка словаря
    :param data: список словарей и значение для ключа state
    :param state: str
    :return: возвращает новый список, содержащий только те словари,
    у которых ключ state

    """
    return [item for item in data if item.get("state") == state]


def dict_sort(data: list[dict], sort: bool = True) -> list[dict]:
    """
    Сортировка по возрастанию или убыванию даты в зависимости от условия
    :param data: list[dict]
    :param sort: bool
    :return: list[dict]
    """
    # data.sort(key=lambda data: data["date"])
    sort_data = sorted(data, key=itemgetter("date"), reverse=sort)
    return sort_data


input_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
result_state = "CANCELED"
print(dict_on_state(input_data, result_state))
print(dict_sort(input_data, False))
