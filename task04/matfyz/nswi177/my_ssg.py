#!/usr/bin/env python3

"""
my_ssg - My simple static site generator for
the NSWI177 course at MFF CUNI.
"""

from markdown import markdown
from jinja2 import Environment, FileSystemLoader

import argparse
import distutils.dir_util
import os
import pathlib
import sys
import shutil

import matfyz.nswi177.mdyml as mdyml
import matfyz.nswi177.files as files

def markdownify(content):
    return markdown(content)

class Site():
    def __init__(self, path_to_root):
        self.path_to_root = path_to_root

def generate_one_file(template, all_pages, base_dir, input_filename, destination_filename):
    """
    Generate one HTML file from Markdown source.

    Parameters
    ----------
    template
        Templating engine object.
    all_pages: list
        List of all pages (already pre-parsed).
    base_dir: str
        Base directory with content
    input_filename: str
        Filename to process.
    destination_filename: str
        Where to store the converted file.
    """
    print("{} => {}".format(input_filename, destination_filename))
    (meta, content) = mdyml.load_markdown_with_yaml_header_from_file(input_filename)
    pathtosite = os.path.relpath(base_dir, os.path.dirname(input_filename))+'/'

    rendered = template.render(meta, content=content, SITE=Site(pathtosite))
    with open(destination_filename, 'w') as out:
        out.write(rendered)

def get_html_filename(relative_markdown_filename):
    """
    Get HTML filename from given Markdown filename.
    """
    return os.path.splitext(relative_markdown_filename)[0] + '.html'

def action_generate(content_dir, templates_dir, static_dir, destination_dir):
    """
    Callback for the `generate` action.

    Parameters
    ----------
    content_dir: str
        Path to directory with input Markdown files.
    templates_dir: str
        Path to directory with Jinja templates.
    static_dir: str
        Path to directory with static files (CSS, images etc.).
    destinatation_dir: str
        Path to directory where to put the generated files.
    """
    env = Environment(loader=FileSystemLoader(templates_dir))
    env.filters['markdownify'] = markdownify
    try:
       template = env.get_template('main.j2')
    except:
       raise Exception ("no template found")
    #https://jinja.palletsprojects.com/en/2.11.x/api/

    if os.path.isdir(static_dir):
            distutils.dir_util.copy_tree(static_dir, destination_dir)

    for (file_in, file_in_rel, relative_dirname) in files.relative_paths_walk(content_dir, '*.md'):
            dir_out = os.path.join(destination_dir, relative_dirname)
            file_out = os.path.join(destination_dir, get_html_filename(file_in_rel))

            pathlib.Path(dir_out).mkdir(parents=True, exist_ok=True)
            generate_one_file(template, [], content_dir, file_in, file_out)


def main():
    """
    Entry point of the whole program.

    Only parses command-line arguments and executes the right callback.
    """

    args = argparse.ArgumentParser(description='My SSG')
    args_sub = args.add_subparsers(help='Select what to do')
    args.set_defaults(action='help')
    args_help = args_sub.add_parser('help', help='Show this help.')
    args_help.set_defaults(action='help')

    args_version = args_sub.add_parser(
        'version',
        help='Show version of this tool.'
    )
    args_version.set_defaults(action='version')

    args_generate = args_sub.add_parser(
        'generate',
        help='Generate the web.'
    )
    args_generate.set_defaults(action='generate')
    args_generate.add_argument(
        '--content',
        dest='content_dir',
        default='content/',
        metavar='PATH',
        help='Directory with source (content) files.'
    )
    args_generate.add_argument(
        '--templates',
        dest='templates_dir',
        default='templates/',
        metavar='PATH',
        help='Directory with Jinja templates.'
    )
    args_generate.add_argument(
        '--static',
        dest='static_dir',
        default='static/',
        metavar='PATH',
        help='Directory with static files (images, styles, ...).'
    )
    args_generate.add_argument(
        '--destination',
        dest='destination_dir',
        default='out/',
        metavar='PATH',
        help='Directory where to store the result.'
    )

    if len(sys.argv) < 2:
        # pylint: disable=too-few-public-methods,missing-class-docstring
        class HelpConfig:
            def __init__(self):
                self.action = 'help'
        config = HelpConfig()
    else:
        config = args.parse_args()

    if config.action == 'help':
        args.print_help()
    elif config.action == 'version':
        print("1.0")
    elif config.action == 'generate':
        action_generate(
            config.content_dir,
            config.templates_dir,
            config.static_dir,
            config.destination_dir
        )
    else:
        raise Exception("Internal error, unknown action")

if __name__ == '__main__':
    main()
