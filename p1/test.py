from utils import gen_random_arr, gen_item_dict
from controllers import Grapher
from utils.data import apple, orange

class Classifier():

    def __init__(self, objs: list):
        total_objs = 0
        for obj in objs:
            total_objs += obj.size
        data = {}
        for obj in objs:
            obj.p = obj.size / total_objs
            for characteristic in obj.characteristics:
                if characteristic not in data:
                    data[characteristic] = {}
                for item in obj.characteristics[characteristic].data:
                    if(item not in data[characteristic]):
                        data[characteristic][item] = {}
                    data[characteristic][item][obj.name] = obj.characteristics[characteristic].data[item]
        self.objs = objs
        self.total_objs = total_objs
        self.data = data


    def get_probability(self, prox_data, prox_key):
        result = {}
        if(prox_data in self.data[prox_key]):
            total_item_in_key  = 0
            items  = self.data[prox_key][prox_data]
            for item in items: 
                total_item_in_key += items[item]
            for obj in self.objs:
                result[obj.name] = 0
                characteristic = obj.characteristics[prox_key]
                if prox_data in characteristic.data:
                    total_coincidences = characteristic.data[prox_data]
                    p_b_a = total_coincidences / obj.size
                    p_b = total_item_in_key / self.total_objs
                    p_a = obj.size / self.total_objs
                    result[obj.name] = (p_b_a/p_b)*p_a
        return result
    

prox_data = '85'
prox_key = "weigth"
classifier = Classifier([apple, orange])
print(classifier.get_probability(prox_data, prox_key))