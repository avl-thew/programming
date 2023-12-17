import typer
import re
from lab101 import closure, gen, unp

app = typer.Typer()

@app.command()
def run():
    typer.echo(f"Список модулей")
    typer.echo(f"closure: 1")
    typer.echo(f"gen: 2")
    typer.echo(f"unpack: 3")
    module = typer.prompt("Введите номер модуля")
    modules = {
        "1": closure,
        "2": gen,
        "3": unp,
    }
    select_function(modules[module])


def select_function(module: str):
    funcs = [func for func in dir(module) if re.match(r"\b[a-zA-Z]+", func)]
    for i, func in enumerate(funcs):
        typer.echo(f"{func}: {i}")
    func = typer.prompt("Введите номер функции")
    args = typer.prompt("Введите аргументы")
    exec(f"typer.echo(module.{funcs[int(func)]}({args}))")


if __name__ == "__main__":
    app()