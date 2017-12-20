import owstk

#  sc, root, app = owstk.stk.new()
sc, root, app = owstk.stk.current()

satellites = owstk.oneweb.gen1.addSS3Constellation(sc, [0, 1, 410])
facilities = owstk.oneweb.gen1.addSNPs(sc, [4, 10])
sensors = owstk.oneweb.gen1.attachUserAntennas(satellites[0])
sensors = owstk.oneweb.gen1.attachUserAntennas(satellites[1])
