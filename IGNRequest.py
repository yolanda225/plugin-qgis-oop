import requests
import json

BASE_URL = "https://data.geopf.fr/navigation/isochrone?"

class IGNRequest:

    def __init__(self, resource, point, costValue, costType="time", profile="car", direction="departure", crs="EPSG:4326", geometryFormat="geojson", timeUnit="second", constraints=""):
        """initialize IGNRequest object

        Args:
            resource (string): resource used by the calculation, e.g. "bduni"
            point (string): starting point of calculation, e.g. "2.337306,48.849319"
            costValue (float): Value of the criterion used for the calculation (time or distance), e.g. 100
            costType (string): calculation method used (time or distance)
            profile (string): Means of transport used for the calculation, example "car"
            direction (string): Direction of travel used for the calculation, example	"departure"
            crs (enum): Projection used to express coordinates and retrieve geometries, example	"EPSG:4326"
            geometryFormat (enum): Geometry encoding format, e.g. "geojson"
            timeUnit (enum): unit of duration, example	"minute"
            constraints (array): Constraints used for the calculation, example	"{'constraintType':'banned','key':'ways_type','operator':'=','value':'autoroute'}"
        """     
        self.resource = resource
        self.point = point
        self.costValue = costValue
        self.costType = costType
        self.profile = profile
        self.direction = direction
        self.crs = crs
        self.geometryFormat = geometryFormat
        self.timeUnit = timeUnit
        self.constraints = constraints

    def _build_url(self):
        """build the request url with help of the attributes

        Returns:
            str: request url
        """
        url = BASE_URL
        attributes = vars(self)
        #attr_req = {k: v for i, (k, v) in enumerate(attributes.items()) if i < 4}
        for key in attributes:
            url += f"{key}={attributes[key]}&"
        #url = url.rstrip("&") #remove last &
        return url
        
    def do_request(self):
        """send the request and save response to json file
        """
        url = self._build_url()
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
        with open('response.json', 'wb') as f:
            f.write(response.content)
        data = json.loads(response.content)
        geometry = data["geometry"] # needed for windows
        s = json.dumps(geometry)
        return s

# testing
ign_request = IGNRequest("bdtopo-valhalla", "2.337306,48.849319", 100)
ign_request.do_request()
