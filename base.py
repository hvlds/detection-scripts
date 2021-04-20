import os
from utils import *
from create_catkin_ws import build_catkin_ws
from create_colcon_ws import build_colcon_ws
from create_bridge_ws import build_bridge_ws
from camera import only_irmarker
from test import test_apriltag, test_irmarker
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
    """Create workspaces and install the dependendencies
    """
    click.echo("Installing...")

    # Create empty directories for the workspaces
    check_directory(detection_ws)
    make_subdirs(detection_ws)

    # Clone and build the projects on their respective workspaces
    # (ROS1, ROS2 and ros1_bridge)
    build_catkin_ws()
    build_colcon_ws()
    build_bridge_ws()

@cli.command()
def build():
    """Build all the workspaces
    """
    click.echo("Building...")

    # Clone and build the projects on their respective workspaces
    # (ROS1, ROS2 and ros1_bridge)
    build_catkin_ws()
    build_colcon_ws()
    build_bridge_ws()


@cli.command()
def launch_irmarker():
    """Launch the IRMarker detector
    """
    click.echo("Launching IRMarker...")
    only_irmarker()


@cli.command()
@click.option("-o", "--output", "output", required=True, type=str)
def apriltag(output):
    test_apriltag(output)

@cli.command()
@click.option("-o", "--output", "output", required=True, type=str)
def irmarker(output):
    test_irmarker(output)


if __name__ == "__main__":
    cli()
