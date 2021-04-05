from jinja2 import Environment, FileSystemLoader, select_autoescape
from glob import glob
import os
import subprocess
import sass


env = Environment(
  loader=FileSystemLoader("templates"),
  autoescape=select_autoescape(["html", "xml"])
)

templates_list = [
  "index.html",
  "chat.html",
  "forums.html",
  "post.html"
]


# Removes all files in docs folder
def clear_site_folder():
  subprocess.run(["rm", "-r", "docs"])
  subprocess.run(["mkdir", "docs"])


def build_templates():
  for i in templates_list:
    tmp = env.get_template(i)

    with open(f"docs/{i}", "wt") as f:
      f.write(tmp.render())


def build_sass():
  for i in glob("sass/*.scss"):
    if os.path.basename(i)[0] == "_":
      continue

    with open(f"docs/static/{os.path.basename(i).rsplit('.', 1)[0]}.css", "wt") as new_file:
      new_file.write(sass.compile(filename=f"sass/{os.path.basename(i)}", output_style="compressed"))


def build_static():
  os.mkdir("docs/static")
  for i in glob("static/*"):
    with open(i, "rb") as og_file:
      with open(f"docs/static/{os.path.basename(i)}", "wb") as new_file:
        new_file.write(og_file.read())

def build_site():
  clear_site_folder()

  build_templates()
  build_static()
  build_sass()


def run(build=True):
  if build:
    build_site()

  subprocess.run(["python", "-m", "http.server", "8000", "--directory", "docs"])


if __name__ == "__main__":
  run()
