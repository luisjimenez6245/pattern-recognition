from .utils import BaseModel
from .Characteristic import Characteristic
from collections import OrderedDict
from utils import get_centroid

class Class(BaseModel):
    name = ""
    characteristics = {}
    items = []
    z = []

    def load_items(self, items: list):
        helper_characteristics = {}
        for item in items:
            for characteristic in item.characteristics:
                if(characteristic not in helper_characteristics):
                    helper_characteristics[characteristic] = []
                helper_characteristics[characteristic].append(
                    item.characteristics[characteristic])
        characteristics = {}
        for characteristic in helper_characteristics:
            characteristics[characteristic] = Characteristic(
                name=characteristic,
                data=helper_characteristics[characteristic],
                centroide=get_centroid(
                    helper_characteristics[characteristic]
                ),
            )
        characteristics = OrderedDict(characteristics)
        z = []
        for characteristic in characteristics:
            z.append(characteristics[characteristic].centroide)
        self.z = z
        self.characteristics = characteristic
        return self