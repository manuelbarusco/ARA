import scipy.stats as stats
import os
import pandas as pd

"""
This simple script will do a paired t-test between an RDFS specified run 
and the corresponding ACORDAR runs
"""

dirname = os.path.dirname(__file__)

configuration = "[m]"
run = "Basic_Parsing"
similarities_acordar = ["TF-IDF", "BM25", "FSDM", "LMD"]
similarities = ["TFIDFBoost", "BM25Boost", "FSDM", "LMDBoost"]
scores = ["ndcg_cut.5"]
no_empty = False

acordar_scores_directory_path = None
ardfs_scores_directory_path = None

if no_empty:
    acordar_scores_directory_path = os.path.join(dirname, f'../../files/run/ACORDAR/scores-noempty')
    ardfs_scores_directory_path = os.path.join(dirname, f'../../files/run/ARDFS/{run}/scores-noempty')
else:
    acordar_scores_directory_path = os.path.join(dirname, f'../../files/run/ACORDAR/scores')
    ardfs_scores_directory_path = os.path.join(dirname, f'../../files/run/ARDFS/{run}/scores')

if configuration == "[m]":
    acordar_scores_directory_path += "/metadata"
    ardfs_scores_directory_path += "/metadata"
elif configuration == "[d]":
    acordar_scores_directory_path += "/data"
    ardfs_scores_directory_path += "/data"
elif configuration == "[m+d]":
    acordar_scores_directory_path += "/full"
    ardfs_scores_directory_path += "/full"

for i in range(len(similarities_acordar)):
    for score in scores:
        score_path_acordar = acordar_scores_directory_path + "/" + similarities_acordar[i] + score + ".csv"
        score_path_ardfs = ardfs_scores_directory_path + "/" + similarities[i] + score + ".csv"

        #open the two dataframes for the csv files
        df_acordar = pd.read_csv(score_path_acordar, sep = ',')
        df_ardfs = pd.read_csv(score_path_ardfs, sep = ',')

        acordar_scores = list(df_acordar[score])
        ardfs_scores = list(df_ardfs[score])

        #print the results
        print(f"Similarity: {similarities_acordar[i]} Score: {score}")
        print(f"Mean Value ACORDAR: {sum(acordar_scores) / len(acordar_scores)}")
        print(f"Mean Value ARDFS: {sum(ardfs_scores) / len(ardfs_scores)}")
        print(stats.ttest_rel(acordar_scores, ardfs_scores).pvalue)