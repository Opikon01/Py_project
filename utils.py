import json
from datetime import datetime


def get_data():
    """Работа с библиотекой json. Для получения данных"""
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data, filtered_empty_from):
    """Функция фильрует по ключу STATE со значением EXECUTED, так же проверяет на начилие ключа FROM"""
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    if filtered_empty_from:
        data = [x for x in data if 'from' in x]
    return data


def get_last_values(data, count_values):
    """Функция получает последние значения и сортирует их по вермени. Count_values - кол-во значений"""
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:count_values]


def get_formated_data(data):
    """Функция возвращает отформатированые данные.
       Дату, (Перевод от куда , куда) счёт отправителя( первые 6 и последние 4 цифры карты)
       счёт получаетя (последние 4 цифры карты), сумма перевода, валюта.
    """
    formated_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row['description']
        if "from" in row:
            sender = row["from"].split()
            from_bill = sender.pop(-1)
            from_bill = f'{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}'
            from_info = ' '.join(sender)
        else:
            from_info, from_bill = "Счёт скрыт", ""
        recipient = row["to"].split()
        recipient_bill = recipient.pop(-1)
        recipient_bill = f"**{recipient_bill[-4:]}"
        to_info = ' '.join(recipient)
        amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"
        formated_data.append(f"""
{date} {description}
{from_info} {from_bill} -> {to_info} {recipient_bill}
{amount}""")
    return formated_data
