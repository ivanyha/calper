def calculate_percent(mode, *, a=None, b=None):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a и b должны быть числами")

    if mode == "add_pr":
        return a + (a / 100) * b

    if mode == "subtract_pr":
        return a - (a / 100) * b

    if mode == "find_rate":
        if b == 0:
            raise ValueError("b (целое) не может быть 0")
        return a / b * 100

    if mode == "find_part":
        return b * a / 100

    if mode == "find_whole":
        if b == 0:
            raise ValueError("b (процент) не может быть 0")
        return a * 100 / b

    if mode == "percent_diff":
        if a == 0:
          raise ValueError("a (база) не может быть 0")
        promejutok = b - a          
        return promejutok / a * 100 

    raise ValueError(f"неизвестный mode: {mode!r}")


def help_CALPER():
    return """
    CALPER — расчёт процентов.

    Режимы:
      add_pr       — a + b% от a          (a — число, b — процент)
      subtract_pr  — a - b% от a          (a — число, b — процент)
      find_rate    — сколько % составляет a от b   (a — часть, b — целое)
      find_part    — сколько составляет a% от b    (a — процент, b — целое)
      find_whole   — чему равно целое, если a — это b% от него (a — часть, b — процент)
      percent_diff — на сколько % b отличается от a (база — a)

    Пример:
      calculate_percent("add_pr", a=1000, b=38)  -> 1380.0
    """


def inter_mode():
    print(help_CALPER())
    mode = input(
        "mode (add_pr / subtract_pr / find_rate / find_part / find_whole / percent_diff): "
    ).strip()
    try:
        a = float(input("a: "))
        b = float(input("b: "))
    except ValueError:
        print("Ошибка: a и b должны быть числами")
        return
    try:
        print("Результат:", calculate_percent(mode, a=a, b=b))
    except (ValueError, TypeError) as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    inter_mode()
