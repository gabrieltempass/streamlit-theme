<template>
</template>

<script setup>
import { computed, watch } from "vue"
import { Streamlit } from "streamlit-component-lib"

// Streamlit sends a theme object via props that can be used to ensure that the
// component has visuals that match the active theme in a Streamlit app.
const props = defineProps(["theme"])

// Stringify allows to compare the object with itself and trigger only when it
// changes. Computed maintains variable reactivity after stringify.
const theme = computed(() => JSON.stringify(props.theme))

watch(theme, (newTheme) => {
    // Executed immediately, then again when `theme` changes.
    Streamlit.setComponentValue(theme.value)
  },
  { immediate: true }
)
</script>
