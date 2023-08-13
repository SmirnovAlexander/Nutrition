import json
import os
from pprint import pprint

import typer
from loguru import logger
from tqdm import tqdm
from typing_extensions import Annotated

from schemas import Item


def parse_items(
    input_path: Annotated[str, typer.Argument(help="Path to json(s) with items descriptions (list of dicts)")],
    output_path: str = None,
):
    if os.path.isdir(input_path):
        logger.info(f'Input path is a directory, processing all json files in it')

        if input_path.endswith('/'):
            input_path = input_path[:-1]

        # concat all json files in the directory
        data = []
        for file in os.listdir(input_path):
            if file.endswith(".json"):
                with open(os.path.join(input_path, file)) as f:
                    data += json.load(f)

        input_path = os.path.join(os.path.dirname(input_path), os.path.basename(input_path) + '.json')
        logger.info(f'Writing concatenated json to {input_path}')
        with open(input_path, 'w') as f:
            f.write(json.dumps(data, indent=4))

    with open(input_path) as f:
        data = json.load(f)
    logger.info(f'Loaded {len(data)} items from {input_path}')

    items = [Item(**item) for item in tqdm(data)]

    if not output_path:
        output_path = input_path.replace('.json', '_processed.json')
        logger.info(f'No output path provided, using {output_path}')

    with open(output_path, 'w') as f:
        f.write(json.dumps([item.model_dump() for item in items]))


if __name__ == "__main__":
    typer.run(parse_items)
