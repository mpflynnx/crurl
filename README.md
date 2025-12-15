# crurl short for "create URL"
Pronunciation: "**crull**" (like "**krull**")

**crurl** is a Python command line application, which will create a browser independent web link of a given URL.

## Why use **crurl**? 

In today's age of multiple device usage, laptop, tablets and phone. Having access to centralised lists of your favourite website URLs can be difficult. 

Yes, some browsers allow you to sync your bookmarks and history between devices, but mostly the actual data is hidden and only accessible via that specific browser. If you use multiple browsers, be it Edge when on Windows, Firefox on your laptops or Chrome on your android phone. That could mean three browsers to login to and sync. Too quickly the bookmarks are out of sync.

**Crurl** tries to solve this problem. By creating one file for each weblink URL. This file can then be uploaded and shared via your favourite cloud storage provider. The files can be searched by name or by content using whatever tool you prefer whether on Windows or Linux.

**Crurl** works best with **Dropbox** as the Android and iOS apps work great with the .URL file format. By clicking on the file in the app, a `open in browser` button appears, press it then a browser tab opens at the webpage URL.

This is the Python version. Python is great for quickly prototyping an idea. In development is a Rust version.


## Installation

Install **crurl** direct from [github.com]()

- Linux OS instructions
```bash
$ cd ~
$ python3 -m venv .venv # create virtual environment
$ source .venv/bin/activate # activate environment
$ python3 -m pip install git+https://github.com/mpflynnx/crurl.git # install from github
```

### System dependency

This application makes use of the **`xsel`** linux command, which should come with the OS. Otherwise run "sudo apt-get install xsel" or search your distrubutions package repository.

### Viewing help 
```bash
$ .venv/bin/crurl --help
usage: crurl [-h] [-b BOOKMARK] [-w WEBLINK] [--version] [-v] [-o OUTPUT] [-D]
             [-html] [-t] [-f]

A tool to generate a webpage shortcut file.

optional arguments:
  -h, --help            show this help message and exit
  -b BOOKMARK, --bookmark BOOKMARK
                        Unformatted name for shortcut file (default: )
  -w WEBLINK, --weblink WEBLINK
                        Weblink for shortcut (default: )
  --version             Print the application version and exit.
  -v, --verbose         Show all messages. (default: 50)
  -o OUTPUT, --output OUTPUT
                        Where to output the generated files. If not specified,
                        a directory will be created, named "output" in the
                        current path. (default: None)
  -D, --debug           Show all messages, including debug messages. (default:
                        None)
  -html, --html         Weblink to be .html format. (default: url)
  -t, --write_test      Create basic test.py (default: False)
  -f, --force           Overwrite existing bookmark if exists and use the
                        suggested filename (default: False)
```
### Default usage, no arguments
- Use this option when the system clipboard dependency **`xsel`** is installed and the filename title will be automatically retrieved from the weblink title.
- Copy to the clipboard a website URL i.e `https://doc.rust-lang.org/rust-by-example/primitives.html`
- Open a terminal
- Type `crurl` then press `Enter` key
- The contents of the clipboard is validated as a website URL.
- The title from the website is automatically retrieved and used as the filename.
```bash
$ crurl

    Reading url from clipboard...

    Getting title for url...
     ...https://doc.rust-lang.org/rust-by-example/primitives.html

 Are you happy with this filename? "Primitives_Rust_By_Example.url" [yN] y

     New file created at....

/home/mpflynnx/Dropbox/bookmarks/Primitives_Rust_By_Example.url
```
- View the contents of the newly created file using **`cat`**
```bash
$ cat /home/mpflynnx/Dropbox/bookmarks/Primitives_Rust_By_Example.url
[InternetShortcut]
URL="https://doc.rust-lang.org/rust-by-example/primitives.html"
```

### Using the -w argument
- Use this option when the system clipboard dependency **`xsel`** is **not** installed.
- Copy to the clipboard a website URL i.e `https://doc.rust-lang.org/rust-by-example/primitives.html`
- Open a terminal, type `crurl -w`
- Paste the URL after the `-w` argument, then press `Enter` key
- The URL given is validated as a website URL.
- The title from the website is automatically retrieved and used as the filename.
```bash
$ crurl -w https://doc.rust-lang.org/rust-by-example/primitives.html

    Getting title for url...
     ...https://doc.rust-lang.org/rust-by-example/primitives.html

 Are you happy with this filename? "Primitives_Rust_By_Example.url" [yN] y

    New file created at....

/home/mpflynnx/Dropbox/bookmarks/Primitives_Rust_By_Example.url
```
- View the contents of the newly created file using **`cat`**
```bash
$ cat /home/mpflynnx/Dropbox/bookmarks/Primitives_Rust_By_Example.url
[InternetShortcut]
URL="https://doc.rust-lang.org/rust-by-example/primitives.html"
```

### Using the -w and -b arguments
- Use these arguments together when the website title is **not** required to be used as the filename and the system clipboard dependency **`xsel`** is **not** installed.
- Copy to the clipboard a website URL i.e `https://doc.rust-lang.org/rust-by-example/primitives.html`
- Open a terminal
- Type `crurl - w` then paste the URL after the `-w` argument,
- Type -b then in double quotes **`""`** type the required filename to be used i.e "rust by example primitives"
- Press `Enter` key


```bash
$ crurl -w https://doc.rust-lang.org/rust-by-example/primitives.html -b "rust by example primitives"

    Getting title for url...
     ...https://doc.rust-lang.org/rust-by-example/primitives.html

    New file created at....

/home/mpflynnx/Dropbox/bookmarks/rust_by_example_primitives.url
```
- View the contents of the newly created file using **`cat`**
```bash
$ cat /home/mpflynnx/Dropbox/bookmarks/rust_by_example_primitives.url
[InternetShortcut]
URL="https://doc.rust-lang.org/rust-by-example/primitives.html"
```



