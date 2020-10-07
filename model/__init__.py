import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from model.iris_model import IrisModel
from model.crime import CrimeModel
from model.cctv import CctvModel

if __name__ == '__main__':
    # iris = IrisModel()
    # iris.draw_scatter()
    # iris.draw_errors()
    # iris.plot_decision_regions()
    iris.draw_adaline_graph()
    # iris.draw_adaline_gd_graph()