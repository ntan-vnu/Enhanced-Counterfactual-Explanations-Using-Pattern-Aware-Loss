DATA_DIR = '../datasets/BreakHis_v1/'
SUBSETS_FILE = DATA_DIR+'subsets.csv'
IMAGE_SIZE = (256, 256, 3)
CLASS_NAMES = ['mucinous_carcinoma',
               'ductal_carcinoma',
               'adenosis',
               'lobular_carcinoma',
               'fibroadenoma',
               'phyllodes_tumor',
               'tubular_adenoma',
               'papillary_carcinoma']
NUM_CLASS = len(CLASS_NAMES)
CHECKPOINTS_DIR = 'checkpoints/'
CLASSIFIER256_CHECKPOINT = CHECKPOINTS_DIR+'classifier256-20241119093200'
OUTPUTS_DIR = 'outputs/'