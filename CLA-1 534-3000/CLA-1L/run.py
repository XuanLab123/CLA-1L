from calvados import sim
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--path',nargs='?', default='.', const='.', type=str)
    parser.add_argument('--config',nargs='?', default='config.yaml', const='config.yaml', type=str)
    parser.add_argument('--components',nargs='?', default='components.yaml', const='components.yaml', type=str)

    args = parser.parse_args()

    path = args.path
    fconfig = args.config
    fcomponents = args.components

    sim.run(path=path,fconfig=fconfig,fcomponents=fcomponents)


from calvados.analysis import save_conf_prop

save_conf_prop(path="/Users/benjaminhunt/Documents/Xuan_Lab_Files/KULL_CALVADOS/CALVADOS/CLA-1 534-3000/CLA-1L",name="CLA-1L",residues_file="/Users/benjaminhunt/Documents/Xuan_Lab_Files/KULL_CALVADOS/CALVADOS/CLA-1 534-3000/input/residues_CALVADOS2.csv",output_path="data",start=10,is_idr=True,select='all')
