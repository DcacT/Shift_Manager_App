import os
from .helpers.config import config_actions
from .helpers.csv import csv_actions
config_actions.setup_cfg()
csv_actions.generate_empty_availability_data(start_from_scratch=True)
