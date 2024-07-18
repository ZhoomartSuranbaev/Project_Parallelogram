from time import sleep


def get_printing_first() -> None:
    pict_list = [
        "MY FIRST SCRIPT\n\n",
        "    *********",
        "   *       **",
        "  *       * *",
        " *********  *",
        " *       *  *",
        " *       *  *",
        " *       * *",
        " *********",
        "\n\nI LOVE PYTHON",
    ]
    for i in pict_list:
        sleep(0.4)
        print(i)
