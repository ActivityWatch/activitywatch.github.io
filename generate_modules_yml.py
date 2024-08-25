#!/usr/bin/env python3

import os

import yaml

# Directory containing the HTML files
tables_dir = "_includes/tables"

# Output YAML file
output_file = "_data/modules.yml"

# Exclude this file
exclude_file = "github-stats.html"


def load_existing_modules():
    if os.path.exists(output_file):
        with open(output_file, "r") as file:
            data = yaml.safe_load(file)
            return data.get("modules", [])
    return []


def save_modules(modules):
    data = {"modules": modules}
    with open(output_file, "w") as file:
        yaml.dump(data, file, default_flow_style=False)


def generate_modules_yml():
    # List all HTML files in the tables directory, excluding the specified file
    new_modules = [
        f.replace(".html", "")
        for f in os.listdir(tables_dir)
        if f.endswith(".html") and f != exclude_file
    ]

    # Load existing modules
    existing_modules = load_existing_modules()

    # Add new modules to the end of the existing list, preserving order
    for module in new_modules:
        if module not in existing_modules:
            existing_modules.append(module)

    # Save the updated list of modules
    save_modules(existing_modules)

    print(f"Generated {output_file} with modules: {existing_modules}")


if __name__ == "__main__":
    generate_modules_yml()
