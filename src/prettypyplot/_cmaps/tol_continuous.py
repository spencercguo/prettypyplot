"""Bownair colormap.

This is self-defined colormap generated with viscm.

BSD 3-Clause License
Copyright (c) 2020-2021, Daniel Nagel
All rights reserved.

"""
# ~~~ IMPORT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from matplotlib import colors as clr

# ~~~ CMAP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CM_SUNSET_DATA = [
    "#364B9A",
    "#4A7BB7",
    "#6EA6CD",
    "#98CAE1",
    "#C2E4EF",
    "#EAECCC",
    "#FEDA8B",
    "#FDB366",
    "#F67E4B",
    "#DD3D2D",
    "#A50026",
]

CM_NIGHTFALL_DATA = [
    "#125A56",
    "#00767B",
    "#238F9D",
    "#42A7C6",
    "#60BCE9",
    "#9DCCEF",
    "#C6DBED",
    "#DEE6E7",
    "#ECEADA",
    "#F0E6B2",
    "#F9D576",
    "#FFB954",
    "#FD9A44",
    "#F57634",
    "#E94C1F",
    "#D11807",
    "#A01813",
]

CM_YLORBR_DATA = [
    "#FFFFE5",
    "#FFF7BC",
    "#FEE391",
    "#FEC44F",
    "#FB9A29",
    "#EC7014",
    "#CC4C02",
    "#993404",
    "#662506",
]

CM_IRIDESCENT_DATA = [
    "#FEFBE9",
    "#FCF7D5",
    "#F5F3C1",
    "#EAF0B5",
    "#DDECBF",
    "#D0E7CA",
    "#C2E3D2",
    "#B5DDD8",
    "#A8D8DC",
    "#9BD2E1",
    "#8DCBE4",
    "#81C4E7",
    "#7BBCE7",
    "#7EB2E4",
    "#88A5DD",
    "#9398D2",
    "#9B8AC4",
    "#9D7DB2",
    "#9A709E",
    "#906388",
    "#805770",
    "#684957",
    "#46353A",
]

CM_INCANDESCENT_DATA = [
    "#CEFFFF",
    "#C6F7D6",
    "#A2F49B",
    "#BBE453",
    "#D5CE04",
    "#E7B503",
    "#F19903",
    "#F6790B",
    "#F94902",
    "#E40515",
    "#A80003",
]


def _sunset():
    return clr.LinearSegmentedColormap.from_list("sunset", CM_SUNSET_DATA)


def _nightfall():
    return clr.LinearSegmentedColormap.from_list(
        "nightfall", CM_NIGHTFALL_DATA
    )


def _ylorbr():
    return clr.LinearSegmentedColormap.from_list("YlOrBr", CM_YLORBR_DATA)


def _iridescent():
    return clr.LinearSegmentedColormap.from_list(
        "iridescent", CM_IRIDESCENT_DATA
    )


def _incandescent():
    return clr.LinearSegmentedColormap.from_list(
        "incandescent", CM_INCANDESCENT_DATA
    )
