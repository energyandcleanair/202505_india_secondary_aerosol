import os
import earthaccess


def get_data(product: str, output_dir: str, start_date: str, end_date: str):
    # Authenticate with Earthdata Login
    # create account at https://urs.earthdata.nasa.gov/
    earthaccess.login(persist=True)

    # Search for data files
    # no use in defining a bounding box, all data that we need
    # comes in global files
    results = earthaccess.search_data(
        short_name=product,
        temporal=(start_date, end_date),
        count=-1,  # get all records
        version="5.12.4",  # MERRA-2 version
    )

    os.makedirs(output_dir, exist_ok=True)

    # download files
    for granule in results:

        # check if file already exists
        filename = granule['meta']['native-id'].split(':')[-1]
        if os.path.exists(os.path.join(output_dir, filename)):
            continue

        print(f"Downloading {filename}...")
        earthaccess.download(granule, output_dir)


if __name__ == "__main__":

    get_data(product="M2T1NXAER",
             output_dir='/media/work/T7/merra2-M2T1NXAER-V5.12.4',
             start_date="2024-01-01",
             end_date="2024-12-31",
             )
