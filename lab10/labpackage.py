# import typer
# import re
# from lab101 import closure, gen, unp

# app = typer.Typer()

    
# @app.command()
# def run():
#     typer.echo(f"Список модулей")
#     typer.echo(f"closure: 1")
#     typer.echo(f"gen: 2")
#     typer.echo(f"unpack: 3")
#     module = typer.prompt("Введите номер модуля")
#     modules = {
#         "1": closure,
#         "2": gen,
#         "3": unp,
#     }
#     select_function(modules[module])


# def select_function(module: str):
    
#     funcs = [func for func in dir(module) if re.match(r"\b[a-zA-Z]+", func)]
#     for i, func in enumerate(funcs):
#         typer.echo(f"{func}: {i}")
#     func = typer.prompt("Введите номер функции")
#     args = typer.prompt("Введите аргументы")
#     exec(f"typer.echo(module.{funcs[int(func)]}({args}))")
#     gen = prime_num()
#     s = []
#     for _ in range(5):
#         s.append(next(gen))

# if __name__ == "__main__":
#     typer.run(app())  


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
    #exec(f"typer.echo(module.{funcs[int(func)]}({args}))")

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        return True


def generator(limit: int):
    # gen = prime_num()
    s = []
    for i in range(2, limit + 1):
        if is_prime(i):
            s.append(i)
    # return s 
    typer.echo(f"простые числа до {limit}: {primes}")
    

if __name__ == "__main__":
    app()

