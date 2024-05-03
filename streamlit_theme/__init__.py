import os
import json
from contextlib import nullcontext

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


def stylized_container(key):
    """
    Add a spaceless container to the app.
    
    Insert a container into the app, which receives an iframe that does not
    render anything. Style this container using CSS and a unique key. The style
    targeting `"stVerticalBlockBorderWrapper"` removes 1rem of space added by
    the iframe. While the style targeting the div that contains the iframe
    changes its height from 1.5625rem to 0.

    Parameters
    ----------
    key : str, int or None
        A key associated with this container. This needs to be unique since all
        styles will be applied to the container with this key.

    Returns
    -------
    container : DeltaGenerator
        A container object. Elements can be added to this container using
        either the "with" notation or by calling methods directly on the
        returned object.
    """
    key = f"st_theme_{key}"
    selector = f"div.element-container > div.stHtml > span.{key}"
    css = (
        f"""
        <style>
            div[data-testid="stVerticalBlockBorderWrapper"]:has({selector}) {{
                margin-bottom: -1rem;
            }}
            div[data-testid="stVerticalBlock"]:has(> {selector}) div:has(iframe) {{
                height: 0;
            }}
        </style>
        """
        f"<span class='{key}'></span>"
    )
    container = st.container()
    container.html(css)
    return container


def st_theme(adjust=True, key=None):
    """
    Get the active theme of the Streamlit app.

    The function immediately returns the active theme, when it is called. If
    the user manually changes the theme, after the web app is already running,
    it updates the returned value.

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
        ``st.html``.
    key : str or int, optional
        A string or integer to use as a unique key for the component. Multiple
        ``st_themes`` may not share the same key. Defaults to ``None``.

    Returns
    -------
    theme : dict of {str : str} or None
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
    for the app (https://docs.streamlit.io/library/advanced-features/theming),
    and use its value in case of ``st_theme`` returning ``None``.

    Examples
    --------
    >>> import streamlit as st
    >>> from streamlit_theme import st_theme
    >>> theme = st_theme()
    >>> st.write(theme)
    
    .. output::
       https://st-theme-1.streamlit.app/
       height: 300px
    """
    
    if not isinstance(adjust, bool):
        raise StreamlitAPIException(
            "The adjust parameter from st_theme() received an invalid type.\n"
            "\nExpected: *bool*  "
            f"\nGot: *{type(adjust).__name__}*"
        )

    if not isinstance(key, str) and not isinstance(key, int) and key is not None:
        raise StreamlitAPIException(
            "The key parameter from st_theme() received an invalid type.\n"
            "\nExpected: *str* or *int* or *None*  "
            f"\nGot: *{type(key).__name__}*"
        )

    # If `True`, use the `stylized_container` context. Else, do not use it, but
    # still run `_st_theme`.
    with stylized_container(key=key) if adjust else nullcontext():
        theme = _st_theme(key=key, default=None)

    return json.loads(theme) if theme is not None else theme
