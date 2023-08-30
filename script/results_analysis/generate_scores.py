"""
This script will extract the scores needed for a given results analysis, so for example
the ndcg@5 for all the runs of a given query. 
"""

import os
import subprocess
import csv


"""
This function will create the csv output scores file
@param: output_scores_path, path to the output scores file
"""
def generateOutputCSV(output_scores_path: str):
    output_scores_file = open(output_scores_path, "w")
    fieldnames = ['query_id', "score"]
    csv_writer = csv.writer(output_scores_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(fieldnames)

    lines = trec_eval.split("\n")
    for line in lines:
        split = line.split("\t")
        if len(split) == 1:
            break

        query_id = split[1]
        ndcg = float(split[2])

        row = [query_id, ndcg]
        csv_writer.writerow(row) 

    output_scores_file.close()


if __name__ == "__main__":

    dirname = os.path.dirname(__file__)

    #param needed for retrieving the ACORDAR runs and my runs for the scores file production
    run_id = "Stream_Jena_LightRDF_Deduplication"
    configuration = "[d]"
    similarity = "BM25Boost"
    similarity_acordar = "BM25F"
    score = "P.10"

    #trec eval executable
    trec_eval_path = "/home/manuel/Tesi/TREC/trec_eval/trec_eval"

    #input files
    qrels_path = os.path.join(dirname, f'../../files/qrels.txt')
    run_file_path = os.path.join(dirname, f'../../files/run/ARDFS/{run_id}/{similarity}{configuration}.txt')
    acordar_run_path = os.path.join(dirname, f'../../files/run/ACORDAR/{similarity_acordar}{configuration}.txt')

    #output file
    output_scores_directory = os.path.join(dirname, f'../../files/run/ARDFS/{run_id}/scores')
    output_scores_path = os.path.join(dirname, f'../../files/run/ARDFS/{run_id}/scores/{similarity}{configuration}.csv')
    acordar_scores_path = os.path.join(dirname, f'../../files/run/ACORDAR/scores/{similarity_acordar}{configuration}.csv')

    #create directory for our scores if it does not exists 
    if not os.path.exists(output_scores_directory):
        os.makedirs(output_scores_directory)

    #launch the trec_eval command for generating our scores
    trec_eval = subprocess.run(
            [trec_eval_path, '-q', '-m', score, qrels_path, run_file_path], stdout=subprocess.PIPE).stdout.decode('UTF-8')

    #generate our scores file
    generateOutputCSV(output_scores_path)

    #create directory for ACORDAR scores if it does not exists 
    if not os.path.exists(output_scores_directory):
        os.makedirs(output_scores_directory)

    #launch the trec_eval command for generating ACORDAR scores
    trec_eval = subprocess.run(
            [trec_eval_path, '-q', '-m', score, qrels_path, acordar_run_path], stdout=subprocess.PIPE).stdout.decode('UTF-8')

    #generate ACORDAR scores file
    generateOutputCSV(acordar_scores_path)


