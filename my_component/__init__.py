import os
import json

import streamlit as st
import streamlit.components.v1 as components
from streamlit.errors import StreamlitAPIException


_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "my_component",
        url="http://localhost:5173",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _component_func = components.declare_component(
        "my_component",
        path=build_dir
    )


def my_component(adjust=True):
    """Create a new instance of "my_component".

    Parameters
    ----------
    adjust: bool
        The name of the thing we're saying hello to. The component will display
        the text "Hello, {name}!"

    Returns
    -------
    dict of str: str or None
        The number of times the component's "Click Me" button has been clicked.
        (This is the value passed to `Streamlit.setComponentValue` on the
        frontend.)

    """
    if not isinstance(adjust, bool):
        raise StreamlitAPIException(
            "The adjust parameter from st_theme() received an invalid type.\n"
            "\nExpected: *bool*  "
            f"\nGot: *{type(adjust).__name__}*"
        )

    theme = _component_func(key=None, default=None)

    if adjust:
        css = """
            <style>
                div.e1f1d6gn4:has(iframe[title="my_component.my_component"]) {
                    height: 0;
                    margin-bottom: -2rem;
                }
            </style>
        """
        st.markdown(css, unsafe_allow_html=True)

    return json.loads(theme) if theme is not None else theme
