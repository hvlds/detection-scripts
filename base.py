import os
from utils import *
from create_catkin_ws import build_catkin_ws
from create_colcon_ws import build_colcon_ws
from create_bridge_ws import build_bridge_ws
from camera import only_irmarker
import click

def make_subdirs(base_dir):
    os.mkdir(base_dir + "/bridge_ws")
    os.mkdir(base_dir + "/colcon_ws")
    os.mkdir(base_dir + "/catkin_ws")

@click.group()
def cli():
    pass

@cli.command()
def install():
    click.echo("Installing...")

@cli.command()
def launch_irmarker():
    click.echo("Launching IRMarker...")
    # only_irmarker()

if __name__ == "__main__":
    cli()

# if __name__ == "__main__":
#     check_directory(detection_ws)
#     make_subdirs(detection_ws)