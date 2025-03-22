<script>
import { ref, onMounted, onUnmounted } from 'vue'

export default {
  setup() {
    const time = ref(new Date())
    let intervalId = null

    const updateTime = () => {
      time.value = new Date()
    }

    const formattedTime = () => {
      return time.value.toLocaleTimeString('en-US', {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      })
    }

    onMounted(() => {
      intervalId = setInterval(updateTime, 1000)
    })

    onUnmounted(() => {
      clearInterval(intervalId)
    })

    return { formattedTime }
  }
}
</script>

<template>
  <div class="clock-container">
    <div class="clock">
      {{ formattedTime() }}
    </div>
    <div class="description">
      Real-Time Clock with Vue.js
    </div>
  </div>
</template>

<style scoped>
/* Keep existing styles */
</style>
