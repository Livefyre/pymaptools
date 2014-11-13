import collections
import uuid
from copy import deepcopy
from pkg_resources import resource_filename
from contextlib import contextmanager


def uuid1_to_posix(uuid1):
    """Convert a UUID1 timestamp to a standard POSIX timestamp

    >>> uuid1_to_posix("d64736cf-5bfa-11e4-a292-542696da2c01")
    1414209362.290043
    """
    uuid1 = uuid.UUID(uuid1)
    if uuid1.version != 1:
        raise ValueError('only applies to UUID type 1')
    return (uuid1.time - 0x01b21dd213814000) / 1e7


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
    """Deprecated"""
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
