# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""Utility functions."""

# pyre-unsafe

from . import _build, _ffmpeg, _tracing

_mods = [
    _build,
    _ffmpeg,
    _tracing,
]

__all__ = sorted(item for mod in _mods for item in mod.__all__)


def __dir__() -> list[str]:
    return __all__


def __getattr__(name: str):
    mapping = getattr(__getattr__, "__mod_attr_map", None)
    if mapping is None:
        mapping = {}
        for mod in _mods:
            for attr in mod.__all__:
                if attr not in mapping:
                    mapping[attr] = mod
        setattr(__getattr__, "__mod_attr_map", mapping)
    if name in mapping:
        return getattr(mapping[name], name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
