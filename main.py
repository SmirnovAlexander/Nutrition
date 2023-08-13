import json
from pprint import pprint

import typer
from loguru import logger
from typing_extensions import Annotated

from schemas import Item


def parse_items(
    input_path: Annotated[str, typer.Argument(help="Path to json with items descriptions (list of dicts)")],
    output_path: str = None,
):
    with open(input_path) as f:
        data = json.load(f)
    items = [Item(**item) for item in data]

    logger.info(f'Loaded {len(items)} items from {input_path}')

    if not output_path:
        output_path = input_path.replace('.json', '_processed.json')
        logger.info(f'No output path provided, using {output_path}')

    with open(output_path, 'w') as f:
        f.write(json.dumps([item.model_dump() for item in items]))


if __name__ == "__main__":
    typer.run(parse_items)
