import ee
ee.Authenticate()
ee.Initialize(project='tempelhofer-feld')

print(ee.String('Hello from the Earth Engine servers!').getInfo())