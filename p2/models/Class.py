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
        helper_items = []
        counter_charac = 0
        for characteristic in characteristics:
            data = characteristics[characteristic].data
            i = 0
            for item in data:
                if(counter_charac) == 0:
                    helper_items.append([])
                helper_items[i].append(item)
                i += 1
            z.append(characteristics[characteristic].centroide)
            counter_charac += 1
        self.z = z
        self.items = (helper_items)
        self.characteristics = characteristics
        return self

    def update_model(self, value):
        for key in value:
            self.characteristics[key].data.append(value[key])
            self.characteristics[key].centroide = get_centroid(
                self.characteristics[key].data
            )
        characteristics = OrderedDict(self.characteristics)
        z = []
        for characteristic in characteristics:
            z.append(characteristics[characteristic].centroide)
        self.z = z
        
