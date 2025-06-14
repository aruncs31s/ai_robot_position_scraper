# ai_robo_position_scraper


## Installation 

```bash
pip install ai-robot-position-scraper
```

## update
```bash
pip install --upgrade ai-robot-position-scraper
```

## Usage

```python
from position_scraper import extract_positions
print(
    extract_positions(
        "https://github.com/AI-Robot-GCEK/robo-initial-positions/blob/main/src/initial-positions.h"
    )
)
```
output
```
{'LA1_INITIAL_POSITION': 25, 'LA2_INITIAL_POSITION': 30, 'LA3_INITIAL_POSITION': 160, 'RA1_INITIAL_POSITION': 160, 'RA2_INITIAL_POSITION': 160, 'RA3_INITIAL_POSITION': 30, 'LH_INITIAL_POSITION': 93, 'RH_INITIAL_POSITION': 107, 'LL1_INITIAL_POSITION': 130, 'LL2_INITIAL_POSITION': 25, 'LL3_INITIAL_POSITION': 160, 'RL1_INITIAL_POSITION': 60, 'RL2_INITIAL_POSITION': 150, 'RL3_INITIAL_POSITION': 30, 'LF_INITIAL_POSITION': 90, 'RF_INITIAL_POSITION': 99}
```


```python
from position_scraper import extract_names

print(
    extract_names(
        "https://github.com/AI-Robot-GCEK/robo-initial-positions/blob/main/src/initial-positions.h"
    )
)
```

```
['LA1', 'LA2', 'LA3', 'RA1', 'RA2', 'RA3', 'LH', 'RH', 'LL1', 'LL2', 'LL3', 'RL1', 'RL2', 'RL3', 'LF', 'RF']
```