
import typer
import re
from lab101 import closure, gen, unp

app = typer.Typer()


@app.command()
def run():
    typer.echo(f"Список модулей")
    typer.echo(f"closure: 1")
    typer.echo(f"gen: 2")
    typer.echo(f"unp: 3")
    func = typer.prompt("Введите номер функции")
    funcs = {
        "1": closure.logger,
        "2": generator,
        "3": unp.unp,
    }
    for i, f in funcs.items():
        typer.echo(f"{f}: {i}")
    args = typer.prompt("Введите аргументы")

    if func == "1":
        typer.echo(
            funcs[func](args)
        )

    if func == "2":
        typer.echo(
            funcs[func](int(args))
        )

    if func == "3":
        exec(f"typer.echo(funcs[func]({args}))")


def generator(limit: int):
    g = gen.prime_num()
    s = []
    for _ in range(limit):
        s.append(next(g))
    return s


if __name__ == "__main__":
    app()
