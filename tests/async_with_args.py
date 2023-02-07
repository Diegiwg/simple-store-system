import asyncio


class Aync:
    data = None

    def __init__(self, data):
        self.data = data

    async def run(self):
        print(f"Async {self.data}")
        await asyncio.sleep(1)
        print("End")


# Para utilizar a função como callback async, deve-se fazer: callback=Async("valor de teste").run
