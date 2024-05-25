import sys
from cx_Freeze import setup, Executable

# Dependencies to be included in the build
build_exe_options = {
    "packages": ["streamlit"],
    "include_files": [
        "welcome.py",
        "pages",
        "service_token.json"
        # "analyze_img.py",
        # "segmentation.py",
        # "text_xtract.py",
    ]
}

# Define base depending on platform
base = None
# if sys.platform == "win32":
#     base = "Win32GUI"  # For Windows GUI applications

# Setup configuration
setup(
    name="MyStreamlitApp",
    version="1.0",
    description="My Streamlit Application",
    options={"build_exe": build_exe_options},
    executables=[Executable("run.py", base=base)]  # Main script to execute
)