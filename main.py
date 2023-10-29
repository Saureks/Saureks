from src.widget import card_or_account, get_data


def main():
    data = "2018-07-11T02:26:18.671407"
    word = input("Введите данные карты или счета: ")
    print(card_or_account(word))
    print(get_data(data))


if __name__ == "__main__":
    main()
