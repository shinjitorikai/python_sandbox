import pytesseract
from PIL import Image
from tqdm  import tqdm
from pathlib import Path
import os

# 設定値
INPUT_DIR = r'./test'
IMG_EXT = '*.jpg'

def getfilelist(targetdir,pattern,isrecursive):
    p = Path(targetdir)
    if isrecursive == True:
        search_pattern = '**/' + pattern
    else:
        search_pattern = pattern    
    filelist = [str(filename) for filename in list(p.glob(search_pattern))]
    return filelist

def main():
    print('get filelist...')
    filelist = getfilelist(INPUT_DIR,IMG_EXT,False)
    print(' - len(filelist) : ',len(filelist))

    print('execute ocr...')
    for filepath in tqdm(filelist):
        img = Image.open(filepath)
        result = pytesseract.image_to_string(image=img,lang='jpn')
        output_txt = os.path.join(os.path.dirname(filepath), os.path.splitext(os.path.basename(filepath))[0]+'.txt')
        #print(output_txt)
        with open(output_txt,mode='w') as fw:
            fw.write(result)

    print('処理終了')

if __name__ == '__main__':
    main()
