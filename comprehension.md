## Comprehension

# Types of Comprehension
    1. List Comprehension
    2. Dictionary Comprehension
    3. Set Comprehension
    4. Generator Comprehension

1. List Comprehension : make entire list in memory

    - [ expression for item in iterable if condition ]
    - [ tea for tea in menu if "Iced" in tea ]

2. Set Comprehension

    - { expression for item in iterable if condition }

3. Dictionary Comprehension

    - { key: expression for item in iterable if condition }
    - { tea: price / 80 for tea, price in tea_prices_inr.items() }

4. Generator Comprehension : flow like a stream in a memory

    - ( expression for item in iterable if condition )