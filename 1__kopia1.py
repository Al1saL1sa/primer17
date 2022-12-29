#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import os.path
import argparse

spisok = []
new_spisok = []


def add_people(list_people, surname, name, post, data):
    """
    Добавить данные магазина.
    """
    list_people.append(
        {
            "surname": surname,
            "name": name,
            "prise": post,
            "data": data
        }
    )
    return list_people


def display_table(list_people):
    if list_people:
        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 15,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)

        print('| {:^4} | {:^15} | {:^30} | {:^20} | {:^15} | '.format(
            "№",
            "Дата рождения",
            "Фамилия",
            "Имя",
            "Знак Зодиака"
        )
        )

        print(line)

        for idx_new, spisok_new_new in enumerate(list_people, 1):
            print(
                '| {:>4} | {:<15} | {:<30} | {:<20} | {:<15} | '.format(
                    idx_new,
                    spisok_new_new.get('data', ''),
                    spisok_new_new.get('surname', ''),
                    spisok_new_new.get('name', ''),
                    spisok_new_new.get('post', 0)
                )
            )
        print(line)
    else:
        print("Список людей пуст.")


def select_zodiac(list_people, people_sear):
    search_people = []
    for people_sear_itme in list_people:
        if people_sear == people_sear_itme['post']:
            search_people.append(people_sear_itme)
    return search_people


def load_list_people(file_name):
    with open(file_name, 'r', encoding="utf-8") as f:
        return json.load(f)


def save_people(file_name, list_people):
    with open(file_name, 'w', encoding="utf-8") as f:
        json.dump(list_people, f, ensure_ascii=False, indent=4)


def main(command_line=None):
    file_parser = argparse.ArgumentParser(add_help=False)
    file_parser.add_argument(
        "filename",
        action="store",
        help="The data file name"
    )

    parser = argparse.ArgumentParser("workers")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )

    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser(
        "add",
        parents=[file_parser],
        help="Add a new people"
    )

    add.add_argument(
        "-sn",
        "--surname",
        action="store",
        required=True,
        help="The peoples' surname"
    )

    add.add_argument(
        "-n",
        "--name",
        action="store",
        required=True,
        help="The peoples' name"
    )

    add.add_argument(
        "-p",
        "--post",
        action="store",
        required=True,
        help="The peoples' zodiac sign"
    )

    add.add_argument(
        "-dt",
        "--data_birth",
        action="store",
        required=True,
        help="Date of Birth"
    )

    _ = subparsers.add_parser(
        "display",
        parents=[file_parser],
        help="Display all peoples"
    )

    select = subparsers.add_parser(
        "select",
        parents=[file_parser],
        help="Select the product"
    )

    select.add_argument(
        "-f",
        "--find",
        action="store",
        type=str,
        required=True,
        help="The find people"
    )

    args = parser.parse_args(command_line)

    is_dirty = False
    if os.path.exists(args.filename):
        people = load_list_people(args.filename)
    else:
        people = []

    if args.command == "add":
        people = add_people(
            people,
            args.surname,
            args.name,
            args.post,
            args.data
        )
        is_dirty = True

    elif args.command == "display":
        display_table(people)

    elif args.command == "select":
        selected = select_zodiac(people, args.people_sear)
        display_table(selected)

    if is_dirty:
        save_people(args.filename, people)


if __name__ == '__main__':
    main()
