p = "C:/Users/kency/AppData/Local/Temp/repos/r1-minetest-mc/index.html"
s = open(p).read()
old = """  player.x += player.vx*dt*0.12;
  player.z += player.vy? player.vz*dt*0.12 : 0;
  player.y += player.vy*dt*0.12;"
new = """  player.x += player.vx*dt*0.08;
  player.z += player.vz*dt*0.08;
  player.y += player.vy*dt*0.08;"
s = s.replace(old,new,1)
open(p,'w').write(s)
print('done')
"""
s = s.replace(old,new,1)
open(p,'w').write(s)
print("done")