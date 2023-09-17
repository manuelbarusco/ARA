"""
This script will extract the scores needed for a paired T-Test of the runs
"""

import os
import subprocess
import csv


"""
This function will create the csv output scores file
@param: output_scores_path, path to the output scores file
@param: trec_eval, string with the trec_eval results
@param: score, string with the score
"""
def generateOutputCSV(output_scores_path: str, trec_eval, score: str):
    output_scores_file = open(output_scores_path, "w")
    fieldnames = ['query_id', score]
    csv_writer = csv.writer(output_scores_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(fieldnames)

    lines = trec_eval.split("\n")
    for line in lines:
        split = line.split("\t")
        if len(split) == 1:
            break

        query_id = split[1]

        if query_id != "all":

            ndcg = float(split[2])

            row = [query_id, ndcg]
            csv_writer.writerow(row) 

    output_scores_file.close()

"""
This function will create the csv output scores files for the ACORDAR runs
@param: run_path, directory path where all the runs are scored
@param: no_empty, flag that indicates if we have to consider the qrels with empty datasets
"""
def generateAcordarScores(directory_run_path:str, no_empty:bool):
    scores = ["ndcg_cut.5","ndcg_cut.10","map_cut.5","map_cut.10"]
    configurations = ["[d]", "[m]", "[m+d]"]
    similarities = ["BM25", "TF-IDF", "LMD", "FSDM"]

    scores_directory = None

    if no_empty:
        scores_directory = directory_run_path +"/scores-noempty"
    else:
        scores_directory = directory_run_path +"/scores"


    #create the directory for the scores
    if not os.path.exists(scores_directory):
        os.makedirs(scores_directory)

    for configuration in configurations:
        #create the directory
        output_directory = scores_directory

        if configuration == "[m]":
            output_directory = scores_directory +"/metadata"
        elif configuration == "[d]":
            output_directory = scores_directory +"/data"
        elif configuration == "[m+d]":
            output_directory = scores_directory +"/full"
        
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        for similarity in similarities:

            run_file_path = directory_run_path + "/" + similarity + configuration + ".txt"

            for score in scores:

                output_scores_path = output_directory + "/" + similarity + score + ".csv"

                qrels = None

                if no_empty:
                    qrels = qrels_noempty_path
                else:
                    qrels = qrels_path
        
                #launch the trec_eval command for generating the scores
                trec_eval = subprocess.run(
                        [trec_eval_path, '-c', '-q', '-m', score, qrels, run_file_path], stdout=subprocess.PIPE).stdout.decode('UTF-8')

                #generate our scores file
                generateOutputCSV(output_scores_path, trec_eval, score)
        
"""
This function will create the csv output scores files for the ARDFS runs
@param: run_path, directory path where all the runs are scored
@param: no_empty, flag that indicates if we have to consider the qrels with empty datasets
"""
def generateARDFScores(directory_run_path:str, no_empty:bool):
    scores = ["ndcg_cut.5","ndcg_cut.10","map_cut.5","map_cut.10"]
    configurations = ["[d]", "[m]", "[m+d]"]
    #configurations = ["[m]"]
    similarities = ["BM25Boost", "TFIDFBoost", "LMDBoost", "FSDM"]

    scores_directory = None

    if no_empty:
        scores_directory = directory_run_path +"/scores-noempty"
    else:
        scores_directory = directory_run_path +"/scores"

    #create the directory for the scores
    if not os.path.exists(scores_directory):
        os.makedirs(scores_directory)

    for configuration in configurations:
        #create the directory
        output_directory = scores_directory

        if configuration == "[m]":
            output_directory = scores_directory +"/metadata"
        elif configuration == "[d]":
            output_directory = scores_directory +"/data"
        elif configuration == "[m+d]":
            output_directory = scores_directory +"/full"
        
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        for similarity in similarities:

            run_file_path = directory_run_path + "/" + similarity + configuration + ".txt"

            for score in scores:

                output_scores_path = output_directory + "/" + similarity + score + ".csv"

                qrels = None

                if no_empty:
                    qrels = qrels_noempty_path
                else:
                    qrels = qrels_path
        
                #launch the trec_eval command for generating the scores
                trec_eval = subprocess.run(
                        [trec_eval_path, '-c', '-q', '-m', score, qrels, run_file_path], stdout=subprocess.PIPE).stdout.decode('UTF-8')

                #generate our scores file
                generateOutputCSV(output_scores_path, trec_eval, score)
        

if __name__ == "__main__":

    dirname = os.path.dirname(__file__)

    #trec eval executable
    trec_eval_path = "/home/manuel/Tesi/TREC/trec_eval/trec_eval"

    #input files
    qrels_path = os.path.join(dirname, f'../../files/qrels.txt')
    qrels_noempty_path = os.path.join(dirname, f'../../output/qrels_without_empty.txt')
    
    #flag for considering qrels with empty datasets or not
    no_empty = True

    #generateAcordarScores(os.path.join(dirname, f'../../files/run/ACORDAR'), no_empty)
    
    generateARDFScores(os.path.join(dirname, f'../../files/run/ARDFS/Stream_Deduplication'), no_empty)


