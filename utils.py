import os
import numpy
import dotenv
import requests

dotenv.load_dotenv()


def get_todays_input(day):
    return numpy.array(
        [
            int(s)
            for s in requests.get(
                f"https://adventofcode.com/2021/day/{day}/input",
                cookies={"session": os.environ["SESSION"]},
            )
            .text.strip()
            .split("\n")
        ]
    )
