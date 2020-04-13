# Gilded Rose

Hi and welcome to team Gilded Rose. As you know, we are a small inn with a prime location in a
prominent city ran by a friendly innkeeper named Allison. We also buy and sell only the finest goods.
Unfortunately, our goods are constantly degrading in quality as they approach their sell by date. We
have a system in place that updates our inventory for us. It was developed by a no-nonsense type named
Leeroy, who has moved on to new adventures.

### Prerequisites

Have a python environment configured.

## Running the app

From the root directory of the project.
The number_of_days parameter is mandatory.

```bash
$ python main.py <number_of_days>
```

### Running the main text test

From the root directory of the project.
Without number_of_days parameter, the script will run as if it was launched with 1.

```bash
$ python -m test.test_inn <number_of_days>
```

### Running the unit tests

From the root directory of the project.

```bash
$ python -m unittest discover -s test
```

## Refactoring process used in this project

1. Understand how everything works

2. Add unit tests
    * Define limit cases for test cases
    * Increase code coverage

3. Clarify existing code
    * Reorganize and regroup conditions
    * Check unit tests to validate changes
4. Refactor deeply
    * Define each item process regarding quality update
    * Create different classes for each item type
    * Check unit tests to validate changes

5. Add required functionality
    * Check conjured item existing results
    * Define conjured item quality update process
    * Define unit tests

6. Enhance testing methods

7. Reorganize classes and functions
