import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
import rdkit
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential, save_model, load_model
from tensorflow import keras
import tensorflow as tf
tf.keras.backend.set_floatx('float64')
import os,sys

#load index of RDKit substructures used in machine learning models.
selected_keys = pickle.load(open("selected_keys.pickle","rb"))  
Corr_df = pd.DataFrame(selected_keys).reset_index()

#load pre-trained machine learning models for 7 different properties.
models = {}
for col in ['DensityValue', 'TensileModulusValue', 'TensileBreakValue', 'TgValue', 'TdValue', 'TmValue', 'TensileYieldValue']:
    models[col] = load_model(col + '_Ensemble_TrainAllData.model')

#load your own dataframe DF which need to have a "Smiles" column containing the SMILES of your polyimide molecules to be evaluated 
DF = pickle.load(open("Your own dataframe","rb"))  

#Process your molecules using the improved Morgan fingerprint featurization
molecules = DF.Smiles.apply(Chem.MolFromSmiles)
DF.loc[:,['molecules']] = molecules
DF = DF.dropna()

fp = Dataset1.molecules.apply(lambda m: AllChem.GetMorganFingerprint(m, radius=3))
fp_n = fp.apply(lambda m: m.GetNonzeroElements())

#build feature vector of your molecules
MY_finger = []
for polymer in fp_n:
    my_finger = [0] * len(unique_list)
    for key in polymer.keys():
        index = Corr_df[Corr_df[0] == key]['index'].values[0]
        my_finger[index] = polymer[key]
    MY_finger.append(my_finger)
MY_finger_df = pd.DataFrame(MY_finger)  

#make predicitons for your polyimide molecules based on our pre-trained models.
ML_results = pd.DataFrame(Y_pred, columns=['DensityValue', 'TensileModulusValue', 'TensileBreakValue', 'TgValue', 'TdValue', 'TmValue', 'TensileYieldValue'])
for col in ['DensityValue', 'TensileModulusValue', 'TensileBreakValue', 'TgValue', 'TdValue', 'TmValue', 'TensileYieldValue']:
    ML_results[col] = [i[0] for i in modles[col].predict((X_tg))]

