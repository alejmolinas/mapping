# Mapping


*A Python 2 command line utility 
for mapping chinese characters to their stroke order using fontforge and inkscape*


## Installation

```bash
$ git clone https://github.com/alejmolinas/mapping
$ cd mapping
$ pip2 install . --user
```

Directly from git repository
```bash
$ pip2 install git+https://github.com/alejmolinas/mapping.git
```

## Usage example

Description of all commands
```CommandLine
$ fmap --help
```

Creating a working environment
```CommandLine
$ mkdir CNstrokeorder
$ cd CNstrokeorder
$ fmap --env # Download required files and create necessary directories
```
Starting to map from the characters defined on list.txt
```CommandLine
$ fmap -f list.txt
```

Or mapping characters by directly pasting them to the command line
```CommandLine
$ fmap -c 我非常愛貓
```

Automatically open a chinese dictionary with the stroke order of the character to be mapped

```CommandLine
$ fmap -c 我非常愛貓 -o "http://www.zdic.net/hans/"

# Or open a default dictionary
$ fmap -c 我非常愛貓 -o zdict # Identical to previous example

# Default dictionaries: [zdict, tw, moedict, arch]
```

After finishing mapping, all the characters will be located on `CNstrokeorder/glyphs/done`

## Development setup


```sh
$ pip install -e . --user
```

## Misc
- The fontforge python module can be installed by
   `$ sudo apt-get install python-fontforge`

- It is recommended to check the option "Zoom when window is resized" on inkscape `Edit->Preferences->Windows-> Zoom when window is resized`

- This utility was only tested using python 2, inkscape 1.0.1 and ubuntu 18.04
- "Mapping" is a temporary name, name suggestions are very appreciated!
- TODO list is temporary on `mapping/version.py`

## Contributing (WIP)

1. Fork it (<https://github.com/alejmolinas/mapping>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki