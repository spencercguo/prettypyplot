# -*- coding: utf-8 -*-
"""Tests for the cmaps module.

BSD 3-Clause License
Copyright (c) 2020-2021, Daniel Nagel
All rights reserved.

"""
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

from prettypyplot import _cmaps as cmaps


def test_bownair():
    """Test bownair cmap."""
    assert isinstance(
        cmaps.bownair._bownair(),
        LinearSegmentedColormap,
    )


def test_macaw():
    """Test macaw cmap."""
    assert isinstance(
        cmaps.macaw._macaw(),
        LinearSegmentedColormap,
    )


def test_turbo():
    """Test turbo cmap."""
    assert isinstance(
        cmaps.turbo._turbo(),
        LinearSegmentedColormap,
    )


def test_sunset():
    """Test sunset cmap."""
    assert isinstance(
        cmaps.sunset._sunset(),
        LinearSegmentedColormap,
    )


def test_nightfall():
    """Test nightfall cmap."""
    assert isinstance(
        cmaps.nightfall._nightfall(),
        LinearSegmentedColormap,
    )


def test_ylorbr():
    """Test ylorbr cmap."""
    assert isinstance(
        cmaps.ylorbr._ylorbr(),
        LinearSegmentedColormap,
    )


def test_iridescent():
    """Test iridescent cmap."""
    assert isinstance(
        cmaps.iridescent._iridescent(),
        LinearSegmentedColormap,
    )


def test_incandescent():
    """Test incandescent cmap."""
    assert isinstance(
        cmaps.incandescent._incandescent(),
        LinearSegmentedColormap,
    )


def test_discrete():
    """Test discrete cmaps."""
    for cmap in (
        cmaps.discrete._pastel5(),
        cmaps.discrete._pastel6(),
        cmaps.discrete._cbf4(),
        cmaps.discrete._cbf5(),
        cmaps.discrete._cbf8(),
        cmaps.discrete._pastel_rainbow(),
        cmaps.discrete._pastel_spring(),
        cmaps.discrete._pastel_autunm(),
        cmaps.discrete._ufcd(),
        cmaps.discrete._paula(),
        cmaps.discrete._summertimes(),
    ):
        assert isinstance(cmap, ListedColormap)
