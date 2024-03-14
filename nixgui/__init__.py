from nicegui import *
from nicegui import events

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