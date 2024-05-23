from georecl.geoserver import Geoserver

authkey='5b59b9ef-39bb-41e5-b7e5-10c028d6e41c'
client=Geoserver(url='http://localhost:3000/geoserver',authkey=authkey)
res= client.get('http://localhost:3000/geoserver/rest/layers.xml')
print(res.content)