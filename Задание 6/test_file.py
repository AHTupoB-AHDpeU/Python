import pytest
from task2 import merge_and_write


def create_test_data(test_data, test_data2):
    with open("test1.txt", 'w') as f:
        f.writelines(test_data)
    with open("test2.txt", "w") as f:
        f.writelines(test_data2)


def test_merge_and_write(my_fixture):
    test_data = ["Первый файл 111"]
    test_data2 = ["Второй файл 222"]
    create_test_data(test_data, test_data2)

    result = merge_and_write("test1.txt", "test2.txt", "test.txt")
    assert result == "Первый файл 111 Второй файл 222"

    result = merge_and_write("noname.txt", "test2.txt", "test.txt")
    assert result == "Один из файлов не найден"

    result = merge_and_write("tes1.txt", "noname.txt", "test.txt")
    assert result == "Один из файлов не найден"


@pytest.mark.parametrize(
    "a, b, result",
    [
        ("Первый файл 111", "Второй файл 222", "Первый файл 111 Второй файл 222"),
    ]
)
def test_pytest(a, b, result):
    assert merge_and_write("test1.txt", "test2.txt", "test.txt") == result
