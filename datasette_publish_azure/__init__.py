from datasette import hookimpl
from datasette.publish.common import (
    add_common_publish_arguments_and_options,
    # fail_if_publish_binary_not_installed,
)
from datasette.utils import (
    # temporary_docker_directory,
    value_as_boolean,
    ValueAsBooleanError,
)

# from subprocess import run
import click
from click.types import CompositeParamType


class Setting(CompositeParamType):
    name = "setting"
    arity = 2

    def convert(self, config, param, ctx):
        from datasette.app import DEFAULT_SETTINGS

        name, value = config
        if name not in DEFAULT_SETTINGS:
            self.fail(
                f"{name} is not a valid option (--help-config to see all)",
                param,
                ctx,
            )
            return
        # Type checking
        default = DEFAULT_SETTINGS[name]
        if isinstance(default, bool):
            try:
                return name, value_as_boolean(value)
            except ValueAsBooleanError:
                self.fail(f'"{name}" should be on/off/true/false/1/0', param, ctx)
                return
        elif isinstance(default, int):
            if not value.isdigit():
                self.fail(f'"{name}" should be an integer', param, ctx)
                return
            return name, int(value)
        elif isinstance(default, str):
            return name, value
        else:
            # Should never happen:
            self.fail("Invalid option")


@hookimpl
def publish_subcommand(publish):
    @publish.command()
    @add_common_publish_arguments_and_options
    @click.option(
        "--name",
        help="Azure Functions function name to use",
        required=True,
    )
    @click.option(
        "--generate-dir",
        type=click.Path(dir_okay=True, file_okay=False),
        help="Output generated application files here",
    )
    @click.option(
        "--setting",
        "settings",
        type=Setting(),
        help="Setting, see docs.datasette.io/en/stable/settings.html",
        multiple=True,
    )
    def azure(*args, **kwargs):
        "Publish to Azure Functions"
        click.echo("Not yet implemented", err=True)
