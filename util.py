from typing import Any, Callable, List


def try_input(
    func: Callable,
    text: List[str] = None,
    prompt: str = "",
    error: str = "Not a valid choice.",
) -> Any:
    if text:
        print(*text, sep="\n", end="\n" * 2)
    while True:
        try:
            return func(input(prompt))
        except Exception:
            print(error, end="\n" * 2)
