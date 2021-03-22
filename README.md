# Team Engage Static Engine

## What is it?

A Python program that compiles different files into a static, HTML website.

## What features does it support?

The engine currently supports [Jinja2](https://pypi.org/project/Jinja2/), [Sass (SCSS)](https://pypi.org/project/libsass/), and Static files.

## How do I use this program?

First clear out the templates, sass, and static folders.

Put Jinaj2 supported templates inside the templates folder, see [its documentation for guide](https://jinja.palletsprojects.com).
To chose the templates to be rendered, enter their file name into the `templates_list` variable in main.py.

Write Sass (or SCSS) files into the sass folder. The program will ignore files starting with an underscore (_), assuming they will get imported.

Put everything else into the static folder.

Sass and static files will be put under the `/static` path.

Run `python main.py` to build. The function `run()` uses the `http.server` module to host the docs folder. If you just want the files, run `build_site()`.

## Can I use this program for my own project?

Yes!
