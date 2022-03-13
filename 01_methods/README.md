# Solver for Piyavski and Strongin methods

Example:

```sh
python3 -m solver --method strongin --param 2 --xfrom 0 --xto 4 --tests 5
```


Help:

```
usage: __main__.py [-h] [--method METHOD] [--param PARAM] [--xfrom XFROM] [--xto XTO] [--tests TESTS]

optional arguments:
  -h, --help       show this help message and exit
  --method METHOD  method name [piyavski, strongin]
  --param PARAM    method parameter
  --xfrom XFROM    left x boundary
  --xto XTO        right x boundary
  --tests TESTS    number of tests
```
