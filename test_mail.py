from smtplib import SMTP
from time import sleep
from rich.console import Console

console = Console()
tasks = [f"task"]

with console.status("[bold green]Working on tasks...") as status:
    while tasks:
        tasks = tasks.pop(0)
        sleep(1)
        # - Cast response message in list to identify HTTP code
        with SMTP('smtp.google.com') as smtp:
            messg = list(smtp.noop())
            print(messg)

        with SMTP('smtp.office365.com') as smtp:
            messg = list(smtp.noop())
            print(messg)

        with SMTP('smtp.libero.it') as smtp:
            messg = list(smtp.noop())
            print(messg)

        console.log(f"{task} complete")

