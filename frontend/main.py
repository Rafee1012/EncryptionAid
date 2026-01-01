from desktopGUI import run_app
from backend.folderManager import init_app, hasRootFolder

if __name__ == "__main__":
    if (not hasRootFolder()):
        init_app()
    run_app()