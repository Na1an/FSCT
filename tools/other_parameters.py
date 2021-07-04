other_parameters = dict(directory='../',
                        model_filename='../model/model.pth',
                        box_dimensions=[6, 6, 6],
                        box_overlap=[0.5, 0.5, 0.5],
                        min_points_per_box=1000,
                        max_points_per_box=20000,
                        subsample=False,
                        subsampling_min_spacing=0.01,
                        noise_class=0,
                        terrain_class=1,
                        vegetation_class=2,
                        cwd_class=3,
                        stem_class=4,
                        coarse_grid_resolution=6,
                        fine_grid_resolution=0.5,
                        num_neighbours=5,
                        Canopy_coverage_resolution=1.0,
                        run_from_start=1,
                        delete_working_directory=0,
                        sorting_search_angle=20,
                        sorting_search_radius=5,
                        sorting_angle_tolerance=90,
                        max_search_radius=3,
                        max_search_angle=30,
                        )
