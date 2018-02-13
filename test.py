import json
import matplotlib.pyplot as plot

with open('io-exercises/data.json', 'r') as fh:
    data = json.load(fh)
    plot.plot(data['data'])
    plot.show()
    plot.close()