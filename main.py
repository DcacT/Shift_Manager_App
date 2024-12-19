import os
from .helpers.config import config_actions
from .helpers.csv import csv_actions
config_actions.setup_cfg()
data = csv_actions.generate_empty_availability_data(start_from_scratch=True)
csv_actions.write_availability_data(data, 'new_sample.csv')