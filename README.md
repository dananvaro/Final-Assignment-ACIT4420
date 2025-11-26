
# Final Assignment - ACIT 4420

This reposity contains two Python projects, completed as part of the ACIT 4420 course. The task focuses on modular programming, I/O handling, metaprogramming, error handling, RegEx and logging. 



## Structure

```
Final-Assignment-ACIT4420/
│
├── Conway-Game-of-Life/
│   ├── board.py
│   ├── rules.py
│   ├── io_handler.py
│   ├── main.py
│   ├── Patterns/
│   │   ├── beehivepatternWithWErrors.txt
│   │   ├── blinker.txt
│   │   └── random.txt   
│   └── data/
│       └── state_snapshots.txt   
│
└── Smart-Courier-Routing/
    ├── run.log
    └── src/
        ├── main.py
        ├── validators.py
        ├── optimizer.py
        ├── logTime.py
        ├── data/
        │   ├── deliveries.csv
        │   ├── routes.csv
        │   └── rejected.csv
        ├── deliveryModels.py
        └── haversine.py
```



## Task 1 - Smart-Courier-Routing
```
git clone https://github.com/dananvaro/Final-Assignment-ACIT4420.git
cd Smart-Courier-Routing/src

```
To run Smart-Courier-Routing
```
python3 main.py
```
or
```
python main.py
```

## Task 2 - Conway-Game-of-Life
```
cd Conway-Game-of-Life
```
To run Conways Game of Life. Choose between beehivepatternWithErrors.txt, blinker.txt or random.txt patterns. Then choose number of generations.
```
python3 main.py --patternfile <path_to_pattern_file> --generations <number_of_generations> --ruleset default
```
or
```
python main.py --patternfile <path_to_pattern_file> --generations <number_of_generations> --ruleset default

```
Sample 
```
python main.py --patternfile beehivepatternWithErrors.txt --generations 15 --ruleset default
```



