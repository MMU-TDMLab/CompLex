#!/usr/bin/env python3
import csv
import os.path
from collections import defaultdict
import glob
import sys
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from scipy.stats import pearsonr, spearmanr
    
##################################################################################

if __name__ == "__main__":
    #Get input and output dirs:
    [_, input_dir, output_dir] = sys.argv
    
    #Create submission and reference folder paths:
    submission_dir = os.path.join(input_dir, 'res')
    reference_dir = os.path.join(input_dir, 'ref')
    
    result = ''
    
    #Get the submission path:
    submission_fname = os.listdir(submission_dir)[0]
    submission = os.path.join(submission_dir, submission_fname)
    
    #Get the reference path:
    labels_fname = os.listdir(reference_dir)[0]
    reference_file = os.path.join(reference_dir, labels_fname)
    
    # If the question predictions file was supplied, run the scoring on it
    if os.path.exists(submission):
        
        #Read predictions:
        submission_dict = {}
        with open(submission, 'r') as sf:
            csv_reader = csv.reader(sf)
            for item in csv_reader:
                submission_dict[item[0]] = float(item[1])
        
        #Read reference:
        gold_dict = {}
        with open(reference_file, 'r') as rf:
            csv_reader = csv.reader(rf)
            for item in csv_reader:
                gold_dict[item[0]] = float(item[1])
    
        #Produce vectors with reference labels and predictions:
        gold = []
        predicted = []
        
        for key, label in gold_dict.items():
            gold.append(label)
            predicted.append(submission_dict[key])
        
        #Calculate scores:
        pearson_score = pearsonr(gold, predicted)[0]
        spearman_score = spearmanr(gold, predicted)[0]
        mae_score = mean_absolute_error(gold, predicted)
        mse_score = mean_squared_error(gold, predicted)
        rsq_score = r2_score(gold, predicted)
        result += "pearson:{0}\n".format(pearson_score)
        result += "spearman:{0}\n".format(spearman_score)
        result += "mae:{0}\n".format(mae_score)
        result += "mse:{0}\n".format(mse_score)
        result += "r2:{0}".format(rsq_score)
    
    # After all the data is processed, write the result to the output
    with open(os.path.join(output_dir, 'scores.txt'), 'w') as output_file:
        output_file.write(result)
