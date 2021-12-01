import os
import numpy
import dotenv
import requests

dotenv.load_dotenv()


def get_todays_input(day, dtype=numpy.int32, sep="\n"):
    return numpy.fromstring(
        requests.get(
            f"https://adventofcode.com/2021/day/{day}/input",
            cookies={"session": os.environ["SESSION"]},
        ).text,
        dtype=dtype,
        sep=sep,
    )
