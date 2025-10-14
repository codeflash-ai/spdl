# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

# pyre-unsafe

from spdl.io.lib import _libspdl_cuda

# Cache NVCODEC availability result to avoid costly repeated FFI calls
_built_with_nvcodec: bool | None = None

__all__ = [
    "built_with_cuda",
    "built_with_nvcodec",
    "built_with_nvjpeg",
]


def built_with_cuda() -> bool:
    """Check if SPDL is compiled with CUDA support.

    Returns:
        True if SPDL is compiled with CUDA support and
        the related libraries are properly loaded.
    """
    try:
        return _libspdl_cuda.built_with_cuda()
    except Exception:
        return False


def built_with_nvcodec() -> bool:
    """Check if SPDL is compiled with NVCODEC support.

    Returns:
        True if SPDL is compiled with NVCODEC support and
        the related libraries are properly loaded.
    """
    global _built_with_nvcodec
    if _built_with_nvcodec is not None:
        return _built_with_nvcodec
    try:
        _built_with_nvcodec = _libspdl_cuda.built_with_nvcodec()
        return _built_with_nvcodec
    except Exception:
        _built_with_nvcodec = False
        return False


def built_with_nvjpeg() -> bool:
    """Check if SPDL is compiled with NVJPEG support.

    Returns:
        True if SPDL is compiled with NVJPEG support and
        the related libraries are properly loaded.
    """
    try:
        return _libspdl_cuda.built_with_nvjpeg()
    except Exception:
        return False
