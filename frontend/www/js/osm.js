import 'ol/ol.css';
import Feature from 'ol/Feature';
import Map from 'ol/Map';
import View from 'ol/View';
import Point from 'ol/geom/Point';
import {Circle as CircleStyle, Fill, Icon, Stroke, Style} from 'ol/style';

function renderMap(divname, nearbyPeople){
    var map = new ol.Map({
        target: divname,
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM()
            })
        ],
        view: new ol.View({
            center: ol.proj.fromLonLat([coords['longitude'], coords['latitude']]),
            zoom: 16
        })
    });

    var styles = {
        'pmatch': new Style({
            image: new Icon({
                anchor: [0, 0],
                src: '../img/hungry.png'
            })
        }),
        'icon': new Style({
            image: new CircleStyle({
                radius: 7,
                fill: new Fill({color: 'black'}),
                stroke: new Stroke({
                    color: 'white', width: 2
                })
            })
        })
    };
    let featurelist = [];
    featurelist.push(new Feature({
        type: 'icon',
        geometry: new Point([coords['longitude'], coords['latitude']])
    }));
    for(let i of nearbyPeople){
        featurelist.push(new Feature({
            type: 'pmatch',
            geometry: new Point([i['longitude'], i['latitude']])
        }));
    }
    var vectorLayer = new VectorLayer({
        source: new VectorSource({
            features: featurelist
        }),
        style: function(feature) {
            return styles[feature.get('type')];
        }
    });

}
let coords = [-127, 89]
renderMap("map", []);
