import os
import errno
import math
import requests
import pkg_resources


__all__= ["check_env", "create_env", "FONT_NAME", "working_dir", "NUMBERS_NAME",
        "done_path", "glyphs_path", "converted_path", "raw_path"]


FONT_NAME = "CNstrokeorder.sfd"
FONT_URL = "https://rtega.be/chmn/CNstrokeorder.sfd"
NUMBERS_NAME = "numbers.svg"

working_dir = os.path.abspath(os.getcwd())
glyphs_path = working_dir + r"/glyphs/"
done_path = glyphs_path + r"done/"
converted_path = glyphs_path + r"converted/"
raw_path = glyphs_path + r"raw/"

ideal_env = ["glyphs", FONT_NAME, "list.txt"]
ideal_glyphs = ["raw", "converted", "done", "numbers.svg"]


def check_env():
    """ 
    Check if the working environment have the necessary files 
    and directories to start mapping

    Raises
    ------
    EnvironmentError
        If a critical file or directory is not detected on the directory
        the script is being called

    """
    curr_dir_list = os.listdir(working_dir)

    for directory in ideal_env:
        if directory not in curr_dir_list:
            raise EnvironmentError("Missing \'{}\' file or directory, you can generate a clean "
            "environment with fmap --env".format(directory))

        if directory == "glyphs": 
            curr_gly_dir_list = os.listdir(glyphs_path)
            for glydir in ideal_glyphs:
                    if glydir not in curr_gly_dir_list:
                        raise EnvironmentError("Missing \'{}\' file or directory, you can generate a clean "
                        "environment with fmap --env".format(directory+ "/" +glydir))
    return


def make_dir(directory):
    """
        Create a directory if it does not already exist.

    Parameters
    ----------
    directory : str
        Name of the directory to be created
    """
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise e
    return
    

def create_env():
    """
        Create all the missing files or directories needed to start mapping.
        If the .sfd of the original chinese font is missing, the script will
        download it from the page defined in FONT_URL
    """
    if not os.path.isfile(FONT_NAME):

        print("Downloading \'{}\', this might take a while".format(FONT_NAME))
        download_file(FONT_URL, FONT_NAME)
        
    with open("list.txt", "a+") as f:
        pass

    make_dir("glyphs")
    os.chdir("glyphs")
    make_dir("raw")
    make_dir("converted")
    make_dir("done")

    if not os.path.isfile(NUMBERS_NAME):
        num_stream =  pkg_resources.resource_stream(__name__, 'files/numbers.svg')

        with open(NUMBERS_NAME, "wb") as f:
            f.write(num_stream.read())

    os.chdir("..")
    return 


def print_progressbar(total,current,barsize=60):
    """Modified from https://stackoverflow.com/a/61295200
    """
    progress=int(current*barsize/total)
    completed= str(int(current*100/total)) + '%'
    print('[' , chr(9608)*progress,' ',completed,'.'*(barsize-progress),'] ',str(current)+'/'+str(total), sep='', end='\r',flush=True)


def download_file(url, filename, n_chunk=1):
    """Modified from https://stackoverflow.com/a/37574635
        Download a file from the internet
    Parameters
    ----------
    url : str
        Download link
    filename : str
        Name of the output file
    n_chunk : int, optional
        Numbers of download chunks, by default 1
    """
    r = requests.get(url, stream=True)
    # Estimates the number of bar updates
    block_size = 1024
    file_size = int(r.headers.get('Content-Length', None))
    num_bars = math.ceil(file_size / (n_chunk * block_size))
    print_progressbar(num_bars,0)
    with open(filename, 'wb') as f:
        for i, chunk in enumerate(r.iter_content(chunk_size=n_chunk * block_size)):
            f.write(chunk)
            print_progressbar(num_bars, i+1)
    return