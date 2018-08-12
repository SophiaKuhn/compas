from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import time

import compas
import compas_rhino

from compas_rhino.artists.mixins import VertexArtist
from compas_rhino.artists.mixins import EdgeArtist
from compas_rhino.artists.mixins import FaceArtist

try:
    import rhinoscriptsyntax as rs

except ImportError:
    compas.raise_if_ironpython()


__author__    = ['Tom Van Mele', ]
__copyright__ = 'Copyright 2016 - Block Research Group, ETH Zurich'
__license__   = 'MIT License'
__email__     = 'vanmelet@ethz.ch'


__all__ = ['VolMeshArtist']


class VolMeshArtist(FaceArtist, EdgeArtist, VertexArtist):
    """A volmesh artist defines functionality for visualising COMPAS volmeshes in Rhino.

    Parameters
    ----------
    volmesh : compas.datastructures.VolMesh
        A COMPAS volmesh.
    layer : str, optional
        The name of the layer that will contain the volmesh.

    Attributes
    ----------
    layer
    datastructure
    defaults : dict
        Default settings for color, scale, tolerance, ...

    """

    def __init__(self, volmesh, layer=None):
        self.datastructure = volmesh
        self.layer = layer
        self.defaults = {
            'color.vertex' : (255, 0, 0),
            'color.face'   : (255, 255, 255),
            'color.edge'   : (0, 0, 0),
        }

    def redraw(self, timeout=None):
        """Redraw the Rhino view."""
        if timeout:
            time.sleep(timeout)
        rs.EnableRedraw(True)
        rs.Redraw()

    def clear_layer(self):
        """Clear the main layer of the artist."""
        if self.layer:
            compas_rhino.clear_layer(self.layer)

    def clear(self):
        self.clear_vertices()
        self.clear_faces()
        self.clear_edges()


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":

    import compas

    from compas.datastructures import VolMesh
    from compas_rhino.artists.volmeshartist import VolMeshArtist

    volmesh = VolMesh.from_obj(compas.get('boxes.obj'))

    artist = VolMeshArtist(volmesh, layer='VolMeshArtist')

    artist.clear_layer()

    artist.draw_vertices()
    artist.redraw(0.0)

    artist.draw_vertexlabels()
    artist.redraw(1.0)

    artist.draw_faces()
    artist.redraw(1.0)

    artist.draw_facelabels()
    artist.redraw(1.0)

    artist.draw_edges()
    artist.redraw(1.0)

    artist.draw_edgelabels()
    artist.redraw(1.0)
