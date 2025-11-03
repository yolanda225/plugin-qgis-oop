import requests

URL = "https://data.geopf.fr/navigation/getcapabilities"

class IGNCapabilities:
    
    def __init__(self, url):
        self.url = url
        self.json_data = self.request_capabilities()

    def request_capabilities(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
        with open('capabilities.json', 'wb') as f:
            f.write(response.content)
        return response.json()

    def populate_comboBox(self, resource, id, combo_box):
        """populate the combo box with available parameters inside the getcapabilities response

        Args:
            resource (str): one of "bdtopo-pgr", "bdtopo-valhalla", "pgr_sgl_r100_all"
            id (str): one of 'point', 'bbox','costValue', 'profile', 'direction', 'projection', 'geometryFormat', 'timeUnit', 'constraints'
            combo_box (PyQt5.QtWidgets.QComboBox): combo box of dialogue to be populated
        """
        resources = self.json_data.get("resources", [])
        res = next((r for r in resources if r.get("id") == resource), None)
        if not res:
            return
        operation = next((op for op in res.get("availableOperations", []) if op.get("id") == "isochrone"), None)
        if not operation:
            return
        parameter = next((p for p in operation.get("availableParameters", []) if p.get("id") == id), None)
        if not parameter:
            return
        combo_box.addItems(parameter.get("values", []))