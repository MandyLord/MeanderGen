from __future__ import annotations
from dataclasses import dataclass
from math import hypot, radians, sin, cos

@dataclass(frozen=True)
class Vector:
    x: float
    y: float
    @property
    def length(self)->float:
        return hypot(self.x,self.y)
    def normalized(self)->'Vector':
        l=self.length
        return Vector(0.0,0.0) if l==0 else Vector(self.x/l,self.y/l)
    def scaled(self,f:float)->'Vector':
        return Vector(self.x*f,self.y*f)
    def rotated(self,degrees:float)->'Vector':
        a=radians(degrees)
        return Vector(self.x*cos(a)-self.y*sin(a), self.x*sin(a)+self.y*cos(a))

@dataclass(frozen=True)
class Point:
    x: float
    y: float
    def distance_to(self,other:'Point')->float:
        return hypot(other.x-self.x, other.y-self.y)
    def translate(self,v:Vector)->'Point':
        return Point(self.x+v.x,self.y+v.y)
    def vector_to(self,other:'Point')->Vector:
        return Vector(other.x-self.x, other.y-self.y)
    def as_tuple(self):
        return (self.x,self.y)
