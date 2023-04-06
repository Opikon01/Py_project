from utils import get_data, get_filtered_data, get_last_values, get_formated_data


def main():
    COUNT_VALUES = 5
    #Переменная обозначающая, сколько операций по счетам нужно вывести
    FILTERED_EMPTY_FROM = True
    #Переменная для проверки по ключу FROM с флагом TRUE

    data = get_data()
    data = get_filtered_data(data, FILTERED_EMPTY_FROM)
    data = get_last_values(data, COUNT_VALUES)
    data = get_formated_data(data)

    for row in data:
        print(row, end='\n')
    #Цикл, который разделяет счета пустой строкой


if __name__ == "__main__":
    main()
