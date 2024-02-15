import tomli
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

env = Environment(loader=FileSystemLoader(""))

template = env.get_template("template.html")


config_dir = Path('configs')
config_dir.mkdir(exist_ok=True)
output_dir = Path('output')
output_dir.mkdir(exist_ok=True)


for fp in config_dir.glob("*.toml"):

    name = fp.stem
    with open(fp, 'r') as fh:
        page_data = tomli.loads(fh.read())

    output_html = template.render(**page_data)
    output_path = output_dir / f'{name}.html'
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(output_html)
    print("Created", output_path)
