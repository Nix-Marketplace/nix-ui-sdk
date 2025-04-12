from nicegui import *
from nicegui import events
from typing import Optional, Any
import inspect

# ----- CONSTANTS ----- #

# ----- STYLING ----- #

ui.button.default_classes("rounded-md bg-blue-grey-6 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-blue-grey-5 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-grey-6 w-96")
ui.textarea.default_classes("block rounded-md border-none py-1.5 text-blue-grey-9 shadow-sm placeholder:text-blue-grey-4 focus:ring-2 focus:ring-inset focus:ring-blue-grey-6 sm:text-sm sm:leading-6 w-96")
ui.input.default_classes("block rounded-md border-0 py-1.5 text-blue-grey-9 shadow-sm placeholder:text-blue-grey-4 focus:ring-2 focus:ring-inset focus:ring-blue-grey-6 sm:text-sm sm:leading-6 w-96")
ui.number.default_classes("block rounded-md border-0 py-1.5 text-blue-grey-9 shadow-sm placeholder:text-blue-grey-4 focus:ring-2 focus:ring-inset focus:ring-blue-grey-6 sm:text-sm sm:leading-6 w-96")
ui.label.default_classes("max-w-xl text-base leading-7 text-blue-grey-7 lg:max-w-lg w-96")
ui.html.default_classes("max-w-xl text-base leading-7 text-blue-grey-7 lg:max-w-lg w-96")
ui.image.default_classes("max-w-xl text-base leading-7 text-blue-grey-7 lg:max-w-lg w-96")
ui.markdown.default_classes("max-w-xl text-base leading-7 text-blue-grey-7 lg:max-w-lg w-96")
ui.select.default_classes("mt-2 block rounded-md border-0 py-1.5 pl-3 pr-10 text-blue-grey-9 focus:ring-2 focus:ring-blue-grey-6 sm:text-sm sm:leading-6 w-96")
ui.switch.default_classes("relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-blue-grey-6 focus:ring-offset-2 w-96")
ui.upload.default_classes("mt-2 block rounded-md border-0 py-1.5 text-blue-grey-9 shadow-sm focus:ring-2 focus:ring-inset focus:ring-blue-grey-6 sm:text-sm sm:leading-6 w-96").default_props("color=blue-grey")

# ----- RUN CONFIGURATION ----- #

def run(
    *,
    title: str = 'NixGUI App',
    host: str = '0.0.0.0',
    port: int = 8080,
    reload: bool = True,
    show: bool = True,
    dark: bool = False,
    favicon: Optional[str] = None,
    storage_secret: Optional[str] = None,
    **kwargs: Any
) -> None:
    """
    Run the NixGUI application with custom defaults while preserving all NiceGUI's run() functionality.
    
    Args:
        title: The title of the application
        host: The host to run the application on
        port: The port to run the application on
        reload: Whether to reload the application on code changes
        show: Whether to show the application in a browser
        dark: Whether to use dark mode
        favicon: The path to the favicon
        storage_secret: The secret key for storage
        **kwargs: Additional arguments passed to NiceGUI's run() function
    """
    # Get the original run function's signature
    original_run = ui.run
    original_params = inspect.signature(original_run).parameters
    
    # Create a dictionary of default values from the original function
    defaults = {
        param.name: param.default 
        for param in original_params.values() 
        if param.default is not inspect.Parameter.empty
    }
    
    # Update defaults with our custom values
    defaults.update({
        'title': title,
        'host': host,
        'port': port,
        'reload': reload,
        'show': show,
        'dark': dark,
        'favicon': favicon,
        'storage_secret': storage_secret,
    })
    
    # Update with any additional kwargs
    defaults.update(kwargs)
    
    # Call the original run function with our updated parameters
    original_run(**defaults)


