from DataMerger import DataMerger


def main():
    dm = DataMerger(constants_yml_filename="./utils/merge_constants_config.yml")
    dm.start_merging()
    # dm.insert_SMILES_imgs()


if __name__ == '__main__':
    # TODO: parse argments
    main()
