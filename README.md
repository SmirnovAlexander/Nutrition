# Nutrition

Extracting most useful information from Walmart products.

## Installation

In virtualenv execute:
```bash
make install
```

## Running

To view available options, run:

```bash
$ python main.py --help
Usage: main.py [OPTIONS] INPUT_PATH

Arguments:
  INPUT_PATH  Path to json with items descriptions (list of dicts)  [required]

Options:
  --output-path TEXT
  --help              Show this message and exit.
```

Sample usage:
```bash
$ python main.py "./data/milk_three_items.json"
2023-08-13 17:23:45.284 | INFO     | __main__:parse_items:19 - Loaded 3 items from ./data/milk_three_items.json
2023-08-13 17:23:45.284 | INFO     | __main__:parse_items:23 - No output path provided, using ./data/milk_three_items_processed.json
```

## Project notes

вопрос: насколько organic этот продукт
контекст: у сына аллергия, глютен не люблю, подходить ли мне эта пачка чипсов

критерии выбора:
- tradeoff: полезно/дешево
- religious ограничения
- лактоза
- глютен
- сколько сахара и сколько насыщенного
- сколько жира
- физически не можешь прочитать ингридиенты
- organic-не organic
- мало сил - вздувает живот - дискомфорт
- 30+ женщины подписаны на нутрициологов в инстаграме - как мне лучше есть
- снижает чувство вины женщины перед семьей что она сделала что могла

решения:
- помочь покупать organic
- помощник-нутрициолог
- собрать корзину помочь


что сделать:
- топ запросов к нутрициологам
- онлайн нутрициолог

кейс:
- вбиваешь продукт, тебе выдается можно ли его есть
    * если есть корзина, то в целом оценка корзины
- собрать новую корзину
    * нужно будет считать калории
- по списку покупок собрать корзину
- брать готовую корзину, анализировать ее на основе предпочтений и предлагать замены если надо
- organic food (являются ли organic сложные ингридиенты)
- вбиваешь что хочешь молоко/свежие фрукты/бакалея/сыры
    * посмотреть апишку волмарта
    * помогает тебе выбрать
    * можно фолоуапить, а-ля хочу более вкусное или более сладкое
    * можно еще спарсить opinions
- дополнить тем что нужно есть

google: 
- top questions for nutritions
- walmart/instacart food descriptions
