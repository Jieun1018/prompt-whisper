import argparse
from datasets import load_dataset

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, default=None, help="dataset path for datasets.load_dataset")
    parser.add_argument("--name", type=str, default=None, help="dataset name for datasets.load_dataset")
    parser.add_argument("--data_dir", type=str, default="/DB/", help="Dataset stored in DatasetDict format")
    parser.add_argument("--save_dir", type=str, default="/data/proj_asr/hf_dd_data", help="Dataset stored in DatasetDict format")
    parser.add_argument("--cache_dir", type=str, default="/data/proj_asr/hf_data", help="Directory that stores the dataset")
    parser.add_argument("--num_proc", type=int, default=4, help="Num. of proc. to process the dataset")
    
    args = parser.parse_args()
    #print(args.path)
    #print(args.name)
    if args.path == "audiofolder":
        ds = load_dataset(args.path, data_dir=args.data_dir)
    else:
        if args.name is not None:    
            ds = load_dataset(args.path, args.name, cache_dir=args.cache_dir, num_proc=args.num_proc, use_auth_token=True)
        else:
            ds = load_dataset(args.path, cache_dir=args.cache_dir, num_proc=args.num_proc, use_auth_token=True)
    
    #print('8'*20)
    print(ds)
    #print('8'*20)
    
    ds.save_to_disk(f"{args.save_dir}/{args.path}/{args.name}", num_proc=args.num_proc)
    print(f"DatasetDict {args.path}/{args.name} saved into {args.save_dir} from cache folder {args.cache_dir}")
