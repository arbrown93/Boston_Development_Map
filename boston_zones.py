import shapefile as shp


zipcode = '02122'
sf = shp.Reader("../shapefiles/boston_parcels/boston_parcels")
i=0

for shape in sf.shapeRecords():
    if (i<=1):
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        print(shape.record())
        i+=1
        break