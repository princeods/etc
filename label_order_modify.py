from tqdm import tqdm
import glob


path = 'C:\\ProjectPY\\datasets\\03_car\\labels\\'
asdf = str()
qwer = str()

for _fLabel in tqdm(glob.glob(path+'*.txt')):

    with open(_fLabel, 'r') as f:
        
        asdf = f.readline()
        qwer = len(asdf)
        zxcv = asdf[1:qwer]

    print ( f"asdf : {asdf} \n qwer : {qwer} \n zxcv : {zxcv} \n result : {str(2) + zxcv}")

    with open(_fLabel, 'w') as f:

        f.write(str(2) + zxcv)

