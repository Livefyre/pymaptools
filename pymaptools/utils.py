import collections
from copy import deepcopy
from pkg_resources import resource_filename
from contextlib import contextmanager


def deepupdate(dest, source):
    """Recursively update one dict with contents of another

    :param dest: mapping being updated
    :type dest: dict
    :param source: mapping to update with
    :type source: collections.Mapping
    :return: updated mapping
    :rtype: dict
    """
    for key, value in source.iteritems():
        dest[key] = deepupdate(dest.get(key, {}), value) \
            if isinstance(value, collections.Mapping) \
            else value
    return dest


def override(parent, child):
    """Inherit child from parent and return a new object
    """
    return deepupdate(deepcopy(parent), child)


def read_text_file(rel, fname):
    """Read a text resource ignoring comments beginning with pound sign
    :param rel: path
    :type rel: str
    :param fname: path
    :type fname: str
    :rtype: generator
    """
    with open(resource_filename(rel, fname), 'r') as fhandle:
        for line in fhandle:
            stripped = line.strip()
            if not stripped.startswith('#'):
                yield stripped


@contextmanager
def empty_context(*args, **kwargs):
    """Generic empty context wrapper
    """
    yield None
