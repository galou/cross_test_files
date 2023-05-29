from __future__ import annotations

import FreeCAD as fc

from freecad.cross.joint import make_joint
from freecad.cross.link import make_link


def get_object(doc: fc.Document, label: str):
    objs = doc.getObjectsByLabel(label)
    if objs:
        return objs[0]


def rotx(angle_deg: float) -> fc.Rotation:
    return fc.Rotation(fc.Vector(1.0, 0.0, 0.0), angle_deg)


def roty(angle_deg: float) -> fc.Rotation:
    return fc.Rotation(fc.Vector(0.0, 1.0, 0.0), angle_deg)


def rotz(angle_deg: float) -> fc.Rotation:
    return fc.Rotation(fc.Vector(0.0, 0.0, 1.0), angle_deg)


def add_joint(
        robot: fc.DocumentObject,
        name: str,
        origin: fc.Placement,
        ) -> fc.DocumentObject:
    joint = make_joint(name)
    robot.addObject(joint)
    joint.Label2 = name
    joint.Origin = origin
    joint.Type = 'revolute'
    return joint


def add_cross_link(
        robot: fc.DocumentObject,
        name: str,
        name_visual: str,
        name_collision: str,
        mounted_placement: fc.Placement,
        ) -> fc.DocumentObject:
    doc = robot.Document
    cross_link = make_link(name)
    robot.addObject(cross_link)
    cross_link.Label2 = name
    cross_link.Visual = [get_object(doc, name_visual)]
    cross_link.Collision = [get_object(doc, name_collision)]
    cross_link.MountedPlacement = mounted_placement
    return cross_link
