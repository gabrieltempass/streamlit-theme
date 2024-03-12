import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"

class StTheme extends StreamlitComponentBase {
  // Streamlit sends a theme object via props that can be used to ensure that
  // the component has visuals that match the active theme in a Streamlit
  // app.

  componentDidMount() {
    // Run the first time the page is loaded.
    console.log("Mounted")
    console.log(this.props)
    // console.log(this.props)
    console.log(typeof this.props.theme)
    Streamlit.setComponentValue(this.props);
  }

  componentDidUpdate(prevProps: {}) {
    if (JSON.stringify(this.props) !== JSON.stringify(prevProps)) {
      // Run every time the theme object changes.
      console.log("Updated")
      Streamlit.setComponentValue(this.props);
    }
  }

  render() {
    console.log("Rendered")
    return null
  }
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between the component and the Streamlit app, and handles
// passing arguments from Python -> Component.
export default withStreamlitConnection(StTheme)
