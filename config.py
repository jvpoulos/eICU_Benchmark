import json
import os

pe = os.path.exists
pj = os.path.join
HOME = os.path.expanduser("~")

class Config():
    def __init__(self, args):
        self.seed = 36

        # data dir
        self.root_dir = pj( HOME, "Datasets/EHRs/eICU/eICU_benchmark" )
        self.eicu_dir = pj( HOME, "Datasets/EHRs/eICU/csv" )
        self.output_dir = pj( HOME, "Training/eICU_benchmark" )

        # task details
        self.task = args.task #['phen', 'dec', 'mort', 'rlos']
        self.num = args.num #
        self.cat = args.cat #  
        self.n_cat_class = 429        

        self.k_fold = 5
        #model params
        self.model_dir = ''
        self.embedding_dim = 5
        self.epochs = 100
        self.batch_size = 512
        self.save_freq = 500

        self.ann = args.ann #
        self.ohe = args.ohe #
        self.mort_window = args.mort_window #48 
        self.lr = 0.0001
        self.dropout = 0.3
        self.rnn_layers = 2
        self.rnn_units = [64, 64]


        # decompensation
        self.dec_cat = ['apacheadmissiondx', 'ethnicity', 'gender',
                'GCS Total', 'Eyes', 'Motor', 'Verbal']
        self.dec_num = ['admissionheight', 'admissionweight', 'age',
                'Heart Rate', 'MAP (mmHg)','Invasive BP Diastolic',
                'Invasive BP Systolic', 'O2 Saturation', 'Respiratory Rate',
                'Temperature (C)', 'glucose', 'FiO2', 'pH']

        #phenotyping
        self.col_phe = ["Respiratory failure", "Fluid disorders",
                "Septicemia", "Acute and unspecified renal failure",
                "Pneumonia", "Acute cerebrovascular disease",
                "Acute myocardial infarction", "Gastrointestinal hem", "Shock",
                "Pleurisy", "lower respiratory", "Complications of surgical",
                "upper respiratory", "Hypertension with complications",
                "Essential hypertension", "CKD", "COPD", "lipid disorder",
                "Coronary athe", "DM without complication",
                "Cardiac dysrhythmias", "CHF", "DM with complications",
                "Other liver diseases", "Conduction disorders"]

    def write(self, session_str):
        """
        Write all parameter values to pj(self.output_dir, session_str)
        """

        config_dir = pj(self.output_dir, session_str)
        if not pe(config_dir):
            os.makedirs(config_dir)
        config_path =  pj(config_dir, "config.json")
        json.dump(self.__dict__, open(config_path, "w"), indent=4)

