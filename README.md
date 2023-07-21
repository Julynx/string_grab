# string_grab
*Extract one or multiple substrings between two start and end strings.*
```python
text = """Gender: female
       Race: White
       Birthday: 3/23/1973 (50 years old)
       Mobile: 715-523-1076
       Mobile: 715-563-3967
       Street: 4674 Lynn Avenue
       City, State, Zip: Eau Claire, Wisconsin(WI), 54701"""
```
```python
from string_grab import grab

birthday = grab(text, start="Birthday: ", end=" (")
print(birthday)

>> "3/23/1973"
```
```python
from string_grab import grab_all

for number in grab_all(text, start="Mobile: ", end="\n"):
    print(number)

>> "715-523-1076"
>> "715-563-3967"
```
```python
from string_grab import inject

inject(text, "611 Waterwheel Ln", start="Street: ", end="\n")

>> """Gender: female
   Race: White
   Birthday: 3/23/1973 (50 years old)
   Mobile: 715-523-1076
   Mobile: 715-563-3967
   Street: 611 Waterwheel Ln
   City, State, Zip: Eau Claire, Wisconsin(WI), 54701"""
```
