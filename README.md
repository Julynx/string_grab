# string_grab

Extract one or multiple substrings between two start and end strings.

> *Functions: [grab](#grab), [grab_all](#grab_all), [grab_until](#grab_until), [grab_after](#grab_after), [inject](#inject), [inject_until](#inject_until), [inject_after](#inject_after).*

```python
from string_grab import grab

text = '''Gender: female
       Race: White
       Birthday: 3/23/1973
       Mobile: 715-523-1076
       Mobile: 715-563-3967
       Street: 4674 Lynn Avenue
       City, State, Zip: Eau Claire, Wisconsin(WI), 54701'''

birthday = grab(text, start='Birthday: ', end='\n')
print(birthday)

>> '3/23/1973'
```

<br>
<br>

# Main functions

## grab

Returns the first substring between two 'start' and 'end' strings.

> *Variants: [grab_all](#grab_all), [grab_until](#grab_until), [grab_after](#grab_after).*

```python
grab('John likes apples.',
     start='John likes ',
     end='.')

>> 'apples'
```

<br>

## inject

Inserts a substring, replacing everything between two 'start' and 'end' strings.

> *Variants: [inject_until](#inject_until), [inject_after](#inject_after).*

```python
inject('John likes apples.',
       'oranges',
       start='John likes ',
       end='.')

>> 'John likes oranges.'
```

<br>
<br>

# [grab](#grab) variants

## grab_all

Yields all substrings between two 'start' and 'end' strings.

> *See [grab](#grab).*

```python
results = grab_all('John likes apples. John likes oranges.',
                   start='likes ',
                   end='.')

list(results)
>> ['apples', 'oranges']
```

<br>

## grab_until

Returns everything before the 'end' string.

> *See [grab](#grab).*

```python
grab_until('John likes apples.',
           end=' likes')

>> 'John'
```

<br>

## grab_after

Returns everything after the 'start' string.

> *See [grab](#grab).*

```python
grab_after('John likes apples.',
           start='likes ')

>> 'apples.'
```

<br>
<br>

# [inject](#inject) variants

## inject_until

Inserts a substring, replacing everything before the 'end' string.

> *See [inject](#inject).*

```python
inject_until('John likes apples.',
             'Sarah',
             end=' likes')

>> 'Sarah likes apples.'
```

<br>

## inject_after

Inserts a substring, replacing everything after the 'start' string.

> *See [inject](#inject).*

```python
inject_after('Sarah likes apples.',
             'oranges.',
             start='likes ')

>> 'Sarah likes oranges.'
```
