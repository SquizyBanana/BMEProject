BME Group 3:
    Emilie van Eps | Fran Karlović | Jules Verhagen
    Julia Kersten | Nienke Dik | Sven Rozendom

TROUBLESHOOTING:
Audio Stuff (Author: Nienke):
    1. Install the following libraries
        - pydub
        - simpleaudio

    2. You will probably get an error message when installing simpleaudio. Do the following to solve it:
        Go to the following site:
        https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst

        Make sure you download visual studio (just follow the instructions) and select when installing:
            - MSVC 14.0 (I selected multiple)
            - your windows version SDK (newest SDK version is best)
            - C++ adress sanitizer
            - testing tools for core features - build tools, C++ Cmake tools for windows

