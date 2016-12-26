# Flatten File System

We already know what kind of data structure is the Tree.
On famous example of Tree representation if the File System.

Install the `tree` package with `sudo apt-get install tree` to see your File System like a Tree.

Your task for today is to implemented the following function:

```python
def flatten_file_system1(path):
    pass

def flatten_file_system2(path):
    pass
```

## Examples

```python
rositsazz@rositsazz:~/courses/personal $ pwd
/home/rositsazz/courses/personal

rositsazz@rositsazz:~/courses/personal $ tree

.
├── algo
│   ├── linked_list.py
├── baba
│   ├── G
│   └── panda.txt
├── gas_station.py
├── matrix_bombing.py
└── tests

```


```python
ffs = flatten_file_system1(path='/home/rositsazz/courses/personal')
print(ffs)
```

```python
> ['/home/rositsazz/courses/personal',
 '/home/rositsazz/courses/personal/algo',
 '/home/rositsazz/courses/personal/baba',
 '/home/rositsazz/courses/personal/gas_station.py',
 '/home/rositsazz/courses/personal/matrix_bombing.py',
 '/home/rositsazz/courses/personal/tests',
 '/home/rositsazz/courses/personal/algo/linked_list.py',
 '/home/rositsazz/courses/personal/baba/G',
 '/home/rositsazz/courses/personal/baba/panda.txt']
```

```python
ffs = flatten_file_system2(path='/home/rositsazz/courses/personal')
print(ffs)
```

```python
> ['/home/rositsazz/courses/personal',

  '/home/rositsazz/courses/personal/algo',
  '/home/rositsazz/courses/personal/algo/linked_list.py',
  '/home/rositsazz/courses/personal/baba',
  '/home/rositsazz/courses/personal/baba/G',
  '/home/rositsazz/courses/personal/baba/panda.txt',
  '/home/rositsazz/courses/personal/gas_station.py',
  '/home/rositsazz/courses/personal/matrix_bombing.py',
  '/home/rositsazz/courses/personal/tests']
```

