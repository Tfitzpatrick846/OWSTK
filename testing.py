import owstk

if 'app' not in vars():
    app = owstk.stk.app()

if 'root' not in vars():
    root = owstk.stk.root(app)

if 'sc' not in vars():
    sc = owstk.stk.newScenario(root)

satellites = owstk.oneweb.gen1.addSS3Constellation(sc, [0, 1, 410])
facilities = owstk.oneweb.gen1.addSNPs(sc, [4, 10])
sensors = owstk.oneweb.gen1.attachUserAntennas(satellites[0])
sensors = owstk.oneweb.gen1.attachUserAntennas(satellites[1])
