import folium
import pandas as pd

# map = folium.Map

# print(dir(folium))
# print(map)
# print(help(folium.map))


data = pd.read_csv('Volcanoes_USA.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])


# print(data)

def color_producer(elevation):
    if elevation < 1300:
        return 'orange'
    elif 1300 <= elevation <= 2500:
        return 'red'
    else:
        return 'blue'


map = folium.Map(location=[26.7, 82], zoom_start=6)
fgv = folium.FeatureGroup(name='Volcanoes')

for lt, ln, el in zip(lat, lon, elev):
    # fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + ' m', icon=folium.Icon(color=color_producer(el))))
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=7, popup=str(el)+' m',
                                     fill_color=color_producer(el), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
                            else 'green' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'purple'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save('Map1.html')
