from DataMerger import DataMerger


def main():
    dm = DataMerger(constants_yml_filename="./utils/ymlReader.py")
    dm.start_merging()
    dm.insert_SMILES_imgs()
    dm.


if __name__ == '__main__':
    # TODO: parse argments
    main()
