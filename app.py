from dask import dataframe as dd
import os

def main():
    print('File Format conv started')
    src_dir = os.environ.get('SRC_DIR')
    tgt_dir = os.environ.get('TGT_DIR')
    df = dd.read_csv(
            f'{src_dir}/NYSE*.txt.gz',
            names = ['ticker','trade_date','open_price','low_price','high_price',
                     'close_price','volume'],
            blocksize= None)
    print('DF is created and will be written in JSON format')
    df.to_json(
               f'{tgt_dir}/part-*.json.gz',
                orient = 'records',
                lines = True,
                compression = 'gzip',
                name_function = lambda i: '%05d' %i 
    )
    print('File format conv completed')


if __name__ == '__main__':
    main()