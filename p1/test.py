from utils import gen_random_arr, gen_item_dict
from controllers import Grapher, Classifier
from utils.data import apple, orange, mango

classifier = Classifier([apple, orange, mango])

print(classifier.get_probability('85', 'weigth'))