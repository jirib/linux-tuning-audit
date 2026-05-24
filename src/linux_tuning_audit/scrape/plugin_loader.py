# scrape/registry.py

import importlib
import pkgutil
from types import ModuleType

import linux_tuning_audit.scrape.plugins as plugin_package


def iter_plugins() -> list[ModuleType]:
    """
    Discover and import all scrape plugins.
    """
    plugins: list[ModuleType] = []

    for module_info in pkgutil.iter_modules(plugin_package.__path__):
        name = module_info.name

        if name.startswith("_"):
            continue

        module = importlib.import_module(
            f"{plugin_package.__name__}.{name}"
        )
        plugins.append(module)

    return plugins


def plugin_name(plugin: ModuleType) -> str:
    """
    Derive the profile name from the plugin module name.
    """
    return plugin.__name__.rsplit(".", 1)[-1]


def discover_plugins() -> dict[str, ModuleType]:
    """
    Discover and import all scrape plugins, returning a mapping of profile
    name to plugin module.
    """
    return {
        plugin_name(plugin): plugin
        for plugin in iter_plugins()
    }


def load_plugins_for_profiles(profiles: list[str]) -> list[ModuleType]:
    """
    Load the scrape plugins corresponding to the specified profile names.
    """
    available = discover_plugins()
    selected: list[ModuleType] = []

    for profile in profiles:
        try:
            selected.append(available[profile])
        except KeyError:
            raise ValueError(f"No scrape plugin found for profile: {profile}")

    return selected