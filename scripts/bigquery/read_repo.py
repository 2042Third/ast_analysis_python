import numpy as np
import pandas as pd
all_files_in_repo=['../../../bigq_out/data-000000000000.csv','../../../bigq_out/data-000000000001.csv','../../../bigq_out/data-000000000002.csv','../../../bigq_out/data-000000000003.csv','../../../bigq_out/data-000000000004.csv','../../../bigq_out/data-000000000005.csv','../../../bigq_out/data-000000000006.csv','../../../bigq_out/data-000000000007.csv','../../../bigq_out/data-000000000008.csv','../../../bigq_out/data-000000000009.csv','../../../bigq_out/data-000000000010.csv','../../../bigq_out/data-000000000011.csv','../../../bigq_out/data-000000000012.csv','../../../bigq_out/data-000000000013.csv','../../../bigq_out/data-000000000014.csv','../../../bigq_out/data-000000000015.csv','../../../bigq_out/data-000000000016.csv','../../../bigq_out/data-000000000016.csv']
rd = pd.read_csv('../../../bigq_out/data-000000000000.csv')
# print(rd)
print(list(rd.columns.values)[0])
# trainxor = rd[[0]]
# for i in trainxor:
#   print(i)
