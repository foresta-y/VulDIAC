import argparse
import yaml
from model import GNN_Classifier


def parse_options():
    parser = argparse.ArgumentParser(description='VulDet training.')
    parser.add_argument('-i', '--input', help='The dir path of data.', type=str, required=True)
    parser.add_argument('-m', '--model_name', help='The dataset name.', type=str, required=True)
    parser.add_argument('-d', '--device', help='The device.', type=str, required=True)
    args = parser.parse_args()
    return args

def init_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        
    return config

def main():
    args = parse_options()
    data_path = args.input
    model_name = args.model_name
    device = args.device
    config = init_config()
    print(config)
    
    classifier = GNN_Classifier(config=config, dataset_path=data_path, model_name=model_name, device=device)
    classifier.preparation_data()
    classifier.train()

# python vul_graph.py -i ./dgl/devign_cfg/ -m ffmpeg -d cuda:0

# python vul_graph.py -i ./dgl/devign_cfg_wo_rd/ -m ffmpeg_wo_rd -d cuda:0

# python vul_graph.py -i ./dgl/bigvul_cfg/ -m bigvul_112 -d cuda:0

# python vul_graph.py -i ./dgl/reveal_cfg/ -m reveal -d cuda:0

if __name__ == "__main__":
    main()

