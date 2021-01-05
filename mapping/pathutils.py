import os, sys
import errno
import urllib2
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

        font = urllib2.urlopen(FONT_URL)
        font_stream = chunk_read(font, report_hook=chunk_report)
        
        with open(FONT_NAME, "wb") as f:
            f.write(font_stream)
            
        del font_stream
        
    with open("list.txt", "wb") as f:
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


# chunk_report() and chunk_read() from https://stackoverflow.com/a/56619744

def chunk_report(bytes_so_far, chunk_size, total_size):
    percent = float(bytes_so_far) / total_size
    percent = round(percent*100, 2)
    sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" %
                     (bytes_so_far, total_size, percent))
    sys.stdout.flush()
    if bytes_so_far >= total_size:
        sys.stdout.write('\n')


def chunk_read(response, chunk_size=8192, report_hook=None):
    total_size = response.info().get("Content-Length").strip()
    total_size = int(total_size)
    bytes_so_far = 0
    data = b""

    while 1:
        chunk = response.read(chunk_size)
        bytes_so_far += len(chunk)

        if not chunk:
            break

        if report_hook:
            report_hook(bytes_so_far, chunk_size, total_size)

        data += chunk

    return data