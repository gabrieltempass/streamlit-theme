[![PyPI - Version](https://img.shields.io/pypi/v/st-theme)](https://pypi.org/project/st-theme/)
[![Downloads](https://static.pepy.tech/badge/st-theme/month)](https://pepy.tech/project/st-theme)
[![GitHub License](https://img.shields.io/github/license/gabrieltempass/streamlit-theme?color=blue)](https://github.com/gabrieltempass/streamlit-theme/blob/main/LICENSE)

# Streamlit Theme

A component that returns the active theme of the Streamlit app.

[![Overview](https://github.com/gabrieltempass/streamlit-theme/raw/main/images/st_theme_1.gif)](https://st-theme-1.streamlit.app/)

## Installation

``` bash
pip install st-theme
```

## Usage

The function immediately returns the active theme, when it is called. If the
user manually changes the theme, after the web app is already running, it
updates the returned value.

## Parameters

**adjust** : `bool`, `default=True`</br>
If set to ``True``, which is the default, it makes a CSS adjustment and removes
a space that would otherwise be added to the page by calling the ``st_theme``
function.

Streamlit components are meant to render something in the web app, and
Streamlit adds a space for them even when there is nothing to render. Since
``st_theme`` does not render anything, and only communicates with the frontend
to fetch the active theme, it makes a CSS adjustment to remove this space.

In most cases, the CSS adjustment does not interfere with the rest of the web
app, however there could be some situations where this occurs. If this happens,
or it is desired to disable it, pass ``False`` to `adjust` and, when necessary,
make your own CSS adjustment with ``st.html``.

**key** : `str` or `int`, optional</br>
A string or integer to use as a unique key for the component. Multiple
``st_themes`` may not share the same key. Defaults to ``None``.

## Returns

**theme** : `dict of {str : str}` or `None`</br>
A dictionary with the style settings being used by the active theme of the
Streamlit app, or ``None``, if for some reason it could not be fetched.

## Notes

There is a known bug, that depends on the browser, where the theme is not
returned immediately when the function is called. But it is returned normally
when the user changes it.

This can be a problem in determining the initial theme of the web app. Because,
by default, Streamlit uses the user's operating system setting (which might be
unknown) to automatically apply the light or dark mode to the app, when it is
first rendered.

To solve the issue, it is recommended to set a
[default theme configuration](https://docs.streamlit.io/library/advanced-features/theming)
for the app, and use its value in case of ``st_theme`` returning ``None``.

## Examples

A basic example:

``` python
import streamlit as st
from streamlit_theme import st_theme
theme = st_theme()
st.write(theme)
```
[![Example 1](https://github.com/gabrieltempass/streamlit-theme/raw/main/images/st_theme_1.gif)](https://st-theme-1.streamlit.app/)
[**[App]**](https://st-theme-1.streamlit.app/) 
[**[Source]**](https://github.com/gabrieltempass/streamlit-theme/blob/main/examples/st_theme_1.py)

An example showing the CSS adjustment made, when set to ``True``:

``` python
import streamlit as st
from streamlit_theme import st_theme

adjust = st.toggle("Make the CSS adjustment")

st.write("Input:")
st.code(
    f"""
    st.write("Lorem ipsum")
    st_theme(adjust={adjust})
    st.write("Lorem ipsum")
    """
)

st.write("Output:")
st.write("Lorem ipsum")
st_theme(adjust=adjust)
st.write("Lorem ipsum")
```
[![Example 2](https://github.com/gabrieltempass/streamlit-theme/raw/main/images/st_theme_2.gif)](https://st-theme-2.streamlit.app/)
[**[App]**](https://st-theme-2.streamlit.app/) 
[**[Source]**](https://github.com/gabrieltempass/streamlit-theme/blob/main/examples/st_theme_2.py)

## Requirements

To use this Streamlit component in your app, you will need:
* **Python 3.8+**
* **Streamlit 1.33+**
* The CSS adjustment depends on the
  [browser compatibility with the :has pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/:has#browser_compatibility)

## Development

Ensure you have [Python 3.8+](https://www.python.org/downloads/),
[Node.js](https://nodejs.org) and
[npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
installed.

1. Clone this repository:
``` bash
git clone git@github.com:gabrieltempass/streamlit-theme.git
```

2. Go to the `frontend` directory and initialize and run the component template
frontend:
``` bash
cd streamlit-theme/streamlit_theme/frontend
```
``` bash
npm install
npm run dev
```

3. From a separate terminal, go to the repository root directory, create a new
Python virtual environment, activate it and install Streamlit and the template
as an editable package:
``` bash
cd streamlit-theme
```
``` bash
python3 -m venv venv
. venv/bin/activate
pip install streamlit
pip install -e .
```

Still from the same separate terminal, run the example Streamlit app:
``` bash
streamlit run streamlit_theme/example.py
```

If all goes well, you should see something like this:

![Quickstart success](https://github.com/gabrieltempass/streamlit-theme/raw/main/images/development.png)

Modify the frontend code at
`streamlit_theme/frontend/src/StTheme.vue`.
Modify the Python code at `streamlit_theme/__init__.py`.

## References

This Streamlit component was made with the [streamlit-component-vue-vite-template](https://github.com/gabrieltempass/streamlit-component-vue-vite-template), by
[@gabrieltempass](https://github.com/gabrieltempass).
