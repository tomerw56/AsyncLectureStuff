import asyncio
import time

async def async_count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

def regular_count():
    print("One")
    time.sleep(1)
    print("Two")


def regular_main():
    for _ in range(3):
        regular_count()

async def async_main():
    await asyncio.gather(async_count(),async_count(),async_count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(async_main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


    s = time.perf_counter()
    regular_main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")