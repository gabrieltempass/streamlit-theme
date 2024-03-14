<template>
  <div id="app">
    <WithStreamlitConnection v-slot="{ theme }">
      <StTheme :theme="theme" />
    </WithStreamlitConnection>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue"
import StTheme from "./StTheme.vue"

// "withStreamlitConnection" is a scoped slot. It bootstraps the connection
// between the component and the Streamlit app, and handles passing arguments
// from Python -> Component.

import WithStreamlitConnection from "./streamlit/WithStreamlitConnection.vue"

export default defineComponent({
  name: "App",
  components: {
    StTheme,
    WithStreamlitConnection,
  },
})
</script>

<style>
body {
  margin: 0px;
}
</style>
