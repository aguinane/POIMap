import toml
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(""))

template = env.get_template("template.html")

with open('config.toml', 'r') as fh:
    page_data = toml.loads(fh.read())

output_html = template.render(**page_data)
file_path = 'output.html'
with open(file_path, "w", encoding="utf-8") as fh:
    fh.write(output_html)
print("Created", file_path)
