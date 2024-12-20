from kgcnn.data.datasets.MatBenchDataset2020 import MatBenchDataset2020


class SampleAllMPEhullDataset(MatBenchDataset2020):
    r"""Store and process :obj:`SampleAllMPEhullDataset` from `MatBench <https://matbench.materialsproject.org/>`__
    database.  Name within Matbench: 'matbench_mp_gap'.

    Matbench test dataset for predicting DFT PBE band gap from structure.
    Adapted from Materials Project database. Removed entries having a formation energy (or energy above the convex hull)
    more than 150meV and those containing noble gases. Retrieved April 2, 2019.
    For benchmarking w/ nested cross validation, the order of the dataset must be identical to the retrieved data;
    refer to the Automatminer/Matbench publication for more details.

        * Number of samples: 77679
        * Task type: regression
        * Input type: structure

    """

    def __init__(self, reload=False, verbose: int = 10):
        r"""Initialize 'band_gap_order_exp' dataset.

        Args:
            reload (bool): Whether to reload the data and make new dataset. Default is False.
            verbose (int): Print progress or info for processing where 60=silent. Default is 10.
        """
        # Use default base class init()
        super(SampleAllMPEhullDataset, self).__init__("sample_all_materials_data_ehull_processed", reload=reload, verbose=verbose)
        self.label_names = "e above hull"
        self.label_units = "eV/atom"
