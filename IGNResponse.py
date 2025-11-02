import json
import os
from qgis.PyQt.QtCore import QFile, QTextStream


class IGNResponse:

    def __init__(self, path_to_json):
        self.path_to_json = path_to_json

    def read_json_from_file(self):
        """Reads json file and returns string

        Returns:
            str: json data from file
        """
        file = QFile(self.path_to_json)
        if file.open(QFile.ReadOnly | QFile.Text):
            text_stream = QTextStream(file)
            data = text_stream.readAll()
            data = json.loads(data)
            print("Loaded:", data)
        else:
            print("Could not open response.json resource")

        return json.dumps(data) 

