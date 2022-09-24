from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 800
height = 800

# Materiales

brick = Material(diffuse = (2.55, 1.27, 0.8), spec = 16,matType = OPAQUE)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8,matType = OPAQUE)

mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior=1.5, matType = TRANSPARENT)
pinkglass = Material(diffuse = (1.55, 0.92, 1.03), spec = 64, ior=1.5, matType = TRANSPARENT)


rtx = Raytracer(width, height)

rtx.envMap = Texture("parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1), intensity = 0.8 ))
#rtx.lights.append( PointLight(point = (0,0,0)))

rtx.scene.append( Sphere(V3(-3,1,-10), 1, glass)  )
rtx.scene.append( Sphere(V3(0,1,-10), 1, pinkglass)  )
rtx.scene.append( Sphere(V3(3,1,-10), 1, brick)  )
rtx.scene.append( Sphere(V3(-3,-3,-10), 1, stone)  )
rtx.scene.append( Sphere(V3(0,-3,-10), 1, mirror)  )
rtx.scene.append( Sphere(V3(3,-3,-10), 1, mirror)  )

rtx.glRender()

rtx.glFinish("output.bmp")