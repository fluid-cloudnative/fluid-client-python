import ray

runtime_env = {"pip": ["s3fs", "fluid"]}

ray.init(address="ray://127.0.0.1:10001", runtime_env=runtime_env)


@ray.remote(runtime_env=runtime_env)
def read_parquet_samples(dataset_name, parquet_dataset_root):
    from pyarrow.fs import PyFileSystem, FSSpecHandler
    from fluid.io import FluidFileSystem

    fs = FluidFileSystem(
        dataset_name=dataset_name
    )

    root = parquet_dataset_root
    print(fs.ls(root))
    pa_fs = PyFileSystem(FSSpecHandler(fs))
    ds = ray.data.read_parquet(root, filesystem=pa_fs)

    return ds


@ray.remote(runtime_env=runtime_env)
def read_parquet_samples_given_files(dataset_name, parquet_dataset_root):
    from pyarrow.fs import PyFileSystem, FSSpecHandler
    from fluid.io import FluidFileSystem

    fs = FluidFileSystem(
        dataset_name=dataset_name
    )

    root = parquet_dataset_root
    print(fs.ls(root))
    parquet_files = [path for path in fs.ls(root, detail=False) if path.endswith(".parquet")]
    pa_fs = PyFileSystem(FSSpecHandler(fs))
    ds = ray.data.read_parquet(parquet_files, filesystem=pa_fs)

    return ds


@ray.remote(runtime_env=runtime_env)
def transform_dataset_pokemon(ds):
    ds = ds.map(lambda x: {"image": x['image'], "caption": x['text']})
    return ds


@ray.remote(runtime_env=runtime_env)
def transform_dataset_magicbrush(ds):
    ds = ds.map(lambda x: {"source_img": x['source_img'], "mask_img": x['mask_img'], "target_img": x['target_img']})
    return ds


@ray.remote(runtime_env=runtime_env)
def take_one(ds):
    return ds.take(1)


dataset_name = "sd-dataset"

# osunlp/MagicBrush: https://huggingface.co/datasets/osunlp/MagicBrush

ray_ds_1 = read_parquet_samples.remote(dataset_name, "datasets/osunlp-MagicBrush/")
transformed_ds_1 = transform_dataset_magicbrush.remote(ray_ds_1)
first_sample_1 = ray.get(take_one.remote(transformed_ds_1))

# lambdalabs/pokemon-blip-captions: https://huggingface.co/datasets/lambdalabs/pokemon-blip-captions

ray_ds_2 = read_parquet_samples_given_files.remote(dataset_name, "datasets/lambdalabs-pokemon-blip-captions/data")
transformed_ds_2 = transform_dataset_pokemon.remote(ray_ds_2)
first_sample_2 = ray.get(take_one.remote(transformed_ds_2))
