import os
import json

import streamlit as st
import streamlit.components.v1 as components
from streamlit.errors import StreamlitAPIException


_RELEASE = False

if not _RELEASE:
    _st_theme = components.declare_component(
        "st_theme",
        url="http://localhost:5173",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _st_theme = components.declare_component(
        "st_theme",
        path=build_dir
    )


def st_theme(adjust=True, key=None):
    """
    Get the active theme of the Streamlit app.

    The function immediately returns the active theme, when it is called. If
    the user manually changes the theme, after the web app is already running,
    it updates the returned value.

    The ``st_theme`` command must only be set once in the script.

    Parameters
    ----------
    adjust : bool, default=True
        If set to ``True``, which is the default, it makes a CSS adjustment and
        removes a space that would otherwise be added to the page by calling
        the ``st_theme`` function.

        Streamlit components are meant to render something in the web app, and
        Streamlit adds a space for them even when there is nothing to render.
        Since ``st_theme`` does not render anything, and only communicates with
        the frontend to fetch the active theme, it makes a CSS adjustment to
        remove this space.

        In most cases, the CSS adjustment does not interfere with the rest of
        the web app, however there could be some situations where this occurs.
        If this happens, or it is desired to disable it, pass ``False`` to
        `adjust` and, when necessary, make your own CSS adjustment with
        ``st.markdown``.
    key : str or int, optional
        A string or integer to use as a unique key for the component. Multiple
        ``st_themes`` may not share the same key. Defaults to ``None``.

    Returns
    -------
    theme : dict of str: str or None
        A dictionary with the style settings being used by the active theme of
        the Streamlit app, or ``None``, if for some reason it could not be
        fetched.

    Notes
    -----
    There is a known bug, that depends on the browser, where the theme is not
    returned immediately when the function is called. But it is returned
    normally when the user changes it.

    This can be a problem in determining the initial theme of the web app.
    Because, by default, Streamlit uses the user's operating system setting
    (which might be unknown) to automatically apply the light or dark mode to
    the app, when it is first rendered.

    To solve the issue, it is recommended to set a default theme configuration
    (https://docs.streamlit.io/library/advanced-features/theming) for the app,
    and use its value in case of ``st_theme`` returning ``None``.

    Examples
    -------
    >>> from st_theme import st_theme
    >>> theme = st_theme()
    >>> theme
    {
        "primaryColor": "#ff4b4b"
        "backgroundColor": "#ffffff"
        "secondaryBackgroundColor": "#f0f2f6"
        "textColor": "#31333F"
        "base": "light"
        "font": ""Source Sans Pro", sans-serif"
        "linkText": "#0068c9"
        "fadedText05": "rgba(49, 51, 63, 0.1)"
        "fadedText10": "rgba(49, 51, 63, 0.2)"
        "fadedText20": "rgba(49, 51, 63, 0.3)"
        "fadedText40": "rgba(49, 51, 63, 0.4)"
        "fadedText60": "rgba(49, 51, 63, 0.6)"
        "bgMix": "rgba(248, 249, 251, 1)"
        "darkenedBgMix100": "hsla(220, 27%, 68%, 1)"
        "darkenedBgMix25": "rgba(151, 166, 195, 0.25)"
        "darkenedBgMix15": "rgba(151, 166, 195, 0.15)"
        "lightenedBg05": "hsla(0, 0%, 100%, 1)"
    }
    """
    if not isinstance(adjust, bool):
        raise StreamlitAPIException(
            "The adjust parameter from st_theme() received an invalid type.\n"
            "\nExpected: *bool*  "
            f"\nGot: *{type(adjust).__name__}*"
        )

    theme = _st_theme(key=key, default=None)

    if adjust:
        css = """
            <style>
                div.e1f1d6gn4:has(iframe[title="streamlit_theme.st_theme"]) {
                    height: 0;
                    margin-bottom: -2rem;
                }
            </style>
        """
        st.markdown(css, unsafe_allow_html=True)

    return json.loads(theme) if theme is not None else theme
